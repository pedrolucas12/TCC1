# Bases de Dados

> Guia completo das fontes de dados epidemiológicos e climáticos para o projeto de previsão de surtos de dengue.

---

## 📊 Visão Geral

O projeto utiliza duas categorias principais de dados:

1. **Dados Epidemiológicos**: Casos de dengue (SINAN/DataSUS)
2. **Dados Climáticos**: Temperatura, precipitação, umidade (INMET, CHIRPS, ERA5, NASA)
3. **Dados Auxiliares**: População, malhas municipais, índices socioeconômicos (IBGE)

---

## 🏥 DADOS EPIDEMIOLÓGICOS

### 1. OpenDataSUS / SINAN - Dengue

#### Descrição
- **Fonte**: Ministério da Saúde do Brasil
- **Sistema**: SINAN (Sistema de Informação de Agravos de Notificação)
- **Cobertura**: Nacional, todos os municípios brasileiros
- **Período**: 2007 até o presente
- **Granularidade**: Microdados individuais de notificações

#### Links Oficiais
- **Catálogo**: [OpenDataSUS - Arboviroses Dengue](https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue)
- **S3 (downloads diretos)**: `https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/json/`
- **Dicionário de Dados** (PDF): [dic_dados_dengue.pdf](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/dic_dados_dengue.pdf)

#### Formato dos Dados
- **Formatos disponíveis**: JSON, CSV, DBF
- **Arquivos por ano**: Ex.: `DENGBR25.json.zip` (2025), `DENGBR24.json.zip` (2024)
- **Tamanho**: ~100MB a 500MB por ano (compactado)

#### Campos Principais

| Campo | Descrição | Tipo | Uso |
|-------|-----------|------|-----|
| `dt_notific` | Data da notificação | Date | Análise temporal |
| `dt_sin_pri` | Data dos primeiros sintomas | Date | **Principal para séries temporais** |
| `sem_pri` | Semana epidemiológica dos sintomas | String (YYYYWW) | Agregação temporal |
| `sem_not` | Semana epidemiológica da notificação | String (YYYYWW) | Atraso de notificação |
| `nu_ano` | Ano da notificação | Integer | Filtro temporal |
| `id_municip` | Código IBGE do município (residência) | String (7 dígitos) | **Chave espacial** |
| `id_mn_resi` | Código município residência | String | Join espacial |
| `classificacao_final` | Classificação do caso | String | Filtro de casos |
| `criterio_confirmacao` | Como o caso foi confirmado | String | Qualidade do dado |
| `evolucao` | Evolução do caso | String | Análise de gravidade |
| `idade` | Idade do paciente | Integer | Estratificação |
| `sexo` | Sexo | String (M/F) | Estratificação |

#### Valores Importantes para Filtros

**`criterio_confirmacao`**:
- `LABORATORIAL`: Confirmado por exame
- `CLÍNICO-EPIDEMIOLÓGICO`: Confirmado por critério clínico
- `EM INVESTIGAÇÃO`: Ainda em investigação
- `DESCARTADO`: Não é dengue

**`classificacao_final`**:
- `DENGUE`: Caso confirmado
- `DENGUE COM SINAIS DE ALARME`: Caso grave
- `DENGUE GRAVE`: Caso muito grave
- `DESCARTADO`: Não confirmado

#### Exemplo de Download (Python)

```python
import requests, zipfile, io, json
import pandas as pd

def download_sinan_dengue(year):
    """
    Baixa dados SINAN de dengue do OpenDataSUS
    year: dois dígitos (ex: 24 para 2024)
    """
    url = f"https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/json/DENGBR{year}.json.zip"
    
    print(f"Baixando dados de 20{year}...")
    r = requests.get(url, timeout=120)
    
    z = zipfile.ZipFile(io.BytesIO(r.content))
    json_file = [n for n in z.namelist() if n.endswith(".json")][0]
    
    with z.open(json_file) as f:
        data = json.load(f)
    
    df = pd.json_normalize(data)
    print(f"Total de registros: {len(df)}")
    return df

# Uso
df_2024 = download_sinan_dengue(24)
```

#### Limitações e Considerações
- ⚠️ **Subnotificação**: Muitos casos assintomáticos ou leves não são notificados
- ⚠️ **Atraso de notificação**: Diferença entre `dt_sin_pri` e `dt_notific` (médias de 7-14 dias)
- ⚠️ **Qualidade variável**: Alguns campos podem estar incompletos
- ✅ **Cobertura ampla**: Praticamente todos os municípios brasileiros
- ✅ **Histórico longo**: Dados desde 2007

---

### 2. TabNet / DATASUS (Dados Agregados)

#### Descrição
- Interface web para consultar dados já agregados
- Útil para validação rápida
- Menos flexível que microdados

