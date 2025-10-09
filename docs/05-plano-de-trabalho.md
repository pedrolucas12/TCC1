# Plano de Trabalho e Cronograma

> Planejamento detalhado das atividades, cronograma e entregáveis do TCC.

---

## 🎯 Objetivos do TCC

### Objetivo Geral
Desenvolver um modelo preditivo para surtos de dengue em municípios brasileiros utilizando séries temporais epidemiológicas combinadas com dados climáticos, comparando diferentes técnicas de modelagem (estatística, machine learning e deep learning).

### Objetivos Específicos

1. **Coletar e integrar** dados epidemiológicos (SINAN) e climáticos (CHIRPS, ERA5, INMET) em escala municipal e resolução semanal

2. **Construir um pipeline ETL** reproduzível e documentado para processamento dos dados

3. **Realizar análise exploratória** para identificar padrões temporais, sazonalidade e correlações entre clima e dengue

4. **Desenvolver features** relevantes incluindo lags temporais, médias móveis, anomalias climáticas e variáveis socioeconômicas

5. **Implementar e comparar** modelos de previsão:
   - Baseline estatístico (SARIMA/SARIMAX, Prophet)
   - Machine Learning (Random Forest, XGBoost)
   - Deep Learning (LSTM)

6. **Avaliar os modelos** usando métricas apropriadas (RMSE, MAE, AUC) e validação temporal

7. **Interpretar os resultados** identificando variáveis climáticas mais preditivas, lags ótimos e diferenças regionais

8. **Desenvolver um sistema de alerta** com limiares calibrados para detecção precoce de surtos

9. **Documentar todo o processo** em formato acadêmico (monografia) e técnico (código aberto)

---

## 📅 Cronograma Detalhado (18 meses)

### Fase 1: Fundamentação Teórica (Meses 1-2)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 1-2 | Revisão bibliográfica: dengue e clima | Lista de 30+ papers |
| 3-4 | Revisão: modelos de séries temporais | Fichamento de técnicas |
| 5-6 | Revisão: ML/DL para epidemiologia | Tabela comparativa |
| 7-8 | Escrita: introdução e referencial teórico | Rascunho cap. 1 e 2 |

**Entregáveis:**
- ✅ Bibliografia completa (30+ referências)
- ✅ Fichamento de papers principais
- ✅ Rascunho dos capítulos teóricos

---

### Fase 2: Preparação de Dados (Meses 3-4)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 9-10 | Download SINAN (2010-2024) | Raw data armazenada |
| 11 | Download CHIRPS, ERA5 | Raw data climática |
| 12 | Download malhas IBGE, população | Shapefiles + tabelas |
| 13-14 | Implementar ETL: SINAN | Script `download_sinan.py` |
| 15 | Implementar ETL: Clima | Script `download_climate.py` |
| 16 | Testes de qualidade de dados | Relatório de qualidade |

**Entregáveis:**
- ✅ Scripts ETL funcionais
- ✅ Dados brutos organizados em `data/raw/`
- ✅ Relatório de qualidade dos dados
- ✅ Documentação do pipeline de coleta

---

### Fase 3: Processamento e Feature Engineering (Meses 5-6)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 17-18 | Limpeza e normalização SINAN | Dados limpos |
| 19 | Agregação espacial (zonal stats) | Clima por município |
| 20 | Agregação temporal (diário → semanal) | Dataset semanal |
| 21 | Feature engineering: lags | Features de lag |
| 22 | Feature engineering: médias móveis, anomalias | Features adicionais |
| 23 | Join final: casos + clima + população | Dataset completo |
| 24 | Armazenamento PostgreSQL/Parquet | BD estruturado |

**Entregáveis:**
- ✅ Dataset processado e pronto para modelagem
- ✅ Dicionário de features (metadados)
- ✅ Notebook de preprocessamento
- ✅ Dados em `data/processed/`

---

### Fase 4: Análise Exploratória (Meses 6-7)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 25 | Análise descritiva: casos de dengue | Estatísticas descritivas |
| 26 | Análise temporal: tendências e sazonalidade | Gráficos temporais |
| 27 | Análise espacial: mapas coropléticos | Mapas |
| 28 | Análise de correlações: clima vs dengue | Matriz de correlação |
| 29 | Cross-correlation function (CCF) | Identificação de lags |
| 30 | Escrita: seção de análise exploratória | Rascunho do cap. 3 |

