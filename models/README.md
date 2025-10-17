# Modelos de Predição de Dengue# Diretório de Modelos



Este diretório contém os modelos de machine learning e estatísticos para previsão de surtos de dengue.Este diretório contém os modelos treinados e artefatos relacionados.



## 📊 Modelo SARIMA## 📂 Estrutura



**SARIMA** = Seasonal AutoRegressive Integrated Moving Average```

models/

Modelo estatístico clássico para séries temporais com sazonalidade, baseado em **Xavier et al. (2021) - PLOS ONE**.├── baseline/          # Modelos baseline (SARIMA, Prophet)

├── ml/                # Modelos ML (RF, XGBoost)

### Características├── dl/                # Modelos DL (LSTM, BiLSTM)

├── ensemble/          # Modelos ensemble

- **Sazonalidade**: 52 semanas (ciclo anual)├── checkpoints/       # Checkpoints durante treinamento

- **Variáveis exógenas**: Dados climáticos (precipitação acumulada, temperatura, índice de risco)└── configs/           # Configurações de modelos (YAML/JSON)

- **Lag temporal**: 1-2 meses (4-8 semanas) - achado crítico do paper```

- **Estrutura**: SARIMA(1,1,1)(1,1,1)[52]

  - (1,1,1): ordem não-sazonal (AR, diferenciação, MA)## ⚠️ Importante

  - (1,1,1,52): ordem sazonal com período de 52 semanas

- **Modelos treinados NÃO são versionados** no Git (são muito grandes)

### Arquivos- **Configurações e metadados SÃO versionados**

- Use versionamento semântico para modelos (v1.0.0, v1.1.0, etc.)

```

models/## 💾 Formatos de Salvamento

├── train_sarima.py              # Script de treinamento

└── README.md                    # Esta documentação### Scikit-learn / XGBoost

```python

data/processed/models/import joblib

├── sarima_dengue_v1.pkl         # Modelo treinado (54 MB)

├── sarima_dengue_v1.pkl.json    # Metadados (AIC, BIC, métricas)# Salvar

├── diagnostics_*.png            # Gráficos de diagnóstico (ACF, PACF)joblib.dump(model, 'models/ml/xgboost_v1.0.0.pkl')

└── forecast_*.png               # Visualização de previsões

```# Carregar

model = joblib.load('models/ml/xgboost_v1.0.0.pkl')

### Uso```



#### Treinar modelo### Keras / TensorFlow

```bash```python

cd models# Salvar

python train_sarima.pymodel.save('models/dl/lstm_v1.0.0.h5')

```

# Carregar

#### Carregar modelo salvofrom tensorflow.keras.models import load_model

```pythonmodel = load_model('models/dl/lstm_v1.0.0.h5')

from train_sarima import SARIMADengueModel```



# Carregar### Statsmodels

results = SARIMADengueModel.load_model('../data/processed/models/sarima_dengue_v1.pkl')```python

# Salvar

# Fazer previsãoresults.save('models/baseline/sarima_v1.0.0.pkl')

forecast = results.forecast(steps=12, exog=X_test)  # 12 semanas à frente

```# Carregar

from statsmodels.iolib.smpickle import load_pickle

### Métricas de Desempenho (Dados Simulados)results = load_pickle('models/baseline/sarima_v1.0.0.pkl')

```

**⚠️ IMPORTANTE**: Estes resultados são com dados SIMULADOS. Serão atualizados quando dados reais do SINAN estiverem disponíveis.

## 📋 Metadados do Modelo

- **MAE**: 44 casos (erro absoluto médio)

- **RMSE**: 49 casos (raiz do erro quadrático médio)Para cada modelo treinado, salve um arquivo JSON com metadados:

- **MAPE**: 24.62% (erro percentual médio absoluto)

- **R²**: -3.87 (coeficiente de determinação)```json

{

**Nota**: R² negativo indica que o modelo atualmente não está performando bem - esperado com dados simulados e série curta (40 semanas).  "model_name": "xgboost_municipios_v1.0.0",

  "model_type": "XGBRegressor",

### Parâmetros do Modelo  "training_date": "2025-10-15",

  "data_period": "2010-2024",

#### Ordem não-sazonal (p,d,q) = (1,1,1)  "features": ["temperatura_lag4", "precipitacao_lag8", "casos_lag1"],

- **p=1**: 1 lag auto-regressivo (AR)  "hyperparameters": {

- **d=1**: 1 diferenciação (tornar série estacionária)    "n_estimators": 500,

- **q=1**: 1 lag de média móvel (MA)    "max_depth": 6,

    "learning_rate": 0.05

#### Ordem sazonal (P,D,Q,s) = (1,1,1,52)  },

- **P=1**: 1 lag sazonal AR  "performance": {

- **D=1**: 1 diferenciação sazonal    "train_rmse": 23.4,

- **Q=1**: 1 lag sazonal MA    "val_rmse": 28.1,

- **s=52**: período sazonal (52 semanas = 1 ano)    "test_rmse": 31.7,

    "train_mae": 15.2,

### Variáveis Exógenas (Clima)    "val_mae": 18.9,

    "test_mae": 21.3

Baseadas em **Xavier et al. (2021)**:  },

  "file_size_mb": 245.8,

1. **`precip_acum_8sem`**: Precipitação acumulada 8 semanas (2 meses)  "notes": "Modelo treinado em todos os municípios com >5 anos de dados"

   - **ACHADO CRÍTICO DO PAPER**: Lag de 1-2 meses é mais preditivo}

   ```

