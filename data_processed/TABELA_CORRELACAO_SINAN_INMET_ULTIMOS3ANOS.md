# 📊 Tabela de Correlação e Causalidade: SINAN vs INMET
## Período: 02/01/2022 a 22/12/2024 (156 semanas)

---

## 📋 Informações do Período Analisado

| Métrica | Valor |
|---------|-------|
| **Data de Início** | 02 de Janeiro de 2022 |
| **Data de Fim** | 22 de Dezembro de 2024 |
| **Total de Semanas** | 156 semanas |
| **Total de Casos de Dengue** | 463,560 casos notificados |
| **Média de Casos por Semana** | 2971.5 casos/semana |

---

## 📖 Glossário de Métricas

### 🔍 Correlação de Pearson (r)
- **O que é**: Mede a relação linear entre duas variáveis
- **Interpretação**: 
  - |r| ≥ 0.7 → Correlação **Forte** 🔴
  - 0.4 ≤ |r| < 0.7 → Correlação **Moderada** 🟡
  - 0.2 ≤ |r| < 0.4 → Correlação **Fraca** 🟢
  - |r| < 0.2 → Correlação **Muito Fraca** ⚪
- **Direção**: 
  - r > 0 → **Positiva** ↑ (quando uma aumenta, a outra também aumenta)
  - r < 0 → **Negativa** ↓ (quando uma aumenta, a outra diminui)

### 📈 Correlação de Spearman (ρ)
- **O que é**: Mede a relação monotônica entre duas variáveis (não necessariamente linear)
- **Vantagem**: É mais robusta a outliers do que Pearson
- **Mesma interpretação de força e direção** que Pearson

### ⏱️ Teste de Causalidade de Granger
- **O que é**: Verifica se uma variável (ex: chuva) ajuda a **prever** a outra (ex: casos de dengue)
- **Lags**: Testa se dados de 1, 2, 3 ou 4 semanas anteriores são úteis para previsão
- **Interpretação**: 
  - p-valor < 0.05 → **Significativo** ✅ (há evidência de causalidade temporal)
  - p-valor ≥ 0.05 → **Não significativo** ❌ (não há evidência de causalidade)
- **Importância**: Se significativo, a variável climática pode ser usada para prever casos futuros de dengue

---

## 📊 Resultados Detalhados

| Variável Climática         | Descrição                                     | Média           | Desvio Padrão   | Valor Mínimo   | Valor Máximo     |   Correlação de Pearson (r) | Força da Correlação   | Direção    |   Correlação de Spearman (ρ) | Força Spearman   | Interpretação                                                                                                        |   Causalidade Lag 1 (p-valor) | Significativo Lag 1?   |   Causalidade Lag 2 (p-valor) | Significativo Lag 2?   |   Causalidade Lag 3 (p-valor) | Significativo Lag 3?   |   Causalidade Lag 4 (p-valor) | Significativo Lag 4?   | Melhor Lag Causal   | Conclusão Causalidade                                   |
|----------------------------|-----------------------------------------------|-----------------|-----------------|----------------|------------------|-----------------------------|-----------------------|------------|------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------|------------------------|-------------------------------|------------------------|-------------------------------|------------------------|-------------------------------|------------------------|---------------------|---------------------------------------------------------|
| Precipitação (mm)          | Quantidade total de chuva acumulada na semana | 32.58 mm/semana | 53.04 mm/semana | 0.00 mm/semana | 330.00 mm/semana |                      0.2041 | Fraca 🟢              | Positiva ↑ |                       0.2601 | Fraca            | Correlação fraca positiva (Pearson) / fraca (Spearman) entre precipitação (mm) e casos de dengue                     |                        0.0198 | ✅ SIM                 |                        0.0189 | ✅ SIM                 |                        0.0643 | ❌ NÃO                 |                        0.0474 | ✅ SIM                 | Lag 2 (p=0.0189)    | ✅ Há evidência de causalidade (melhor lag: 2 semanas)  |
| Umidade Relativa do Ar (%) | Umidade relativa média do ar durante a semana | 65.15 %         | 14.63 %         | 26.85 %        | 89.10 %          |                      0.3731 | Fraca 🟢              | Positiva ↑ |                       0.5132 | Moderada         | Correlação fraca positiva (Pearson) / moderada (Spearman) entre umidade relativa do ar (%) e casos de dengue         |                        0.2954 | ❌ NÃO                 |                        0.5192 | ❌ NÃO                 |                        0.6537 | ❌ NÃO                 |                        0.5196 | ❌ NÃO                 | Nenhum              | ❌ Não há evidência estatística de causalidade temporal |
| Temperatura Média (°C)     | Temperatura média do ar durante a semana      | 21.73 °C        | 1.79 °C         | 16.73 °C       | 26.65 °C         |                      0.1155 | Muito Fraca ⚪        | Positiva ↑ |                       0.0123 | Muito Fraca      | Correlação muito fraca positiva (Pearson) / muito fraca (Spearman) entre temperatura média (°c) e casos de dengue    |                        0.4445 | ❌ NÃO                 |                        0.6611 | ❌ NÃO                 |                        0.3682 | ❌ NÃO                 |                        0.5089 | ❌ NÃO                 | Nenhum              | ❌ Não há evidência estatística de causalidade temporal |
| Pressão Atmosférica (hPa)  | Pressão atmosférica média na semana           | 887.56 hPa      | 1.91 hPa        | 882.23 hPa     | 892.41 hPa       |                     -0.1059 | Muito Fraca ⚪        | Negativa ↓ |                      -0.1835 | Muito Fraca      | Correlação muito fraca negativa (Pearson) / muito fraca (Spearman) entre pressão atmosférica (hpa) e casos de dengue |                        0.1828 | ❌ NÃO                 |                        0.1173 | ❌ NÃO                 |                        0.2173 | ❌ NÃO                 |                        0.5585 | ❌ NÃO                 | Nenhum              | ❌ Não há evidência estatística de causalidade temporal |

