# Respostas às Instruções do Professor Orientador - TCC 1

## 1. INTRODUÇÃO

### Por que esse trabalho é importante?

Este trabalho é importante por várias razões fundamentais:

**Impacto em Saúde Pública:**
- A dengue é uma doença viral transmitida pelo mosquito *Aedes aegypti* que representa um **grave problema de saúde pública no Brasil**, sendo endêmica em praticamente todo o território nacional
- Permite **alertas precoces de surtos**, auxiliando na **alocação de recursos** (agentes de saúde, inseticidas) e melhorando o **planejamento de campanhas** de prevenção
- Com base nos dados analisados, foram registrados **1.502.259 casos de dengue apenas em 2025**, demonstrando a magnitude do problema

**Relevância Técnica e Acadêmica:**
- Desafio técnico complexo envolvendo integração de múltiplas fontes de dados, modelagem de séries temporais não-lineares e tratamento de dados geoespaciais
- Oportunidade de aplicar técnicas avançadas de Inteligência Artificial (Machine Learning e Deep Learning) em um problema real de grande impacto social
- Gap de implementação: existem poucos sistemas operacionais em nível municipal, criando oportunidade para desenvolver um pipeline reproduzível e código aberto

### Do que se trata o assunto que estou abordando?

**A Dengue:**
- Doença viral transmitida principalmente pelo mosquito *Aedes aegypti*
- **Gravidade da doença**: A dengue pode apresentar desde formas assintomáticas até casos graves com complicações hemorrágicas e síndrome do choque da dengue, podendo levar ao óbito
- **Limitações e perigos**: Os dados analisados mostram que em 2025 houve **2.270 óbitos confirmados** por dengue, demonstrando a gravidade da doença. Casos graves podem requerer hospitalização (foram registradas **58.955 hospitalizações** em 2025)
- **Sazonalidade marcante**: A doença apresenta padrões sazonais claros, com picos geralmente entre janeiro e maio, variando por região
- **Afeta milhões de pessoas**: Os dados de 2025 mostram que a doença está distribuída em todo o território nacional, com maior concentração em estados como São Paulo (852.320 casos), Minas Gerais (156.781 casos) e Paraná (109.960 casos)

**Fatores que influenciam a transmissão:**
- **Fatores climáticos**: Temperatura entre 20-30°C favorece o vetor; chuvas criam criadouros; umidade alta aumenta sobrevivência do mosquito
- **Fatores socioeconômicos**: Saneamento básico deficiente, densidade populacional, condições de moradia, acesso a água tratada
- **Fatores ambientais**: Urbanização não planejada, descarte inadequado de lixo, acúmulo de água em recipientes

### Qual a relevância da tecnologia que eu vou abordar para atacar o problema?

**Séries Temporais e Dados Climáticos:**
- Existe **vasta literatura científica** demonstrando que variáveis climáticas têm **forte influência** sobre a dinâmica de transmissão da dengue
- Modelos de previsão que combinam séries temporais epidemiológicas (SINAN/DataSUS) com covariáveis climáticas (INMET, satélites, reanalysis) têm apresentado **excelentes resultados** na literatura científica
- A tecnologia permite **previsão antecipada** de surtos, com janelas de tempo suficientes para ações preventivas (tipicamente 3-8 semanas de antecedência)

**Técnicas de Machine Learning e Deep Learning:**
- **LSTM (Long Short-Term Memory)**: Redes neurais recorrentes que capturam dependências temporais de longo prazo, sendo estado-da-arte para séries temporais
- **XGBoost e Random Forest**: Modelos de Machine Learning que capturam não-linearidades e interações complexas entre variáveis
- **SARIMA/SARIMAX**: Modelos estatísticos que incorporam sazonalidade e variáveis exógenas climáticas
- Trabalhos recentes aplicados no Brasil demonstram que a **incorporação de dados climáticos** melhora significativamente a acurácia das previsões

