# Scripts de Processamento de Dados

Este diretório contém os scripts para coleta e processamento de dados para o TCC.

## 📁 Estrutura

```
scripts/data/
├── download_sinan.py          # Download de casos de dengue (SINAN/DataSUS)
├── download_climate.py        # Download de dados climáticos (NASA POWER)
├── process_inmet_bulk.py      # 🆕 Processamento massivo de dados INMET
└── analyze_inmet.py           # 🆕 Análise exploratória dos dados INMET
```

## 🌦️ Processamento de Dados INMET

### 1. Processamento Massivo (`process_inmet_bulk.py`)

Este script processa múltiplos arquivos CSV do INMET e gera datasets consolidados.

#### **O que faz:**
- ✅ Lê todos os arquivos CSV do INMET de um diretório
- ✅ Extrai metadados (região, UF, estação, coordenadas, altitude)
- ✅ Consolida dados horários de todas as estações
- ✅ **Agrega por semana epidemiológica** (crucial para junção com SINAN!)
- ✅ **Cria features com lags temporais** (1, 2, 3, 4, 8, 12 semanas)
- ✅ Salva em formato Parquet (eficiente)

#### **Uso:**

```bash
# Processar todos os arquivos da pasta Downloads/2025
python process_inmet_bulk.py --input "C:/Users/pedro.santana/Downloads/2025" --output "../../data/processed/inmet"

# Com arquivos individuais também
python process_inmet_bulk.py --input "C:/Users/pedro.santana/Downloads/2025" --output "../../data/processed/inmet" --save-individual
```

#### **Saídas geradas:**

```
data/processed/inmet/
├── inmet_consolidated_2025.parquet      # Dados horários consolidados
├── inmet_weekly_2025.parquet            # Dados agregados por semana
├── inmet_weekly_lagged_2025.parquet     # Dados semanais + lags (PRONTO PARA MODELAGEM!)
└── inmet_metadata.csv                   # Metadados das estações
```

---

### 2. Análise Exploratória (`analyze_inmet.py`)

Gera visualizações e estatísticas dos dados processados.

#### **O que faz:**
- 📊 Analisa padrões sazonais de **precipitação** (criadouros do mosquito)
- 🌡️ Analisa distribuição de **temperatura** (faixa ideal 20-30°C)
- 💧 Calcula **umidade relativa**
- ⚠️ **Identifica "janelas de risco"** para dengue:
  - Temperatura entre 20-30°C
  - Precipitação > 50mm/semana
  - Umidade > 60%
- 🗺️ Ranqueia estados por risco climático

#### **Uso:**

```bash
python analyze_inmet.py --data-dir "../../data/processed/inmet" --output-dir "../../data/processed/inmet/analises"
```

#### **Saídas geradas:**

```
data/processed/inmet/analises/
├── analise_precipitacao.png       # Padrões de chuva
├── analise_temperatura.png        # Distribuição de temperatura
├── analise_risco.png              # Estados com maior risco
└── semanas_risco_alto.csv         # Dataset com semanas de alto risco
```

---

## 🔗 Integração com Dados de Dengue

### Pipeline Completo:

```
1. INMET (clima)                    2. SINAN (dengue)
   ↓                                   ↓
   process_inmet_bulk.py              download_sinan.py
   ↓                                   ↓
   Dados semanais por estação         Casos semanais por município
   ↓                                   ↓
   └──────────────┬────────────────────┘
                  ↓
           JOIN ESPACIAL
      (estação → município mais próximo)
                  ↓
           DATASET FINAL
    (município + semana + clima + casos)
                  ↓
         FEATURE ENGINEERING
      (lags, médias móveis, anomalias)
                  ↓
           MODELAGEM
    (SARIMA, XGBoost, LSTM)
```

---

## 📊 Variáveis Climáticas Relevantes

### Precipitação 🌧️
- **Por que é importante?**: Chuva cria criadouros (pneus, vasos, calhas)
- **Lag típico**: 3-8 semanas entre chuva e pico de casos
- **Métrica**: Precipitação acumulada semanal (mm)

### Temperatura 🌡️
- **Por que é importante?**: Afeta ciclo de vida do mosquito e replicação viral
- **Faixa ideal**: 20-30°C
- **Métrica**: Temperatura média, mínima, máxima

### Umidade 💧
- **Por que é importante?**: Umidade alta aumenta sobrevivência do mosquito
- **Limiar**: > 60% considerado favorável
- **Métrica**: Umidade relativa média

---

## 🎯 Exemplo de Workflow Completo

### Passo 1: Processar dados INMET
```bash
cd scripts/data/
python process_inmet_bulk.py \
    --input "C:/Users/pedro.santana/Downloads/2025" \
    --output "../../data/processed/inmet"
```

**Resultado:** Arquivos `.parquet` com dados semanais e lags

### Passo 2: Analisar padrões climáticos
```bash
python analyze_inmet.py \
    --data-dir "../../data/processed/inmet" \
    --output-dir "../../data/processed/inmet/analises"
```

**Resultado:** Gráficos e relatórios de análise exploratória

### Passo 3: Baixar dados de dengue (próximo)
```bash
python download_sinan.py --start-year 25 --end-year 25
```

### Passo 4: Juntar datasets e treinar modelo
- Ver notebook: `notebooks/02_juntar_clima_dengue.ipynb` (a ser criado)

---

## 🚀 Performance

### Otimizações:
- **Parquet**: 3-5x menor que CSV, leitura muito mais rápida
- **Agregação semanal**: Reduz volume de dados em ~168x (24h × 7 dias)
- **Lags pré-computados**: Evita recalcular durante treinamento

### Tamanho esperado:
- Dados horários (273 dias, 100 estações): ~50 MB
- Dados semanais: ~500 KB
- Dados com lags: ~2 MB

---

## ⚠️ Problemas Comuns

### Encoding
Se aparecer caracteres estranhos (Ã§, ã):
- Os arquivos INMET usam `latin1` (ISO-8859-1)
- Script já configurado corretamente

### Decimais
- INMET usa **vírgula** (,) como separador decimal
- Script converte automaticamente para ponto (.)

### Datas
- Formato INMET: `2025/01/01`
- Convertido para `datetime` do pandas

---

## 📚 Referências

### Dados INMET
- **Site**: https://portal.inmet.gov.br/
- **BDMEP**: https://bdmep.inmet.gov.br/
- **Formato**: CSV com separador `;` e decimal `,`

### Literatura Relevante
- Lags de precipitação (3-8 semanas) são preditores fortes
- Temperatura entre 20-30°C é ideal para *Aedes aegypti*
- Umidade > 60% aumenta sobrevivência do vetor

---

## 📝 TODO (Próximos Passos)

- [ ] Criar script de join espacial (estações → municípios)
- [ ] Implementar interpolação espacial (IDW ou Kriging)
- [ ] Adicionar dados de outras fontes (CHIRPS, ERA5)
- [ ] Criar pipeline automatizado (Airflow/Prefect)
- [ ] Adicionar testes unitários

---

**Dúvidas?** Consulte a documentação completa em `docs/03-bases-de-dados.md`