---

## 🎯 Resumo Executivo

### Principais Achados


#### Precipitação (mm)

- **Correlação com casos de dengue**: Fraca 🟢 Positiva ↑
- **Pearson (r)**: 0.2041 _(Nota: Correlação de Spearman é fraca - ρ = 0.2601)_
- **Spearman (ρ)**: 0.2601
- **Causalidade Temporal**: ✅ Há evidência de causalidade (melhor lag: 2 semanas)


#### Umidade Relativa do Ar (%)

- **Correlação com casos de dengue**: Fraca 🟢 Positiva ↑
- **Pearson (r)**: 0.3731 _(Nota: Correlação de Spearman é moderada - ρ = 0.5132)_
- **Spearman (ρ)**: 0.5132
- **Causalidade Temporal**: ❌ Não há evidência estatística de causalidade temporal


#### Temperatura Média (°C)

- **Correlação com casos de dengue**: Muito Fraca ⚪ Positiva ↑
- **Pearson (r)**: 0.1155 _(Nota: Correlação de Spearman é muito fraca - ρ = 0.0123)_
- **Spearman (ρ)**: 0.0123
- **Causalidade Temporal**: ❌ Não há evidência estatística de causalidade temporal


#### Pressão Atmosférica (hPa)

- **Correlação com casos de dengue**: Muito Fraca ⚪ Negativa ↓
- **Pearson (r)**: -0.1059 _(Nota: Correlação de Spearman é muito fraca - ρ = -0.1835)_
- **Spearman (ρ)**: -0.1835
- **Causalidade Temporal**: ❌ Não há evidência estatística de causalidade temporal


---

## 📝 Notas Metodológicas

1. **Fonte dos Dados**:
   - Casos de dengue: SINAN (Sistema de Informação de Agravos de Notificação)
   - Dados climáticos: INMET (Instituto Nacional de Meteorologia)
   - Estação meteorológica: Brasília (A001)

2. **Agregação Temporal**: 
   - Dados agregados por semana epidemiológica
   - Variáveis climáticas: média semanal (temperatura, umidade, pressão) ou soma semanal (precipitação)

3. **Significância Estatística**:
   - Correlações: valores apresentados sem teste de significância adicional (valores próximos de zero indicam ausência de relação)
   - Causalidade de Granger: nível de significância de 5% (α = 0.05)

4. **Limitações**:
   - Correlação não implica causalidade direta
   - Outros fatores não considerados podem influenciar os casos de dengue
   - Atraso de notificação pode afetar a correlação temporal

---

**Data de geração**: 24 de Novembro de 2025 às 19:33:17