### Pergunta de pesquisa:

**Como o uso combinado de modelos de séries temporais (SARIMA, Prophet), Machine Learning (XGBoost, Random Forest) e Deep Learning (LSTM) com variáveis climáticas (temperatura, precipitação, umidade) pode melhorar a previsão de surtos de dengue em municípios brasileiros, e quais variáveis climáticas e janelas temporais (lags) são mais preditivas para diferentes regiões do país?**

Esta pergunta de pesquisa:
- Não pode ser respondida com sim ou não
- Expande o conhecimento do campo ao:
  - Comparar sistematicamente diferentes abordagens de modelagem
  - Identificar quais variáveis climáticas são mais importantes para cada região
  - Determinar janelas temporais ótimas (lags) para previsão
  - Contribuir com evidências práticas para sistemas de alerta em saúde pública

### Objetivos:

**Objetivo Geral:**
Desenvolver e comparar modelos preditivos de surtos de dengue para municípios brasileiros utilizando séries temporais epidemiológicas combinadas com variáveis climáticas, avaliando o desempenho de diferentes abordagens (modelos estatísticos, Machine Learning e Deep Learning) e identificando as variáveis e janelas temporais mais preditivas para diferentes contextos regionais.

**Objetivos Específicos:**

1. **Coletar e processar dados epidemiológicos e climáticos**
   - Implementar pipeline ETL para dados SINAN (OpenDataSUS) de casos de dengue
   - Integrar dados climáticos de múltiplas fontes (INMET, CHIRPS, ERA5, NASA POWER)
   - Padronizar e agregar dados por município e semana epidemiológica

2. **Realizar análise exploratória e feature engineering**
   - Analisar padrões temporais e espaciais dos casos de dengue
   - Criar features temporais (lags de 1-12 semanas, médias móveis)
   - Identificar correlações cruzadas entre variáveis climáticas e casos de dengue
   - Calcular anomalias climáticas e variáveis derivadas

3. **Implementar modelos baseline estatísticos**
   - Desenvolver modelos SARIMA/SARIMAX com variáveis exógenas climáticas
   - Implementar modelo Prophet com regressores climáticos
   - Estabelecer baseline de performance para comparação

4. **Desenvolver modelos de Machine Learning**
   - Implementar Random Forest e XGBoost com features temporais e climáticas
   - Realizar tuning de hiperparâmetros usando validação cruzada temporal
   - Aplicar técnicas de seleção de features (SHAP, feature importance)

5. **Implementar modelos de Deep Learning**
   - Desenvolver arquiteturas LSTM e BiLSTM para capturar dependências temporais
   - Ajustar hiperparâmetros (arquitetura, dropout, epochs)
   - Avaliar modelos híbridos e ensemble

6. **Avaliar e comparar modelos**
   - Implementar validação temporal (TimeSeriesSplit) para evitar vazamento de dados
   - Calcular métricas de avaliação (RMSE, MAE, MAPE para regressão; AUC, Precision, Recall para classificação de surtos)
   - Comparar desempenho entre modelos e identificar o melhor para cada contexto

7. **Interpretar resultados e identificar variáveis importantes**
   - Aplicar SHAP para interpretabilidade dos modelos
   - Identificar quais variáveis climáticas e lags são mais preditivos por região
   - Analisar casos de sucesso e falha dos modelos

8. **Desenvolver sistema de alerta prático**
   - Calibrar limiares adaptativos por município para definição de surtos
   - Criar sistema de alerta com níveis de risco

---

## 2. REVISÃO BIBLIOGRÁFICA

### Qual o campo que estou abordando?

**Epidemiologia Computacional e Saúde Pública Digital:**
- O trabalho está inserido no campo interdisciplinar que combina **Epidemiologia**, **Ciência de Dados**, **Machine Learning** e **Saúde Pública**
- Área específica: **Previsão de doenças infecciosas usando séries temporais e dados ambientais**
- Foco em **arboviroses**, especificamente dengue, que é uma doença transmitida por vetores

