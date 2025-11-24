import os
import pandas as pd

TEX_DIR = "docs/template/extracted/editaveis"
DATA_FILE = "data_processed/dataset_unificado.csv"
CORR_FILE = "data_processed/TABELA_CORRELACAO_SINAN_INMET_ULTIMOS3ANOS.csv"

def get_extended_stats():
    df = pd.read_csv(DATA_FILE)
    df['data'] = pd.to_datetime(df['data'])
    df['ano'] = df['data'].dt.year
    df['mes'] = df['data'].dt.month
    
    stats = {}
    stats['total_cases'] = int(df['casos_dengue'].sum())
    
    # Yearly breakdown
    yearly = df.groupby('ano')['casos_dengue'].agg(['sum', 'mean', 'max']).round(0)
    stats['cases_2022'] = int(yearly.loc[2022, 'sum'])
    stats['cases_2023'] = int(yearly.loc[2023, 'sum'])
    stats['cases_2024'] = int(yearly.loc[2024, 'sum'])
    stats['mean_2022'] = int(yearly.loc[2022, 'mean'])
    stats['mean_2023'] = int(yearly.loc[2023, 'mean'])
    stats['mean_2024'] = int(yearly.loc[2024, 'mean'])
    
    # Peak
    peak_row = df.loc[df['casos_dengue'].idxmax()]
    stats['max_cases'] = int(peak_row['casos_dengue'])
    stats['peak_date'] = peak_row['data'].strftime('%d/%m/%Y')
    stats['peak_rain'] = peak_row.get('chuva', 0)
    stats['peak_temp'] = peak_row.get('temperatura_media', 0)
    stats['peak_umid'] = peak_row.get('umidade', 0)
    
    # Monthly pattern
    monthly = df.groupby('mes')['casos_dengue'].mean().sort_values(ascending=False)
    stats['peak_month'] = monthly.index[0]
    stats['peak_month_cases'] = int(monthly.iloc[0])
    
    # Correlation table
    corr_df = pd.read_csv(CORR_FILE)
    stats['best_var'] = corr_df.loc[corr_df['Pearson'].abs().idxmax(), 'Variável']
    stats['best_pearson'] = corr_df.loc[corr_df['Pearson'].abs().idxmax(), 'Pearson']
    
    # Granger results for chuva
    chuva_row = corr_df[corr_df['Variável'] == 'Chuva'].iloc[0]
    stats['granger_chuva_lag1'] = chuva_row['Granger Lag 1 (p-value)']
    stats['granger_chuva_sig1'] = chuva_row['Sig Lag 1']
    
    return stats

