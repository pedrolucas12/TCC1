# Tema e Motivação do TCC

## 📌 Tema Principal

**Previsão de surtos de dengue utilizando séries temporais e dados climáticos**

## 🎯 Título Completo

**"Desenvolvimento de um Modelo de Previsão para Surtos de Dengue em Municípios Brasileiros utilizando Séries Temporais e Dados Climáticos"**

---

## 💡 Resumo e Motivação

### Contexto

A dengue é uma doença viral transmitida principalmente pelo mosquito *Aedes aegypti*, representando um grave problema de saúde pública no Brasil e em outros países tropicais. A incidência da doença está fortemente relacionada a fatores ambientais e climáticos que favorecem a proliferação do vetor.

### Importância do Tema

Existe **vasta literatura científica** demonstrando que variáveis climáticas têm forte influência sobre a dinâmica de transmissão da dengue:

- 🌡️ **Temperatura**: Afeta o ciclo de vida do mosquito e a replicação viral
- 🌧️ **Precipitação**: Cria criadouros para as larvas do *Aedes aegypti*
- 💧 **Umidade**: Influencia a sobrevivência e atividade do vetor

### Estado da Arte

Modelos de previsão que combinam:
- **Séries temporais epidemiológicas** (SINAN / DataSUS)
- **Covariáveis climáticas** (INMET, satélites, reanalysis)

Têm apresentado **excelentes resultados** na literatura científica.

### Técnicas Modernas Aplicadas

#### 1. Modelos Estatísticos Clássicos
- ARIMA / SARIMA
- SARIMAX (com variáveis exógenas)
- Prophet

#### 2. Machine Learning
- Random Forest
- XGBoost
- Gradient Boosting com features temporais

#### 3. Deep Learning
- **LSTM** (Long Short-Term Memory): Redes recorrentes para séries temporais
- **BiLSTM**: LSTM bidirecional
- **Modelos híbridos espaço-temporais**: Combinam informação geográfica
- **Abordagens com seleção de janelas temporais**: Otimização de lags

### Aplicações Recentes no Brasil

Trabalhos recentes aplicaram LSTM em **escala nacional** e compararam:
- Métodos estatísticos (ARIMA/SARIMA)
- Machine Learning tradicional
- Deep Learning

Resultados mostram que a **incorporação de dados climáticos** melhora significativamente a acurácia das previsões.

---

## 🎓 Justificativa Acadêmica

### Por que este tema é relevante?

1. **Impacto em Saúde Pública**
   - Permite **alertas precoces** de surtos
   - Auxilia na **alocação de recursos** (agentes de saúde, inseticidas)
   - Melhora o **planejamento de campanhas** de prevenção

2. **Desafio Técnico Complexo**
   - Integração de múltiplas fontes de dados
   - Modelagem de séries temporais não-lineares
   - Tratamento de dados geoespaciais
   - Aplicação de técnicas avançadas de IA

3. **Dados Públicos Disponíveis**
   - Brasil possui excelentes bases de dados abertas
   - SINAN/DataSUS: microdados de notificações
   - INMET: dados meteorológicos históricos
   - Satélites: CHIRPS, ERA5, NASA POWER

4. **Gap de Implementação**
   - Poucos sistemas operacionais em nível municipal
   - Oportunidade de criar pipeline reproduzível
   - Código aberto para benefício da comunidade

---

## 🔬 Questões de Pesquisa

Este TCC busca responder:

1. **Até que ponto variáveis climáticas melhoram a acurácia de previsão de casos de dengue?**

2. **Quais lags ou janelas (semanas atrás) são mais preditivos para cada município ou região?**

3. **Qual modelo (ARIMA, RandomForest, XGBoost, LSTM) apresenta melhor desempenho para previsão municipal?**

4. **É possível generalizar modelos entre municípios** (treinar em um e prever em outro)?

5. **Como interpretar as importâncias das variáveis climáticas** e gerar alertas acionáveis?

---

