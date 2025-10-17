#!/usr/bin/env python3
"""
Script para processamento massivo de dados INMET

Este script processa múltiplos arquivos CSV do INMET (Instituto Nacional de Meteorologia)
e gera datasets consolidados para análise de correlação com casos de dengue.

Dados do INMET contêm:
- Temperatura (média, mínima, máxima)
- Precipitação acumulada
- Umidade relativa do ar
- Pressão atmosférica
- Velocidade do vento
- Radiação solar
- Outros parâmetros meteorológicos

Essas variáveis climáticas são fundamentais para:
1. Entender padrões sazonais de chuva (criadouros do Aedes aegypti)
2. Correlacionar temperatura com reprodução do mosquito
3. Identificar janelas temporais críticas para surtos de dengue

CRITÉRIOS CIENTÍFICOS (Aedes aegypti):
- 🌡️ TEMPERATURA IDEAL: 25-30°C (reprodução acelerada)
  * Abaixo de 25°C: reprodução mais lenta
  * 25-30°C: ciclo ovo-adulto de 7-10 dias (IDEAL)
  * Acima de 30°C: reprodução ainda ocorre mas pode haver estresse térmico
  
- 🌧️ PRECIPITAÇÃO: Qualquer valor > 0 mm indica chuva
  * Cria criadouros (água parada em recipientes)
  * Precipitação acumulada semanal > 10mm já é relevante
  * Lag típico: 3-8 semanas entre chuva e pico de casos

- 💧 UMIDADE: > 60% favorece sobrevivência do mosquito

Autor: Pedro Lucas & Thiago
Projeto: TCC - Previsão de Surtos de Dengue
Data: Outubro 2025
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import glob
import re
import warnings
warnings.filterwarnings('ignore')

class INMETProcessor:
    """
    Classe para processamento massivo de arquivos INMET
    """
    
    def __init__(self, input_dir, output_dir):
        """
        Inicializa o processador
        
        Args:
            input_dir (str): Diretório com os arquivos CSV do INMET
            output_dir (str): Diretório para salvar os resultados processados
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Metadados dos arquivos processados
        self.metadata = []
        
    def list_files(self):
        """
        Lista todos os arquivos CSV no diretório de entrada
        
        Returns:
            list: Lista de caminhos dos arquivos CSV
        """
        pattern = str(self.input_dir / "*.CSV")
        files = glob.glob(pattern)
        print(f"\n{'='*70}")
        print(f"INMET - Processamento Massivo de Dados Climáticos")
        print(f"{'='*70}")
        print(f"Diretório: {self.input_dir}")
        print(f"Total de arquivos encontrados: {len(files)}")
        print(f"{'='*70}\n")
        return sorted(files)
    
    def parse_filename(self, filepath):
        """
        Extrai informações do nome do arquivo INMET
        
        Padrão: INMET_REGIAO_UF_CODIGO_ESTACAO_DATA-INICIO_A_DATA-FIM.CSV
        Exemplo: INMET_CO_DF_A001_BRASILIA_01-01-2025_A_30-09-2025.CSV
        
        Args:
            filepath (str): Caminho do arquivo
            
        Returns:
            dict: Dicionário com metadados extraídos
        """
        filename = Path(filepath).stem
        
        # Padrão regex para nome dos arquivos INMET
        pattern = r'INMET_([A-Z]+)_([A-Z]{2})_([A-Z0-9]+)_(.+?)_(\d{2}-\d{2}-\d{4})_A_(\d{2}-\d{2}-\d{4})'
        match = re.match(pattern, filename)
        
        if match:
            regiao, uf, codigo, estacao, data_inicio, data_fim = match.groups()
            return {
                'arquivo': Path(filepath).name,
                'regiao': regiao,
                'uf': uf,
                'codigo_estacao': codigo,
                'estacao': estacao.replace('_', ' '),
                'data_inicio': data_inicio,
                'data_fim': data_fim
            }
        else:
            return {
                'arquivo': Path(filepath).name,
                'regiao': None,
                'uf': None,
                'codigo_estacao': None,
                'estacao': None,
                'data_inicio': None,
                'data_fim': None
            }
    
    def read_inmet_file(self, filepath):
        """
        Lê um arquivo CSV do INMET
        
        Formato dos arquivos INMET:
        - Linhas 1-8: Metadados (REGIAO, UF, ESTACAO, CODIGO, LAT, LON, ALT, DATA FUNDACAO)
        - Linha 9: Cabeçalhos das colunas
        - Linha 10+: Dados horários
        - Separador: ; (ponto e vírgula)
        - Encoding: latin1 (ISO-8859-1)
        - Decimais: vírgula (,)
        
        Args:
            filepath (str): Caminho do arquivo
            
        Returns:
            tuple: (DataFrame com dados, dict com metadados da estação)
        """
        try:
            # Ler metadados das primeiras 8 linhas
            with open(filepath, 'r', encoding='latin1') as f:
                lines = [f.readline().strip() for _ in range(8)]
            
            metadata_estacao = {}
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().replace(';', '')
                    value = value.strip().replace(';', '')
                    metadata_estacao[key] = value
            
            # Ler dados (pular primeiras 8 linhas de metadata)
            df = pd.read_csv(
                filepath,
                encoding='latin1',
                sep=';',
                skiprows=8,
                decimal=',',  # Importante: INMET usa vírgula para decimais
                na_values=['', ' ', 'null', 'NULL']
            )
            
            # Limpar nomes de colunas (remover espaços extras e caracteres especiais)
            df.columns = df.columns.str.strip()
            
            # Converter coluna Data para datetime
            if 'Data' in df.columns:
                df['Data'] = pd.to_datetime(df['Data'], format='%Y/%m/%d', errors='coerce')
            
            # Processar hora UTC
            if 'Hora UTC' in df.columns:
                df['Hora'] = df['Hora UTC'].str.replace(' UTC', '').str.strip()
                # Criar datetime completo
                df['DateTime'] = pd.to_datetime(
                    df['Data'].astype(str) + ' ' + df['Hora'],
                    format='%Y-%m-%d %H%M',
                    errors='coerce'
                )
            
            return df, metadata_estacao
            
        except Exception as e:
            print(f"[ERRO] Falha ao ler {Path(filepath).name}: {e}")
            return None, None
    
    def process_file(self, filepath, verbose=False):
        """
        Processa um arquivo INMET individual
        
        Args:
            filepath (str): Caminho do arquivo
            verbose (bool): Se True, imprime informações detalhadas
            
        Returns:
            pd.DataFrame: DataFrame processado
        """
        meta = self.parse_filename(filepath)
        
        if verbose:
            print(f"\n📄 Processando: {meta['estacao']} ({meta['uf']})")
        
        df, metadata_estacao = self.read_inmet_file(filepath)
        
        if df is None:
            return None
        
        # Adicionar metadados do arquivo ao DataFrame
        df['codigo_estacao'] = meta['codigo_estacao']
        df['nome_estacao'] = meta['estacao']
        df['uf'] = meta['uf']
        df['regiao'] = meta['regiao']
        
        # Adicionar metadados da estação (lat, lon, altitude)
        if metadata_estacao:
            df['latitude'] = metadata_estacao.get('LATITUDE', None)
            df['longitude'] = metadata_estacao.get('LONGITUDE', None)
            df['altitude'] = metadata_estacao.get('ALTITUDE', None)
        
        # Armazenar metadata completo
        self.metadata.append({
            **meta,
            **metadata_estacao,
            'total_registros': len(df),
            'data_processamento': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        if verbose:
            print(f"   ✅ {len(df)} registros | Período: {meta['data_inicio']} a {meta['data_fim']}")
        
        return df
    
    def process_all_files(self, save_individual=False, save_consolidated=True):
        """
        Processa todos os arquivos CSV no diretório
        
        Args:
            save_individual (bool): Se True, salva cada arquivo processado individualmente
            save_consolidated (bool): Se True, salva um arquivo consolidado com todos os dados
            
        Returns:
            pd.DataFrame: DataFrame consolidado com todos os dados
        """
        files = self.list_files()
        
        if not files:
            print("[AVISO] Nenhum arquivo CSV encontrado!")
            return None
        
        all_data = []
        
        print("🔄 Iniciando processamento...\n")
        
        for i, filepath in enumerate(files, 1):
            print(f"[{i}/{len(files)}] {Path(filepath).name}", end=" ... ")
            
            df = self.process_file(filepath, verbose=False)
            
            if df is not None:
                all_data.append(df)
                print("✅")
                
                # Salvar individual se solicitado
                if save_individual:
                    meta = self.parse_filename(filepath)
                    output_file = self.output_dir / f"inmet_{meta['uf']}_{meta['codigo_estacao']}.parquet"
                    df.to_parquet(output_file, index=False)
            else:
                print("❌")
        
        if not all_data:
            print("\n[ERRO] Nenhum arquivo foi processado com sucesso!")
            return None
        
        # Consolidar todos os dados
        print(f"\n📊 Consolidando {len(all_data)} arquivos...")
        df_consolidated = pd.concat(all_data, ignore_index=True)
        
        print(f"\n{'='*70}")
        print(f"RESUMO DO PROCESSAMENTO")
        print(f"{'='*70}")
        print(f"Total de arquivos processados: {len(all_data)}")
        print(f"Total de registros: {len(df_consolidated):,}")
        
        if 'Data' in df_consolidated.columns:
            print(f"Período: {df_consolidated['Data'].min()} a {df_consolidated['Data'].max()}")
        
        print(f"Estados: {df_consolidated['uf'].nunique()}")
        print(f"Estações: {df_consolidated['codigo_estacao'].nunique()}")
        print(f"{'='*70}\n")
        
        # Gerar estatísticas
        print("📊 Gerando estatísticas...")
        stats = self.generate_summary_statistics(df_consolidated)
        
        if stats:
            print("\n🌧️  Precipitação:")
            if 'precipitacao' in stats:
                for key, value in stats['precipitacao'].items():
                    print(f"  - {key}: {value:.2f}")
            
            print("\n🌡️  Temperatura:")
            if 'temperatura' in stats:
                for key, value in stats['temperatura'].items():
                    print(f"  - {key}: {value:.2f}")
            
            print("\n💧 Umidade:")
            if 'umidade' in stats:
                for key, value in stats['umidade'].items():
                    print(f"  - {key}: {value:.2f}")
        
        # Salvar consolidado
        if save_consolidated:
            output_file = self.output_dir / "inmet_consolidated_2025.parquet"
            df_consolidated.to_parquet(output_file, index=False)
            print(f"\n💾 Arquivo consolidado salvo: {output_file}")
            
            # Salvar metadata
            metadata_file = self.output_dir / "inmet_metadata.csv"
            pd.DataFrame(self.metadata).to_csv(metadata_file, index=False)
            print(f"📋 Metadata salvo: {metadata_file}")
            
            # Criar agregações semanais (CRUCIAL para TCC!)
            print("\n📅 Criando agregação semanal...")
            df_weekly = self.aggregate_by_week(df_consolidated)
            
            if df_weekly is not None:
                output_weekly = self.output_dir / "inmet_weekly_2025.parquet"
                df_weekly.to_parquet(output_weekly, index=False)
                print(f"💾 Dados semanais salvos: {output_weekly}")
                print(f"   Total de semanas-estação: {len(df_weekly):,}")
                
                # Criar features com lags
                print("\n⏰ Criando features com lags temporais...")
                df_lagged = self.create_lagged_features(df_weekly)
                
                output_lagged = self.output_dir / "inmet_weekly_lagged_2025.parquet"
                df_lagged.to_parquet(output_lagged, index=False)
                print(f"💾 Dados com lags salvos: {output_lagged}")
                print(f"   Lags criados: 1, 2, 3, 4, 8, 12 semanas")
        
        return df_consolidated
    
    def generate_summary_statistics(self, df):
        """
        Gera estatísticas resumidas dos dados climáticos
        
        Foca nas variáveis mais relevantes para dengue:
        - Precipitação (qualquer valor > 0 mm indica chuva)
        - Temperatura (ideal: 25-30°C para Aedes aegypti)
        - Umidade (> 60% favorece sobrevivência)
        
        Args:
            df (pd.DataFrame): DataFrame consolidado
            
        Returns:
            dict: Dicionário com estatísticas
        """
        # Identificar colunas relevantes (podem ter nomes variados)
        col_precip = [c for c in df.columns if 'PRECIPITA' in c.upper()][0] if any('PRECIPITA' in c.upper() for c in df.columns) else None
        col_temp = [c for c in df.columns if 'TEMPERATURA DO AR' in c.upper() and 'HORARIA' in c.upper()][0] if any('TEMPERATURA DO AR' in c.upper() and 'HORARIA' in c.upper() for c in df.columns) else None
        col_umidade = [c for c in df.columns if 'UMIDADE RELATIVA DO AR' in c.upper() and 'HORARIA' in c.upper()][0] if any('UMIDADE RELATIVA DO AR' in c.upper() and 'HORARIA' in c.upper() for c in df.columns) else None
        
        stats = {}
        
        if col_precip:
            # Qualquer precipitação > 0 indica chuva
            horas_com_chuva = (df[col_precip] > 0).sum()
            total_horas = len(df)
            
            stats['precipitacao'] = {
                'total_mm': df[col_precip].sum(),
                'media_mm': df[col_precip].mean(),
                'max_mm': df[col_precip].max(),
                'horas_com_chuva': horas_com_chuva,
                'percentual_horas_chuva': (horas_com_chuva / total_horas) * 100,
                'precipitacao_media_quando_chove': df[df[col_precip] > 0][col_precip].mean() if horas_com_chuva > 0 else 0
            }
        
        if col_temp:
            # Faixa ideal: 25-30°C
            temp_ideal = df[col_temp].between(25, 30)
            temp_reproduz = df[col_temp] >= 25  # Temperatura mínima para reprodução rápida
            
            stats['temperatura'] = {
                'media_c': df[col_temp].mean(),
                'min_c': df[col_temp].min(),
                'max_c': df[col_temp].max(),
                'std_c': df[col_temp].std(),
                'percentual_faixa_ideal_25_30c': (temp_ideal.sum() / len(df)) * 100,
                'percentual_acima_25c': (temp_reproduz.sum() / len(df)) * 100
            }
        
        if col_umidade:
            umid_favoravel = df[col_umidade] > 60  # > 60% favorece mosquito
            
            stats['umidade'] = {
                'media_pct': df[col_umidade].mean(),
                'min_pct': df[col_umidade].min(),
                'max_pct': df[col_umidade].max(),
                'percentual_acima_60': (umid_favoravel.sum() / len(df)) * 100
            }
        
        return stats
    
    def aggregate_by_state(self, df):
        """
        Agrega dados por estado e período
        
        Útil para análise regional de padrões climáticos
        
        Args:
            df (pd.DataFrame): DataFrame consolidado
            
        Returns:
            pd.DataFrame: DataFrame agregado por UF
        """
        # Identificar colunas numéricas relevantes
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        # Remover colunas que não devem ser agregadas
        exclude = ['latitude', 'longitude', 'altitude']
        numeric_cols = [c for c in numeric_cols if c not in exclude]
        
        # Agregar por UF
        df_uf = df.groupby('uf')[numeric_cols].agg(['mean', 'std', 'min', 'max'])
        
        return df_uf
    
    def aggregate_by_week(self, df):
        """
        Agrega dados por semana epidemiológica
        
        CRÍTICO PARA O TCC: Dengue é reportada semanalmente!
        
        Esta agregação permite juntar com dados do SINAN.
        
        Args:
            df (pd.DataFrame): DataFrame consolidado
            
        Returns:
            pd.DataFrame: DataFrame agregado por estação + semana epidemiológica
        """
        if 'DateTime' not in df.columns or 'Data' not in df.columns:
            print("[ERRO] Coluna DateTime/Data não encontrada!")
            return None
        
        # Adicionar semana epidemiológica
        df['ano'] = df['Data'].dt.year
        df['semana_epi'] = df['Data'].dt.isocalendar().week
        df['ano_semana'] = df['ano'].astype(str) + '_' + df['semana_epi'].astype(str).str.zfill(2)
        
        # Identificar colunas de precipitação, temperatura e umidade
        col_precip = [c for c in df.columns if 'PRECIPITA' in c.upper()][0] if any('PRECIPITA' in c.upper() for c in df.columns) else None
        col_temp = [c for c in df.columns if 'TEMPERATURA DO AR' in c.upper() and 'HORARIA' in c.upper()][0] if any('TEMPERATURA DO AR' in c.upper() and 'HORARIA' in c.upper() for c in df.columns) else None
        col_umidade = [c for c in df.columns if 'UMIDADE RELATIVA DO AR' in c.upper() and 'HORARIA' in c.upper()][0] if any('UMIDADE RELATIVA DO AR' in c.upper() and 'HORARIA' in c.upper() for c in df.columns) else None
        
        # Definir agregações
        agg_dict = {
            'codigo_estacao': 'first',
            'nome_estacao': 'first',
            'uf': 'first',
            'regiao': 'first',
            'latitude': 'first',
            'longitude': 'first',
            'altitude': 'first',
            'ano': 'first',
            'semana_epi': 'first'
        }
        
        if col_precip:
            agg_dict[col_precip] = ['sum', 'mean', 'max']  # Soma semanal é importante!
        if col_temp:
            agg_dict[col_temp] = ['mean', 'min', 'max', 'std']
        if col_umidade:
            agg_dict[col_umidade] = ['mean', 'min', 'max']
        
        # Agregar por estação + ano + semana
        df_weekly = df.groupby(['codigo_estacao', 'ano', 'semana_epi']).agg(agg_dict).reset_index()
        
        # Achatar colunas multi-nível
        df_weekly.columns = ['_'.join(col).strip('_') if isinstance(col, tuple) else col for col in df_weekly.columns.values]
        
        return df_weekly
    
    def create_lagged_features(self, df_weekly, lags=[1, 2, 3, 4, 8, 12]):
        """
        Cria features com lags temporais + indicadores epidemiológicos
        
        BASEADO EM: Xavier et al. (2021) - PLOS ONE
        "Analysis of climate factors and dengue incidence in Rio de Janeiro"
        
        DESCOBERTAS DO PAPER:
        - Precipitação de 1-2 MESES ATRÁS (t-1, t-2) prediz dengue
        - Temperatura > 22-24°C aumenta população de Aedes aegypti  
        - Epidemias: crescimento 4-6 sem + explosão 10-12 sem
        - Maiores incidências: Abril-Maio (após período chuvoso)
        
        Args:
            df_weekly (pd.DataFrame): DataFrame semanal
            lags (list): Lags em semanas (1,2,3,4=1mês, 8=2meses, 12=3meses)
            
        Returns:
            pd.DataFrame: DataFrame com lags + indicadores de risco
        """
        df_lagged = df_weekly.copy()
        df_lagged = df_lagged.sort_values(['codigo_estacao', 'ano', 'semana_epi'])
        
        # Identificar colunas climáticas principais
        col_precip_sum = [c for c in df_lagged.columns if 'sum' in c.lower() and 'PRECIPITA' in c.upper()]
        col_precip_sum = col_precip_sum[0] if col_precip_sum else None
        
        col_temp_mean = [c for c in df_lagged.columns if 'mean' in c.lower() and 'TEMPERATURA' in c.upper()]
        col_temp_mean = col_temp_mean[0] if col_temp_mean else None
        
        col_umid_mean = [c for c in df_lagged.columns if 'mean' in c.lower() and 'UMIDADE' in c.upper()]
        col_umid_mean = col_umid_mean[0] if col_umid_mean else None
        
        # === 1. LAGS TRADICIONAIS (todas variáveis numéricas) ===
        numeric_cols = df_lagged.select_dtypes(include=[np.number]).columns
        exclude = ['ano', 'semana_epi', 'latitude', 'longitude', 'altitude']
        numeric_cols = [c for c in numeric_cols if c not in exclude]
        
        for col in numeric_cols:
            for lag in lags:
                df_lagged[f'{col}_lag{lag}'] = df_lagged.groupby('codigo_estacao')[col].shift(lag)
        
        # === 2. PRECIPITAÇÃO ACUMULADA (paper: 2 meses preditivo) ===
        if col_precip_sum:
            # 4 semanas (~1 mês)
            df_lagged['precip_acum_4sem'] = df_lagged.groupby('codigo_estacao')[col_precip_sum].transform(
                lambda x: x.rolling(window=4, min_periods=1).sum()
            )
            # 8 semanas (~2 meses) - CRÍTICO SEGUNDO PAPER
            df_lagged['precip_acum_8sem'] = df_lagged.groupby('codigo_estacao')[col_precip_sum].transform(
                lambda x: x.rolling(window=8, min_periods=1).sum()
            )
            # 12 semanas (~3 meses) - sazonalidade
            df_lagged['precip_acum_12sem'] = df_lagged.groupby('codigo_estacao')[col_precip_sum].transform(
                lambda x: x.rolling(window=12, min_periods=1).sum()
            )
        
        # === 3. MÉDIAS MÓVEIS DE TEMPERATURA ===
        if col_temp_mean:
            df_lagged['temp_media_4sem'] = df_lagged.groupby('codigo_estacao')[col_temp_mean].transform(
                lambda x: x.rolling(window=4, min_periods=1).mean()
            )
            df_lagged['temp_media_8sem'] = df_lagged.groupby('codigo_estacao')[col_temp_mean].transform(
                lambda x: x.rolling(window=8, min_periods=1).mean()
            )
        
        # === 4. INDICADORES DE RISCO EPIDEMIOLÓGICO ===
        if col_temp_mean and col_precip_sum and col_umid_mean:
            # Temperatura favorável (>= 22°C - paper Xavier et al.)
            df_lagged['temp_favoravel'] = (df_lagged[col_temp_mean] >= 22).astype(int)
            # Temperatura ideal (25-30°C - ciclo mais rápido)
            df_lagged['temp_ideal'] = (df_lagged[col_temp_mean].between(25, 30)).astype(int)
            # Chuva relevante (> 10mm/semana)
            df_lagged['chuva_relevante'] = (df_lagged[col_precip_sum] > 10).astype(int)
            # Umidade favorável (> 60%)
            df_lagged['umid_favoravel'] = (df_lagged[col_umid_mean] > 60).astype(int)
            
            # ÍNDICE DE RISCO COMPOSTO (0-4 pontos)
            df_lagged['indice_risco_dengue'] = (
                df_lagged['temp_favoravel'] +
                df_lagged['chuva_relevante'] +
                df_lagged['umid_favoravel'] +
                (df_lagged['precip_acum_8sem'] > 80).astype(int)  # Chuva acumulada alta
            )
        
        return df_lagged


def main():
    """
    Função principal
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Processamento massivo de dados INMET para análise de dengue',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  # Processar todos os arquivos da pasta Downloads/2025
  python process_inmet_bulk.py --input "C:/Users/pedro.santana/Downloads/2025" --output "../../data/processed/inmet"
  
  # Salvar também arquivos individuais
  python process_inmet_bulk.py --input "C:/Users/pedro.santana/Downloads/2025" --output "../../data/processed/inmet" --save-individual
        """
    )
    
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Diretório com os arquivos CSV do INMET'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='../../data/processed/inmet',
        help='Diretório de saída para arquivos processados'
    )
    
    parser.add_argument(
        '--save-individual',
        action='store_true',
        help='Salvar cada arquivo processado individualmente'
    )
    
    args = parser.parse_args()
    
    # Criar processador
    processor = INMETProcessor(args.input, args.output)
    
    # Processar todos os arquivos
    df = processor.process_all_files(
        save_individual=args.save_individual,
        save_consolidated=True
    )
    
    if df is not None:
        print("\n✅ Processamento concluído com sucesso!")
        print(f"\nPróximos passos:")
        print("1. Analisar os dados consolidados")
        print("2. Calcular médias semanais/mensais")
        print("3. Juntar com dados de dengue do SINAN")
        print("4. Treinar modelos de previsão")
    else:
        print("\n❌ Processamento falhou!")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
