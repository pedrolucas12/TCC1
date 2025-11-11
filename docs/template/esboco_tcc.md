# Esboço do TCC - Mapeamento do Template

Este documento relaciona cada seção do template LaTeX (`docs/template/extracted`) com os conteúdos já produzidos no repositório, indicando onde estão as informações, quais dados e scripts suportam cada parte e quais lacunas ainda precisam ser preenchidas.

## 1. Elementos Pré-Textuais

### `editaveis/informacoes.tex`
- **Campos a preencher:** autor, curso, título, data, palavras-chave, orientador, coorientador, CDU, data da aprovação, membros da banca.
- **Sugestões:**
  - Autor: `Pedro Lucas Pereira` / `Thiago ...` (confirmar conforme matrícula).
  - Curso: `Engenharia de Software` (FGA).
  - Título proposto (README): *Desenvolvimento de um Modelo de Previsão para Surtos de Dengue em Municípios Brasileiros utilizando Séries Temporais e Dados Climáticos*.
  - Palavras-chave iniciais: `dengue`, `previsão de surtos`, `séries temporais`, `dados climáticos`, `machine learning`.
  - Orientador / coorientador: confirmar com professor.
  - CDU / banca / data: preencher após definição oficial.

### `editaveis/resumo.tex`
- Basear-se em `docs/01-tema-e-motivacao.md` e no resumo do projeto (`README.md`, seção "Tema do TCC").
- Estrutura recomendada (200-250 palavras): problema de saúde pública, motivação, fontes de dados (SINAN, INMET, CHIRPS, ERA5, NASA POWER), abordagem metodológica (SARIMAX, Random Forest, XGBoost, LSTM), resultados esperados.
- Palavras-chave alinhadas às do arquivo de informações.

### `editaveis/abstract.tex`
- Tradução fiel do resumo para inglês.
- Palavras-chave em inglês: `dengue`, `outbreak forecasting`, `time series`, `climate data`, `machine learning`.

### Listas (`abreviaturas.tex`, `simbolos.tex`)
- Abreviaturas e siglas já utilizadas nas docs:
  - SINAN, INMET, CHIRPS, ERA5, NASA POWER, IBGE, LSTM, SARIMAX, RMSE, MAE, MAPE.
- Símbolos: caso seja necessário incluir variáveis matemáticas (por exemplo, \(y_{t}\), \(\hat{y}_{t}\), \(\mathrm{RMSE}\)).

### Agradecimentos/Dedicação/Epígrafe
- Conteúdo pessoal, opcional.

## 2. Parte Textual

### `editaveis/introducao.tex`
- Utilizar `docs/respostas.md` (seção 1) e `docs/01-tema-e-motivacao.md`.
- Estrutura sugerida:
  1. Contextualização da dengue no Brasil (dados SINAN 2025, importância de previsão).
  2. Motivação: impacto em saúde pública, desafios técnicos.
  3. Problema de pesquisa: pergunta formulada em `respostas.md`.
  4. Objetivo geral e específicos.
  5. Estrutura do documento (descrição dos capítulos seguintes).
- Citações potenciais (a partir de `docs/02-referencias-bibliograficas.md`): Fan et al. (2015), Naish et al. (2014), Chen et al. (2025).

### `editaveis/aspectosgerais.tex`
- Documento já contém orientações gerais; pode ser substituído por capítulo "Fundamentação Teórica" ou removido conforme necessidade.
- Sugestão: renomear capítulo para "Revisão Bibliográfica" e preencher com conteúdo de `docs/respostas.md` (seção 2) + `docs/02-referencias-bibliograficas.md`.
- Estrutura recomendada:
  - 2.1. Epidemiologia da dengue.
  - 2.2. Relação clima-dengue (temperatura, precipitação, umidade).
  - 2.3. Modelos preditivos em saúde (SARIMA, ML, DL).
  - 2.4. Trabalhos correlatos no Brasil (Chen et al., Bomfim et al., Silva et al.).

### `editaveis/consideracoes.tex`
- Pode ser utilizado para "Metodologia".
- Inserir pipeline completo descrito em `docs/04-metodologia.md`.
- Incluir figuras/tabelas:
  - Pipeline (pode ser desenhado com base no diagrama textual da metodologia).
  - Tabela com modelos e hiperparâmetros previstos (`docs/MODELOS_IA.md`).

### `editaveis/textoepostexto.tex`
- Sugestão: transformar em capítulo "Resultados Preliminares" ou "Análise de Dados".
- Conteúdo já disponível:
  - `notebooks/01_analise_dados_inmet.ipynb` (precisa ser atualizado após executar).
  - Scripts: `analyze_dengue_data.py`, `create_visualizations.py`.
  - Saídas: `data/processed/sinan_summary.txt`, `data/processed/visualizations/*.png`.
