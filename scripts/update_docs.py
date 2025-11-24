import os
import pandas as pd
import shutil

TEX_DIR = "docs/template/extracted/editaveis"
DATA_FILE = "data_processed/dataset_unificado.csv"
CORR_FILE = "data_processed/TABELA_CORRELACAO_SINAN_INMET_ULTIMOS3ANOS.csv"

def get_stats():
    df = pd.read_csv(DATA_FILE)
    df['data'] = pd.to_datetime(df['data'])
    
    stats = {}
    stats['total_cases'] = int(df['casos_dengue'].sum())
    
    # Peak
    peak_row = df.loc[df['casos_dengue'].idxmax()]
    stats['max_cases'] = int(peak_row['casos_dengue'])
    stats['peak_date'] = peak_row['data'].strftime('%d/%m/%Y')
    
    # Yearly stats
    yearly = df.groupby('ano')['casos_dengue'].sum()
    stats['cases_2022'] = int(yearly.get(2022, 0))
    stats['cases_2023'] = int(yearly.get(2023, 0))
    stats['cases_2024'] = int(yearly.get(2024, 0))
    
    # Correlations
    corr_df = pd.read_csv(CORR_FILE)
    # Find best absolute Pearson
    corr_df['abs_p'] = corr_df['Pearson'].abs()
    best = corr_df.sort_values('abs_p', ascending=False).iloc[0]
    stats['best_var'] = best['Variável']
    stats['best_pearson'] = best['Pearson']
    
    return stats

def generate_introducao(stats):
    return f"""\\chapter[Introdução]{{Introdução}}
\\label{{cap:introducao}}

A dengue é uma arbovirose sistêmica de evolução benigna na maioria dos casos, mas que pode apresentar manifestações graves e letais. O agente etiológico é um vírus de RNA de fita simples e polaridade positiva (DENV), pertencente à família \\textit{{Flaviviridae}} e ao gênero \\textit{{Flavivirus}}. A transmissão ocorre pela picada de fêmeas infectadas de mosquitos do gênero \\textit{{Aedes}}, sendo o \\textit{{Aedes aegypti}} o vetor primário em áreas urbanas.

\\section{{Contextualização e Importância do Trabalho}}

Nas últimas décadas, a doença consolidou-se como um dos mais críticos desafios de saúde pública global. O Distrito Federal (DF), especificamente, tornou-se um cenário alarmante nos últimos anos.

Dados consolidados para este trabalho mostram que, entre 2022 e 2024, o DF acumulou \\textbf{{{stats['total_cases']:,} casos notificados}} de dengue. O ano de 2024, em particular, foi marcado por uma epidemia sem precedentes, registrando {stats['cases_2024']:,} casos — um volume superior à soma dos dois anos anteriores (2022: {stats['cases_2022']:,}; 2023: {stats['cases_2023']:,}). O pico dessa crise ocorreu na semana de {stats['peak_date']}, contabilizando {stats['max_cases']:,} casos em apenas sete dias.

A escolha do Distrito Federal como estudo de caso justifica-se, portanto, pela magnitude e explosividade desses surtos recentes, bem como pelas características climáticas específicas da região (Cerrado).

\\section{{Definição do Problema}}

O problema central abordado é a dificuldade de prever, com precisão e horizonte temporal útil, a ocorrência de surtos explosivos como o de 2024. A análise preliminar sugere que variáveis climáticas, como chuva e umidade, antecedem o aumento de casos em várias semanas (fenômeno de \\textit{{lag}}).

\\section{{Objetivos}}

\\subsection{{Objetivo Geral}}

Desenvolver e avaliar modelos preditivos baseados em Inteligência Artificial para a previsão de casos de dengue no Distrito Federal, utilizando uma base de dados unificada do período de 2022 a 2024.

\\subsection{{Objetivos Específicos}}

\\begin{{enumerate}}
    \\item Coletar e processar dados do SINAN e INMET para o triênio 2022-2024.
    \\item Analisar correlações temporais e defasagens (lags) entre clima e dengue.
    \\item Implementar modelos preditivos (SARIMA, XGBoost, LSTM) no futuro TCC 2.
\\end{{enumerate}}
"""

