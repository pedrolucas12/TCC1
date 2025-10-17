# 🚀 GUIA DE EXECUÇÃO - Processamento de Dados INMET

## ✅ Status Atual

- [x] Arquivos INMET baixados: `C:\Users\pedro.santana\Downloads\2025\`
- [x] Scripts criados e prontos para uso
- [ ] **Próximo passo:** Executar o processamento

---

## 📋 Passo a Passo

### **Passo 1: Abrir Terminal no VS Code**

1. Abra o VS Code
2. Abra o terminal: `Ctrl + '` ou `Terminal > New Terminal`
3. Navegue até a pasta de scripts:

```powershell
cd c:\Users\pedro.santana\Documents\UnB\TCC1\scripts\data
```

---

### **Passo 2: Executar Processamento dos Dados INMET**

```powershell
python process_inmet_bulk.py --input "C:\Users\pedro.santana\Downloads\2025" --output "..\..\data\processed\inmet"
```

**O que vai acontecer:**
- 🔄 Lê todos os ~273 arquivos CSV
- 📊 Extrai temperatura, precipitação, umidade
- 📅 Agrega por semana epidemiológica
- ⏰ Cria lags (1-12 semanas atrás)
- 💾 Salva em formato Parquet (eficiente)

**Tempo estimado:** 2-5 minutos

---

### **Passo 3: Gerar Análises e Visualizações**

Após o processamento, execute:

```powershell
python analyze_inmet.py --data-dir "..\..\data\processed\inmet" --output-dir "..\..\data\processed\inmet\analises"
```

**O que vai gerar:**
- 📈 Gráfico de padrões de precipitação
- 🌡️ Análise de temperatura (faixa ideal 20-30°C)
- ⚠️ Identificação de "semanas de risco" para dengue
- 🗺️ Ranking de estados com maior risco climático

**Tempo estimado:** 1-2 minutos

---

### **Passo 4: Verificar Resultados**

Cheque os arquivos gerados:

```powershell
# Listar arquivos processados
ls ..\..\data\processed\inmet

# Ver primeiras linhas do arquivo semanal
python -c "import pandas as pd; df = pd.read_parquet('../../data/processed/inmet/inmet_weekly_2025.parquet'); print(df.head()); print(f'\nTotal: {len(df)} semanas-estação')"
```

---

## 🎯 Estrutura de Dados Gerada

### 1. **inmet_consolidated_2025.parquet**
- Dados horários de todas as estações
- ~6,500 linhas × 273 estações = ~1.7M registros
- Colunas: Data, Hora, Precipitação, Temperatura, Umidade, Pressão, Vento, etc.

### 2. **inmet_weekly_2025.parquet** ⭐ PRINCIPAL
- Dados agregados por semana epidemiológica
- ~39 semanas × 273 estações = ~10,600 registros
- Variáveis agregadas: soma (precipitação), média (temp, umidade), min, max

### 3. **inmet_weekly_lagged_2025.parquet** 🔥 PARA MODELAGEM
- Dados semanais + features com lags temporais
- Permite treinar modelos com janelas de 1-12 semanas
- **Este é o arquivo que você vai usar para prever dengue!**

### 4. **inmet_metadata.csv**
- Metadados de cada estação
- Coordenadas (lat, lon), altitude, UF, região
- Útil para join espacial com municípios

---

## 🔍 Exploração Inicial (Jupyter/Python)

Depois de processar, você pode explorar os dados:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados semanais
df = pd.read_parquet('../../data/processed/inmet/inmet_weekly_2025.parquet')

# Ver estrutura
print(df.info())
print(df.head())

# Resumo por estado
print(df.groupby('uf').size().sort_values(ascending=False))

# Precipitação média por UF
precip_col = [c for c in df.columns if 'PRECIPITA' in c.upper() and 'sum' in c.lower()][0]
df.groupby('uf')[precip_col].mean().sort_values(ascending=False).plot(kind='barh')
plt.xlabel('Precipitação média semanal (mm)')
plt.title('Estados mais chuvosos - Jan-Set 2025')
plt.tight_layout()
plt.show()
```

---

## 🔗 Próximos Passos (Após Processamento)

### **1. Juntar com Dados de Dengue**

Você vai precisar:
- Baixar dados SINAN (casos de dengue por município + semana)
- Fazer **join espacial**: estação meteorológica → município mais próximo
- Criar dataset final: `município + semana + clima + casos_dengue`

### **2. Feature Engineering**

- Calcular lags de clima (já feito! ✅)
- Adicionar médias móveis
- Calcular anomalias climáticas
- Adicionar dados populacionais (IBGE)

### **3. Modelagem**

- **Baseline:** SARIMA (modelo estatístico)
- **ML:** XGBoost, Random Forest
- **DL:** LSTM (redes neurais recorrentes)
- **Ensemble:** Combinar modelos

---

## 📊 Exemplo de Análise Rápida

Após executar os scripts, você pode verificar resultados assim:

```powershell
# Ver estatísticas básicas
python -c "import pandas as pd; df = pd.read_parquet('../../data/processed/inmet/inmet_weekly_2025.parquet'); print(df.describe())"

# Ver colunas disponíveis
python -c "import pandas as pd; df = pd.read_parquet('../../data/processed/inmet/inmet_weekly_2025.parquet'); print(list(df.columns))"

# Ver estados únicos
python -c "import pandas as pd; df = pd.read_parquet('../../data/processed/inmet/inmet_weekly_2025.parquet'); print(df['uf'].unique())"
```

---

## ❓ Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'pandas'"
```powershell
pip install pandas numpy pyarrow matplotlib seaborn
```

### Erro: "FileNotFoundError: [Errno 2] No such file"
- Verifique se o caminho está correto
- Use caminhos absolutos se necessário

### Arquivos muito grandes?
- Parquet é otimizado (3-5x menor que CSV)
- Dados semanais são ~1000x menores que horários

---

## 📞 Suporte

Se tiver dúvidas:
1. Consulte `scripts/data/README.md`
2. Veja exemplos em `notebooks/01_analise_dados_inmet.ipynb`
3. Leia documentação em `docs/03-bases-de-dados.md`

---

## ✅ Checklist

- [ ] Terminal aberto no diretório correto
- [ ] Executei `process_inmet_bulk.py`
- [ ] Arquivos `.parquet` foram criados
- [ ] Executei `analyze_inmet.py`
- [ ] Gráficos foram gerados
- [ ] Verifiquei os resultados
- [ ] Pronto para juntar com dados de dengue!

---

**Boa sorte com o TCC! 🎓📊**
