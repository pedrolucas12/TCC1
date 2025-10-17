#!/usr/bin/env python3
"""
Script para análise exploratória dos dados INMET processados

Este script analisa os dados climáticos processados e gera visualizações
e estatísticas úteis para o TCC de previsão de dengue.

Análises incluídas:
- Padrões sazonais de precipitação (criadouros)
- Distribuição de temperatura (faixa ideal 20-30°C)
- Correlação entre variáveis climáticas
- Identificação de "janelas de risco" para dengue

Autor: Pedro Lucas & Thiago
Projeto: TCC - Previsão de Surtos de Dengue
Data: Outubro 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configurações de visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')


def load_processed_data(data_dir):
    """
    Carrega dados processados do INMET
    
    Args:
        data_dir (str): Diretório com os dados processados
        
    Returns:
        tuple: (df_hourly, df_weekly, df_lagged, metadata)
    """
    data_path = Path(data_dir)
    
    print("\n📂 Carregando dados processados...")
    
    # Dados horários consolidados
    hourly_file = data_path / "inmet_consolidated_2025.parquet"
    df_hourly = pd.read_parquet(hourly_file) if hourly_file.exists() else None
    if df_hourly is not None:
        print(f"  ✅ Dados horários: {len(df_hourly):,} registros")
    
    # Dados semanais
    weekly_file = data_path / "inmet_weekly_2025.parquet"
    df_weekly = pd.read_parquet(weekly_file) if weekly_file.exists() else None
    if df_weekly is not None:
        print(f"  ✅ Dados semanais: {len(df_weekly):,} semanas-estação")
    
    # Dados com lags
    lagged_file = data_path / "inmet_weekly_lagged_2025.parquet"
    df_lagged = pd.read_parquet(lagged_file) if lagged_file.exists() else None
    if df_lagged is not None:
        print(f"  ✅ Dados com lags: {len(df_lagged):,} registros")
    
    # Metadata
    metadata_file = data_path / "inmet_metadata.csv"
    metadata = pd.read_csv(metadata_file) if metadata_file.exists() else None
    if metadata is not None:
        print(f"  ✅ Metadata: {len(metadata)} estações")
    
    return df_hourly, df_weekly, df_lagged, metadata


def analyze_precipitation_patterns(df_weekly, output_dir):
    """
    Analisa padrões de precipitação
    
    Foco: Identificar épocas de maior chuva (= mais criadouros)
    
    CRITÉRIO CIENTÍFICO:
    - Qualquer precipitação > 0 mm indica chuva
    - Chuva cria criadouros (água parada)
    - Precipitação acumulada > 10mm/semana já é relevante
    - Lag típico: 3-8 semanas entre chuva e pico de dengue
    """
    print("\n🌧️  Analisando padrões de precipitação...")
    
    # Identificar coluna de precipitação
    precip_cols = [c for c in df_weekly.columns if 'PRECIPITA' in c.upper() and 'sum' in c.lower()]
    if not precip_cols:
        print("  ⚠️  Coluna de precipitação não encontrada")
        return
    
    col_precip = precip_cols[0]
    
    # Agregar por semana do ano (média entre anos)
    df_weekly['semana'] = df_weekly['semana_epi']
    precip_semanal = df_weekly.groupby('semana')[col_precip].agg(['mean', 'std', 'min', 'max'])
    
    # Identificar semanas com chuva (> 0 mm)
    df_weekly['houve_chuva'] = df_weekly[col_precip] > 0
    df_weekly['chuva_relevante'] = df_weekly[col_precip] > 10  # > 10mm/semana
    
    pct_semanas_chuva = df_weekly['houve_chuva'].mean() * 100
    pct_chuva_relevante = df_weekly['chuva_relevante'].mean() * 100
    
    # Visualização
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Gráfico 1: Precipitação média por semana
    ax1.plot(precip_semanal.index, precip_semanal['mean'], linewidth=2, label='Média', color='steelblue')
    ax1.fill_between(
        precip_semanal.index,
        precip_semanal['mean'] - precip_semanal['std'],
        precip_semanal['mean'] + precip_semanal['std'],
        alpha=0.3,
        label='± 1 desvio padrão',
        color='steelblue'
    )
    ax1.axhline(y=10, color='orange', linestyle='--', linewidth=2, label='Limiar relevante (10mm/semana)')
    ax1.set_xlabel('Semana Epidemiológica', fontsize=12)
    ax1.set_ylabel('Precipitação (mm/semana)', fontsize=12)
    ax1.set_title('Padrão Sazonal de Precipitação - Brasil 2025\n(Qualquer precipitação > 0 indica chuva)', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Boxplot por UF
    top_ufs = df_weekly['uf'].value_counts().head(10).index
    df_top = df_weekly[df_weekly['uf'].isin(top_ufs)]
    
    sns.boxplot(data=df_top, x='uf', y=col_precip, ax=ax2)
    ax2.axhline(y=10, color='orange', linestyle='--', linewidth=2, label='Limiar relevante (10mm)')
    ax2.set_xlabel('Estado', fontsize=12)
    ax2.set_ylabel('Precipitação (mm/semana)', fontsize=12)
    ax2.set_title('Distribuição de Precipitação por Estado', fontsize=14, fontweight='bold')
    ax2.tick_params(axis='x', rotation=45)
    ax2.legend()
    
    plt.tight_layout()
    output_file = Path(output_dir) / "analise_precipitacao.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"  💾 Gráfico salvo: {output_file}")
    plt.close()
    
    # Estatísticas
    print(f"\n  📊 Estatísticas de Precipitação:")
    print(f"     Média geral: {df_weekly[col_precip].mean():.2f} mm/semana")
    print(f"     Máximo: {df_weekly[col_precip].max():.2f} mm/semana")
    print(f"     % semanas com chuva (> 0mm): {pct_semanas_chuva:.1f}%")
    print(f"     % semanas com chuva relevante (> 10mm): {pct_chuva_relevante:.1f}%")
    print(f"     Semana mais chuvosa (média): {precip_semanal['mean'].idxmax()}")
    print(f"     Semana mais seca (média): {precip_semanal['mean'].idxmin()}")


def analyze_temperature_patterns(df_weekly, output_dir):
    """
    Analisa padrões de temperatura
    
    Foco: Faixa IDEAL para o Aedes aegypti (25-30°C)
    
    CRITÉRIO CIENTÍFICO:
    - 25-30°C: Reprodução IDEAL (ciclo ovo-adulto em 7-10 dias)
    - Acima de 25°C: Reprodução acelerada
    - Abaixo de 25°C: Reprodução mais lenta
    - Calor intenso (verão) = Maior proliferação
    """
    print("\n🌡️  Analisando padrões de temperatura...")
    
    # Identificar coluna de temperatura
    temp_cols = [c for c in df_weekly.columns if 'TEMPERATURA' in c.upper() and 'mean' in c.lower() and 'HORARIA' in c.upper()]
    if not temp_cols:
        print("  ⚠️  Coluna de temperatura não encontrada")
        return
    
    col_temp = temp_cols[0]
    
    # Calcular % de tempo na faixa IDEAL (25-30°C)
    df_weekly['temp_ideal'] = df_weekly[col_temp].between(25, 30)
    df_weekly['temp_favoravel'] = df_weekly[col_temp] >= 25
    pct_ideal = df_weekly['temp_ideal'].mean() * 100
    pct_favoravel = df_weekly['temp_favoravel'].mean() * 100
    
    # Visualização
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Histograma
    ax1.hist(df_weekly[col_temp].dropna(), bins=50, edgecolor='black', alpha=0.7)
    ax1.axvspan(25, 30, alpha=0.3, color='red', label='Faixa IDEAL para Aedes (25-30°C)')
    ax1.axvline(x=25, color='darkred', linestyle='--', linewidth=2, label='Limiar reprodução acelerada (25°C)')
    ax1.set_xlabel('Temperatura (°C)', fontsize=12)
    ax1.set_ylabel('Frequência', fontsize=12)
    ax1.set_title('Distribuição de Temperatura Média Semanal\n(Ciclo ovo-adulto: 7-10 dias em 25-30°C)', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Série temporal por UF
    top_ufs = df_weekly['uf'].value_counts().head(5).index
    for uf in top_ufs:
        df_uf = df_weekly[df_weekly['uf'] == uf].groupby('semana_epi')[col_temp].mean()
        ax2.plot(df_uf.index, df_uf.values, marker='o', label=uf, alpha=0.7)
    
    ax2.axhline(y=25, color='darkred', linestyle='--', alpha=0.7, linewidth=2, label='Limite inferior ideal (25°C)')
    ax2.axhline(y=30, color='red', linestyle='--', alpha=0.5, label='Limite superior ideal (30°C)')
    ax2.set_xlabel('Semana Epidemiológica', fontsize=12)
    ax2.set_ylabel('Temperatura Média (°C)', fontsize=12)
    ax2.set_title('Temperatura ao Longo do Ano - Top 5 Estados\n(Verão = Maior proliferação)', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    output_file = Path(output_dir) / "analise_temperatura.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"  💾 Gráfico salvo: {output_file}")
    plt.close()
    
    # Estatísticas
    print(f"\n  📊 Estatísticas de Temperatura:")
    print(f"     Média geral: {df_weekly[col_temp].mean():.2f} °C")
    print(f"     Mínima: {df_weekly[col_temp].min():.2f} °C")
    print(f"     Máxima: {df_weekly[col_temp].max():.2f} °C")
    print(f"     % na faixa IDEAL (25-30°C): {pct_ideal:.1f}%")
    print(f"     % acima de 25°C (reprodução acelerada): {pct_favoravel:.1f}%")


def identify_risk_windows(df_weekly, output_dir):
    """
    Identifica "janelas de risco" para dengue
    
    Condições IDEAIS para Aedes aegypti (baseado em literatura científica):
    - Temperatura entre 25-30°C (reprodução acelerada, ciclo 7-10 dias)
    - Precipitação > 10mm/semana (criadouros)
    - Umidade > 60% (sobrevivência do mosquito)
    
    IMPORTANTE: 
    - Dias quentes (verão) = Maior proliferação
    - Chuva anterior (3-8 semanas) prediz surtos
    """
    print("\n⚠️  Identificando janelas de risco para dengue...")
    
    # Identificar colunas
    temp_col = [c for c in df_weekly.columns if 'TEMPERATURA' in c.upper() and 'mean' in c.lower() and 'HORARIA' in c.upper()][0]
    precip_col = [c for c in df_weekly.columns if 'PRECIPITA' in c.upper() and 'sum' in c.lower()][0]
    umid_col = [c for c in df_weekly.columns if 'UMIDADE' in c.upper() and 'mean' in c.lower() and 'HORARIA' in c.upper()][0]
    
    # Definir critérios CIENTÍFICOS
    df_weekly['temp_ideal'] = df_weekly[temp_col].between(25, 30)  # Faixa IDEAL
    df_weekly['temp_favoravel'] = df_weekly[temp_col] >= 25  # Reprodução acelerada
    df_weekly['precip_relevante'] = df_weekly[precip_col] > 10  # > 10mm relevante
    df_weekly['precip_presente'] = df_weekly[precip_col] > 0  # Qualquer chuva
    df_weekly['umid_favoravel'] = df_weekly[umid_col] > 60
    
    # Risco ALTO: Todas condições ideais
    df_weekly['risco_alto'] = (
        df_weekly['temp_ideal'] & 
        df_weekly['precip_relevante'] & 
        df_weekly['umid_favoravel']
    )
    
    # Risco MODERADO: Temperatura favorável + alguma chuva + umidade ok
    df_weekly['risco_moderado'] = (
        df_weekly['temp_favoravel'] & 
        df_weekly['precip_presente'] & 
        df_weekly['umid_favoravel'] &
        ~df_weekly['risco_alto']  # Não é alto
    )
    
    # Estatísticas
    pct_risco_alto = df_weekly['risco_alto'].mean() * 100
    pct_risco_moderado = df_weekly['risco_moderado'].mean() * 100
    pct_temp_ideal = df_weekly['temp_ideal'].mean() * 100
    
    print(f"\n  📊 Análise de Risco:")
    print(f"     % semanas com RISCO ALTO: {pct_risco_alto:.1f}%")
    print(f"     % semanas com RISCO MODERADO: {pct_risco_moderado:.1f}%")
    print(f"     % semanas com temperatura IDEAL (25-30°C): {pct_temp_ideal:.1f}%")
    print(f"     Total de semanas de RISCO ALTO: {df_weekly['risco_alto'].sum():,}")
    
    # Risco por estado
    risco_uf = df_weekly.groupby('uf')['risco_alto'].mean().sort_values(ascending=False)
    
    print(f"\n  🗺️  Top 10 Estados com maior % de semanas de RISCO ALTO:")
    for i, (uf, pct) in enumerate(risco_uf.head(10).items(), 1):
        print(f"     {i}. {uf}: {pct*100:.1f}%")
    
    # Visualização
    fig, ax = plt.subplots(figsize=(12, 8))
    risco_uf.head(15).plot(kind='barh', ax=ax, color='orangered')
    ax.set_xlabel('% de Semanas com Risco Alto', fontsize=12)
    ax.set_ylabel('Estado', fontsize=12)
    ax.set_title('Estados com Maior Proporção de Semanas de Alto Risco para Dengue\n(Temp: 25-30°C | Precip: >10mm | Umid: >60%)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    
    # Converter para porcentagem
    vals = ax.get_xticks()
    ax.set_xticklabels([f'{x*100:.0f}%' for x in vals])
    
    plt.tight_layout()
    output_file = Path(output_dir) / "analise_risco.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n  💾 Gráfico salvo: {output_file}")
    plt.close()
    
    # Salvar dataset de risco ALTO
    output_csv_alto = Path(output_dir) / "semanas_risco_alto.csv"
    df_weekly[df_weekly['risco_alto']].to_csv(output_csv_alto, index=False)
    print(f"  💾 Dataset RISCO ALTO salvo: {output_csv_alto}")
    
    # Salvar dataset de risco MODERADO
    output_csv_mod = Path(output_dir) / "semanas_risco_moderado.csv"
    df_weekly[df_weekly['risco_moderado']].to_csv(output_csv_mod, index=False)
    print(f"  💾 Dataset RISCO MODERADO salvo: {output_csv_mod}")


def main():
    """
    Função principal
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Análise exploratória de dados INMET processados'
    )
    
    parser.add_argument(
        '--data-dir',
        type=str,
        default='../../data/processed/inmet',
        help='Diretório com os dados processados'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='../../data/processed/inmet/analises',
        help='Diretório de saída para gráficos e relatórios'
    )
    
    args = parser.parse_args()
    
    # Criar diretório de saída
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    
    # Carregar dados
    df_hourly, df_weekly, df_lagged, metadata = load_processed_data(args.data_dir)
    
    if df_weekly is None:
        print("\n❌ Dados semanais não encontrados!")
        print("Execute primeiro: python process_inmet_bulk.py")
        return 1
    
    print("\n" + "="*70)
    print("INICIANDO ANÁLISE EXPLORATÓRIA")
    print("="*70)
    
    # Análises
    analyze_precipitation_patterns(df_weekly, args.output_dir)
    analyze_temperature_patterns(df_weekly, args.output_dir)
    identify_risk_windows(df_weekly, args.output_dir)
    
    print("\n" + "="*70)
    print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("="*70)
    print(f"\nResultados salvos em: {args.output_dir}")
    print("\n🎯 Próximos passos para o TCC:")
    print("  1. Baixar dados de dengue do SINAN")
    print("  2. Fazer join espacial (estações INMET → municípios)")
    print("  3. Calcular correlações cruzadas (climate lag vs casos)")
    print("  4. Treinar modelos preditivos (SARIMA, XGBoost, LSTM)")
    
    return 0


if __name__ == '__main__':
    exit(main())