**Entregáveis:**
- ✅ Notebook EDA completo com visualizações
- ✅ Relatório de insights principais
- ✅ Identificação de lags preliminares

---

### Fase 5: Modelagem Baseline (Meses 8-9)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 31-32 | Implementar SARIMA/SARIMAX | Modelo baseline 1 |
| 33 | Implementar Prophet | Modelo baseline 2 |
| 34 | Validação temporal (TimeSeriesSplit) | Métricas baseline |
| 35 | Tuning de hiperparâmetros | Modelos otimizados |
| 36 | Análise de resíduos | Diagnóstico de modelos |

**Entregáveis:**
- ✅ Modelos baseline treinados
- ✅ Métricas de avaliação (RMSE, MAE)
- ✅ Notebook de modelagem baseline

---

### Fase 6: Modelagem com Machine Learning (Meses 10-11)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 37-38 | Implementar Random Forest | Modelo RF |
| 39-40 | Implementar XGBoost | Modelo XGBoost |
| 41 | Grid search / Optuna para tuning | Hiperparâmetros ótimos |
| 42 | Feature selection (SHAP, importance) | Features selecionadas |
| 43 | Validação cruzada temporal | Métricas robustas |
| 44 | Comparação com baseline | Tabela comparativa |

**Entregáveis:**
- ✅ Modelos ML treinados e otimizados
- ✅ Análise SHAP de interpretabilidade
- ✅ Comparação baseline vs ML

---

### Fase 7: Deep Learning (Meses 12-13)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 45-46 | Preparar dados para LSTM (reshape) | Dados em formato 3D |
| 47-48 | Implementar LSTM | Modelo LSTM |
| 49 | Implementar BiLSTM | Modelo BiLSTM |
| 50 | Tuning (arquitetura, dropout, epochs) | Modelos otimizados |
| 51 | Avaliar e comparar com ML | Comparação completa |
| 52 | Ensemble (voting/stacking) | Modelo ensemble |

**Entregáveis:**
- ✅ Modelos DL treinados
- ✅ Comparação completa: Estatística vs ML vs DL
- ✅ Modelo ensemble final

---

### Fase 8: Interpretação e Análise Regional (Mês 14)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 53 | Análise SHAP detalhada (features importantes) | Gráficos SHAP |
| 54 | Análise de lags ótimos por região | Tabela de lags regionais |
| 55 | Casos de sucesso e falha | Estudos de caso |
| 56 | Transfer learning entre municípios | Experimentos de generalização |

**Entregáveis:**
- ✅ Relatório de interpretabilidade
- ✅ Análise regional de lags
- ✅ Insights para gestores de saúde

---

### Fase 9: Sistema de Alerta (Mês 15)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 57 | Definir limiares de surto por município | Tabela de limiares |
| 58 | Calibrar sistema de alerta | Sistema calibrado |
| 59 | Avaliar performance (precision, recall) | Métricas de alerta |
| 60 | Dashboard interativo (Streamlit/Dash) | Dashboard funcional |

**Entregáveis:**
- ✅ Sistema de alerta operacional
- ✅ Dashboard web
- ✅ Documentação para uso

---

### Fase 10: Validação Robusta e Testes (Mês 16)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 61 | Validação em municípios não vistos | Teste de generalização |
| 62 | Análise de sensibilidade | Robustez do modelo |
| 63 | Testes estatísticos (Diebold-Mariano) | Significância das diferenças |
| 64 | Refinamentos finais | Modelos finalizados |

**Entregáveis:**
- ✅ Validação completa
- ✅ Análise de sensibilidade
- ✅ Modelos finais salvos

---

### Fase 11: Redação do TCC (Meses 17-18)

