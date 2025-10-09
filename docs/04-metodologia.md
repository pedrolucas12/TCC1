# Metodologia

> Abordagem metodológica completa para desenvolvimento do modelo de previsão de surtos de dengue.

---

## 🎯 Visão Geral

Este documento descreve a metodologia completa do TCC, desde a coleta de dados até a avaliação final dos modelos preditivos.

---

## 📊 1. PIPELINE GERAL

```
┌──────────────────────────────────────────────────────────────┐
│                    METODOLOGIA COMPLETA                       │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   1. COLETA DE DADOS (ETL)          │
        │   - SINAN (casos dengue)            │
        │   - CHIRPS/ERA5 (clima)             │
        │   - IBGE (população, geometrias)    │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   2. LIMPEZA E NORMALIZAÇÃO         │
        │   - Padronização de datas           │
        │   - Códigos IBGE (7 dígitos)        │
        │   - Filtro de casos prováveis       │
        │   - Tratamento de missing           │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   3. AGREGAÇÃO ESPACIAL/TEMPORAL    │
        │   - Casos por município-semana      │
        │   - Zonal stats clima → município   │
        │   - Join com população              │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   4. FEATURE ENGINEERING            │
        │   - Lags (1-12 semanas)             │
        │   - Médias móveis (4, 8 semanas)    │
        │   - Anomalias climáticas            │
        │   - Variáveis socioeconômicas       │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   5. ANÁLISE EXPLORATÓRIA           │
        │   - Distribuições, tendências       │
        │   - Correlações cruzadas            │
        │   - Sazonalidade                    │
        │   - Visualizações                   │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   6. SELEÇÃO DE FEATURES            │
        │   - Correlação cruzada (CCF)        │
        │   - Importância de features (RF)    │
        │   - SHAP values                     │
        │   - Windowed correlation            │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   7. DIVISÃO TREINO/VALIDAÇÃO/TESTE │
        │   - TimeSeriesSplit (rolling)       │
        │   - Sem vazamento temporal          │
        │   - Validação cruzada temporal      │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   8. MODELAGEM                      │
        │   Baseline: SARIMA, Prophet         │
        │   ML: RF, XGBoost                   │
        │   DL: LSTM, BiLSTM                  │
        │   Ensemble: Voting/Stacking         │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   9. AVALIAÇÃO E COMPARAÇÃO         │
        │   - RMSE, MAE, MAPE                 │
        │   - AUC, Precision, Recall (surtos) │
        │   - Análise por município/região    │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   10. INTERPRETAÇÃO                 │
        │   - SHAP para XGBoost               │
        │   - Feature importance              │
        │   - Análise de lags ótimos          │
        │   - Casos de sucesso/falha          │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   11. SISTEMA DE ALERTA             │
        │   - Calibração de limiares          │
        │   - Definição de "surto"            │
        │   - Dashboard operacional           │
        └─────────────────────────────────────┘
```

---

## 🔧 2. DETALHAMENTO POR ETAPA

### ETAPA 1: Coleta de Dados (ETL)

#### Dados Epidemiológicos
- **Fonte**: OpenDataSUS / SINAN
- **Período**: 2010-2024 (ou mais recente)
- **Método**: Download via S3 (JSON por ano)
- **Armazenamento**: Raw layer (arquivos originais + metadata)

#### Dados Climáticos
- **Precipitação**: CHIRPS (NetCDF, diário)
- **Temperatura/Umidade**: ERA5 ou NASA POWER
- **Período**: Sincronizar com dados epidemiológicos
- **Armazenamento**: NetCDF ou Parquet particionado

#### Dados Auxiliares
- **Malhas**: Shapefile IBGE (municípios)
- **População**: Estimativas anuais IBGE
- **Armazenamento**: GeoPackage ou PostGIS

---

### ETAPA 2: Limpeza e Normalização

#### Tratamentos Necessários

**Datas**
```python
# Converter datas para datetime
df['dt_sintomas'] = pd.to_datetime(df['dt_sin_pri'], errors='coerce')
df['dt_notific'] = pd.to_datetime(df['dt_notific'], errors='coerce')

# Extrair semana epidemiológica
df['ano_semana'] = df['sem_pri']  # formato YYYYWW
df['ano'] = df['ano_semana'].str[:4].astype(int)
df['semana'] = df['ano_semana'].str[4:].astype(int)
```

**Códigos Municipais**
```python
# Padronizar código IBGE (7 dígitos)
df['ibge_municipio'] = df['id_municip'].astype(str).str.zfill(7)
```

