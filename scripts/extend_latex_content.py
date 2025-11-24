import os
import shutil

TEX_DIR = "docs/template/extracted/editaveis"

def update_introducao_extended():
    print(">>> Extending Introdução...")
    path = os.path.join(TEX_DIR, "introducao.tex")
    
    new_content = r"""\chapter[Introdução]{Introdução}
\label{cap:introducao}

A dengue é uma doença viral sistêmica de evolução benigna na maioria dos casos, mas que pode apresentar manifestações graves, incluindo a síndrome do choque da dengue e óbito. O agente etiológico é um vírus de RNA de fita simples e polaridade positiva (DENV), pertencente à família \textit{Flaviviridae} e ao gênero \textit{Flavivirus}. Existem quatro sorotipos antigenicamente distintos (DENV-1, DENV-2, DENV-3 e DENV-4), e a infecção por um deles confere imunidade permanente apenas para aquele sorotipo específico, havendo a possibilidade de infecções subsequentes pelos demais, o que aumenta o risco de formas graves da doença.

A transmissão ocorre primordialmente pela picada de fêmeas infectadas de mosquitos do gênero \textit{Aedes}, sendo o \textit{Aedes aegypti} o vetor primário em áreas urbanas. A biologia do vetor é intrinsecamente ligada às condições ambientais: a temperatura influencia a velocidade de reprodução e o período de incubação viral, enquanto a chuva fornece os criadouros aquáticos essenciais para a fase larvária.

\section{Contextualização e Motivação}

Nas últimas décadas, a dengue consolidou-se como um dos mais críticos desafios de saúde pública global, especialmente em regiões tropicais e subtropicais. A urbanização desordenada, as mudanças climáticas e a mobilidade humana global têm facilitado a expansão da área de atuação do vetor.

No Brasil, o cenário epidemiológico é caracterizado pela hiperendemicidade, com ciclos epidêmicos recorrentes. O Distrito Federal (DF), foco deste estudo, tornou-se um cenário alarmante e emblemático dessa crise sanitária nos últimos anos. Localizado no bioma Cerrado, o DF apresenta um regime pluviométrico bem definido, alternando entre uma estação seca e uma chuvosa, o que modula sazonalmente a dinâmica da transmissão.

A motivação para este trabalho nasce da observação dos dados alarmantes recentes. Dados consolidados e processados para esta pesquisa revelam que, no triênio compreendido entre 2022 e 2024, o Distrito Federal acumulou um total de \textbf{463.560 casos notificados} de dengue.

O ano de 2024, em particular, representou um ponto de inflexão histórica. Diferente dos anos anteriores, que seguiram padrões sazonais esperados (2022 com 85.346 casos e 2023 com 64.897 casos), 2024 registrou uma epidemia explosiva e sem precedentes, totalizando \textbf{313.317 casos} notificados. Esse volume representa um aumento superior a 360\% em relação ao ano anterior e supera a soma de toda a série histórica recente. O pico dessa crise ocorreu na semana epidemiológica iniciada em 18 de fevereiro de 2024, quando o sistema de saúde registrou mais de 25 mil casos em apenas sete dias.

Esse cenário de colapso, com superlotação de hospitais e esgotamento de recursos, evidencia a incapacidade dos métodos tradicionais de vigilância em prever, com a antecedência necessária, a magnitude de tais eventos extremos. A reatividade do sistema de saúde, que muitas vezes atua apenas após a detecção do aumento de casos, resulta em uma resposta tardia e menos eficaz.

\section{Relevância da Tecnologia}

A complexidade da dinâmica de transmissão da dengue reside na sua natureza multifatorial e não-linear. Fatores climáticos como precipitação, temperatura, umidade relativa do ar e pressão atmosférica interagem de forma complexa para criar as condições ideais para a proliferação do mosquito. Além disso, existe um fenômeno crucial conhecido como "defasagem temporal" ou \textit{lag}: a chuva que ocorre hoje não resulta em mosquitos adultos imediatamente, mas sim semanas depois, após o ciclo de eclosão dos ovos e desenvolvimento das larvas.

Os métodos estatísticos clássicos muitas vezes falham em capturar essas nuances não-lineares e as interações complexas entre múltiplas variáveis exógenas. É nesse contexto que a tecnologia de Inteligência Artificial (IA) se torna uma ferramenta indispensável.

Algoritmos de Aprendizado de Máquina (\textit{Machine Learning}), como o \textit{Gradient Boosting} (XGBoost), e de Aprendizado Profundo (\textit{Deep Learning}), como as Redes Neurais Recorrentes (LSTM - \textit{Long Short-Term Memory}), possuem a capacidade intrínseca de modelar dependências temporais de longo prazo e identificar padrões sutis em grandes volumes de dados (\textit{Big Data}). A aplicação dessas tecnologias permite transformar dados brutos climáticos e epidemiológicos em inteligência preditiva acionável, oferecendo aos gestores públicos uma janela de oportunidade ("horizonte de previsão") para atuar preventivamente antes que o surto atinja seu pico.

\section{Pergunta de Pesquisa}

Considerando a gravidade do cenário epidemiológico no Distrito Federal e o potencial inexplorado das variáveis ambientais como preditores antecipados, este trabalho propõe-se a responder à seguinte questão central:

\begin{quote}
\textit{Como a integração de dados climáticos exógenos (precipitação, temperatura, umidade, pressão) com a série temporal histórica de casos de dengue no Distrito Federal, utilizando janelas temporais defasadas (\textit{lags}) otimizadas, pode aprimorar a capacidade de modelos de Inteligência Artificial em antecipar e dimensionar surtos epidêmicos severos, como o evento extremo observado em 2024?}
\end{quote}

\section{Objetivos}

\subsection{Objetivo Geral}

Desenvolver, treinar e avaliar modelos preditivos baseados em Inteligência Artificial (SARIMA, XGBoost e LSTM) para a previsão semanal de casos de dengue no Distrito Federal, utilizando uma base de dados unificada, tratada e enriquecida com variáveis climáticas do período de 2022 a 2024, visando fornecer uma ferramenta de alerta antecipado para a saúde pública.

\subsection{Objetivos Específicos}

Para alcançar o objetivo geral, foram definidos os seguintes objetivos específicos, que compõem a metodologia deste trabalho:

\begin{enumerate}
    \item \textbf{Coleta e Integração de Dados:} Construir um \textit{pipeline} computacional automatizado para a extração, limpeza e unificação de dados epidemiológicos (do Sistema de Informação de Agravos de Notificação - SINAN) e dados meteorológicos (do Instituto Nacional de Meteorologia - INMET) referentes ao Distrito Federal no período de 2022 a 2024.
    
    \item \textbf{Análise Exploratória e de Correlação:} Realizar uma análise estatística profunda para quantificar a influência das variáveis climáticas sobre a incidência de dengue, identificando através de correlação cruzada (\textit{Cross-Correlation}) e testes de causalidade de Granger quais são os tempos de defasagem (\textit{lags}) mais significativos para cada variável ambiental.
    
    \item \textbf{Desenvolvimento de Modelos (Planejamento TCC 2):} Implementar e otimizar algoritmos de previsão de séries temporais, comparando uma abordagem estatística clássica (SARIMA) com abordagens de Machine Learning baseadas em árvores (XGBoost) e Redes Neurais Profundas (LSTM).
    
    \item \textbf{Avaliação de Desempenho (Planejamento TCC 2):} Validar os modelos utilizando a técnica de validação cruzada em janela deslizante (\textit{Time Series Cross-Validation}) e métricas robustas de erro (RMSE, MAE), com foco específico na capacidade dos modelos de generalizar e prever o pico epidêmico extremo de 2024.
\end{enumerate}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Introdução extended.")

def update_aspectos_gerais_extended():
    print(">>> Extending Aspectos Gerais...")
    path = os.path.join(TEX_DIR, "aspectosgerais.tex")
    
    new_content = r"""\chapter{Revisão Bibliográfica e Fundamentação Teórica}
