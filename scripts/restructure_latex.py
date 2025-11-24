import os
import shutil

TEX_DIR = "docs/template/extracted/editaveis"

def update_introducao_structure():
    print(">>> Structuring Introdução...")
    path = os.path.join(TEX_DIR, "introducao.tex")
    
    # Read existing content to preserve stats if possible, but structure dictates rewrite
    # Actually, we should rewrite to match the "Modelo básico" structure:
    # 1. Contextualização
    # 2. Relevância da Tecnologia
    # 3. Pergunta de Pesquisa
    # 4. Objetivos (Geral e Específicos)
    
    new_content = r"""\chapter[Introdução]{Introdução}
\label{cap:introducao}

\section{Contextualização e Importância do Trabalho}

A dengue é uma arbovirose sistêmica de evolução benigna na maioria dos casos, mas que pode apresentar manifestações graves e letais. Nas últimas décadas, a doença consolidou-se como um dos mais críticos desafios de saúde pública global, especialmente em regiões tropicais. O agente etiológico é um vírus de RNA da família \textit{Flaviviridae} (DENV), transmitido principalmente pela fêmea do mosquito \textit{Aedes aegypti}.

O Distrito Federal (DF), foco deste estudo, tornou-se um cenário alarmante. Dados consolidados para este trabalho revelam que, entre 2022 e 2024, foram notificados \textbf{463,560 casos} de dengue na região. O ano de 2024 foi particularmente crítico, registrando uma epidemia explosiva com 313,317 casos, superando vastamente a soma dos dois anos anteriores. Compreender a dinâmica desses surtos é vital para mitigar o colapso do sistema de saúde e salvar vidas.

\section{Relevância da Tecnologia}

Diante da complexidade e da não-linearidade dos fatores que influenciam a proliferação do vetor — como chuva, temperatura e umidade —, os métodos estatísticos tradicionais muitas vezes falham em capturar padrões complexos com antecedência suficiente.

A tecnologia de Inteligência Artificial (IA), especificamente algoritmos de Aprendizado de Máquina (\textit{Machine Learning}) e Aprendizado Profundo (\textit{Deep Learning}), apresenta-se como uma solução promissora. A capacidade desses algoritmos de processar grandes volumes de dados climáticos e epidemiológicos (Big Data) e identificar padrões de defasagem temporal (\textit{lags}) permite a construção de modelos preditivos mais robustos, capazes de antecipar surtos e orientar ações preventivas.

\section{Pergunta de Pesquisa}

Este trabalho propõe-se a responder à seguinte questão:

\begin{quote}
\textit{Como a integração de dados climáticos exógenos (precipitação, temperatura, umidade) com a série temporal de casos de dengue no Distrito Federal, utilizando janelas temporais defasadas (\textit{lags}), pode aprimorar a capacidade de modelos de IA em antecipar surtos epidêmicos severos como o de 2024?}
\end{quote}

\section{Objetivos}

\subsection{Objetivo Geral}
Desenvolver e avaliar modelos preditivos baseados em Inteligência Artificial para a previsão de casos de dengue no Distrito Federal, utilizando uma base de dados unificada e tratada do período de 2022 a 2024.

\subsection{Objetivos Específicos}
\begin{enumerate}
    \item \textbf{Coletar e processar dados}: Construir um \textit{pipeline} automatizado para extração e integração de dados do SINAN (casos semanais) e do INMET (variáveis climáticas) para o triênio 2022-2024.
    \item \textbf{Analisar correlações}: Quantificar a influência estatística e a defasagem temporal (\textit{lag}) das variáveis climáticas sobre a incidência de dengue.
    \item \textbf{Implementar e avaliar modelos}: Desenvolver, treinar e comparar o desempenho de algoritmos estatísticos (SARIMA) e de Machine Learning (XGBoost, LSTM) na previsão de novos casos (Etapa prevista para o TCC 2).
\end{enumerate}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Introdução updated.")

def update_aspectos_gerais_structure():
    # Aspects Gerais is often Chapter 2 or part of Methodology.
    # User requested "Revisão Bibliográfica" as item 2.
    # Let's map "Aspectos Gerais" or create a new "revisaobibliografica.tex" if needed.
    # Usually "Aspectos Gerais" in UnB template covers data sources. 
    # But the user specifically asked for "Revisão Bibliográfica".
    # I will update "aspectosgerais.tex" to serve as "Fundamentação Teórica / Revisão Bibliográfica" 
    # OR create a dedicated file if "aspectosgerais" is strictly for data description.
    # Looking at the file list, there is no "revisaobibliografica.tex".
    # I will adapt "aspectosgerais.tex" to be the Chapter 2: Revisão Bibliográfica & Dados.
    
    print(">>> Structuring Aspectos Gerais (Revisão Bibliográfica)...")
    path = os.path.join(TEX_DIR, "aspectosgerais.tex")
    
    new_content = r"""\chapter{Revisão Bibliográfica e Dados}
\label{cap:revisao}

\section{A Dengue e o Cenário Epidemiológico}

A dengue é uma doença febril aguda que afeta milhões de pessoas anualmente. O vírus possui quatro sorotipos (DENV-1 a 4), e a infecção por um deles confere imunidade permanente apenas para aquele sorotipo específico.