**Filtro de Casos**
```python
# Manter apenas casos prováveis/confirmados
filtro_casos = df['criterio_confirmacao'].isin([
    'LABORATORIAL',
    'CLÍNICO-EPIDEMIOLÓGICO'
])
df_filtrado = df[filtro_casos]
```

**Tratamento de Missing**
- Identificar % de missing por coluna
- Imputar ou remover conforme criticidade
- Documentar decisões

---

### ETAPA 3: Agregação Espacial e Temporal

#### Agregação Temporal de Casos

```python
# Agregar casos por município-semana
casos_semana = df_filtrado.groupby([
    'ibge_municipio', 
    'ano', 
    'semana'
]).agg({
    'id_notificacao': 'count',  # Total de casos
    'idade': 'mean',            # Idade média
    'evolucao': lambda x: (x == 'ÓBITO').sum()  # Óbitos
}).reset_index()

casos_semana.columns = ['ibge_municipio', 'ano', 'semana', 
                        'casos', 'idade_media', 'obitos']
```

#### Agregação Espacial de Clima

**Zonal Statistics (CHIRPS → Município)**

```python
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats

# Carregar shapefile municípios
municipios = gpd.read_file('malha_municipal.shp')

# Para cada dia de dados CHIRPS
stats = zonal_stats(
    municipios.geometry,
    'chirps_2024_01_01.tif',
    stats=['mean', 'sum', 'min', 'max']
)

# Resultado: precipitação média por município
municipios['precip_mm'] = [s['mean'] for s in stats]
```

#### Agregação Temporal de Clima (Diário → Semanal)

```python
# Converter para semanal (soma para chuva, média para temperatura)
clima_semanal = clima_diario.groupby([
    'ibge_municipio',
    pd.Grouper(key='data', freq='W-MON')  # Semana começa segunda
]).agg({
    'precipitacao': 'sum',      # Soma da semana
    'temperatura': 'mean',       # Média da semana
    'umidade': 'mean'
}).reset_index()
```

---

### ETAPA 4: Feature Engineering

#### Features Temporais (Lags)

```python
def create_lags(df, col, lags=12):
    """Criar features de lag para uma coluna"""
    for lag in range(1, lags + 1):
        df[f'{col}_lag{lag}'] = df.groupby('ibge_municipio')[col].shift(lag)
    return df

# Aplicar para variáveis climáticas
df = create_lags(df, 'precipitacao', lags=12)
df = create_lags(df, 'temperatura', lags=12)
df = create_lags(df, 'umidade', lags=8)

# Aplicar para casos passados (autoregressivo)
df = create_lags(df, 'casos', lags=4)
```

#### Médias Móveis

```python
# Média móvel de 4 semanas
df['precip_ma4'] = df.groupby('ibge_municipio')['precipitacao'].transform(
    lambda x: x.rolling(window=4, min_periods=1).mean()
)

# Média móvel de 8 semanas
df['temp_ma8'] = df.groupby('ibge_municipio')['temperatura'].transform(
    lambda x: x.rolling(window=8, min_periods=1).mean()
)
```

#### Somas Acumuladas

```python
# Precipitação acumulada últimas 4 semanas
df['precip_cum4'] = df.groupby('ibge_municipio')['precipitacao'].transform(
    lambda x: x.rolling(window=4, min_periods=1).sum()
)
```

#### Anomalias Climáticas

```python
# Calcular climatologia (média histórica por semana do ano)
climatologia = df.groupby(['ibge_municipio', 'semana'])['temperatura'].mean()

# Anomalia = observado - climatologia
df['temp_anomalia'] = df.apply(
    lambda row: row['temperatura'] - climatologia.loc[
        (row['ibge_municipio'], row['semana'])
    ],
    axis=1
)
```

#### Features Socioeconômicas

```python
# Join com dados IBGE
df = df.merge(populacao_ibge, on='ibge_municipio', how='left')

# Taxa per capita
df['casos_per_100k'] = (df['casos'] / df['populacao']) * 100000

# Log de população (escala)
df['log_populacao'] = np.log1p(df['populacao'])
```

#### Features Espaciais

```python
# Casos em municípios vizinhos (windowed correlation)
# Requer matriz de adjacência

# Latitude/Longitude do centroid
df['lat'] = df['ibge_municipio'].map(municipios.set_index('codigo')['lat_centroid'])
df['lon'] = df['ibge_municipio'].map(municipios.set_index('codigo')['lon_centroid'])
```

#### Features Temporais (Sazonalidade)