\label{cap:revisao}

Este capítulo apresenta a fundamentação teórica necessária para a compreensão do problema abordado, discutindo a epidemiologia da dengue, o impacto socioeconômico da doença e o estado da arte das tecnologias de previsão baseadas em Inteligência Artificial. Além disso, detalha-se a estrutura das bases de dados reais utilizadas neste estudo.

\section{A Dengue: Epidemiologia e Dinâmica de Transmissão}

A dengue é, atualmente, a arbovirose mais importante do mundo em termos de morbidade e mortalidade humana. O vírus (DENV) possui quatro sorotipos distintos (DENV-1, DENV-2, DENV-3 e DENV-4). A co-circulação desses sorotipos em uma mesma região é um fator de risco crítico, pois a infecção prévia por um sorotipo pode, em alguns casos, exacerbar a resposta imune em uma infecção secundária por um sorotipo diferente, levando a quadros de Dengue Grave (anteriormente denominada Dengue Hemorrágica).

A dinâmica de transmissão da doença é complexa e fortemente influenciada por fatores ambientais e sociais. O vetor \textit{Aedes aegypti} é um mosquito altamente adaptado ao ambiente urbano e peridomiciliar. Seu ciclo de vida compreende quatro fases: ovo, larva, pupa e adulto. As fases imaturas ocorrem necessariamente na água, enquanto a fase adulta é aérea.
\begin{itemize}
    \item \textbf{Influência da Chuva:} A precipitação é fundamental para a criação e manutenção de criadouros larvários (pneus, vasos, caixas d'água destampadas), aumentando a densidade vetorial.
    \item \textbf{Influência da Temperatura:} Temperaturas mais elevadas aceleram o metabolismo do mosquito, encurtando o tempo de desenvolvimento larvário e o período de incubação extrínseco do vírus dentro do vetor, o que aumenta a frequência de repasto sanguíneo e a taxa de transmissão.
\end{itemize}

\subsection{Impacto Social e Econômico}

O impacto da dengue transcende a esfera clínica individual, gerando um fardo pesado para a sociedade e para a economia. Epidemias de grande magnitude, como a observada no Distrito Federal em 2024, provocam:
\begin{itemize}
    \item \textbf{Sobrecarga do Sistema de Saúde:} A procura massiva por atendimento ambulatorial e internação esgota rapidamente os recursos hospitalares, leitos e insumos, prejudicando o atendimento a outras patologias.
    \item \textbf{Absenteísmo e Perda de Produtividade:} A doença afeta predominantemente a população economicamente ativa, gerando dias perdidos de trabalho e estudo, com impacto direto no PIB local.
    \item \textbf{Custos Diretos e Indiretos:} Os custos envolvem desde o tratamento dos pacientes e campanhas de controle vetorial até os custos previdenciários e a perda de qualidade de vida da população.
\end{itemize}

\section{Estado da Arte em Previsão Epidemiológica}

A capacidade de antecipar surtos de doenças infecciosas tem sido uma prioridade de pesquisa global. A evolução das técnicas de previsão pode ser dividida em abordagens clássicas e abordagens modernas baseadas em dados (\textit{Data-Driven}).

\subsection{Modelagem Estatística Clássica (SARIMA)}
O modelo SARIMA (\textit{Seasonal AutoRegressive Integrated Moving Average}) é uma extensão do modelo ARIMA que suporta explicitamente a sazonalidade univariada. Ele é amplamente utilizado como \textit{baseline} em estudos epidemiológicos devido à sua robustez teórica e capacidade de modelar tendências lineares e ciclos sazonais.
No entanto, sua principal limitação é a dificuldade em incorporar múltiplas variáveis exógenas (covariáveis climáticas) de maneira não-linear. O SARIMA assume que as relações passadas se repetem linearmente no futuro, o que pode ser insuficiente para prever surtos explosivos causados por anomalias climáticas complexas.

\subsection{Machine Learning e Algoritmos de Boosting (XGBoost)}
O \textit{Extreme Gradient Boosting} (XGBoost) representa o estado da arte em algoritmos baseados em árvores de decisão. Diferente dos modelos lineares, o XGBoost constrói um conjunto (\textit{ensemble}) de modelos fracos (árvores de decisão) de forma sequencial, onde cada novo modelo tenta corrigir os erros dos anteriores.
\textbf{Vantagens para o problema:}
\begin{itemize}
    \item Capacidade de capturar interações não-lineares complexas entre variáveis (ex: a chuva só aumenta a dengue se a temperatura estiver acima de um certo limiar).
    \item Robustez a dados faltantes (\textit{missing values}) e \textit{outliers}.
    \item Importância de Atributos (\textit{Feature Importance}): Permite identificar quais variáveis climáticas são mais relevantes para a previsão.
\end{itemize}

\subsection{Deep Learning e Redes Neurais Recorrentes (LSTM)}
As redes LSTM (\textit{Long Short-Term Memory}) são uma arquitetura especial de Redes Neurais Recorrentes (RNN) projetadas para superar o problema de "esquecimento" de dependências longas. Em séries temporais epidemiológicas, eventos ocorridos há vários meses (ex: um verão muito chuvoso) podem influenciar o tamanho da população de mosquitos meses depois. As células de memória da LSTM conseguem reter essa informação relevante por longos períodos, tornando-as ideais para modelar os efeitos defasados (\textit{lags}) do clima sobre a doença.

\section{Caracterização das Bases de Dados Reais}

Para garantir a validade ecológica e a aplicabilidade prática deste estudo, foram utilizados exclusivamente dados reais e oficiais referentes ao Distrito Federal.

\subsection{Dados Epidemiológicos (SINAN/InfoDengue)}
Os dados de notificação de dengue foram obtidos através da API do projeto InfoDengue, que cura e padroniza os dados do Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
\begin{itemize}
    \item \textbf{Abrangência Temporal:} Semanas epidemiológicas de 2022 a 2024 (156 semanas contínuas).
    \item \textbf{Abrangência Espacial:} Município de Brasília (Geocódigo IBGE: 5300108).
    \item \textbf{Natureza do Dado:} Casos prováveis (soma de casos confirmados e suspeitos), refletindo a carga real sobre o sistema de saúde.
\end{itemize}

\subsection{Dados Meteorológicos (INMET)}
As variáveis climáticas foram extraídas do Banco de Dados Meteorológicos para Ensino e Pesquisa (BDMEP) do Instituto Nacional de Meteorologia (INMET).
\begin{itemize}
    \item \textbf{Fonte:} Estação Meteorológica Automática de Brasília (A001).
    \item \textbf{Variáveis Processadas:}
    \begin{enumerate}
        \item \textbf{Precipitação (Chuva):} Acumulado semanal (mm). Variável crítica para formação de criadouros.
        \item \textbf{Temperatura Média, Mínima e Máxima:} Médias semanais (°C). Variável crítica para a velocidade do ciclo viral.
        \item \textbf{Umidade Relativa do Ar:} Média semanal (%). Variável crítica para a sobrevivência do mosquito adulto (em ambientes secos, o mosquito desidrata e morre mais rápido).
        \item \textbf{Pressão Atmosférica:} Média semanal.
    \end{enumerate}
\end{itemize}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Aspectos Gerais extended.")

def update_metodologia_extended():
    print(">>> Extending Metodologia...")
    path = os.path.join(TEX_DIR, "metodologia.tex")
    
    new_content = r"""\chapter{Metodologia}
\label{cap:metodologia}

Este capítulo descreve detalhadamente o fluxo metodológico adotado, desde a engenharia de dados até a estratégia de análise estatística, garantindo a reprodutibilidade científica do estudo. A abordagem metodológica é quantitativa, descritiva e analítica, baseada em dados secundários de domínio público.

\section{Pipeline de Engenharia de Dados}

Dada a heterogeneidade das fontes de dados (SINAN e INMET), foi necessário desenvolver um \textit{pipeline} computacional robusto em linguagem Python para a extração, transformação e carga (ETL) das informações.

\subsection{1. Coleta e Padronização}
Os dados foram coletados de forma automatizada. Para os dados do INMET, que originalmente apresentam frequência horária ou diária, foi aplicado um processo de agregação temporal para compatibilizá-los com a granularidade semanal dos dados epidemiológicos.
\begin{itemize}
    \item Para a variável \textbf{Precipitação}, utilizou-se a soma acumulada da semana.
    \item Para as variáveis de \textbf{Temperatura, Umidade e Pressão}, utilizou-se a média aritmética das observações diárias.
    \item As datas foram padronizadas para o formato ISO 8601 (YYYY-MM-DD) e alinhadas pela data de início da Semana Epidemiológica (SE), que convencionalmente se inicia aos domingos.
\end{itemize}

\subsection{2. Tratamento e Unificação}
Foi realizada uma inspeção de qualidade dos dados para identificar valores espúrios (\textit{outliers} impossíveis, ex: temperatura de 200°C) ou dados faltantes (\textit{missing values}). Pequenas lacunas nas séries climáticas foram preenchidas utilizando interpolação linear, um método adequado para variáveis físicas contínuas. Em seguida, os \textit{datasets} de clima e saúde foram unificados (\textit{merged}) em uma única estrutura tabular, resultando em uma série temporal multivariada com 156 observações semanais.

\section{Análise Estatística Exploratória}

Antes da modelagem, realizou-se uma investigação profunda da estrutura de correlação dos dados para fundamentar a seleção de atributos (\textit{Feature Selection}).

\subsection{Correlação e Defasagem Temporal (Lags)}
A relação entre clima e dengue não é instantânea. O ciclo biológico impõe um atraso natural. Para capturar esse fenômeno, utilizou-se a Função de Correlação Cruzada (\textit{Cross-Correlation Function} - CCF).
Calculou-se a correlação de Pearson entre a série de casos ($Y_t$) e as séries climáticas defasadas ($X_{t-k}$) para $k = 0, 1, ..., 8$ semanas.
\[
r_k = \frac{\sum_{t=k+1}^T (y_t - \bar{y})(x_{t-k} - \bar{x})}{\sqrt{\sum_{t=1}^T (y_t - \bar{y})^2} \sqrt{\sum_{t=1}^T (x_t - \bar{x})^2}}
\]
Esse procedimento permite identificar, por exemplo, se a chuva de 2 meses atrás tem maior poder preditivo sobre os casos atuais do que a chuva da semana corrente.

\subsection{Teste de Causalidade de Granger}
Para ir além da simples correlação e investigar a precedência temporal estatística, aplicou-se o Teste de Causalidade de Granger. O teste avalia se a inclusão de valores passados de uma variável $X$ (Clima) reduz significativamente o erro de previsão da variável $Y$ (Casos), em comparação com um modelo que usa apenas os valores passados de $Y$.
A verificação foi feita para defasagens de 1 a 4 semanas, considerando um nível de significância de 5\% ($p < 0,05$).

\section{Planejamento da Modelagem Preditiva (TCC 2)}

A fase de construção dos modelos preditivos, a ser executada na etapa seguinte da pesquisa (TCC 2), seguirá uma abordagem experimental rigorosa.

\subsection{Algoritmos Selecionados}
\begin{enumerate}
    \item \textbf{SARIMA:} Será implementado utilizando a biblioteca \texttt{statsmodels}, com seleção automática de hiperparâmetros ($p,d,q$) e ($P,D,Q$) baseada no critério de informação de Akaike (AIC).
    \item \textbf{XGBoost:} Será implementado via biblioteca \texttt{xgboost}, com otimização de hiperparâmetros (taxa de aprendizado, profundidade da árvore) via \textit{Grid Search}.
    \item \textbf{LSTM:} Será construída com \texttt{TensorFlow/Keras}, testando arquiteturas com camadas de \textit{Dropout} para evitar \textit{overfitting} e camadas densas para a regressão final.
\end{enumerate}

\subsection{Estratégia de Validação e Métricas}
Dada a natureza temporal dos dados, a validação tradicional (separação aleatória treino/teste) é inadequada, pois violaria a ordem cronológica ("olhar para o futuro"). Será utilizada a validação \textbf{Walk-Forward} ou \textbf{Time Series Cross-Validation}.
O desempenho será mensurado pelas métricas:
\begin{itemize}
    \item \textbf{RMSE (Root Mean Squared Error):} Penaliza erros grandes, útil para prever picos.
    \item \textbf{MAE (Mean Absolute Error):} Mede o erro médio absoluto, de fácil interpretação.
\end{itemize}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("    ✔ Metodologia extended.")

if __name__ == "__main__":
    update_introducao_extended()
    update_aspectos_gerais_extended()
    update_metodologia_extended()