def generate_aspectos(stats):
    return r"""\chapter{Aspectos Gerais}

\section{Bases de Dados}

Para a realização deste estudo, foi construída uma base de dados unificada cobrindo integralmente as semanas epidemiológicas dos anos de 2022, 2023 e 2024.

\subsection{Dados Epidemiológicos (SINAN)}
Os dados foram obtidos via API do InfoDengue (SINAN), abrangendo o município de Brasília (Geocódigo 5300108). A variável principal utilizada foi o número de casos semanais notificados.

\subsection{Dados Meteorológicos (INMET)}
Os dados climáticos provêm da Estação Automática de Brasília (A001) do Instituto Nacional de Meteorologia (INMET). Foram processadas as variáveis de Temperatura Média, Precipitação (Chuva), Umidade Relativa e Pressão Atmosférica, agregadas semanalmente para compatibilidade com os dados epidemiológicos.

\section{Processamento Automatizado}

Todo o fluxo de dados foi automatizado através de um \textit{pipeline} computacional em Python, que executa:
\begin{enumerate}
    \item Download automático dos dados brutos.
    \item Limpeza e padronização de datas (padrão ISO YYYY-MM-DD).
    \item Agregação semanal (Soma para chuva, Média para demais variáveis).
    \item Unificação (Merge) das bases de dados.
\end{enumerate}
"""

def generate_resultados(stats):
    return f"""\\chapter{{Resultados Preliminares}}
\\label{{cap:resultados}}

Neste capítulo, apresentamos a análise dos dados consolidados de 2022 a 2024.

\\section{{Evolução Temporal}}

A análise da série temporal revela o caráter explosivo do surto de 2024 em comparação aos anos anteriores.

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.95\\textwidth]{{figuras/evolucao_temporal_combinada.png}}
    \\caption{{Evolução temporal: Casos de Dengue vs Chuva (2022-2024).}}
    \\label{{fig:temporal}}
\\end{{figure}}

\\section{{Análise de Correlação}}

A matriz de correlação abaixo resume as relações lineares entre as variáveis. A variável com maior correlação observada foi a \\textbf{{{stats['best_var']}}}, com um coeficiente de Pearson de {stats['best_pearson']}.

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{figuras/heatmap_correlacao_oficial.png}}
    \\caption{{Matriz de Correlação de Pearson.}}
    \\label{{fig:heatmap}}
\\end{{figure}}

\\section{{Decomposição e Sazonalidade}}

A decomposição STL (Sazonalidade, Tendência e Resíduo) permite isolar o componente sazonal da doença, que apresenta picos recorrentes no início do ano (fevereiro/março).

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.9\\textwidth]{{figuras/decomposicao_stl_casos.png}}
    \\caption{{Decomposição STL da série de casos.}}
    \\label{{fig:stl}}
\\end{{figure}}

\\section{{Análise de Defasagem (Lags)}}

A análise de correlação cruzada confirma que a precipitação influencia os casos de dengue com um atraso significativo (lag), sugerindo que as chuvas de hoje impactam a proliferação do vetor semanas depois.

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{figuras/analise_lags_crosscorr.png}}
    \\caption{{Correlação Cruzada: Chuva defasada vs Casos.}}
    \\label{{fig:lags}}
\\end{{figure}}
"""

def update_docs():
    print("--- STEP 5: UPDATING DOCS ---")
    if not os.path.exists(DATA_FILE):
        print("❌ Data file missing.")
        return

    stats = get_stats()
    print(f"    Stats loaded: Total Cases {stats['total_cases']}")
    
    # Map filenames to generators
    mapping = {
        "introducao.tex": generate_introducao,
        "aspectosgerais.tex": generate_aspectos,
        "resultados_preliminares.tex": generate_resultados
    }
    
    for fname, generator in mapping.items():
        path = os.path.join(TEX_DIR, fname)
        if os.path.exists(path):
            # Backup
            shutil.copy(path, path + ".bak")
            # Write
            content = generator(stats)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    ✔ Updated {fname}")
        else:
            print(f"    ⚠️ File {fname} not found in template.")

if __name__ == "__main__":
    update_docs()