| Semana | Atividades | Entregáveis |
|--------|-----------|-------------|
| 65-66 | Escrita: Metodologia | Capítulo 3 completo |
| 67-68 | Escrita: Resultados | Capítulo 4 completo |
| 69 | Escrita: Discussão | Capítulo 5 completo |
| 70 | Escrita: Conclusão e Trabalhos Futuros | Capítulo 6 completo |
| 71 | Revisão geral, formatação ABNT | Versão preliminar |
| 72 | Preparar apresentação (slides) | Slides prontos |
| 73-74 | Revisões com orientador | Versão final |
| 75 | Entrega e defesa | **TCC COMPLETO** |

**Entregáveis:**
- ✅ Monografia completa (formato ABNT)
- ✅ Apresentação (slides)
- ✅ Código no GitHub (público)
- ✅ Defesa do TCC

---

## 📦 Entregáveis Finais

### 1. Monografia (Documento Acadêmico)

**Estrutura prevista:**
- Resumo / Abstract
- 1. Introdução
- 2. Referencial Teórico
- 3. Metodologia
- 4. Resultados
- 5. Discussão
- 6. Conclusão e Trabalhos Futuros
- Referências Bibliográficas
- Apêndices (códigos, tabelas adicionais)

**Páginas estimadas:** 80-120 páginas

---

### 2. Código e Repositório GitHub

**Conteúdo:**
```
TCC1/
├── README.md (com badges, instruções)
├── docs/ (toda documentação)
├── scripts/ (ETL e processamento)
├── notebooks/ (análises e modelos)
├── models/ (modelos treinados salvos)
├── data/ (estrutura, sem dados brutos)
├── requirements.txt
├── LICENSE (MIT)
└── .gitignore
```

**Características:**
- ✅ Código limpo e comentado
- ✅ Documentação completa
- ✅ Reproduzível (requirements.txt)
- ✅ Licença open source (MIT)

---

### 3. Artigo Científico (Opcional, pós-defesa)

**Formato:** Artigo para submissão em conferência/journal
- **Opções:** SBCAS, ENIA, Brazilian Journal of Bioinformatics
- **Páginas:** 8-12 páginas (formato conferência)

---

### 4. Dashboard Interativo

**Tecnologia:** Streamlit ou Plotly Dash
**Funcionalidades:**
- Visualização de casos históricos
- Previsões para próximas semanas
- Alertas de surto por município
- Mapas interativos
- Análise de variáveis climáticas

---

### 5. Apresentação (Defesa)

**Formato:** PDF (slides)
**Duração:** 20-30 minutos + perguntas
**Conteúdo:**
- Introdução e motivação (3 min)
- Objetivos e hipóteses (2 min)
- Metodologia (5 min)
- Resultados principais (8 min)
- Discussão e conclusões (4 min)
- Trabalhos futuros (2 min)

---

## 🎯 Hipóteses a Serem Testadas

### H1: Melhoria com Clima
**Hipótese:** A inclusão de variáveis climáticas melhora significativamente a acurácia de previsão em comparação a modelos baseados apenas em série histórica de casos.

**Teste:** Comparar RMSE de modelos com e sem variáveis climáticas (teste estatístico de Diebold-Mariano).

---

### H2: Superioridade de ML/DL
**Hipótese:** Modelos de Machine Learning (XGBoost) e Deep Learning (LSTM) superam modelos estatísticos clássicos (SARIMA) em acurácia preditiva.

**Teste:** Comparar RMSE/MAE em validação cruzada temporal.

---

### H3: Transfer Learning
**Hipótese:** Para municípios com poucos dados históricos, usar informação de municípios vizinhos (windowed correlation) melhora a previsão.

**Teste:** Comparar performance em municípios com <3 anos de dados, com e sem features de municípios vizinhos.

---

### H4: Variabilidade Regional de Lags
**Hipótese:** A relação temporal ótima entre clima e dengue (lags) varia por região geográfica.

**Teste:** Análise de feature importance de lags por região (Norte, Nordeste, Sul, Sudeste, Centro-Oeste).

---

## 📊 Métricas de Sucesso

### Critérios Técnicos

1. **Acurácia Preditiva**
   - RMSE < 50 casos/semana (municípios grandes)
   - MAE < 30 casos/semana
   - MAPE < 40%

2. **Detecção de Surtos**
   - Recall > 0.75 (detectar 75% dos surtos)
   - Precision > 0.60 (reduzir falsos alarmes)
   - AUC > 0.80