```python
# Semana do ano (cíclica)
df['semana_sin'] = np.sin(2 * np.pi * df['semana'] / 52)
df['semana_cos'] = np.cos(2 * np.pi * df['semana'] / 52)

# Mês
df['mes'] = pd.to_datetime(
    df['ano'].astype(str) + df['semana'].astype(str) + '1',
    format='%Y%W%w'
).dt.month
```

---

### ETAPA 5: Análise Exploratória de Dados (EDA)

#### Objetivos
1. Entender distribuições de casos e clima
2. Identificar tendências e sazonalidade
3. Detectar correlações
4. Identificar outliers/anomalias

#### Análises Principais

**Distribuição de Casos**
- Histograma de casos por semana
- Casos por município (mapa)
- Evolução temporal (série temporal)

**Sazonalidade**
- Boxplot de casos por mês
- Decomposição de série temporal (tendência, sazonalidade, resíduo)

**Correlações**
- Matriz de correlação entre variáveis climáticas e casos
- Cross-correlation function (CCF) para identificar lags ótimos

**Análise Espacial**
- Mapa coroplético de incidência
- Clusters espaciais (Moran's I)

---

### ETAPA 6: Seleção de Features

#### Métodos

**1. Correlação Cruzada (Cross-Correlation Function)**
```python
from statsmodels.tsa.stattools import ccf

# CCF entre temperatura e casos (com lags)
correlacoes = ccf(df['temperatura'], df['casos'], adjusted=False)

# Identificar lag com maior correlação
lag_otimo = np.argmax(np.abs(correlacoes))
```

**2. Feature Importance (Random Forest)**
```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)

# Importâncias
importancias = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
```

**3. SHAP (Interpretabilidade)**
```python
import shap

explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

# Plot de importância
shap.summary_plot(shap_values, X_test)
```

**4. Windowed Correlation** (Ferdousi et al., 2021)
- Técnica para usar dados de municípios vizinhos
- Útil para municípios com poucos dados históricos

---

### ETAPA 7: Divisão Treino/Validação/Teste

#### Princípio Fundamental
⚠️ **NUNCA vazar informação do futuro para o passado**

#### TimeSeriesSplit (Rolling Window)

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)

for fold, (train_idx, test_idx) in enumerate(tscv.split(X)):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
    
    # Treinar modelo
    model.fit(X_train, y_train)
    
    # Avaliar
    pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, pred, squared=False)
    print(f"Fold {fold}: RMSE = {rmse:.2f}")
```

#### Divisão Recomendada
- **Treino**: 70% (primeiros anos)
- **Validação**: 15% (anos intermediários) - para tuning
- **Teste**: 15% (últimos anos) - avaliação final

Exemplo:
- Treino: 2010-2019
- Validação: 2020-2021
- Teste: 2022-2024

---

### ETAPA 8: Modelagem

#### Modelos a Serem Testados

#### 1. Baseline Estatístico: SARIMA/SARIMAX

**Características**
- Modelo autoregressivo com sazonalidade
- SARIMAX permite variáveis exógenas (clima)
- Interpretável

**Implementação**
```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(
    y_train,
    order=(1, 1, 1),          # (p, d, q)
    seasonal_order=(1, 1, 1, 52),  # (P, D, Q, s) - sazonalidade semanal
    exog=X_train[['temperatura', 'precipitacao']]
)

results = model.fit()
forecast = results.forecast(steps=len(X_test), exog=X_test)
```

#### 2. Prophet (Facebook)

**Características**
- Lida bem com sazonalidade múltipla
- Robusto a missing data
- Fácil de usar

**Implementação**
```python
from prophet import Prophet

model = Prophet(yearly_seasonality=True, weekly_seasonality=False)

# Adicionar regressores
model.add_regressor('temperatura')
model.add_regressor('precipitacao')

model.fit(train_df)
forecast = model.predict(test_df)
```

#### 3. Random Forest

**Características**
- Captura não-linearidades
- Robusto a outliers
- Feature importance interpretável

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    min_samples_split=10,
    random_state=42
)

rf.fit(X_train, y_train)
pred = rf.predict(X_test)
```

#### 4. XGBoost

**Características**
- Estado-da-arte para dados tabulares
- Muito usado em competições
- SHAP para interpretação

```python
import xgboost as xgb

xgb_model = xgb.XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='reg:squarederror',
    random_state=42
)

xgb_model.fit(X_train, y_train)
pred = xgb_model.predict(X_test)
```

#### 5. LSTM (Long Short-Term Memory)