#### Link
[TabNet - Dengue](https://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet%2Fcnv%2Fdenguebbr.def)

---

### 3. InfoDengue (Fiocruz / FGV)

#### Descrição
- Sistema de monitoramento e alerta de arboviroses
- API pública com dados processados
- Útil para **benchmarking**

#### Características
- Dados semanais por município
- Níveis de alerta (verde, amarelo, laranja, vermelho)
- Incorpora dados climáticos e tweets

#### API
- **Documentação**: [API InfoDengue](https://info.dengue.mat.br/services/api)
- **Endpoint exemplo**: `/api/alertcity?geocode=3304557&disease=dengue&format=json&ew_start=1&ew_end=52&ey_start=2020&ey_end=2024`

---

## 🌦️ DADOS CLIMÁTICOS

### 1. INMET / BDMEP (Instituto Nacional de Meteorologia)

#### Descrição
- **Tipo**: Dados de estações meteorológicas terrestres
- **Cobertura**: ~500 estações automáticas no Brasil
- **Qualidade**: Alta (medições diretas)
- **Granularidade**: Horária ou diária

#### Variáveis Disponíveis
- Temperatura (média, mín, máx)
- Precipitação acumulada
- Umidade relativa
- Pressão atmosférica
- Radiação solar
- Velocidade/direção do vento

#### Links
- **BDMEP**: [https://bdmep.inmet.gov.br/](https://bdmep.inmet.gov.br/)
- **Portal INMET**: [https://portal.inmet.gov.br/](https://portal.inmet.gov.br/manual)

#### Limitações
- ❌ **Distribuição irregular**: Nem todos os municípios têm estações
- ❌ **Dados pontuais**: Representam apenas o local da estação
- ✅ **Alta qualidade**: Medições precisas
- ✅ **Longo histórico**: Muitas estações com décadas de dados

#### Estratégia de Uso
1. Baixar dados das estações
2. Mapear cada estação ao município mais próximo
3. Ou usar interpolação espacial

---

### 2. CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)

#### Descrição
- **Tipo**: Precipitação por satélite + estações
- **Cobertura**: Global (50°S a 50°N)
- **Resolução espacial**: ~5.5 km (0.05°)
- **Resolução temporal**: Diária
- **Período**: 1981 até o presente (atualização contínua)

#### Vantagens
- ✅ **Cobertura espacial completa**: Todos os municípios
- ✅ **Resolução adequada**: Permite agregação por município
- ✅ **Validado com estações**: Alta correlação com INMET
- ✅ **Fácil processamento**: Formato NetCDF padrão

#### Links
- **Site oficial**: [https://www.chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps)
- **FTP**: ftp://ftp.chg.ucsb.edu/pub/org/chg/products/CHIRPS-2.0/

#### Formato
- NetCDF (.nc)
- GeoTIFF (.tif)

#### Exemplo de Uso (Python)

```python
import xarray as xr
import geopandas as gpd

# Abrir dados CHIRPS
ds = xr.open_dataset('chirps-v2.0.2024.days_p05.nc')

# Carregar shapefile de municípios
municipios = gpd.read_file('malha_municipal.shp')

# Calcular média de precipitação por município
# (usa zonal statistics - rasterio/rasterstats)
```

#### Recomendação
⭐ **CHIRPS é altamente recomendado** para precipitação devido à cobertura espacial completa.

---

### 3. ERA5 (Copernicus Climate Data Store)

#### Descrição
- **Tipo**: Reanálise atmosférica global
- **Fonte**: ECMWF (European Centre for Medium-Range Weather Forecasts)
- **Resolução espacial**: ~31 km (0.25° ou 0.1°)
- **Resolução temporal**: Horária
- **Período**: 1950 até o presente

#### Variáveis Disponíveis (100+)
- Temperatura (2m, superfície)
- Precipitação
- Umidade relativa/específica
- Velocidade do vento
- Radiação
- Pressão
- E muito mais...

#### Links
- **Climate Data Store**: [https://cds.climate.copernicus.eu/](https://cds.climate.copernicus.eu/)
- **ERA5 single levels**: [Dataset](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels)

#### Como Acessar
1. Criar conta gratuita no CDS
2. Instalar `cdsapi` (Python)
3. Fazer requisições via API

#### Exemplo (Python)

```python
import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['2m_temperature', 'total_precipitation'],
        'year': '2024',
        'month': '01',
        'day': '01',
        'time': '12:00',
        'area': [-10, -50, -25, -40],  # N, W, S, E (bounding box Brasil)
        'format': 'netcdf'
    },
    'download.nc')
```

#### Recomendação
⭐ **ERA5 é excelente** para variáveis além de precipitação (temperatura, umidade, vento).

---

### 4. NASA POWER (Prediction Of Worldwide Energy Resources)

#### Descrição
- **Tipo**: API para dados meteorológicos/solares
- **Cobertura**: Global
- **Resolução espacial**: ~0.5° x 0.625°
- **Resolução temporal**: Diária
- **Período**: 1981 até ~7 dias atrás

#### Vantagens
- ✅ **API simples**: Requisição HTTP por coordenada
- ✅ **Sem necessidade de conta**: Acesso livre
- ✅ **Rápido para protótipos**: Ideal para testes iniciais
- ✅ **Múltiplas variáveis**: Temp, precip, umidade, radiação

#### Variáveis Úteis
- `T2M`: Temperatura a 2m (°C)
- `PRECTOTCORR`: Precipitação total corrigida (mm/dia)
- `RH2M`: Umidade relativa a 2m (%)
- `WS2M`: Velocidade do vento a 2m (m/s)

#### Exemplo de Uso (Python)

```python
import requests
import pandas as pd

def get_nasa_power(lat, lon, start_date, end_date):
    """
    Baixa dados NASA POWER para uma coordenada
    """
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    params = {
        "parameters": "T2M,PRECTOTCORR,RH2M",
        "community": "AG",
        "longitude": lon,
        "latitude": lat,
        "start": start_date,  # YYYYMMDD
        "end": end_date,
        "format": "JSON"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Converter para DataFrame
    df = pd.DataFrame(data['properties']['parameter'])
    df.index = pd.to_datetime(df.index, format='%Y%m%d')
    
    return df

# Exemplo: Brasília
df_clima = get_nasa_power(-15.8, -47.9, "20200101", "20241231")
```

#### Links
- **Homepage**: [https://power.larc.nasa.gov/](https://power.larc.nasa.gov/)
- **Documentação API**: [API Docs](https://power.larc.nasa.gov/docs/services/api/)

#### Recomendação
⭐ **NASA POWER é ideal** para prototipagem rápida e validação de conceito.

---

## 🗺️ DADOS AUXILIARES

### 1. IBGE - Malhas Territoriais

#### Descrição
- Shapefiles dos limites municipais brasileiros
- Códigos IBGE de 7 dígitos (padrão nacional)
- Atualizados anualmente

#### Link
[Malhas Municipais - IBGE](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html)

#### Uso
- Mapear códigos de município (SINAN) para geometrias
- Calcular centroids para consultas de clima
- Zonal statistics (média de grade climática dentro do município)

---

### 2. IBGE - População e Indicadores

#### Dados Disponíveis
- População por município (Censo, estimativas anuais)
- PIB municipal
- Índice de saneamento
- Taxa de urbanização
- Densidade demográfica

#### Uso
- Normalização de casos (casos per capita)
- Variáveis de controle em modelos

---

## 📋 RESUMO: QUAL FONTE USAR?

### Para Casos de Dengue
✅ **Recomendado**: OpenDataSUS / SINAN (microdados)
- Download via S3
- Processar localmente
- Agregar por município + semana

### Para Precipitação
✅ **Recomendado**: CHIRPS
- Cobertura espacial completa
- Resolução adequada
- Fácil agregação por município

🔄 **Alternativa**: NASA POWER (prototipagem)
🔄 **Complementar**: INMET (validação/comparação)

### Para Temperatura e Umidade
✅ **Recomendado**: ERA5 ou NASA POWER
- ERA5: Melhor resolução e qualidade
- NASA POWER: Mais simples de usar

🔄 **Alternativa**: INMET (quando disponível)

### Para Geometrias e População
✅ **Recomendado**: IBGE
- Malhas municipais (shapefile)
- Estimativas populacionais

---

## 🔗 Pipeline de Integração

```
┌─────────────────┐
│  SINAN (JSON)   │────┐
└─────────────────┘    │
                       │    ┌──────────────────┐
┌─────────────────┐    │    │                  │
│ CHIRPS (NetCDF) │────┼───▶│  ETL Pipeline    │
└─────────────────┘    │    │  (Python/SQL)    │
                       │    │                  │
┌─────────────────┐    │    └──────────────────┘
│  ERA5 (NetCDF)  │────┤             │
└─────────────────┘    │             ▼
                       │    ┌──────────────────┐
┌─────────────────┐    │    │  PostgreSQL +    │
│ IBGE (Shapefile)│────┘    │  PostGIS         │
└─────────────────┘         └──────────────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ Features Semanais│
                            │ (município-semana)│
                            └──────────────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │   Modelagem ML   │
                            │ (SARIMA/XGB/LSTM)│
                            └──────────────────┘
```

---

## 📝 Checklist de Coleta

- [ ] Baixar SINAN dengue (2015-2024)
- [ ] Baixar CHIRPS (2015-2024) para regiões de interesse
- [ ] Registrar conta no Copernicus CDS
- [ ] Testar API NASA POWER
- [ ] Baixar malha municipal IBGE (ano mais recente)
- [ ] Baixar estimativas populacionais IBGE
- [ ] Documentar versões e datas de download

---

*Última atualização: Outubro 2025*