def update_resultados_extended():
    print(">>> Extending Resultados Preliminares...")
    path = os.path.join(TEX_DIR, "resultados_preliminares.tex")
    stats = get_extended_stats()
    
    meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 
             6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro',
             11: 'novembro', 12: 'dezembro'}
    
    new_content = f"""\\chapter{{Resultados Preliminares}}
\\label{{cap:resultados}}

Este capítulo apresenta os resultados da análise exploratória e estatística dos dados unificados de dengue e variáveis climáticas para o Distrito Federal no período de 2022 a 2024. A base de dados consolidada compreende 156 semanas epidemiológicas contínuas, sem lacunas temporais significativas, totalizando {stats['total_cases']:,} casos notificados no triênio.

\\section{{Caracterização Descritiva da Série Temporal}}

A análise descritiva revela uma disparidade impressionante entre os anos estudados. Enquanto 2022 e 2023 apresentaram perfis epidemiológicos relativamente controlados, com médias semanais de {stats['mean_2022']:,} e {stats['mean_2023']:,} casos, respectivamente, o ano de 2024 caracterizou-se por uma epidemia de magnitude sem precedentes, com média semanal de {stats['mean_2024']:,} casos.

O comportamento sazonal é claramente observável. Os meses de maior incidência histórica concentram-se no primeiro trimestre do ano, com picos típicos em {meses[stats['peak_month']]}, período que coincide com o auge da estação chuvosa no Cerrado. Esse padrão é consistente com a biologia do vetor, que requer água estagnada para completar seu ciclo de desenvolvimento.

\\section{{Evolução Temporal e Sazonalidade}}

A Figura \\ref{{fig:temporal}} apresenta a série temporal completa de casos de dengue sobreposta à precipitação semanal acumulada. Observa-se uma correspondência visual entre períodos de maior volume pluviométrico e subsequentes picos de casos, porém com um deslocamento temporal (\textit{{lag}}).

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.95\\textwidth]{{figuras/evolucao_temporal_combinada.png}}
    \\caption{{Evolução temporal dos casos de dengue e precipitação no Distrito Federal (2022-2024). O eixo esquerdo representa os casos notificados e o eixo direito a precipitação em milímetros.}}
    \\label{{fig:temporal}}
\\end{{figure}}

O evento extremo de 2024 é evidente: a semana epidemiológica iniciada em {stats['peak_date']} registrou o pico histórico de {stats['max_cases']:,} casos em apenas sete dias. Nesse momento crítico, as condições climáticas eram favoráveis à proliferação do vetor: umidade relativa do ar de {stats['peak_umid']:.1f}\\%, temperatura média de {stats['peak_temp']:.1f}°C e precipitação acumulada de {stats['peak_rain']:.1f} mm.

\\section{{Decomposição STL e Componentes Temporais}}

A decomposição STL (Seasonal and Trend decomposition using Loess) permite isolar três componentes fundamentais da série temporal: a tendência de longo prazo, a sazonalidade recorrente e o resíduo (ruído aleatório).

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.9\\textwidth]{{figuras/decomposicao_stl_casos.png}}
    \\caption{{Decomposição STL da série temporal de casos de dengue, revelando a componente de tendência (aumento geral), sazonalidade (ciclos anuais) e resíduos.}}
    \\label{{fig:stl}}
\\end{{figure}}

A análise da componente sazonal confirma que o padrão cíclico anual é robusto e previsível, com picos recorrentes concentrados entre as semanas epidemiológicas 6 e 14 (fevereiro a abril). A componente de tendência revela um crescimento de fundo, possivelmente relacionado à expansão urbana e ao aumento da população suscetível. Os resíduos mostram variabilidade não explicada pelos componentes sazonal e tendência, justificando a necessidade de incorporar variáveis climáticas externas na modelagem preditiva.

\\section{{Análise de Correlação}}

\\subsection{{Correlação Linear (Pearson e Spearman)}}

A análise de correlação linear foi conduzida para quantificar a força da associação entre as variáveis climáticas e o número de casos semanais. A Tabela \\ref{{tab:correlacao}} apresenta os coeficientes de Pearson e Spearman calculados.

A variável climática que apresentou a maior correlação linear imediata com os casos foi a \\textbf{{{stats['best_var']}}}, com um coeficiente de Pearson de {stats['best_pearson']:.4f}. O coeficiente de Spearman, que mede associações monotônicas (não necessariamente lineares), foi ainda mais elevado para essa variável, sugerindo uma relação robusta e não-linear subjacente.

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{figuras/heatmap_correlacao_oficial.png}}
    \\caption{{Matriz de correlação de Pearson entre todas as variáveis do estudo. Valores próximos de +1 indicam correlação positiva forte; valores próximos de -1, correlação negativa forte; valores próximos de 0, ausência de correlação linear.}}
    \\label{{fig:heatmap}}
\\end{{figure}}

\\subsection{{Correlação Cruzada e Defasagem Temporal}}

A análise de correlação cruzada foi fundamental para desvendar o fenômeno de defasagem temporal. Calculou-se a correlação entre a série de casos ($Y_t$) e as séries climáticas defasadas de $k$ semanas ($X_{{t-k}}$), para $k = 0, 1, ..., 8$.

\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{figuras/analise_lags_crosscorr.png}}
    \\caption{{Função de Correlação Cruzada: Correlação entre casos de dengue e precipitação defasada de 0 a 8 semanas. O aumento gradual da correlação com o aumento do lag sugere que a chuva leva tempo para manifestar seu efeito biológico sobre a população de mosquitos.}}
    \\label{{fig:lags}}
\\end{{figure}}

Os resultados são reveladores: enquanto a correlação imediata (lag 0) entre chuva e casos é relativamente baixa ($r = 0.09$), a correlação aumenta progressivamente ao longo do tempo, atingindo seu pico aproximadamente 7 a 8 semanas após o evento chuvoso ($r \\approx 0.27$). Esse padrão é biologicamente consistente com o ciclo de vida do mosquito: a chuva cria os criadouros, os ovos eclodem, as larvas se desenvolvem, e os mosquitos adultos emergem semanas depois, iniciando o ciclo de transmissão.

\\section{{Teste de Causalidade de Granger}}

Para validar estatisticamente a precedência temporal e a causalidade no sentido de Granger, foram realizados testes formais de hipótese. Os resultados indicam que a \\textbf{{precipitação}} apresenta evidência estatística de causalidade de Granger nos lags 1 e 2 semanas (valor-p < 0.05), confirmando que as chuvas antecedem e melhoram a previsão dos casos futuros.

Por outro lado, a umidade relativa, embora apresente a maior correlação linear imediata, não demonstrou causalidade de Granger estatisticamente significativa nos lags testados (1 a 4 semanas), sugerindo que sua relação com os casos pode ser mais indireta ou mediada por outras variáveis não observadas.

\\section{{Implicações para a Modelagem}}

Os achados desta análise preliminar fornecem direcionamentos claros para a etapa de modelagem preditiva (TCC 2):

\\begin{{enumerate}}
    \\item \\textbf{{Variáveis Clave:}} A precipitação e a umidade devem ser incorporadas aos modelos, mas com tratamentos diferentes: a chuva com defasagens de 1-2 semanas (devido ao Granger), e a umidade de forma mais imediata ou como variável de contexto.
    
    \\item \\textbf{{Engenharia de Atributos:}} Será necessário criar variáveis de lag explícitas (ex: `chuva_lag_1`, `chuva_lag_2`) para alimentar os algoritmos de Machine Learning.
    
    \\item \\textbf{{Sazonalidade:}} A decomposição STL confirma que os modelos devem ser capazes de capturar a sazonalidade anual, seja através de componentes sazonais explícitos (SARIMA) ou através de atributos temporais cíclicos (ML).
\\end{{enumerate}}
"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Resultados Preliminares extended.")

def create_cronograma():
    print(">>> Creating Cronograma...")
    path = os.path.join(TEX_DIR, "cronograma.tex")
    
    new_content = r"""\chapter{Cronograma de Execução}