\subsection{Impacto Social e Econômico}
Epidemias de dengue geram custos elevados para o sistema público de saúde, devido ao aumento de internações e tratamentos de suporte, além do impacto econômico decorrente do afastamento da força de trabalho. No Brasil, e especificamente no DF, a sazonalidade da doença coincide com períodos de chuva e calor, exigindo planejamento estratégico anual.

\section{Tecnologias de Previsão e Estado da Arte}

A previsão de séries temporais epidemiológicas tem evoluído de modelos compartimentais (SIR/SEIR) para abordagens baseadas em dados (\textit{Data-Driven}).

\subsection{Modelos Estatísticos Clássicos}
O modelo SARIMA (Seasonal AutoRegressive Integrated Moving Average) é uma referência no setor, capaz de capturar a sazonalidade linear. No entanto, sua capacidade de incorporar múltiplas variáveis exógenas (clima) de forma não-linear é limitada.

\subsection{Machine Learning e Deep Learning}
Algoritmos como \textbf{XGBoost} (baseado em árvores de decisão) e \textbf{LSTM} (Long Short-Term Memory, uma rede neural recorrente) representam o estado da arte. O XGBoost destaca-se pela interpretabilidade e rapidez, enquanto LSTMs são projetadas para aprender dependências de longo prazo em sequências temporais, ideais para modelar os efeitos defasados do clima sobre o vetor.

\section{Bases de Dados Utilizadas}

Para este estudo, consolidou-se uma base de dados unificada (2022-2024) combinando duas fontes primárias:

\subsection{SINAN (Dados Epidemiológicos)}
Fonte: API InfoDengue.
\begin{itemize}
    \item \textbf{Variável Alvo:} Casos semanais notificados de dengue em Brasília.
    \item \textbf{Granularidade:} Semanal (Semana Epidemiológica).
\end{itemize}

\subsection{INMET (Dados Meteorológicos)}
Fonte: Estação Automática A001 (Brasília).
\begin{itemize}
    \item \textbf{Variáveis Explicativas:} Precipitação (mm), Temperatura Média (°C), Umidade Relativa (%) e Pressão Atmosférica.
    \item \textbf{Tratamento:} Os dados foram agregados semanalmente para alinhamento temporal com os casos de dengue.
\end{itemize}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Aspectos Gerais (Revisão) updated.")

def update_metodologia_structure():
    print(">>> Structuring Metodologia...")
    path = os.path.join(TEX_DIR, "metodologia.tex")
    
    new_content = r"""\chapter{Metodologia}
\label{cap:metodologia}

Este capítulo detalha o planejamento estruturado e os métodos computacionais empregados no desenvolvimento deste trabalho.

\section{Etapas do Desenvolvimento}

\subsection{1. Coleta e Pré-processamento de Dados}
O primeiro passo consistiu na construção de um \textit{pipeline} automatizado em Python.
\begin{itemize}
    \item \textbf{Coleta:} Scripts específicos baixaram dados do SINAN (via API) e do INMET (arquivos CSV).
    \item \textbf{Limpeza:} Tratamento de valores nulos (interpolação linear para variáveis climáticas contínuas) e padronização de datas.
    \item \textbf{Unificação:} Fusão das bases de dados utilizando a data de início da semana epidemiológica como chave primária (`inner join`).
\end{itemize}

\subsection{2. Análise Estatística e Seleção de Variáveis}
Para definir quais variáveis climáticas integrar aos modelos, foram aplicados:
\begin{itemize}
    \item \textbf{Correlação de Pearson e Spearman:} Para medir a força da relação linear e monotônica.
    \item \textbf{Correlação Cruzada (\textit{Cross-Correlation}):} Para identificar o tempo de defasagem (\textit{lag}) ideal entre o evento climático (ex: chuva) e o aumento de casos.
    \item \textbf{Teste de Causabilidade de Granger:} Para validar estatisticamente se a série temporal climática antecede e melhora a previsão da série de casos.
\end{itemize}

\subsection{3. Modelagem Preditiva (Planejamento TCC 2)}
Os algoritmos selecionados para implementação são:
\begin{itemize}
    \item \textbf{SARIMA:} Como \textit{baseline} estatístico.
    \item \textbf{XGBoost:} Para capturar relações não-lineares entre variáveis exógenas.
    \item \textbf{LSTM:} Para modelagem profunda de sequências temporais complexas.
\end{itemize}

\section{Estratégia de Validação}
Os modelos serão avaliados utilizando a técnica de \textbf{Validação Cruzada em Janela Deslizante} (\textit{Time Series Cross-Validation}), garantindo que o treino ocorra sempre no passado e o teste no futuro, respeitando a ordem temporal dos dados. As métricas de desempenho adotadas serão o RMSE (Raiz do Erro Quadrático Médio) e o MAE (Erro Absoluto Médio).

\section{Ferramentas Utilizadas}
\begin{itemize}
    \item \textbf{Linguagem:} Python 3.9+.
    \item \textbf{Bibliotecas:} Pandas (manipulação), Statsmodels (estatística), Scikit-learn e TensorFlow/Keras (Machine Learning), Seaborn (visualização).
    \item \textbf{Ambiente:} Jupyter Notebooks e Scripts modulares.
\end{itemize}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Metodologia updated.")

if __name__ == "__main__":
    update_introducao_structure()
    update_aspectos_gerais_structure()
    update_metodologia_structure()