### Qual o impacto social, econômico, etc. desse campo?

**Impacto Social:**
- **Prevenção de mortes**: A dengue pode ser fatal; em 2025 foram registrados 2.270 óbitos no Brasil
- **Melhoria na qualidade de vida**: Previsão permite ações preventivas que reduzem incidência
- **Redução de sobrecarga no sistema de saúde**: Alertas antecipados permitem melhor alocação de recursos
- **Equidade em saúde**: Sistema de alerta pode beneficiar especialmente populações mais vulneráveis

**Impacto Econômico:**
- **Custos diretos de saúde**: Tratamento, hospitalização (58.955 casos em 2025), exames laboratoriais
- **Custos indiretos**: Absenteísmo, redução de produtividade, impacto no turismo
- **Custos de controle**: Campanhas de prevenção, aplicação de inseticidas, agentes de saúde
- Estudos estimam que a dengue custa bilhões de dólares anualmente em países endêmicos

**Impacto em Saúde Pública:**
- **Planejamento de recursos**: Permite alocação antecipada de agentes de saúde, inseticidas, equipes médicas
- **Otimização de campanhas**: Timing adequado para campanhas de conscientização e eliminação de criadouros
- **Monitoramento em tempo real**: Sistemas de alerta fornecem informação atualizada para gestores

### Como esse campo se estrutura?

**A Dengue:**
- **Manifestação**: Doença viral que pode apresentar desde casos assintomáticos até formas graves
- **Sintomas principais**: Febre, mialgia, cefaleia, exantema, vômito, náusea, dor retro-orbital, entre outros
- **Pessoas afetadas**: Dados de 2025 mostram 1.502.259 casos notificados, distribuídos em todos os estados brasileiros
- **Riscos para pacientes**: 
  - Casos graves podem evoluir para dengue hemorrágica ou síndrome do choque da dengue
  - Grupos de risco: idosos, gestantes, pessoas com doenças crônicas (diabetes, hipertensão, doenças hematológicas)
- **Existe cura?**: Não existe tratamento específico antiviral; tratamento é sintomático e de suporte
- **Diagnóstico precoce**: É fundamental para evitar complicações e reduzir mortalidade
- **Importância da previsão**: Previsão antecipada permite ações preventivas que podem reduzir significativamente a incidência

**Estrutura Epidemiológica:**
- **Vetor**: Mosquito *Aedes aegypti*
- **Ciclo de transmissão**: Humanos infectados → mosquito → humanos saudáveis
- **Período de incubação**: 4-10 dias após picada do mosquito
- **Sazonalidade**: Padrões claros, variando por região brasileira

### Qual a tecnologia escolhi para tratar esse problema?

**Abordagem Híbrida:**
1. **Modelos Estatísticos Clássicos**
   - **SARIMA/SARIMAX**: Modelos autoregressivos integrados de médias móveis com sazonalidade e variáveis exógenas
   - **Prophet**: Framework desenvolvido pelo Facebook para previsão de séries temporais com sazonalidade múltipla

2. **Machine Learning**
   - **Random Forest**: Ensemble de árvores de decisão que captura não-linearidades e interações
   - **XGBoost**: Gradient boosting que é estado-da-arte para dados tabulares

3. **Deep Learning**
   - **LSTM (Long Short-Term Memory)**: Redes neurais recorrentes especializadas em séries temporais
   - **BiLSTM**: LSTM bidirecional que captura padrões em ambas as direções temporais

### Quais são as vantagens dessa tecnologia para esse problema?

**Vantagens da Abordagem Híbrida:**

1. **Modelos Estatísticos (SARIMA/SARIMAX, Prophet):**
   - **Interpretabilidade**: Resultados são interpretáveis e alinhados com teoria estatística
   - **Robustez**: Funcionam bem mesmo com poucos dados
   - **Sazonalidade**: Capturam naturalmente padrões sazonais
   - **Baseline confiável**: Estabelecem baseline para comparação