2. **`temp_favoravel`**: Temperatura ≥22°C (threshold biológico)

   - Aumenta população de Aedes aegypti## 🏆 Registro de Modelos

   

3. **`indice_risco_dengue`**: Índice composto (0-4 pontos)Mantenha uma tabela comparativa:

   - Combina temperatura + precipitação + umidade

| Modelo | Versão | RMSE (test) | MAE (test) | Data | Notebook |

### Diagnósticos|--------|--------|-------------|------------|------|----------|

| SARIMA | v1.0.0 | 45.2 | 32.1 | 2025-10-01 | `baseline_models.ipynb` |

#### Teste de Estacionariedade (ADF)| Prophet | v1.0.0 | 42.8 | 30.5 | 2025-10-01 | `baseline_models.ipynb` |

- **P-valor > 0.05**: Série NÃO estacionária (esperado)| RandomForest | v1.0.0 | 35.6 | 24.2 | 2025-10-15 | `ml_models.ipynb` |

- **Solução**: Diferenciação (d=1, D=1)| XGBoost | v1.0.0 | 31.7 | 21.3 | 2025-10-20 | `ml_models.ipynb` |

| LSTM | v1.0.0 | 29.4 | 19.8 | 2025-11-05 | `dl_models.ipynb` |

#### Gráficos ACF/PACF| Ensemble | v1.0.0 | 28.1 | 18.5 | 2025-11-10 | `ensemble.ipynb` |

- **ACF**: Identifica componente MA e sazonalidade

- **PACF**: Identifica componente AR## 🔄 Versionamento



Arquivos salvos em `data/processed/models/diagnostics_*.png`Use versionamento semântico:

- **Major** (1.0.0): Mudanças grandes (nova arquitetura, novas features)

### Limitações Atuais- **Minor** (1.1.0): Melhorias (tuning, mais dados)

- **Patch** (1.0.1): Correções de bugs

1. **Dados simulados**: Modelo precisa ser retreinado com dados reais do SINAN

2. **Série curta**: Apenas 40 semanas (ideal: 2-3 anos = 104-156 semanas)## 📊 Monitoramento de Modelos

3. **Sem dados de dengue**: Aguardando download do SINAN

4. **Componente sazonal limitado**: s=52 requer pelo menos 104 observações para funcionar bem### Durante o Treinamento

- Salve checkpoints a cada N epochs (modelos DL)

### Próximos Passos- Registre métricas de treino e validação

- Use TensorBoard ou logs para acompanhar

1. ✅ **Implementar SARIMA** - CONCLUÍDO

2. ⏳ **Download dados SINAN** - Pendente### Após o Treinamento

3. ⏳ **Join espacial** (estações → municípios) - Pendente- Avalie em conjunto de teste separado

4. ⏳ **Retreinar com dados reais** - Pendente- Calcule intervalos de confiança

5. ⏳ **Comparar com XGBoost e LSTM** - Pendente- Teste em diferentes subgrupos (regiões, tamanhos de município)



### Referências Científicas## 🧪 Boas Práticas



**Xavier, D. R., et al. (2021)**  1. **Sempre salve o preprocessor junto com o modelo**

*"Analysis of climate factors and dengue incidence in the metropolitan region of Rio de Janeiro, Brazil"*     ```python

PLOS ONE 16(5): e0251403     joblib.dump({

DOI: [10.1371/journal.pone.0251403](https://doi.org/10.1371/journal.pone.0251403)       'model': model,

       'scaler': scaler,

**Achados principais**:       'feature_names': feature_names

- Lag de 1-2 meses para precipitação   }, 'model_bundle.pkl')

- Temperatura >22-24°C aumenta vetor   ```

- Padrão epidêmico: 4-6 semanas crescimento + 10-12 semanas explosão

- Pico: Abril-Maio (outono, após verão chuvoso)2. **Documente decisões de modelagem**

- Modelo ARMAX mensal   - Por que escolheu esses hiperparâmetros?

   - Quais features foram removidas e por quê?

## 🚀 Outros Modelos (Em Desenvolvimento)   - Houve overfitting? Como foi tratado?



### XGBoost3. **Mantenha reprodutibilidade**

- Gradient boosting para séries temporais   - Fixe random seeds

- Permite features não-lineares   - Documente versões de bibliotecas

- Rápido e eficiente   - Salve configurações de treino



### LSTM## 🚀 Deployment

- Rede neural recorrente

- Captura dependências temporais longasPara colocar modelo em produção:

- Requer mais dados e poder computacional1. Salvar modelo + preprocessor + metadados

2. Criar script de inferência

---3. Testar com dados de exemplo

4. Documentar API (se aplicável)

**Autor**: Pedro Lucas Santana  

**TCC**: Predição de Surtos de Dengue usando Machine Learning  ## 🔗 Recursos

**Instituição**: Universidade de Brasília (UnB)  

**Data**: Outubro 2025- [Scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)

- [Keras Model Saving](https://keras.io/api/models/model_saving_apis/)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) (opcional)

---

*Para mais informações sobre modelagem, consulte `docs/04-metodologia.md`*