**Características**
- Redes neurais recorrentes
- Captura dependências de longo prazo
- Estado-da-arte para séries temporais

```python
import tensorflow as tf
from tensorflow.keras import layers, models

# Reshapear dados para LSTM: (samples, timesteps, features)
X_train_lstm = X_train.values.reshape((X_train.shape[0], timesteps, n_features))

model = models.Sequential([
    layers.LSTM(64, activation='relu', input_shape=(timesteps, n_features)),
    layers.Dropout(0.2),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X_train_lstm, y_train, epochs=50, batch_size=32, validation_split=0.2)

pred = model.predict(X_test_lstm)
```

#### 6. Ensemble (Stacking/Voting)

```python
from sklearn.ensemble import VotingRegressor

ensemble = VotingRegressor([
    ('rf', rf),
    ('xgb', xgb_model)
])

ensemble.fit(X_train, y_train)
pred = ensemble.predict(X_test)
```

---

### ETAPA 9: Avaliação e Comparação

#### Métricas para Previsão de Contagem

**RMSE (Root Mean Squared Error)**
```python
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(y_true, y_pred, squared=False)
```

**MAE (Mean Absolute Error)**
```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_true, y_pred)
```

**MAPE (Mean Absolute Percentage Error)**
```python
mape = np.mean(np.abs((y_true - y_pred) / (y_true + 1))) * 100
```

#### Métricas para Classificação de Surtos

**Definir Limiar de Surto**
```python
# Exemplo: percentil 75 histórico por município
limiares = df.groupby('ibge_municipio')['casos'].quantile(0.75)

df['surto'] = df.apply(
    lambda row: 1 if row['casos'] > limiares[row['ibge_municipio']] else 0,
    axis=1
)
```

**Métricas de Classificação**
```python
from sklearn.metrics import roc_auc_score, precision_score, recall_score

auc = roc_auc_score(y_true_class, y_pred_proba)
precision = precision_score(y_true_class, y_pred_class)
recall = recall_score(y_true_class, y_pred_class)
```

#### Comparação de Modelos

```python
resultados = pd.DataFrame({
    'Modelo': ['SARIMA', 'Prophet', 'RF', 'XGBoost', 'LSTM'],
    'RMSE': [rmse_sarima, rmse_prophet, rmse_rf, rmse_xgb, rmse_lstm],
    'MAE': [mae_sarima, mae_prophet, mae_rf, mae_xgb, mae_lstm],
    'AUC': [auc_sarima, auc_prophet, auc_rf, auc_xgb, auc_lstm]
})

print(resultados.sort_values('RMSE'))
```

---

### ETAPA 10: Interpretação

#### SHAP para XGBoost
```python
import shap

explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

# Plot
shap.summary_plot(shap_values, X_test)
shap.dependence_plot('temperatura_lag4', shap_values, X_test)
```

#### Análise de Lags Ótimos
- Identificar quais lags são mais importantes por região
- Comparar com literatura

---

### ETAPA 11: Sistema de Alerta

#### Calibração de Limiares
```python
# Limiar adaptativo por município
limiares = df.groupby('ibge_municipio')['casos'].apply(
    lambda x: x.quantile(0.75)  # Ajustar conforme necessário
)

# Classificar previsões
df['alerta'] = df['pred_casos'] > df['ibge_municipio'].map(limiares)
```

---

## 📈 3. TÉCNICAS AVANÇADAS

### Transfer Learning entre Municípios
- Treinar em municípios com muitos dados
- Aplicar em municípios com poucos dados
- Fine-tuning com dados locais

### Modelos Hierárquicos
- Modelos por região (Norte, Nordeste, etc.)
- Compartilhamento de parâmetros

### Nowcasting
- Correção de atraso de notificação
- Previsão do presente (dados ainda não consolidados)

---

## ✅ 4. CHECKLIST METODOLÓGICO

- [ ] Dados brutos coletados e armazenados
- [ ] ETL documentado e reproduzível
- [ ] Limpeza e qualidade verificadas
- [ ] Features criadas e documentadas
- [ ] EDA completa com visualizações
- [ ] Divisão temporal sem vazamento
- [ ] Modelos baseline implementados
- [ ] Modelos avançados implementados
- [ ] Validação cruzada temporal realizada
- [ ] Métricas comparadas entre modelos
- [ ] Interpretação (SHAP) realizada
- [ ] Sistema de alerta calibrado
- [ ] Código versionado no Git
- [ ] Documentação completa

---

*Última atualização: Outubro 2025*