2. **Machine Learning (Random Forest, XGBoost):**
   - **Não-linearidades**: Capturam relações complexas entre variáveis
   - **Feature importance**: Permitem identificar variáveis mais importantes
   - **SHAP**: Ferramentas de interpretabilidade (especialmente XGBoost)
   - **Robustez a outliers**: Menos sensíveis a valores extremos

3. **Deep Learning (LSTM, BiLSTM):**
   - **Dependências temporais**: Capturam padrões de longo prazo em séries temporais
   - **Estado-da-arte**: Melhores resultados em muitos problemas de séries temporais
   - **Aprendizado automático**: Não requer especificação manual de features temporais complexas
   - **Flexibilidade**: Arquiteturas podem ser adaptadas ao problema específico

**Vantagens da Integração de Dados Climáticos:**
- **Melhoria da acurácia**: Literatura mostra melhoria significativa ao incluir variáveis climáticas
- **Previsão antecipada**: Lags climáticos permitem previsão com semanas de antecedência
- **Interpretabilidade biológica**: Relações entre clima e proliferação do mosquito são biologicamente fundamentadas

### Como essa tecnologia é estruturada?

**Estrutura de uma Rede Neural LSTM:**
- **Células LSTM**: Unidades fundamentais que possuem três portões (forget, input, output)
- **Camadas**: Múltiplas camadas LSTM podem ser empilhadas
- **Dropout**: Técnica de regularização para evitar overfitting
- **Camadas densas**: Camadas fully connected para fazer previsões finais
- **Input shape**: Dados organizados em formato 3D (samples, timesteps, features)

**Estrutura de XGBoost:**
- **Árvores de decisão**: Conjunto de árvores que fazem previsões
- **Gradient boosting**: Treinamento sequencial onde cada árvore corrige erros da anterior
- **Regularização**: L1 e L2 para evitar overfitting
- **Features**: Aceita features tabulares (temperatura, precipitação, lags, etc.)

**Estrutura de SARIMAX:**
- **Componentes ARIMA**: Autoregressivo (AR), Integrado (I), Médias Móveis (MA)
- **Componente sazonal**: Captura padrões que se repetem periodicamente
- **Variáveis exógenas (X)**: Permite incorporar variáveis climáticas externas

### Como é o estado da arte da tecnologia utilizada?

**Estado da Arte em Previsão de Dengue:**

1. **Trabalhos Recentes no Brasil:**
   - **Chen et al. (2025)**: Framework LSTM que integra informação temporal, climática e espacial para previsão de dengue em escala nacional no Brasil
   - **Bomfim et al. (2023)**: Aplicação de LSTM em nível de bairro para previsão de dengue
   - **Silva et al. (2024)**: Demonstra melhoria significativa ao incluir variáveis climáticas em modelos de Machine Learning

2. **Técnicas Avançadas:**
   - **Ensemble methods**: Combinação de múltiplos modelos para melhor performance
   - **Multitask learning**: Modelos que preveem múltiplas arboviroses simultaneamente
   - **Windowed correlation**: Técnica para incorporar dados de municípios vizinhos
   - **Transfer learning**: Aplicação de modelos treinados em uma região para outra

3. **Avaliação de Performance:**
   - **Métricas principais**: RMSE, MAE, MAPE para regressão; AUC, Precision, Recall para classificação
   - **Validação temporal**: Rolling-window cross-validation para evitar vazamento de dados
   - **Comparação sistemática**: Benchmarks entre diferentes abordagens

4. **Pontos Fortes e Fracos:**

   **Pontos Fortes:**
   - LSTM: Excelente para capturar padrões temporais complexos
   - XGBoost: Alta performance em dados tabulares, interpretável via SHAP
   - SARIMA: Interpretável, estabelece baseline sólido
   - Integração climática: Melhora significativamente a acurácia

   **Pontos Fracos:**
   - LSTM: Requer muitos dados e pode ser computacionalmente caro
   - Modelos estatísticos: Podem ter dificuldade com não-linearidades complexas
   - Todos: Requerem dados históricos suficientes para treinamento

