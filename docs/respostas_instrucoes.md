1 - 
1.1 - Por que esse trabalho é importante?
Nos acreditamos que este trabalho pode auxiliar na prediçao de possiveis surtos de dengue em municipios brasileios, combinando dados de serie temporarias(INMETRO) e dados historicos de casos de dengue (SINAN), e assim faremos um modelo preditivo estatísticos que sera utilizado como ferramenta de campanhas de prevencao de dengue, assim diminuindo possiveis surtos.

1.2 - Do que se trata o assunto que estou abordando (e.g. Qual a gravidade da doença que estou tratando, que tipo de limitações ou perigos que a pessoa com essa doença possui?)
- DENGUE: Doença viral transmitida principalmente pelo mosquito *Aedes aegypti. Gravidade da doença: A dengue pode apresentar desde formas assintomáticas até casos graves com complicações hemorrágicas e síndrome do choque da dengue, podendo levar ao óbito. Limitações e perigos: Os dados analisados mostram que em 2025 houve **2.270 óbitos confirmados** por dengue, demonstrando a gravidade da doença. Casos graves podem requerer hospitalização (foram registradas **58.955 hospitalizações** em 2025). Sazonalidade marcante**: A doença apresenta padrões sazonais claros, com picos geralmente entre janeiro e maio, variando por região. Afeta milhões de pessoas**: Os dados de 2025 mostram que a doença está distribuída em todo o território nacional, com maior concentração em estados como São Paulo (852.320 casos), Minas Gerais (156.781 casos) e Paraná (109.960 casos)

1.3 - Qual a relevância da tecnologia que eu vou abordar para atacar o problema possui nesse campo?
A ferramenta vai ser utilizada a fim de auxiliar na otimizacao de recursos e mobilizacao de pessoas para campanhas da dengue, provendo uma visao mais precisa de periodos de sazionalidades da doenca. 
**Técnicas de Machine Learning e Deep Learning:**
- **LSTM (Long Short-Term Memory)**: Redes neurais recorrentes que capturam dependências temporais de longo prazo, sendo estado-da-arte para séries temporais
- **XGBoost e Random Forest**: Modelos de Machine Learning que capturam não-linearidades e interações complexas entre variáveis
- **SARIMA/SARIMAX**: Modelos estatísticos que incorporam sazonalidade e variáveis exógenas climáticas
- Trabalhos recentes aplicados no Brasil demonstram que a **incorporação de dados climáticos** melhora significativamente a acurácia das previsões

1.4. Pergunta de pesquisa: Elabore uma pergunta que sintetize o que você está propondo. Uma boa pergunta de pesquisa não deve ser respondida com sim ou não e idealmente ela deve ser construída de uma forma que, após ser respondida, expanda o conhecimento do campo que está sendo abordado. (e.g. Como o uso de algoritmos de CNNs pode auxiliar no diagnóstico de câncer de mama em diferentes estágios e de que forma algoritmos de XAI podem auxiliar os médicos e responsáveis a compreender a classificação dada pelos algoritmos CNN?)
**Como o uso combinado de modelos de séries temporais (SARIMA, Prophet), Machine Learning (XGBoost, Random Forest) e Deep Learning (LSTM) com variáveis climáticas (temperatura, precipitação, umidade) pode melhorar a previsão de surtos de dengue em municípios brasileiros, e quais variáveis climáticas e janelas temporais (lags) são mais preditivas para diferentes regiões do país?**

1.5. Objetivos: Os objetivos são a resposta a sua pergunta de pesquisa. Você terá um objetivo geral (a resposta direta a pergunta de pesquisa) e os objetivos específicos, que são os passos a serem seguidos para chegar no (ou nos) objetivo(s) geral(is) (e.g. Objetivo geral: criar algoritmos de CNN para classificação de câncer de mama em estágio inicial, intermediário e avançado e criar algoritmos de XAI baseados em mapa de calor para identificar as regiões da tomografia computadorizada que mais contribuíram para a classificação. Objetivos específicos: 1. construir arquiteturas VGG16 e RESNET e adaptá-las ao problema. 2. Fazer testes preliminares para a escolha das funções de ativação, camadas de dropout, etc. E assim por diante).
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


   Link do YT da playlist:
   https://www.youtube.com/playlist?list=PLSDVadsSlXTC_ghWOlMOyyLn3otiBDRbP


   