3. **Reprodutibilidade**
   - Código roda sem erros
   - Documentação completa
   - Resultados replicáveis

### Critérios Acadêmicos

1. **Monografia**
   - Estrutura ABNT completa
   - Redação clara e objetiva
   - Figuras e tabelas de qualidade

2. **Defesa**
   - Apresentação clara e objetiva
   - Resposta adequada às perguntas
   - Demonstração de domínio do tema

---

## 🚧 Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Dados incompletos/corrompidos | Média | Alto | Download múltiplas fontes, validação de qualidade |
| Modelos não convergem | Baixa | Médio | Começar com baselines simples, tuning gradual |
| Falta de poder computacional (LSTM) | Média | Médio | Usar Google Colab Pro, AWS Free Tier |
| Atraso no cronograma | Alta | Alto | Buffers de 2 semanas entre fases |
| Dificuldade na interpretação | Média | Médio | SHAP, feature importance, consulta com orientador |

---

## 📚 Recursos Necessários

### Computacionais
- **Hardware**: Laptop com 16GB RAM (disponível)
- **GPU**: Google Colab Pro (~$10/mês) ou AWS (créditos educacionais)
- **Armazenamento**: 50GB para dados (~20GB SINAN + 20GB clima)

### Software
- Python 3.9+
- PostgreSQL + PostGIS (opcional)
- Jupyter Lab
- Git + GitHub

### Bibliográficos
- Acesso a journals (via CAPES/UnB)
- Papers baixados (PDF)

### Orientação
- Reuniões quinzenais com orientador
- Feedback em marcos principais (fim de cada fase)

---

## 🏆 Contribuições Esperadas

### Científica
- Comparação sistemática de métodos para previsão de dengue no Brasil
- Análise regional de lags climáticos
- Técnicas de transfer learning para municípios com poucos dados

### Prática
- Pipeline reproduzível e open source
- Ferramenta utilizável por gestores de saúde pública
- Dashboard para monitoramento

### Educacional
- Material didático para séries temporais em saúde
- Exemplo completo de projeto de Data Science
- Código bem documentado para comunidade

---

## ✅ Checklist de Progresso

### Planejamento
- [x] Tema definido
- [x] Cronograma elaborado
- [ ] Orientador definido
- [ ] Plano aprovado

### Execução
- [ ] Bibliografia completa
- [ ] Dados coletados
- [ ] ETL implementado
- [ ] EDA realizada
- [ ] Features criadas
- [ ] Modelos baseline implementados
- [ ] Modelos ML implementados
- [ ] Modelos DL implementados
- [ ] Análise de interpretabilidade
- [ ] Sistema de alerta

### Finalização
- [ ] Monografia rascunho
- [ ] Monografia revisada
- [ ] Código no GitHub
- [ ] Apresentação preparada
- [ ] Ensaio de defesa
- [ ] **DEFESA DO TCC**

---

## 📅 Datas Importantes (Exemplo - Ajustar conforme calendário UnB)

| Evento | Data Prevista | Status |
|--------|--------------|--------|
| Início do projeto | Outubro 2025 | ✅ |
| Entrega Proposta TCC1 | Dezembro 2025 | 🔄 |
| Apresentação TCC1 | Fevereiro 2026 | 🔄 |
| Qualificação (TCC2) | Agosto 2026 | 🔄 |
| Entrega versão preliminar | Março 2027 | 🔄 |
| Entrega versão final | Abril 2027 | 🔄 |
| Defesa Final | Maio 2027 | 🔄 |

---

## 📞 Contatos Úteis

- **Orientador**: [A definir]
- **Co-orientador**: [Opcional]
- **Coordenação de TCC**: [Contato da coordenação]

---

## 📖 Referências do Plano

Este plano de trabalho foi elaborado com base em:
- Diretrizes de TCC do curso de Engenharia de Software - UnB
- Trabalhos similares na literatura (ver [Referências Bibliográficas](./02-referencias-bibliograficas.md))
- Boas práticas de projetos de Data Science

---

*Última atualização: Outubro 2025*
*Versão: 1.0*