5. **Onde são usadas atualmente:**
   - **InfoDengue (Fiocruz/FGV)**: Sistema operacional de alerta de arboviroses no Brasil
   - **Sistemas de saúde pública**: Vários países usam modelos preditivos para planejamento
   - **Pesquisa acadêmica**: Múltiplos estudos publicados recentemente usando ML/DL

---

## 3. METODOLOGIA

### O que será feito?

**Pipeline Completo de Desenvolvimento:**

1. **Coleta e Processamento de Dados (ETL)**
   - Download de dados SINAN (OpenDataSUS) de casos de dengue
   - Integração de dados climáticos (INMET, CHIRPS, ERA5, NASA POWER)
   - Download de dados auxiliares (IBGE: malhas municipais, população)

2. **Limpeza e Normalização**
   - Padronização de datas e semanas epidemiológicas
   - Normalização de códigos IBGE (7 dígitos)
   - Filtro de casos prováveis/confirmados
   - Tratamento de dados faltantes

3. **Agregação Espacial e Temporal**
   - Agregação de casos por município e semana epidemiológica
   - Zonal statistics para agregar dados climáticos por município
   - Agregação temporal de dados diários para semanais

4. **Feature Engineering**
   - Criação de lags temporais (1-12 semanas) para variáveis climáticas e casos
   - Médias móveis (4, 8 semanas)
   - Somas acumuladas (precipitação acumulada)
   - Anomalias climáticas (diferença da climatologia)
   - Features socioeconômicas (população, casos per capita)
   - Features temporais cíclicas (semana do ano em formato seno/cosseno)

5. **Análise Exploratória de Dados (EDA)**
   - Análise de distribuições, tendências e sazonalidade
   - Correlações cruzadas entre variáveis climáticas e casos
   - Visualizações (mapas, séries temporais, histogramas)

6. **Seleção de Features**
   - Cross-correlation function (CCF) para identificar lags ótimos
   - Feature importance (Random Forest)
   - SHAP values para interpretabilidade

7. **Divisão de Dados**
   - TimeSeriesSplit (rolling window) para validação temporal
   - Divisão: Treino (70%), Validação (15%), Teste (15%)
   - Garantia de ausência de vazamento temporal

8. **Modelagem**
   - Implementação de modelos baseline (SARIMA, Prophet)
   - Implementação de modelos de ML (Random Forest, XGBoost)
   - Implementação de modelos de DL (LSTM, BiLSTM)
   - Tuning de hiperparâmetros

9. **Avaliação e Comparação**
   - Cálculo de métricas (RMSE, MAE, MAPE, AUC, Precision, Recall)
   - Comparação sistemática entre modelos
   - Análise por município/região

10. **Interpretação**
    - Análise SHAP para XGBoost
    - Identificação de variáveis e lags mais importantes
    - Análise de casos de sucesso e falha

11. **Sistema de Alerta**
    - Calibração de limiares adaptativos por município
    - Definição de níveis de alerta (verde, amarelo, laranja, vermelho)

### Quais algoritmos devem ser criados?

**Algoritmos de Modelagem:**

1. **SARIMA/SARIMAX**
   - Modelo autoregressivo integrado de médias móveis com sazonalidade
   - Incorpora variáveis exógenas climáticas
   - Parâmetros: (p, d, q) × (P, D, Q, s) onde s=52 (semanas)

2. **Prophet**
   - Framework para previsão com sazonalidade múltipla
   - Incorpora regressores climáticos

3. **Random Forest**
   - Ensemble de árvores de decisão
   - Hiperparâmetros: n_estimators, max_depth, min_samples_split