\label{cap:cronograma}

Este capítulo apresenta o planejamento temporal detalhado das atividades do TCC 1 e do TCC 2, organizadas por etapas e com estimativa de duração em semanas.

\section{Atividades do TCC 1}

O TCC 1 foi dedicado à construção da base de dados e à análise exploratória preliminar. As atividades já executadas e suas durações estimadas foram:

\begin{enumerate}
    \item \textbf{Revisão Bibliográfica e Fundamentação Teórica} (4 semanas)
    \begin{itemize}
        \item Pesquisa sobre epidemiologia da dengue e dinâmica de transmissão.
        \item Revisão do estado da arte em modelos preditivos para saúde pública.
        \item Estudo das tecnologias de Machine Learning e Deep Learning aplicadas a séries temporais epidemiológicas.
    \end{itemize}
    
    \item \textbf{Identificação e Caracterização das Bases de Dados} (2 semanas)
    \begin{itemize}
        \item Mapeamento das fontes de dados oficiais (SINAN e INMET).
        \item Análise da estrutura, formato e qualidade dos dados brutos.
        \item Definição da estratégia de coleta e padronização.
    \end{itemize}
    
    \item \textbf{Desenvolvimento do Pipeline de Engenharia de Dados} (3 semanas)
    \begin{itemize}
        \item Programação de scripts para download automatizado (API InfoDengue e arquivos INMET).
        \item Implementação de rotinas de limpeza e tratamento de dados.
        \item Criação do módulo de agregação temporal (diário para semanal).
        \item Desenvolvimento do algoritmo de unificação (merge) das bases.
    \end{itemize}
    
    \item \textbf{Análise Estatística Exploratória} (3 semanas)
    \begin{itemize}
        \item Geração de estatísticas descritivas e visualizações exploratórias.
        \item Cálculo de correlações de Pearson e Spearman.
        \item Implementação da análise de correlação cruzada (lags de 0 a 8 semanas).
        \item Execução dos testes de causalidade de Granger.
    \end{itemize}
    
    \item \textbf{Redação e Documentação} (2 semanas)
    \begin{itemize}
        \item Redação dos capítulos de Introdução, Revisão Bibliográfica e Metodologia.
        \item Incorporação dos resultados preliminares e figuras geradas.
        \item Revisão textual e formatação conforme normas ABNT.
    \end{itemize}
