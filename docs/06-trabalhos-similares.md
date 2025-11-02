# Trabalhos Similares

> Análise de trabalhos relacionados à previsão de surtos de dengue utilizando Machine Learning, Deep Learning e dados climáticos.

---

## 📚 Visão Geral

Esta seção apresenta trabalhos relevantes que abordam a previsão de casos de dengue utilizando diferentes abordagens metodológicas, com foco especial em:

- Modelos de Machine Learning e Deep Learning
- Uso de dados climáticos e meteorológicos
- Aplicações no contexto brasileiro
- Sistemas de vigilância e alerta precoce

---

## 🇧🇷 Trabalho 1: InfoDengue - Sistema de Alerta Nacional

### 📋 Informações Gerais

- **Plataforma**: [InfoDengue](https://info.dengue.mat.br/)
- **Instituições**: FIOCRUZ, FGV/EMAp
- **Escopo**: Sistema nacional de vigilância e alerta para dengue, zika e chikungunya
- **Status**: Operacional desde ~2015, atualização semanal

### 🎯 Objetivo

Fornecer alertas semanais sobre risco de surtos de dengue para municípios brasileiros, integrando dados epidemiológicos e climáticos em tempo real.

### 🔧 Metodologia

#### Dados Utilizados
- **Epidemiológicos**: Casos notificados do SINAN (atualização semanal)
- **Climáticos**: Dados meteorológicos de estações locais
- **Populacional**: Dados censitários do IBGE
- **Geográficos**: Informações municipais

#### Técnicas de Modelagem
- **Nowcasting**: Estimativa de casos em tempo real (correção de atraso de notificação)
- **Modelos estatísticos**: Para estimativa de incidência corrigida
- **Indicadores de alerta**: Classificação em níveis de risco (verde, amarelo, laranja, vermelho)
- **Análise espacial**: Identificação de condições favoráveis à transmissão

### 📊 Resultados e Contribuições

#### Funcionalidades
- ✅ **Relatórios municipais e estaduais**: Atualização semanal
- ✅ **API pública**: Acesso programático aos dados
- ✅ **Visualizações interativas**: Mapas e gráficos temporais
- ✅ **Sistema de alertas**: Classificação por níveis de atenção

#### Impacto
- Usado por secretarias de saúde em todo o Brasil
- Referência para tomada de decisão em saúde pública
- Integração com ações de controle vetorial

### 💡 Relevância para este TCC

- **Fonte de dados**: InfoDengue pode fornecer dados processados e validados
- **Benchmark**: Sistema operacional para comparação de performance
- **Metodologia**: Técnicas de nowcasting e definição de limiares de alerta
- **Validação**: Casos reais de uso em gestão de saúde pública

### 🔗 Links
- Site principal: https://info.dengue.mat.br/
- Relatórios: https://info.dengue.mat.br/report/
- API: https://info.dengue.mat.br/services/api

---

## 🧠 Trabalho 2: LSTM com SHAP para Previsão de Dengue no Brasil

### 📋 Informações Gerais

- **Título**: "Forecasting dengue across Brazil with LSTM neural networks and SHAP-driven lagged climate and spatial effects"
- **Autores**: Chen, X., Moraga, P.
- **Publicação**: BMC Public Health (2025)
- **DOI**: 10.1186/s12889-025-22106-7
- **Tipo**: Artigo científico (peer-reviewed)

### 🎯 Objetivo

Desenvolver um modelo de previsão de dengue para o Brasil utilizando redes LSTM, incorporando efeitos climáticos com lags temporais e efeitos espaciais, com interpretabilidade via SHAP.

### 🔧 Metodologia

#### Dados Utilizados
- **Período**: Dados históricos de dengue no Brasil
- **Variáveis climáticas**: Temperatura, precipitação, umidade (com diferentes lags temporais)
- **Variáveis espaciais**: Informações geográficas e de municípios vizinhos
- **Granularidade**: Municipal

#### Técnicas de Modelagem
- **Arquitetura**: LSTM (Long Short-Term Memory)
- **Feature engineering**: 
  - Lags climáticos (exploração de diferentes janelas temporais)
  - Efeitos espaciais (correlação com municípios vizinhos)
- **Interpretabilidade**: SHAP (SHapley Additive exPlanations) para explicar contribuições das features

#### Validação
- Validação temporal (train/test split temporal)
- Métricas de performance para previsão de séries temporais

### 📊 Resultados e Contribuições

#### Principais Achados
- ✅ **LSTM demonstrou boa adaptabilidade**: Captura padrões complexos e não-lineares
- ✅ **Robustez do modelo**: Performance consistente em diferentes regiões
- ✅ **Importância dos lags**: Identificação de janelas temporais ótimas para variáveis climáticas
- ✅ **Efeitos espaciais**: Informação de municípios vizinhos melhora previsões
- ✅ **Interpretabilidade**: SHAP permite entender quais features são mais importantes

#### Métricas
- Performance superior a modelos baseline
- Capacidade de capturar sazonalidade e tendências

### 💡 Relevância para este TCC

- **Arquitetura LSTM**: Referência para implementação de deep learning
- **SHAP para interpretabilidade**: Técnica essencial para explicar modelos complexos
- **Análise de lags**: Metodologia para identificar janelas temporais ótimas
- **Efeitos espaciais**: Abordagem para incorporar informação geográfica
- **Contexto brasileiro**: Estudo específico para a realidade do Brasil

### 🔗 Links
- Artigo: https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22106-7

---

## 🤖 Trabalho 3: Machine Learning para Previsão de Dengue em Cidades Brasileiras

### 📋 Informações Gerais

- **Título**: "Machine-Learning-Based Forecasting of Dengue Fever in Brazilian Cities Using Epidemiologic and Meteorological Variables"
- **Autores**: Roster, K., Connaughton, C., Rodrigues, F.A.
- **Publicação**: American Journal of Epidemiology (2022)
- **DOI**: 10.1093/aje/kwac090
- **PMID**: 35584963

### 🎯 Objetivo

Desenvolver e comparar diferentes modelos de machine learning para previsão mensal de casos de dengue em cidades brasileiras, avaliando a contribuição de variáveis epidemiológicas e meteorológicas.

### 🔧 Metodologia

#### Dados Utilizados
- **Período**: 2007-2019 (12 anos)
- **Variáveis epidemiológicas**: Casos mensais históricos de dengue
- **Variáveis meteorológicas**: Dados climáticos locais
- **Escopo**: Múltiplas cidades brasileiras (geograficamente diversas)
- **Horizonte de previsão**: 1 mês à frente

#### Algoritmos Comparados
1. **Random Forest** (melhor desempenho geral)
2. **Gradient Boosting Regression**
3. **Feed-Forward Neural Network** (Rede Neural densa)
4. **Support Vector Regression (SVR)**
5. **Seasonal Naive Baseline** (baseline para comparação)

#### Feature Selection
- Comparação de diferentes métodos de seleção de features
- Avaliação da contribuição de variáveis epidemiológicas vs meteorológicas

#### Validação
- Validação temporal (train/test split)
- Avaliação out-of-sample
- Análise de erro por cidade

### 📊 Resultados e Contribuições

#### Principais Achados
- ✅ **Random Forest com casos históricos**: Melhor modelo geral
  - Treinado principalmente em casos mensais de dengue
  - Produziu menores erros que todos os outros modelos
- ✅ **Variabilidade regional**: Diferentes modelos funcionam melhor em diferentes cidades
- ✅ **Performance superior ao baseline**: Todos os modelos ML superaram o baseline sazonal ingênuo

#### Métricas
- **MAE mediano**: 12.2 casos por mês (todas as cidades)
- **MAE otimizado**: 11.9 casos (selecionando melhor modelo por cidade)
- Erros baixos considerando diversidade geográfica

#### Contribuições
- Demonstração da utilidade de **ensemble de árvores de decisão** para vigilância de dengue
- Evidência de que **modelos específicos por cidade** podem melhorar performance
- Validação em dataset geograficamente diverso (generalização)

### 💡 Relevância para este TCC

- **Comparação de algoritmos**: Metodologia para avaliar múltiplos modelos ML
- **Feature selection**: Técnicas para identificar variáveis mais importantes
- **Validação robusta**: Abordagem temporal e geográfica
- **Benchmark brasileiro**: Resultados em cidades brasileiras para comparação
- **Ensemble models**: Random Forest como forte baseline ML
- **Análise de heterogeneidade**: Necessidade de modelos específicos por região

### 📈 Implicações Práticas

- Machine learning pode contribuir significativamente para vigilância de dengue
- Modelos de ensemble (Random Forest, XGBoost) são particularmente eficazes
- Importância de validação em múltiplas cidades para garantir generalização

### 🔗 Links
- PubMed: https://pubmed.ncbi.nlm.nih.gov/35584963/
- DOI: https://doi.org/10.1093/aje/kwac090

---

## 📊 Comparação entre os Trabalhos

| Aspecto | InfoDengue | Chen & Moraga (2025) | Roster et al. (2022) |
|---------|------------|----------------------|----------------------|
| **Tipo** | Sistema operacional | Pesquisa acadêmica | Pesquisa acadêmica |
| **Modelo principal** | Nowcasting + estatística | LSTM + SHAP | Random Forest |
| **Horizonte** | Tempo real (correção atraso) | Variável | 1 mês |
| **Dados climáticos** | ✅ Sim | ✅ Sim (com lags) | ✅ Sim |
| **Escopo geográfico** | Nacional (todos municípios) | Brasil (municipal) | Múltiplas cidades BR |
| **Interpretabilidade** | Relatórios semanais | ✅ SHAP | Feature importance |
| **Uso prático** | ✅ Operacional | Pesquisa | Pesquisa |
| **Período de dados** | Atualização contínua | Histórico | 2007-2019 |
| **Espacialidade** | Mapas e análise espacial | ✅ Efeitos espaciais | Multi-cidades |

---

## 🎯 Lacunas e Oportunidades para este TCC

### 1. Comparação Sistemática de Métodos
- **Lacuna**: Poucos trabalhos comparam estatística, ML e DL no mesmo framework
- **Oportunidade**: Implementar SARIMA, XGBoost e LSTM com mesmos dados

### 2. Análise Regional de Lags
- **Lacuna**: Variação regional de lags climáticos pouco explorada
- **Oportunidade**: Análise detalhada por região geográfica (Norte, Nordeste, etc.)

### 3. Transfer Learning para Municípios Pequenos
- **Lacuna**: Municípios com poucos dados históricos são difíceis de modelar
- **Oportunidade**: Usar informação de municípios vizinhos (spatial features)

### 4. Pipeline Reproduzível e Open Source
- **Lacuna**: Muitos trabalhos não disponibilizam código ou dados
- **Oportunidade**: Código completo no GitHub, documentação detalhada, reproduzível

### 5. Integração de Múltiplas Fontes Climáticas
- **Lacuna**: Uso limitado a dados locais (estações)
- **Oportunidade**: Combinar INMET, CHIRPS, ERA5 (satélite + reanalysis)

### 6. Sistema de Alerta Calibrado
- **Lacuna**: Limiares de alerta muitas vezes arbitrários
- **Oportunidade**: Calibração baseada em dados, otimização de precision/recall

---

## 📖 Outras Referências Relevantes

### Trabalhos Citados nos Artigos
- **Xu et al. (2020)**: "Forecast of Dengue Cases in 20 Chinese Cities Based on the Deep Learning Method"
- **Patil & Pandya (2021)**: "Forecasting Dengue Hotspots Associated With Variation in Meteorological Parameters"
- **Sylvestre et al. (2022)**: "Data-driven methods for dengue prediction and surveillance using real-world and Big Data: A systematic review"

### Temas para Revisão Adicional
- Modelos epidemiológicos compartimentais (SIR, SEIR)
- Nowcasting para correção de atraso de notificação
- Modelos espaço-temporais (STARIMA, ConvLSTM)
- Ensemble learning para séries temporais
- Calibração de sistemas de alerta

---

## ✅ Principais Aprendizados

### 🔬 Metodológicos

1. **Validação temporal é essencial**: Train/test splits temporais evitam data leakage
2. **Feature engineering é crítico**: Lags, médias móveis, anomalias climáticas
3. **Interpretabilidade importa**: SHAP, feature importance para explicar modelos
4. **Ensemble models funcionam bem**: Random Forest, XGBoost consistentemente bons
5. **Deep Learning precisa justificativa**: LSTM útil para padrões complexos, mas requer mais dados

### 🌍 Contextuais

1. **Heterogeneidade regional**: Brasil é diverso, modelos podem variar por região
2. **Dados climáticos são preditivos**: Temperatura, precipitação, umidade relevantes
3. **Lags variam**: Relação clima-dengue tem defasagem temporal (2-12 semanas)
4. **Sistemas operacionais existem**: InfoDengue é referência nacional
5. **Generalização é desafio**: Modelos precisam funcionar em múltiplas cidades

---

## �️ Tecnologias Escolhidas para o Projeto

Esta seção descreve as ferramentas, plataformas e tecnologias que serão utilizadas no desenvolvimento deste TCC, cobrindo aspectos de modelagem, armazenamento de dados, processamento e deployment.

---

### 💾 Armazenamento e Infraestrutura de Dados

#### Opção 1: Google Cloud Platform (GCP) - **RECOMENDADO**

**Justificativa:**
- ✅ **Créditos educacionais**: Google Cloud oferece $300 em créditos gratuitos + créditos adicionais para estudantes
- ✅ **BigQuery**: Data warehouse escalável ideal para séries temporais
- ✅ **Cloud Storage**: Armazenamento de dados brutos (SINAN, CHIRPS, ERA5)
- ✅ **Vertex AI**: Plataforma integrada para ML/DL, notebooks gerenciados
- ✅ **Earth Engine**: Acesso direto a dados climáticos de satélite

**Serviços a serem utilizados:**

| Serviço | Uso | Custo Estimado |
|---------|-----|----------------|
| **Cloud Storage** | Raw data (SINAN, clima) | ~$5/mês (50GB) |
| **BigQuery** | Data warehouse, queries SQL | ~$10/mês (200GB) |
| **Vertex AI Notebooks** | Jupyter Notebooks gerenciados | ~$20/mês (quando ativo) |
| **Vertex AI Training** | Treinamento de modelos (LSTM) | ~$10-30/job |
| **Cloud Run** | API de previsão + Dashboard | ~$5/mês |

**Total estimado:** $50-100/mês (coberto por créditos educacionais)

**Arquitetura proposta:**
```
Raw Data (Cloud Storage)
    ↓
ETL (Cloud Functions / Dataflow)
    ↓
BigQuery (Data Warehouse)
    ↓
Vertex AI (Modeling)
    ↓
Cloud Storage (Modelos treinados)
    ↓
Cloud Run (API + Dashboard)
```

---

#### Opção 2: Amazon Web Services (AWS)

**Justificativa:**
- ✅ **AWS Educate**: Créditos gratuitos para estudantes
- ✅ **S3**: Armazenamento de dados
- ✅ **Athena**: Queries SQL sobre S3 (serverless)
- ✅ **SageMaker**: Plataforma completa de ML/DL
- ✅ **EC2**: Máquinas virtuais para processamento pesado

**Serviços equivalentes:**

| Serviço AWS | Equivalente GCP | Uso |
|-------------|-----------------|-----|
| **S3** | Cloud Storage | Raw data |
| **Athena** | BigQuery | Data warehouse |
| **SageMaker** | Vertex AI | ML/DL platform |
| **Lambda** | Cloud Functions | ETL serverless |
| **EC2** | Compute Engine | VMs para processamento |

---

#### Opção 3: Solução Híbrida (Local + Cloud)

**Para orçamento limitado:**
- **Local (Laptop)**: Desenvolvimento, EDA, modelos pequenos
- **Google Colab Pro**: Treinamento de modelos DL (~$10/mês)
- **GitHub**: Versionamento de código
- **PostgreSQL local + Parquet**: Armazenamento de dados processados
- **Streamlit Cloud**: Dashboard gratuito (500MB)

---

### 🤖 Modelos e Bibliotecas de Machine Learning

#### Modelos Estatísticos

**Bibliotecas:**
```python
# Séries Temporais Clássicas
statsmodels==0.14.0      # ARIMA, SARIMA, SARIMAX
prophet==1.1.5           # Prophet (Meta/Facebook)
pmdarima==2.0.4          # Auto-ARIMA
```

**Justificativa:**
- SARIMA: Baseline clássico, bem estabelecido na literatura
- Prophet: Robusto a dados faltantes, fácil interpretação de sazonalidade

---

#### Modelos de Machine Learning

**Bibliotecas:**
```python
# Ensemble Methods
scikit-learn==1.3.0      # Random Forest, Gradient Boosting
xgboost==2.0.0           # XGBoost (melhor performance em tabular)
lightgbm==4.1.0          # LightGBM (alternativa rápida)
catboost==1.2.0          # CatBoost (handling de categorias)

# Feature Engineering
featuretools==1.28.0     # Automated feature engineering
tsfresh==0.20.0          # Time series feature extraction
```

**Justificativa:**
- XGBoost: Estado da arte para dados tabulares, usado em Roster et al. (2022)
- Scikit-learn: Random Forest como baseline ML
- LightGBM/CatBoost: Alternativas para comparação

---

#### Modelos de Deep Learning

**Bibliotecas:**
```python
# Deep Learning Frameworks
tensorflow==2.14.0       # Framework principal
keras==2.14.0            # API de alto nível
pytorch==2.1.0           # Alternativa (se necessário)

# Arquiteturas Específicas
tensorflow-addons==0.22.0  # Camadas adicionais
keras-tuner==1.4.0         # Hyperparameter tuning
```

**Arquiteturas a implementar:**
1. **LSTM** (Long Short-Term Memory): Baseline DL
2. **BiLSTM** (Bidirectional LSTM): Captura contexto passado e futuro
3. **GRU** (Gated Recurrent Unit): Alternativa mais leve
4. **CNN-LSTM**: Híbrido para padrões espaciais e temporais

**Justificativa:**
- LSTM: Usado em Chen & Moraga (2025), padrão para séries temporais
- TensorFlow/Keras: Ecosistema maduro, integração com Google Cloud

---

#### Modelos Pré-treinados do Hugging Face 🤗

**Opções a explorar:**

##### 1. TimeGPT (Nixtla)
```python
from nixtla import TimeGPT
```
- **Descrição**: Modelo foundation pré-treinado para séries temporais
- **Uso**: Zero-shot forecasting sem fine-tuning
- **Prós**: State-of-the-art, sem necessidade de treino
- **Contras**: API paga após período trial

##### 2. Chronos (Amazon)
```python
from chronos import ChronosPipeline
```
- **Descrição**: Família de modelos transformer para forecasting
- **Modelos**: chronos-t5-tiny, chronos-t5-small, chronos-t5-base
- **Uso**: Fine-tuning em dados de dengue
- **Prós**: Open source, diferentes tamanhos, bons resultados
- **Contras**: Requer GPU para modelos maiores

##### 3. Lag-Llama
```python
from lag_llama import LagLlamaModel
```
- **Descrição**: Modelo transformer pré-treinado especificamente para séries temporais univariadas
- **Uso**: Fine-tuning ou zero-shot
- **Prós**: Especializado em forecasting, open source
- **Contras**: Documentação limitada

##### 4. Informer / Autoformer
```python
from transformers import InformerModel, AutoformerModel
```
- **Descrição**: Transformers otimizados para séries temporais longas
- **Uso**: Long sequence time-series forecasting
- **Prós**: Eficiente para séries longas, atenção sparse
- **Contras**: Mais complexo de implementar

**Estratégia de uso:**
1. **Baseline Hugging Face**: Testar Chronos zero-shot
2. **Fine-tuning**: Adaptar Chronos-T5-small aos dados brasileiros
3. **Comparação**: Avaliar vs modelos tradicionais (LSTM custom)
4. **Transfer Learning**: Usar embeddings de modelos pré-treinados como features

**Links:**
- Chronos: https://huggingface.co/amazon/chronos-t5-small
- Lag-Llama: https://huggingface.co/time-series-foundation-models/Lag-Llama
- TimeGPT: https://nixtla.github.io/nixtla/

---

### 📊 Interpretabilidade e Análise

**Bibliotecas:**
```python
# Interpretabilidade
shap==0.43.0             # SHAP values (Chen & Moraga, 2025)
lime==0.2.0              # Local Interpretable Model-agnostic Explanations
eli5==0.13.0             # Feature importance

# Visualização
plotly==5.17.0           # Gráficos interativos
matplotlib==3.8.0        # Gráficos estáticos
seaborn==0.13.0          # Visualizações estatísticas
folium==0.15.0           # Mapas interativos
```

**Justificativa:**
- SHAP: Estado da arte em interpretabilidade, usado em trabalhos similares
- Plotly: Dashboards interativos de qualidade

---

### 🗄️ Processamento de Dados Geoespaciais

**Bibliotecas:**
```python
# Dados Geoespaciais
geopandas==0.14.0        # DataFrames geoespaciais
rasterio==1.3.9          # Processamento de rasters (CHIRPS, ERA5)
xarray==2023.10.0        # Dados multidimensionais (NetCDF)
earthengine-api==0.1.377 # Google Earth Engine

# Zonal Statistics
rasterstats==0.19.0      # Estatísticas zonais (clima por município)
shapely==2.0.2           # Geometrias
```

**Justificativa:**
- GeoPandas: Padrão para dados geoespaciais em Python
- Rasterio/xarray: Processar dados climáticos de satélite (NetCDF, GeoTIFF)
- Earth Engine: Acesso a dados climáticos pré-processados

---

### 🚀 Deployment e Produtização

#### Dashboard e Visualização

**Opção 1: Streamlit (RECOMENDADO para TCC)**
```python
streamlit==1.28.0
```
- **Prós**: Fácil de desenvolver, gratuito no Streamlit Cloud
- **Contras**: Menos customizável

**Opção 2: Plotly Dash**
```python
dash==2.14.0
```
- **Prós**: Mais customizável, componentes React
- **Contras**: Requer mais código

**Opção 3: Gradio**
```python
gradio==4.0.0
```
- **Prós**: Focado em ML, integração com Hugging Face Spaces
- **Contras**: Menos flexível para dashboards complexos

---

#### API de Previsão

**FastAPI (RECOMENDADO)**
```python
fastapi==0.104.0
uvicorn==0.24.0
```

**Exemplo de endpoint:**
```python
@app.post("/predict")
async def predict_dengue(
    municipality: str,
    weeks_ahead: int = 4
):
    # Carregar modelo
    # Fazer previsão
    # Retornar JSON
    return {
        "municipality": municipality,
        "predictions": [...],
        "alert_level": "amarelo"
    }
```

**Deployment:**
- **Cloud Run** (GCP): Serverless, escala automática
- **AWS Lambda** + API Gateway
- **Heroku** (free tier para desenvolvimento)

---

### 🔧 MLOps e Versionamento

**Ferramentas:**

| Ferramenta | Uso | Custo |
|-----------|-----|-------|
| **Git + GitHub** | Versionamento de código | Gratuito |
| **DVC** (Data Version Control) | Versionamento de dados/modelos | Gratuito |
| **MLflow** | Tracking de experimentos | Gratuito (self-hosted) |
| **Weights & Biases** | Tracking de experimentos | Gratuito (tier acadêmico) |
| **Docker** | Containerização | Gratuito |

**Workflow proposto:**
```
1. Desenvolvimento local (VS Code + Jupyter)
2. Tracking de experimentos (MLflow / W&B)
3. Versionamento (Git + DVC)
4. Treinamento em cloud (Vertex AI / SageMaker)
5. Deployment (Cloud Run / Lambda)
```

---

### 📦 Stack Completo Recomendado

#### Para Desenvolvimento
```
- OS: Linux (WSL2 no Windows) / macOS
- IDE: VS Code + Jupyter Lab
- Python: 3.9 - 3.11
- Ambiente: conda ou venv
```

#### Para Dados
```
- Armazenamento: Google Cloud Storage (raw) + BigQuery (processed)
- Formato: Parquet (eficiente) + CSV (backup)
- Banco geoespacial: PostGIS (se necessário)
```

#### Para Modelagem
```
- Baseline: SARIMA (statsmodels), Prophet
- ML: XGBoost, Random Forest (scikit-learn)
- DL: LSTM (TensorFlow/Keras), Chronos (Hugging Face)
- Interpretabilidade: SHAP
```

#### Para Deployment
```
- Dashboard: Streamlit Cloud (gratuito)
- API: FastAPI + Cloud Run
- Monitoring: Google Cloud Monitoring
```

---

### 💰 Estimativa de Custos

| Item | Opção Gratuita | Opção Paga | Recomendado TCC |
|------|----------------|------------|-----------------|
| **Armazenamento** | GitHub (código) | GCP $10/mês | GCP (créditos) |
| **Processamento** | Google Colab | GCP $50/mês | Colab Pro $10 |
| **Dashboard** | Streamlit Cloud | Cloud Run $10/mês | Streamlit Cloud |
| **GPU (DL)** | Colab Free | Colab Pro+ $50/mês | Colab Pro |
| **Tracking** | MLflow local | W&B $49/mês | W&B free tier |
| **TOTAL** | **$0** | **$169/mês** | **$10/mês** |

**Recomendação:** Usar stack gratuita + Colab Pro ($10/mês) é suficiente para o TCC.

---

### 🎓 Justificativa Acadêmica das Escolhas

#### Por que Hugging Face?
- **Estado da arte**: Modelos foundation representam o cutting edge
- **Reprodutibilidade**: Modelos pré-treinados com checkpoints públicos
- **Transfer learning**: Aproveitar conhecimento de outras séries temporais
- **Comparação justa**: Avaliar modelos tradicionais vs foundation models

#### Por que Google Cloud?
- **Créditos educacionais**: $300 + créditos adicionais
- **Earth Engine**: Acesso fácil a dados climáticos
- **Ecosistema integrado**: Storage → BigQuery → Vertex AI → Deployment
- **Escalabilidade**: Começar pequeno, escalar se necessário

#### Por que TensorFlow (vs PyTorch)?
- **Integração GCP**: Vertex AI otimizado para TensorFlow
- **Keras**: API simples e didática
- **TensorFlow Lite**: Deploy em dispositivos móveis (trabalho futuro)
- **Documentação**: Mais recursos para séries temporais

---

### 📚 Recursos de Aprendizado

**Para Hugging Face:**
- Curso: https://huggingface.co/learn/nlp-course
- Documentação: https://huggingface.co/docs/transformers
- Hub: https://huggingface.co/models

**Para Google Cloud:**
- Qwiklabs: https://www.qwiklabs.com/ (labs gratuitos)
- Documentação: https://cloud.google.com/docs
- Coursera: "Google Cloud Big Data and Machine Learning Fundamentals"

**Para Séries Temporais:**
- Livro: "Forecasting: Principles and Practice" (Hyndman & Athanasopoulos)
- Curso: "Time Series Analysis with Python" (Udemy)

---

### ✅ Decisões Finais

**Stack escolhido:**

```yaml
Infrastructure:
  - Cloud: Google Cloud Platform (créditos educacionais)
  - Storage: Cloud Storage (raw) + BigQuery (processed)
  - Compute: Vertex AI Notebooks + Colab Pro

Data Processing:
  - Language: Python 3.10
  - Geospatial: GeoPandas, Rasterio, Earth Engine
  - ETL: Cloud Functions (serverless)

Modeling:
  - Baseline: SARIMA (statsmodels), Prophet
  - ML: XGBoost, Random Forest
  - DL: LSTM (TensorFlow/Keras)
  - Foundation: Chronos-T5 (Hugging Face)
  - Interpretability: SHAP

Deployment:
  - Dashboard: Streamlit Cloud
  - API: FastAPI + Cloud Run
  - Tracking: Weights & Biases (free tier)
  - Version Control: Git + DVC
```

**Critérios de escolha:**
1. ✅ **Custo zero ou baixo**: Créditos educacionais + free tiers
2. ✅ **Reprodutibilidade**: Código e modelos públicos
3. ✅ **Escalabilidade**: Funciona local, pode escalar para cloud
4. ✅ **Estado da arte**: Inclui modelos foundation (Hugging Face)
5. ✅ **Documentação**: Ampla comunidade e recursos de aprendizado

---

## �🔄 Próximos Passos

Com base nos trabalhos similares, as próximas etapas deste TCC são:

1. ✅ **Definir baseline**: SARIMA e Prophet (inspirado em InfoDengue)
2. ✅ **Implementar ML**: Random Forest e XGBoost (Roster et al.)
3. ✅ **Implementar DL**: LSTM com SHAP (Chen & Moraga)
4. ✅ **Testar Foundation Models**: Chronos (Hugging Face) com fine-tuning
5. ✅ **Feature engineering**: Lags climáticos, efeitos espaciais
6. ✅ **Validação robusta**: Temporal e geográfica
7. ✅ **Interpretabilidade**: SHAP, análise de lags por região
8. ✅ **Sistema de alerta**: Calibração de limiares
9. ✅ **Deployment**: Dashboard Streamlit + API FastAPI

---

*Última atualização: Novembro 2025*
*Versão: 1.1*