4. **XGBoost**
   - Gradient boosting
   - Hiperparâmetros: n_estimators, max_depth, learning_rate, subsample, colsample_bytree

5. **LSTM**
   - Rede neural recorrente com células LSTM
   - Arquitetura: LSTM layers → Dropout → Dense layers
   - Hiperparâmetros: número de unidades, número de camadas, dropout rate, epochs, batch_size

6. **BiLSTM**
   - LSTM bidirecional
   - Captura padrões em ambas as direções temporais

7. **Ensemble (opcional)**
   - Voting ou Stacking de múltiplos modelos

**Algoritmos Auxiliares:**

- **Feature Engineering**: Criação de lags, médias móveis, anomalias
- **Seleção de Features**: CCF, feature importance, SHAP
- **Validação Temporal**: TimeSeriesSplit com rolling window
- **Calibração de Limiares**: Definição de limiares adaptativos por município

### Como os algoritmos serão testados?

**Estratégia de Validação:**

1. **Validação Temporal (TimeSeriesSplit)**
   - Rolling-window cross-validation
   - Garantia de que dados de teste são sempre posteriores aos de treino
   - Múltiplos folds temporais para robustez

2. **Divisão de Dados**
   - **Treino**: 70% (primeiros anos, ex: 2010-2019)
   - **Validação**: 15% (anos intermediários, ex: 2020-2021) - para tuning
   - **Teste**: 15% (últimos anos, ex: 2022-2024) - avaliação final

3. **Métricas de Avaliação**

   **Para Previsão de Contagem (Regressão):**
   - **RMSE (Root Mean Squared Error)**: Penaliza erros grandes
   - **MAE (Mean Absolute Error)**: Erro médio absoluto
   - **MAPE (Mean Absolute Percentage Error)**: Erro percentual

   **Para Classificação de Surtos:**
   - **AUC (Area Under ROC Curve)**: Capacidade de discriminar surtos
   - **Precision**: Proporção de surtos previstos que realmente ocorreram
   - **Recall**: Proporção de surtos reais que foram previstos
   - **F1-Score**: Média harmônica de precision e recall

4. **Testes Estatísticos**
   - Teste de significância de diferenças entre modelos
   - Análise de resíduos (para modelos estatísticos)
   - Teste de normalidade dos erros

5. **Análise por Subgrupos**
   - Performance por região (Norte, Nordeste, Sudeste, Sul, Centro-Oeste)
   - Performance por município (análise de casos específicos)
   - Performance em diferentes épocas do ano (sazonalidade)

### Qual(ais) base(s) de dados será(ão) usada(s)?

**Dados Epidemiológicos:**

1. **OpenDataSUS / SINAN - Dengue**
   - **Fonte**: Ministério da Saúde do Brasil
   - **Cobertura**: Nacional, todos os municípios brasileiros
   - **Período**: 2007 até o presente (dados de 2025 já coletados: 1.502.259 registros)
   - **Granularidade**: Microdados individuais de notificações
   - **Formato**: JSON, CSV, DBF
   - **Campos principais**: 
     - `dt_notific`: Data da notificação
     - `dt_sin_pri`: Data dos primeiros sintomas (principal para séries temporais)
     - `sem_pri`: Semana epidemiológica dos sintomas
     - `id_municip`: Código IBGE do município (7 dígitos)
     - `classificacao_final`: Classificação do caso
     - `evolucao`: Evolução do caso (incluindo óbito)
   - **Link**: https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue

**Dados Climáticos:**

2. **INMET / BDMEP**
   - **Tipo**: Dados de estações meteorológicas terrestres
   - **Cobertura**: ~500 estações automáticas no Brasil
   - **Variáveis**: Temperatura (média, mín, máx), precipitação, umidade relativa, pressão, radiação, vento
   - **Granularidade**: Horária ou diária
   - **Link**: https://bdmep.inmet.gov.br/

