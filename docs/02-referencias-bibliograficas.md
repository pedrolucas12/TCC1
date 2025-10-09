# Referências Bibliográficas

> Compilação de trabalhos, artigos, TCCs e recursos relacionados ao tema de previsão de surtos de dengue usando séries temporais e dados climáticos.

---

## 📚 Trabalhos Científicos Principais

### Meta-Análises e Revisões Sistemáticas

1. **Fan et al. (2015)**
   - *A Systematic Review and Meta-Analysis of Dengue Risk with Temperature*
   - Journal: International Journal of Environmental Research and Public Health
   - Mostra associação forte entre temperatura média e dengue (efeito positivo; OR significativo por 1°C)
   - **Meta-análise frequentemente citada**
   - [Link](https://www.mdpi.com/1660-4601/12/1/1)

2. **Naish et al. (2014)**
   - *Climate change and dengue: a critical and systematic review of quantitative evidence*
   - Conclui que transmissão de dengue é sensível a temperatura, chuva e umidade
   - Importante para justificar hipótese climática
   - [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3986908/)

3. **Li et al. (2020)**
   - *Effects of ambient temperature and precipitation on the risk of dengue fever*
   - Evidencia associação com temperatura e precipitação
   - Estudo de painel e meta-análise
   - [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0013935120309403)

4. **Kirk et al. (2024)**
   - *Temperature impacts on dengue incidence are nonlinear and mediated by climatic factors*
   - PLOS Climate
   - Mostra relação **não linear** com temperatura (pico em ~24°C)
   - Importante para modelagem (usar termos quadráticos ou splines)
   - [PLOS Climate](https://journals.plos.org/climate/article?id=10.1371%2Fjournal.pclm.0000152)

---

## 🤖 Aplicações de Machine Learning e Deep Learning

### Modelos LSTM e Redes Neurais

5. **Chen et al. (2025)**
   - *Forecasting dengue across Brazil with LSTM neural networks*
   - BMC Public Health
   - Framework LSTM que integra informação temporal, climática e espacial
   - **Modelo de referência recente para o Brasil**
   - [BMC](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-22106-7)

6. **Bomfim et al. (2023)**
   - *Enhancing dengue time-series forecasting at the neighborhood level using LSTM models*
   - ENIAC - Sociedade Brasileira de Computação
   - Aplica LSTM em nível de bairro
   - [SBC](https://sol.sbc.org.br/index.php/eniac/article/view/25735)

7. **Silva et al. (2024)**
   - *When climate variables improve dengue forecasting: a machine learning approach*
   - arXiv
   - Demonstra melhoria significativa ao incluir variáveis climáticas
   - [arXiv](https://arxiv.org/abs/2404.05266)

8. **Multitask LSTM (2025)**
   - *Multitask LSTM for Arboviral Outbreak Prediction Using Climate and Disease Data*
   - arXiv
   - Abordagem multitarefa para prever múltiplas arboviroses
   - [arXiv](https://arxiv.org/pdf/2505.04566)

### Ensemble e Machine Learning Tradicional

9. **Nature Scientific Reports (2024)**
   - *A reproducible ensemble machine learning approach to forecast dengue outbreaks*
   - Nature
   - Pipeline reproduzível com ensemble de modelos
   - [Nature](https://www.nature.com/articles/s41598-024-52796-9)

10. **Kempfert et al. (2020)**
    - *Time Series Methods and Ensemble Models to Nowcast Dengue at the State Level in Brazil*
    - arXiv
    - Compara métodos de séries temporais e ensembles
    - **Nowcasting** (previsão de curto prazo)
    - [arXiv](https://arxiv.org/abs/2006.02483)

11. **GeoSeeq Dengue (2024)**
    - *GeoSeeq Dengue: machine learning multimodal models*
    - BioRxiv
    - Modelos preditivos que combinam dados epidemiológicos e ambientais
    - Exemplo de pipeline multimodal

### Feature Selection e Correlação

12. **Ferdousi et al. (2021)**
    - *A windowed correlation based feature selection method to improve time series prediction of dengue fever cases*
    - arXiv
    - Técnica de correlação por janelas para seleção de features
    - **Útil para incorporar dados de municípios vizinhos**
    - [arXiv](https://arxiv.org/abs/2104.10289)

---

## 🇧🇷 Estudos Brasileiros Específicos

### Séries Temporais e Clima no Brasil

13. **Silva et al. (2024)**
    - *Relação entre temperatura do ar e incidência de dengue: estudo de séries temporais*
    - Cadernos de Saúde Pública
    - Análise temporal específica para o Brasil
    - [SciELO](https://www.scielo.br/j/csp/a/JB4c4wnkKHqcmYYYQLfyvzx/)

14. **Gomes et al. (2024)**
    - *Time series study in Minas Gerais, Brazil (2010–2019)*
    - PMC
    - Estudo estadual em Minas Gerais
    - [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10962433/)

15. **Silva et al. (2022)**
    - *Tendência temporal e distribuição espacial da dengue no Brasil, 2009-2019*
    - Revista Cogitare Enfermagem
    - Análise espaço-temporal para todo o Brasil
    - [SciELO](https://www.scielo.br/j/cenf/a/jK5Jz7kyw6d9yQZXszC7VQD/?lang=pt)

16. **Silva et al. (2025)**
    - *Análise de séries temporais interrompida, Brasil, 2001-2022*
    - Revista RESS
    - Série temporal longa para o país inteiro
    - [SciELO Saúde Pública](https://www.scielosp.org/article/ress/2025.v34/e20240424/pt/)

### Estudos Regionais

17. **Orssatto et al. (2022)**
    - *Aplicação de séries temporais na estimação do número de casos de dengue em Cascavel-PR*
    - Revista Brasileira de Computação Aplicada
    - Estudo municipal no Paraná
    - [ResearchGate](https://www.researchgate.net/publication/365973843)

18. **População / NEPO (UNICAMP)**
    - *Dengue e Chikungunya: estudos da relação temporal e espacial*
    - Texto NEPO
    - Estudo sobre relação espaço-temporal
    - [NEPO](https://www.nepo.unicamp.br/publicacoes/textos_nepo/textos_nepo_72.pdf)

19. **Pereira (2012)**
    - *O clima tropical e a dengue*
    - Monografia UFPA
    - Foco em clima tropical amazônico
    - [UFPA](https://repositorio.ufpa.br/bitstreams/f29da418-302b-4cad-99e8-ec880504e5b9/download)

### Large-Scale Epidemiological Modeling

20. **EpiScanner (2024)**
    - *Large-scale Epidemiological modeling: Scanning for Mosquito-Borne Diseases Spatio-temporal Patterns in Brazil*
    - arXiv
    - Pipeline para processar séries de todos os municípios (2010–2023)
    - **Excelente referência/benchmark**
    - [arXiv](https://arxiv.org/abs/2407.21286)

---

## 🎓 Trabalhos de Conclusão de Curso (TCCs)

21. **Lizzi (2012)**
    - *Predição do número mensal de casos de dengue*
    - Tese de Doutorado - Universidade de São Paulo
    - Um dos primeiros trabalhos brasileiros sobre predição de dengue
    - [USP](https://www.teses.usp.br/teses/disponiveis/17/17139/tde-20122012-090810/publico/ElisangelaVersaoCorrigida.pdf)

22. **Monografia UFOP (2019)**
    - *Previsão de dengue usando ARIMA/SARIMA*
    - Trabalho aplicando modelos clássicos em Minas Gerais

23. **Aquino Junior (2014)**
    - *A dengue em área de fronteira: riscos e vulnerabilidades na Tríplice Fronteira de Foz do Iguaçu*
    - Tese UFPR
    - Análise em região de fronteira
    - [UFPR](https://acervodigital.ufpr.br/xmlui/bitstream/handle/1884/38008/R%20-%20T%20-%20JOSE%20AQUINO%20JUNIOR.pdf)

---

## 🏥 Saneamento e Saúde Pública

24. **Vicente (2019)**
    - *Efeito do saneamento básico sobre saúde pública*
    - TCC USP
    - Relação entre saneamento e doenças infecciosas
    - [USP](https://bdta.abcd.usp.br/directbitstream/9bd9bc73-5807-4e03-8bf0-23c9c9d64e1b/Vicente_Artur_TCC.pdf)

25. **Ladeira (2014)**
    - *Influência dos serviços de saneamento básico nas taxas de mortalidade em menores de cinco anos e incidência de dengue*
    - TCC UFJF
    - [UFJF](https://www2.ufjf.br/engsanitariaeambiental/files/2014/02/TCC_FINAL_CAROLINE.pdf)

26. **David (2019)**
    - *Saneamento básico e mortalidade infantil*
    - Monografia UFOP
    - [UFOP](https://www.monografias.ufop.br/bitstream/35400000/2371/6/MONOGRAFIA_SaneamentoB%C3%A1sicoSa%C3%BAde.pdf)

---

## 🔧 Ferramentas e Recursos Computacionais

### Pacotes R e Python

27. **microdatasus (R)**
    - Pacote R para facilitar download e pré-processamento de microdados do DATASUS
    - Inclui funções para SINAN dengue
    - [Documentação](https://rfsaldanha.github.io/microdatasus/reference/index.html)

### Sistemas Operacionais de Monitoramento

28. **InfoDengue (Fiocruz / FGV)**
    - Sistema de alerta já pronto com API pública
    - Útil para benchmarking e dados processados
    - [InfoDengue API](https://info.dengue.mat.br/services/api)

---

## 📊 Fontes de Dados (Referências Técnicas)

### Dados Epidemiológicos

29. **OpenDataSUS - Dengue**
    - Portal oficial de dados abertos do SUS
    - Arquivos JSON/CSV por ano (S3)
    - [OpenDataSUS](https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue)
    - [Dicionário de dados](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/dic_dados_dengue.pdf)

30. **TabNet / DATASUS**
    - Interface web para dados agregados
    - [TabNet Dengue](https://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet%2Fcnv%2Fdenguebbr.def)

### Dados Climáticos

31. **INMET / BDMEP**
    - Banco de Dados Meteorológicos para Ensino e Pesquisa
    - Dados de estações meteorológicas brasileiras
    - [BDMEP](https://bdmep.inmet.gov.br/)
    - [Portal INMET](https://portal.inmet.gov.br/manual)

32. **CHIRPS**
    - Climate Hazards Group InfraRed Precipitation with Station data
    - Precipitação por satélite (~0.05° resolução)
    - [CHIRPS](https://www.chc.ucsb.edu/data/chirps)

33. **ERA5 (Copernicus)**
    - Reanálise climática global
    - Múltiplos campos meteorológicos
    - [Copernicus CDS](https://cds.climate.copernicus.eu/)

34. **NASA POWER**
    - API para dados meteorológicos/solares
    - Fácil acesso por coordenada
    - [NASA POWER](https://power.larc.nasa.gov/)

### Dados Geoespaciais

35. **IBGE - Malhas Territoriais**
    - Shapefiles dos municípios brasileiros
    - Códigos IBGE de 7 dígitos
    - [Malhas Municipais](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html)

---

## 📖 Metodologias e Conceitos

### Modelagem de Séries Temporais

- **Hyndman & Athanasopoulos**: *Forecasting: Principles and Practice* (Livro online gratuito)
- **Box & Jenkins**: Metodologia ARIMA clássica
- **Prophet (Facebook)**: Framework para previsão com sazonalidade

### Machine Learning para Séries Temporais

- **SHAP (SHapley Additive exPlanations)**: Interpretação de modelos
- **XGBoost Documentation**: Gradient boosting
- **Keras/TensorFlow**: Implementação de LSTM

### Epidemiologia e Saúde Pública

- **Coura (2013)**: Dinâmica das doenças infecciosas e parasitárias
- **Tauil (2001-2002)**: Aspectos críticos do controle do dengue no Brasil

---

## 🔗 Links Rápidos Úteis

| Recurso | Link Direto |
|---------|-------------|
| OpenDataSUS Dengue | [Catálogo](https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue) |
| JSON 2025 (exemplo) | [S3](https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue/resource/2bc51776-8698-4154-9698-11d2b36370a1) |
| Dicionário SINAN | [PDF](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/dic_dados_dengue.pdf) |
| BDMEP | [Portal](https://bdmep.inmet.gov.br/) |
| CHIRPS | [Dados](https://www.chc.ucsb.edu/data/chirps) |
| Copernicus | [CDS](https://cds.climate.copernicus.eu/) |
| NASA POWER | [API](https://power.larc.nasa.gov/) |
| InfoDengue API | [Docs](https://info.dengue.mat.br/services/api) |
| microdatasus | [GitHub/Docs](https://rfsaldanha.github.io/microdatasus/) |
| Malhas IBGE | [Download](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html) |

---

## 📝 Como Citar Este Trabalho

```
Ferrari, F. (2025). Desenvolvimento de um Modelo de Previsão para Surtos de 
Dengue em Municípios Brasileiros utilizando Séries Temporais e Dados Climáticos. 
Trabalho de Conclusão de Curso (Engenharia de Software) - Universidade de Brasília.
```

---

## 🔄 Atualização Contínua

Esta lista de referências será atualizada continuamente conforme novos trabalhos relevantes forem identificados. Para sugerir adições, abra uma issue no repositório.

---

*Última atualização: Outubro 2025*

