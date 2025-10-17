# Diretório de Dados

Este diretório contém os dados do projeto, organizados em camadas (raw → processed).

## 📂 Estrutura

```
data/
├── raw/           # Dados brutos (não processados)
│   ├── sinan/     # Dados SINAN de dengue
│   └── climate/   # Dados climáticos (CHIRPS, ERA5, NASA POWER)
└── processed/     # Dados processados e prontos para modelagem
    ├── cases/     # Casos agregados por município-semana
    ├── climate/   # Variáveis climáticas agregadas
    └── features/  # Features finais para modelagem
```

## ⚠️ Importante

- **Dados brutos NÃO são versionados** no Git (são muito grandes)
- Use os scripts em `scripts/data/` para baixar os dados das fontes oficiais
- Mantenha um log de quando/como os dados foram baixados

## 🔄 Como Obter os Dados

### 1. Dados SINAN (Casos de Dengue)

```bash
cd scripts/data/
python download_sinan.py --start-year 20 --end-year 24
```

### 2. Dados Climáticos - INMET (2025) ⭐ NOVO

**Arquivos já baixados:** `C:\Users\pedro.santana\Downloads\2025\`

```bash
cd scripts/data/

# Processar todos os arquivos INMET
python process_inmet_bulk.py --input "C:/Users/pedro.santana/Downloads/2025" --output "../../data/processed/inmet"

# Gerar análises e visualizações
python analyze_inmet.py --data-dir "../../data/processed/inmet" --output-dir "../../data/processed/inmet/analises"
```

**O que isso faz:**
- ✅ Processa 273 estações meteorológicas (DF, GO, MS, etc.)
- ✅ Consolida dados horários em formato eficiente (Parquet)
- ✅ **Agrega por semana epidemiológica** (crucial para dengue!)
- ✅ **Cria lags temporais** (1, 2, 3, 4, 8, 12 semanas)
- ✅ Identifica "janelas de risco" para surtos
- ✅ Gera visualizações e estatísticas

**Saídas:**
```
data/processed/inmet/
├── inmet_consolidated_2025.parquet      # Dados horários
├── inmet_weekly_2025.parquet            # Dados semanais
├── inmet_weekly_lagged_2025.parquet     # Pronto para modelagem!
├── inmet_metadata.csv                   # Metadados das estações
└── analises/
    ├── analise_precipitacao.png
    ├── analise_temperatura.png
    ├── analise_risco.png
    └── semanas_risco_alto.csv
```

### 3. Dados Climáticos - NASA POWER (Alternativa)

```bash
cd scripts/data/
python download_climate.py single --lat -15.8 --lon -47.9 --start-date 20200101 --end-date 20241231
```

Para CHIRPS e ERA5, consulte os notebooks em `notebooks/`.

## 📋 Metadados

Sempre salve metadados junto com os dados:
- Data do download
- Fonte exata (URL)
- Versão dos dados (se aplicável)
- Total de registros
- Período coberto

Exemplo: `dengue_2024_metadata.json`

## 💾 Formatos Recomendados

- **Raw**: Formato original (JSON, NetCDF, CSV)
- **Processed**: Parquet (mais eficiente) ou HDF5 (para grandes volumes)
- **Features**: Parquet com índice temporal

## 📊 Tamanho Esperado

- SINAN (1 ano): ~100-500 MB compactado, ~1-3 GB descompactado
- CHIRPS (Brasil, 10 anos): ~50 GB
- ERA5: Variável conforme área e variáveis

Total estimado: **~100 GB** para projeto completo.

## 🔐 Privacidade

Os microdados do SINAN são públicos e anonimizados. Mesmo assim:
- Não compartilhe dados individuais desnecessariamente
- Use sempre dados agregados em publicações
- Siga diretrizes éticas de pesquisa em saúde

---

*Para mais informações, consulte a documentação em `docs/03-bases-de-dados.md`*