3. **CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)**
   - **Tipo**: Precipitação por satélite + estações
   - **Cobertura**: Global (50°S a 50°N)
   - **Resolução espacial**: ~5.5 km (0.05°)
   - **Resolução temporal**: Diária
   - **Período**: 1981 até o presente
   - **Vantagem**: Cobertura espacial completa para todos os municípios
   - **Link**: https://www.chc.ucsb.edu/data/chirps

4. **ERA5 (Copernicus Climate Data Store)**
   - **Tipo**: Reanálise atmosférica global
   - **Resolução espacial**: ~31 km (0.25° ou 0.1°)
   - **Resolução temporal**: Horária
   - **Variáveis**: Temperatura, precipitação, umidade, vento, radiação, pressão
   - **Período**: 1950 até o presente
   - **Link**: https://cds.climate.copernicus.eu/

5. **NASA POWER**
   - **Tipo**: API para dados meteorológicos/solares
   - **Cobertura**: Global
   - **Resolução espacial**: ~0.5° x 0.625°
   - **Resolução temporal**: Diária
   - **Vantagem**: API simples, acesso livre, rápido para prototipagem
   - **Link**: https://power.larc.nasa.gov/

**Dados Auxiliares:**

6. **IBGE - Malhas Territoriais**
   - Shapefiles dos limites municipais brasileiros
   - Códigos IBGE de 7 dígitos
   - **Link**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/

7. **IBGE - População e Indicadores**
   - População por município (estimativas anuais)
   - PIB municipal, índice de saneamento, taxa de urbanização
   - **Uso**: Normalização de casos (casos per capita), variáveis de controle

### Quais testes estatísticos, de viés, de validação, etc serão feitos e como?

**Testes Estatísticos:**

1. **Análise de Estacionariedade**
   - **Teste de Dickey-Fuller Aumentado (ADF)**: Verificar se série temporal é estacionária
   - **Teste de KPSS**: Teste complementar para estacionariedade
   - **Aplicação**: Necessário para modelos ARIMA/SARIMA

2. **Análise de Autocorrelação**
   - **ACF (Autocorrelation Function)**: Identificar padrões autoregressivos
   - **PACF (Partial Autocorrelation Function)**: Identificar ordem do modelo AR
   - **Aplicação**: Determinar parâmetros p e q do modelo SARIMA

3. **Análise de Correlação Cruzada**
   - **CCF (Cross-Correlation Function)**: Identificar lags ótimos entre variáveis climáticas e casos
   - **Aplicação**: Seleção de features temporais

4. **Testes de Normalidade**
   - **Shapiro-Wilk**: Testar normalidade dos resíduos
   - **Q-Q plots**: Visualização de normalidade
   - **Aplicação**: Validação de pressupostos de modelos estatísticos

5. **Testes de Significância**
   - **Teste t**: Comparar médias de erros entre modelos
   - **Teste de Wilcoxon**: Comparação não-paramétrica (quando não há normalidade)
   - **Aplicação**: Verificar se diferenças entre modelos são estatisticamente significativas

6. **Análise de Resíduos**
   - **Ljung-Box test**: Testar autocorrelação dos resíduos
   - **Jarque-Bera test**: Testar normalidade e assimetria dos resíduos
   - **Aplicação**: Diagnóstico de modelos ARIMA/SARIMA

**Testes de Viés:**

1. **Validação Temporal**
   - **TimeSeriesSplit**: Garantir que dados de teste são sempre posteriores
   - **Rolling-window**: Múltiplos folds temporais
   - **Objetivo**: Evitar vazamento de informação do futuro

2. **Validação Espacial**
   - **Hold-out por região**: Testar se modelo generaliza para regiões não vistas
   - **Transfer learning**: Avaliar capacidade de transferência entre municípios

3. **Validação Cruzada Temporal**
   - **Múltiplos folds**: Garantir robustez dos resultados
   - **Objetivo**: Evitar overfitting e estimar erro real do modelo

**Testes de Validação:**