\end{enumerate}

\textbf{Total estimado do TCC 1: 14 semanas}

\section{Planejamento para o TCC 2}

O TCC 2 focará na construção, treinamento e avaliação dos modelos preditivos. O cronograma previsto é:

\begin{enumerate}
    \item \textbf{Feature Engineering e Preparação dos Dados para Modelagem} (2 semanas)
    \begin{itemize}
        \item Criação explícita das variáveis de lag (chuva_lag_1, chuva_lag_2, etc.).
        \item Normalização e padronização das variáveis numéricas.
        \item Divisão dos dados em conjuntos de treino, validação e teste (respeitando ordem temporal).
    \end{itemize}
    
    \item \textbf{Implementação do Modelo Baseline (SARIMA)} (2 semanas)
    \begin{itemize}
        \item Seleção automática de hiperparâmetros (p, d, q)(P, D, Q).
        \item Treinamento do modelo e geração de previsões.
        \item Avaliação inicial do desempenho.
    \end{itemize}
    
    \item \textbf{Implementação e Otimização do XGBoost} (3 semanas)
    \begin{itemize}
        \item Configuração da estrutura de dados para o algoritmo.
        \item Otimização de hiperparâmetros via Grid Search ou Randomized Search.
        \item Treinamento e validação com Time Series Cross-Validation.
        \item Análise da importância das features (Feature Importance).
    \end{itemize}
    
    \item \textbf{Implementação e Otimização da Rede Neural LSTM} (4 semanas)
    \begin{itemize}
        \item Projeto da arquitetura (número de camadas, unidades de memória, dropout).
        \item Preparação dos dados em formato de sequências temporais.
        \item Treinamento com early stopping e monitoramento de overfitting.
        \item Ajuste fino de hiperparâmetros (learning rate, batch size, epochs).
    \end{itemize}
    
    \item \textbf{Comparação de Modelos e Análise de Resultados} (2 semanas)
    \begin{itemize}
        \item Cálculo das métricas de desempenho (RMSE, MAE) para todos os modelos.
        \item Análise dos erros de previsão (resíduos).
        \item Avaliação da capacidade de generalização (especialmente para o evento extremo de 2024).
        \item Comparação crítica dos resultados e discussão dos trade-offs.
    \end{itemize}
    
    \item \textbf{Redação Final e Apresentação} (3 semanas)
    \begin{itemize}
        \item Redação do capítulo de Resultados Finais e Discussão.
        \item Elaboração das Conclusões e Trabalhos Futuros.
        \item Preparação da apresentação para a banca examinadora.
        \item Revisão final e formatação do documento completo.
    \end{itemize}
\end{enumerate}

\textbf{Total estimado do TCC 2: 16 semanas}

\section{Visão Geral do Projeto}

O projeto completo (TCC 1 + TCC 2) está previsto para ser concluído em aproximadamente \textbf{30 semanas} (cerca de 7 a 8 meses), considerando dedicação parcial compatível com a carga horária acadêmica de um estudante de graduação.
"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Cronograma created.")

if __name__ == "__main__":
    update_resultados_extended()
    create_cronograma()

