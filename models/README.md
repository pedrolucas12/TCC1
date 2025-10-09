# Diretório de Modelos

Este diretório contém os modelos treinados e artefatos relacionados.

## 📂 Estrutura

```
models/
├── baseline/          # Modelos baseline (SARIMA, Prophet)
├── ml/                # Modelos ML (RF, XGBoost)
├── dl/                # Modelos DL (LSTM, BiLSTM)
├── ensemble/          # Modelos ensemble
├── checkpoints/       # Checkpoints durante treinamento
└── configs/           # Configurações de modelos (YAML/JSON)
```

## ⚠️ Importante

- **Modelos treinados NÃO são versionados** no Git (são muito grandes)
- **Configurações e metadados SÃO versionados**
- Use versionamento semântico para modelos (v1.0.0, v1.1.0, etc.)

## 💾 Formatos de Salvamento

### Scikit-learn / XGBoost
```python
import joblib

# Salvar
joblib.dump(model, 'models/ml/xgboost_v1.0.0.pkl')

# Carregar
model = joblib.load('models/ml/xgboost_v1.0.0.pkl')
```

### Keras / TensorFlow
```python
# Salvar
model.save('models/dl/lstm_v1.0.0.h5')

# Carregar
from tensorflow.keras.models import load_model
model = load_model('models/dl/lstm_v1.0.0.h5')
```

### Statsmodels
```python
# Salvar
results.save('models/baseline/sarima_v1.0.0.pkl')

# Carregar
from statsmodels.iolib.smpickle import load_pickle
results = load_pickle('models/baseline/sarima_v1.0.0.pkl')
```

## 📋 Metadados do Modelo

Para cada modelo treinado, salve um arquivo JSON com metadados:

```json
{
  "model_name": "xgboost_municipios_v1.0.0",
  "model_type": "XGBRegressor",
  "training_date": "2025-10-15",
  "data_period": "2010-2024",
  "features": ["temperatura_lag4", "precipitacao_lag8", "casos_lag1"],
  "hyperparameters": {
    "n_estimators": 500,
    "max_depth": 6,
    "learning_rate": 0.05
  },
  "performance": {
    "train_rmse": 23.4,
    "val_rmse": 28.1,
    "test_rmse": 31.7,
    "train_mae": 15.2,
    "val_mae": 18.9,
    "test_mae": 21.3
  },
  "file_size_mb": 245.8,
  "notes": "Modelo treinado em todos os municípios com >5 anos de dados"
}
```

## 🏆 Registro de Modelos

Mantenha uma tabela comparativa:

| Modelo | Versão | RMSE (test) | MAE (test) | Data | Notebook |
|--------|--------|-------------|------------|------|----------|
| SARIMA | v1.0.0 | 45.2 | 32.1 | 2025-10-01 | `baseline_models.ipynb` |
| Prophet | v1.0.0 | 42.8 | 30.5 | 2025-10-01 | `baseline_models.ipynb` |
| RandomForest | v1.0.0 | 35.6 | 24.2 | 2025-10-15 | `ml_models.ipynb` |
| XGBoost | v1.0.0 | 31.7 | 21.3 | 2025-10-20 | `ml_models.ipynb` |
| LSTM | v1.0.0 | 29.4 | 19.8 | 2025-11-05 | `dl_models.ipynb` |
| Ensemble | v1.0.0 | 28.1 | 18.5 | 2025-11-10 | `ensemble.ipynb` |

## 🔄 Versionamento

Use versionamento semântico:
- **Major** (1.0.0): Mudanças grandes (nova arquitetura, novas features)
- **Minor** (1.1.0): Melhorias (tuning, mais dados)
- **Patch** (1.0.1): Correções de bugs

## 📊 Monitoramento de Modelos

### Durante o Treinamento
- Salve checkpoints a cada N epochs (modelos DL)
- Registre métricas de treino e validação
- Use TensorBoard ou logs para acompanhar

### Após o Treinamento
- Avalie em conjunto de teste separado
- Calcule intervalos de confiança
- Teste em diferentes subgrupos (regiões, tamanhos de município)

## 🧪 Boas Práticas

1. **Sempre salve o preprocessor junto com o modelo**
   ```python
   joblib.dump({
       'model': model,
       'scaler': scaler,
       'feature_names': feature_names
   }, 'model_bundle.pkl')
   ```

2. **Documente decisões de modelagem**
   - Por que escolheu esses hiperparâmetros?
   - Quais features foram removidas e por quê?
   - Houve overfitting? Como foi tratado?

3. **Mantenha reprodutibilidade**
   - Fixe random seeds
   - Documente versões de bibliotecas
   - Salve configurações de treino

## 🚀 Deployment

Para colocar modelo em produção:
1. Salvar modelo + preprocessor + metadados
2. Criar script de inferência
3. Testar com dados de exemplo
4. Documentar API (se aplicável)

## 🔗 Recursos

- [Scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)
- [Keras Model Saving](https://keras.io/api/models/model_saving_apis/)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) (opcional)

---

*Para mais informações sobre modelagem, consulte `docs/04-metodologia.md`*