## 🌍 Contexto Epidemiológico

### A Dengue no Brasil

- **Doença endêmica** em praticamente todo o território nacional
- **Sazonalidade marcante**: picos geralmente entre janeiro e maio
- **Variabilidade regional**: diferentes padrões de transmissão por região
- **Subnotificação**: muitos casos assintomáticos ou não notificados

### Fatores que Influenciam a Transmissão

#### Fatores Climáticos
- Temperatura entre 20-30°C favorece o vetor
- Chuvas criam criadouros
- Umidade alta aumenta sobrevivência do mosquito

#### Fatores Socioeconômicos
- Saneamento básico deficiente
- Densidade populacional
- Condições de moradia
- Acesso a água tratada

#### Fatores Ambientais
- Urbanização não planejada
- Descarte inadequado de lixo
- Acúmulo de água em recipientes

---

## 💻 Abordagem Técnica

### Granularidade

- **Espacial**: Nível municipal (código IBGE de 7 dígitos)
- **Temporal**: Séries semanais (semana epidemiológica)

### Pipeline Proposto

```
[Dados SINAN] + [Dados Climáticos] 
        ↓
[ETL e Limpeza]
        ↓
[Feature Engineering: lags, médias móveis, anomalias]
        ↓
[Modelagem: SARIMA → RF/XGBoost → LSTM]
        ↓
[Validação Temporal: rolling window]
        ↓
[Interpretação: SHAP, feature importance]
        ↓
[Sistema de Alerta: limiares por município]
```

### Inovações Propostas

1. **Pipeline Reproduzível Open Source**
   - Código completamente documentado
   - Fácil adaptação para outras doenças

2. **Comparação Sistemática de Modelos**
   - Benchmark justo com validação temporal
   - Métricas consistentes

3. **Análise de Transferência entre Municípios**
   - Técnicas de windowed correlation
   - Transfer learning para municípios com poucos dados

4. **Sistema de Alerta Prático**
   - Limiares adaptativos por município
   - Dashboard para gestores de saúde

---

## 📊 Resultados Esperados

### Produtos Acadêmicos

1. **Monografia de TCC** completa e rigorosa
2. **Artigo científico** para submissão em conferência/journal
3. **Código aberto** no GitHub com documentação

### Produtos Técnicos

1. **Pipeline ETL** para dados de dengue e clima
2. **Modelos treinados** e versionados
3. **Notebook interativo** para replicação
4. **Sistema de alerta** com limiares calibrados

### Contribuições Esperadas

- **Científica**: Comparação robusta de métodos para previsão de dengue no Brasil
- **Prática**: Ferramenta utilizável por gestores de saúde pública
- **Educacional**: Material didático para ensino de séries temporais e ML em saúde

---

## 🔗 Referências Iniciais

Este tema está fundamentado em dezenas de estudos científicos recentes. Ver documento completo de [Referências Bibliográficas](./02-referencias-bibliograficas.md) para lista detalhada de:

- Meta-análises sobre clima e dengue
- Trabalhos aplicando LSTM no Brasil
- TCCs e dissertações relacionadas
- Pipelines e sistemas operacionais (InfoDengue, EpiScanner)

---

## 📅 Cronograma Resumido

| Fase | Duração | Atividades |
|------|---------|------------|
| **Revisão Bibliográfica** | 2 meses | Levantamento de papers, TCCs, metodologias |
| **Coleta e Preparação** | 3 meses | ETL, limpeza, feature engineering |
| **Modelagem Baseline** | 2 meses | SARIMA, Prophet |
| **Modelagem Avançada** | 3 meses | RF, XGBoost, LSTM |
| **Análise e Interpretação** | 2 meses | SHAP, validação, testes |
| **Redação e Defesa** | 3 meses | Escrita do TCC, revisões, defesa |

**Total: ~15-18 meses**

Ver [Plano de Trabalho](./05-plano-de-trabalho.md) para cronograma detalhado.

---

*Última atualização: Outubro 2025*