1. **Métricas de Avaliação**
   - **RMSE, MAE, MAPE**: Para regressão (previsão de contagem)
   - **AUC, Precision, Recall, F1**: Para classificação (previsão de surtos)
   - **R²**: Coeficiente de determinação

2. **Análise de Calibração**
   - **Calibration plots**: Verificar se probabilidades previstas correspondem a frequências observadas
   - **Brier score**: Medir calibração de probabilidades

3. **Análise de Robustez**
   - **Sensibilidade a hiperparâmetros**: Variação de performance com diferentes configurações
   - **Sensibilidade a dados faltantes**: Impacto de missing data

4. **Comparação de Modelos**
   - **Tabela comparativa**: Métricas lado a lado
   - **Testes estatísticos**: Verificar significância de diferenças
   - **Análise de custo-benefício**: Balancear acurácia vs complexidade

---

## 4. CRONOGRAMA

**Divisão da Metodologia em Tarefas e Tempo Estimado:**

### Fase 1: Preparação e Revisão Bibliográfica (4 semanas)
- Semana 1-2: Revisão bibliográfica aprofundada
- Semana 3: Definição de metodologia detalhada
- Semana 4: Preparação do ambiente de desenvolvimento

### Fase 2: Coleta e Processamento de Dados (6 semanas)
- Semana 5-6: Implementação de scripts de download (SINAN, INMET)
- Semana 7-8: Processamento e limpeza de dados epidemiológicos
- Semana 9-10: Processamento e integração de dados climáticos

### Fase 3: Agregação e Feature Engineering (4 semanas)
- Semana 11-12: Agregação espacial e temporal (município-semana)
- Semana 13-14: Feature engineering (lags, médias móveis, anomalias)

### Fase 4: Análise Exploratória (4 semanas)
- Semana 15-16: Análise exploratória de dados (EDA)
- Semana 17: Análise de correlações e identificação de lags
- Semana 18: Documentação de insights e visualizações

### Fase 5: Modelagem Baseline (4 semanas)
- Semana 19-20: Implementação de SARIMA/SARIMAX
- Semana 21: Implementação de Prophet
- Semana 22: Validação temporal e ajuste de hiperparâmetros

### Fase 6: Machine Learning (5 semanas)
- Semana 23-24: Implementação de Random Forest
- Semana 25-26: Implementação de XGBoost
- Semana 27: Tuning de hiperparâmetros e feature selection

### Fase 7: Deep Learning (5 semanas)
- Semana 28-29: Preparação de dados para LSTM
- Semana 30-31: Implementação de LSTM e BiLSTM
- Semana 32: Tuning de arquitetura e hiperparâmetros

### Fase 8: Avaliação e Comparação (3 semanas)
- Semana 33: Avaliação de todos os modelos
- Semana 34: Comparação sistemática e análise estatística
- Semana 35: Interpretação com SHAP e análise de features importantes

### Fase 9: Sistema de Alerta e Documentação (3 semanas)
- Semana 36: Desenvolvimento de sistema de alerta
- Semana 37: Calibração de limiares
- Semana 38: Documentação final e preparação de apresentação

### Fase 10: Redação e Revisão (6 semanas)
- Semana 39-41: Redação do TCC
- Semana 42-44: Revisões e ajustes

**Total Estimado: 44 semanas (~11 meses)**

---

## OBSERVAÇÕES FINAIS

Este documento responde às instruções do professor orientador para o TCC 1, fornecendo uma base sólida para o desenvolvimento do trabalho. Todas as respostas estão fundamentadas na documentação existente do projeto, nos dados já coletados (1.502.259 casos de dengue em 2025) e na literatura científica relevante sobre previsão de dengue usando séries temporais e dados climáticos.

As metodologias e técnicas propostas estão alinhadas com o estado da arte da área, incluindo trabalhos recentes publicados em 2024-2025 que demonstram a eficácia de abordagens similares para previsão de dengue no Brasil.

