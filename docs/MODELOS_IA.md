# Modelos de IA - Nomes Exatos

## 📋 Lista Completa dos Modelos que Serão Utilizados

### 1. MODELOS ESTATÍSTICOS (Baseline)

#### 1.1. SARIMA
- **Nome completo**: Seasonal Autoregressive Integrated Moving Average
- **Biblioteca**: `statsmodels.tsa.statespace.sarimax.SARIMAX`
- **Classe**: `SARIMAX`
- **Variante**: SARIMA (sem variáveis exógenas)

#### 1.2. SARIMAX
- **Nome completo**: Seasonal Autoregressive Integrated Moving Average with eXogenous variables
- **Biblioteca**: `statsmodels.tsa.statespace.sarimax.SARIMAX`
- **Classe**: `SARIMAX`
- **Diferença**: Permite incorporar variáveis exógenas (climáticas)

#### 1.3. ARIMA
- **Nome completo**: Autoregressive Integrated Moving Average
- **Biblioteca**: `statsmodels.tsa.arima.model.ARIMA`
- **Classe**: `ARIMA`
- **Nota**: Versão sem sazonalidade (pode ser usado como comparação)

#### 1.4. Prophet
- **Nome completo**: Prophet (Facebook Prophet)
- **Biblioteca**: `prophet.Prophet`
- **Classe**: `Prophet`
- **Desenvolvedor**: Facebook (Meta)

---

### 2. MACHINE LEARNING

#### 2.1. Random Forest
- **Nome completo**: Random Forest Regressor
- **Biblioteca**: `sklearn.ensemble.RandomForestRegressor`
- **Classe**: `RandomForestRegressor`
- **Tipo**: Ensemble de árvores de decisão

#### 2.2. XGBoost
- **Nome completo**: eXtreme Gradient Boosting
- **Biblioteca**: `xgboost.XGBRegressor`
- **Classe**: `XGBRegressor`
- **Desenvolvedor**: Distributed Machine Learning Community

#### 2.3. Gradient Boosting
- **Nome completo**: Gradient Boosting Regressor
- **Biblioteca**: `sklearn.ensemble.GradientBoostingRegressor`
- **Classe**: `GradientBoostingRegressor`
- **Nota**: Pode ser usado como alternativa/comparação ao XGBoost

#### 2.4. LightGBM (Opcional)
- **Nome completo**: Light Gradient Boosting Machine
- **Biblioteca**: `lightgbm.LGBMRegressor`
- **Classe**: `LGBMRegressor`
- **Nota**: Está nas dependências, mas pode ser usado como alternativa

---

### 3. DEEP LEARNING

#### 3.1. LSTM
- **Nome completo**: Long Short-Term Memory
- **Biblioteca**: `tensorflow.keras.layers.LSTM`
- **Classe**: `LSTM` (dentro de `tf.keras.layers`)
- **Framework**: TensorFlow/Keras

#### 3.2. BiLSTM
- **Nome completo**: Bidirectional Long Short-Term Memory
- **Biblioteca**: `tensorflow.keras.layers.Bidirectional` + `LSTM`
- **Classe**: `Bidirectional` (wrapper do LSTM)
- **Framework**: TensorFlow/Keras

#### 3.3. Temporal CNN (Opcional - mencionado no README)
- **Nome completo**: Temporal Convolutional Neural Network
- **Biblioteca**: `tensorflow.keras.layers.Conv1D`
- **Classe**: `Conv1D` (camadas convolucionais 1D)
- **Framework**: TensorFlow/Keras

---

### 4. MODELOS DE ENSEMBLE

#### 4.1. Voting Regressor
- **Nome completo**: Voting Regressor
- **Biblioteca**: `sklearn.ensemble.VotingRegressor`
- **Classe**: `VotingRegressor`
- **Tipo**: Ensemble por votação

#### 4.2. Stacking Regressor (Opcional)
- **Nome completo**: Stacking Regressor
- **Biblioteca**: `sklearn.ensemble.StackingRegressor`
- **Classe**: `StackingRegressor`
- **Tipo**: Ensemble por stacking (meta-learners)

---

## 📦 DEPENDÊNCIAS E BIBLIOTECAS

### Bibliotecas Principais:
- **statsmodels** ≥ 0.14.0 - Para SARIMA/SARIMAX/ARIMA
- **prophet** ≥ 1.1.0 - Para Prophet
- **scikit-learn** ≥ 1.3.0 - Para Random Forest, Gradient Boosting, Voting/Stacking
- **xgboost** ≥ 2.0.0 - Para XGBoost
- **lightgbm** ≥ 4.0.0 - Para LightGBM (opcional)
- **tensorflow** ≥ 2.14.0 - Para LSTM e BiLSTM
- **keras** ≥ 2.14.0 - Interface de alto nível para TensorFlow

---

## 🎯 MODELOS PRINCIPAIS (Foco do Projeto)

### Modelos Obrigatórios (Serão Implementados):

1. **SARIMAX** - Baseline estatístico com variáveis exógenas
2. **Prophet** - Baseline estatístico com sazonalidade
3. **Random Forest** - Machine Learning baseline
4. **XGBoost** - Machine Learning avançado
5. **LSTM** - Deep Learning principal
6. **BiLSTM** - Deep Learning avançado
7. **Voting Regressor** - Ensemble dos melhores modelos

### Modelos Opcionais (Mencionados mas podem não ser implementados):

- **ARIMA** - Comparação com SARIMA
- **Gradient Boosting** - Alternativa ao XGBoost
- **LightGBM** - Alternativa ao XGBoost
- **Temporal CNN** - Alternativa ao LSTM
- **Stacking Regressor** - Alternativa ao Voting

---

## 📝 NOTAÇÃO TÉCNICA PARA O TCC

### Nomes que devem aparecer no texto:

**Modelos Estatísticos:**
- SARIMA (Seasonal Autoregressive Integrated Moving Average)
- SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous variables)
- Prophet (Facebook Prophet)

**Machine Learning:**
- Random Forest
- XGBoost (eXtreme Gradient Boosting)

**Deep Learning:**
- LSTM (Long Short-Term Memory)
- BiLSTM (Bidirectional Long Short-Term Memory)

**Ensemble:**
- Voting Regressor
- Ensemble Methods (termo genérico)

---

## 🔧 IMPLEMENTAÇÃO NO CÓDIGO

### Exemplos de Importação:

```python
# Modelos Estatísticos
from statsmodels.tsa.statespace.sarimax import SARIMAX
from prophet import Prophet

# Machine Learning
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from xgboost import XGBRegressor

# Deep Learning
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout
```

---

## 📊 ORDEM DE IMPLEMENTAÇÃO

1. **Fase 1 - Baseline Estatístico:**
   - SARIMAX
   - Prophet

2. **Fase 2 - Machine Learning:**
   - Random Forest
   - XGBoost

3. **Fase 3 - Deep Learning:**
   - LSTM
   - BiLSTM

4. **Fase 4 - Ensemble:**
   - Voting Regressor (combinando os melhores modelos)

---

*Última atualização: Janeiro 2025*