- Estrutura recomendada:
  - 4.1. Visão geral dos dados SINAN 2025 (estatísticas do resumo gerado pelo script).
  - 4.2. Distribuição geográfica (usar `distribuicao_por_uf.png`).
  - 4.3. Evolução temporal (gera gráfico via `create_visualizations.py` após ajuste).
  - 4.4. Análise demográfica e sintomas (gráficos de idade, sexo, sintomas).
  - 4.5. Limitações/bias dos dados (subnotificação, atraso).

### `editaveis/elementosdotexto.tex`
- Pode ser adequado para "Planejamento de Modelagem" ou "Plano de Trabalho".
- Usar `docs/05-plano-de-trabalho.md` e `docs/respostas.md` (seção 3 e 4).
- Sugerir subseções:
  - 5.1. Cronograma detalhado (transformar tabela do plano).
  - 5.2. Artefatos de software (scripts, pipelines).
  - 5.3. Métricas e critérios de avaliação.

### `editaveis/elementosdopostexto.tex`
- Recomendado para "Conclusões e Próximos Passos" do TCC1.
- Basear-se em `docs/respostas.md` (seção 3, objetivos e próximos passos).
- Estrutura: resumo das contribuições, limitações atuais, passos para TCC2.

## 3. Pós-Textual

### Referências (`bibliografia.bib`)
- Inserir entradas BibTeX usando `docs/02-referencias-bibliograficas.md`.
- Sugestão: iniciar com ~15 referências (Fan2015, Naish2014, Chen2025, Silva2024, Bomfim2023, etc.).

### Apêndices (`editaveis/apendices.tex`)
- Possíveis conteúdos:
  - Código dos scripts principais (`download_sinan.py`, `process_inmet_bulk.py`, `create_visualizations.py`).
  - Tabelas completas de variáveis SINAN.
  - Configurações de ambiente (`requirements.txt`).

### Anexos (`editaveis/anexos.tex`)
- Documentos externos: instruções oficiais, fichas, prints do dashboard (quando existir), outputs completos.

## 4. Dados, APIs e Scripts Existentes

### Fontes de Dados Documentadas (`docs/03-bases-de-dados.md`)
- **Epidemiológicos:** SINAN (OpenDataSUS), TabNet, InfoDengue.
- **Climáticos:** INMET, CHIRPS, ERA5, NASA POWER.
- **Auxiliares:** IBGE (malhas, população).

### Scripts de Coleta e Processamento (`scripts/data/`)
- `download_sinan.py`: download dos microdados SINAN por ano (já usado para 2025).
- `download_climate.py`: coleta inicial via NASA POWER (precisa configuração).
- `process_inmet_bulk.py`: pipeline de processamento INMET (CSV → Parquet).
- `analyze_inmet.py`: análises exploratórias climáticas.

### Scripts/Notebooks Analíticos
- `analyze_dengue_data.py`: resumo exploratório e estatísticas (gera `sinan_summary.txt`).
- `create_visualizations.py`: gráficos principais (UF, temporal, idade, sexo, sintomas, gravidade, correlação).
- `notebooks/01_analise_dados_inmet.ipynb`: template para análise climática (precisa execução após obtenção de dados INMET).

### Dados Já Disponíveis
- `data/raw/sinan/dengue_2025.parquet` (~1.5M registros, 139 colunas).
- `data/raw/sinan/dengue_2025_metadata.json` (metadados do download).
- `data/processed/sinan_summary.txt` (estatísticas básicas).
- `data/processed/visualizations/*.png` (visualizações geradas).

## 5. Lacunas Identificadas
- Dados INMET ainda não processados (`data/processed/inmet/` vazio) → executar `process_inmet_bulk.py` com arquivos CSV.
- Notebook `01_analise_dados_inmet.ipynb` precisa ser atualizado com dados reais.
- Ajustar `create_visualizations.py` (corrigir geração de gráficos interrompida e completar salvamento).
- Inserir gráficos exportados no capítulo de resultados.
- Preparar figuras/tabelas em formato `.pdf` ou `.png` para inserir no LaTeX.
- Compilar BibTeX com as referências listadas.
- Definir oficialmente autores, orientador, data, palavras-chave.

## 6. Próximos Passos para Preenchimento
1. **Pré-textuais**: atualizar `informacoes.tex`, redigir Resumo/Abstract, montar listas de abreviaturas.
2. **Introdução e Revisão**: migrar conteúdo dos documentos existentes para os `.tex` correspondentes.
3. **Metodologia**: copiar/ajustar texto da metodologia, incluir pipeline e tabela de modelos.
4. **Resultados Preliminares**: consolidar análises SINAN, inserir gráficos gerados e tabelas (usar `longtable` ou `tabularx`).
5. **Plano de Trabalho**: converter cronograma para tabela LaTeX.
6. **Conclusões/Próximos Passos**: focar em entregas de TCC1 e planejamento de TCC2.
7. **Referências**: adicionar entradas BibTeX e garantir citações.

---

> **Observação:** manter a pasta `docs/template/extracted` como área de trabalho LaTeX. Após finalizar o esboço em Markdown, iniciar a transcrição dos trechos para os arquivos `.tex`, garantindo consistência com as normas ABNT e com o template fornecido.
