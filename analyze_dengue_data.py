#!/usr/bin/env python3
"""
Script para analisar dados de dengue do SINAN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configurações de visualização
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

def main():
    print("="*70)
    print("ANÁLISE DOS DADOS DE DENGUE - SINAN 2025")
    print("="*70)
    
    # Carregar dados SINAN
    sinan_path = Path('data/raw/sinan/dengue_2025.parquet')
    
    if not sinan_path.exists():
        print("❌ Arquivo SINAN não encontrado!")
        return
    
    print("✅ Carregando dados SINAN...")
    df_sinan = pd.read_parquet(sinan_path)
    print(f"✅ Dados SINAN carregados: {len(df_sinan):,} registros")
    
    # Informações básicas
    print(f"\nColunas disponíveis:")
    for col in df_sinan.columns:
        print(f"  - {col}")
    
    # Análise de dados faltantes
    print(f"\nDados faltantes por coluna:")
    missing_data = df_sinan.isnull().sum()
    for col, missing in missing_data.items():
        if missing > 0:
            print(f"  - {col}: {missing:,} ({missing/len(df_sinan)*100:.1f}%)")
    
    # Primeiras linhas
    print(f"\nPrimeiras 5 linhas:")
    print(df_sinan.head())
    
    # Análise de distribuição geográfica
    print("\n" + "="*70)
    print("DISTRIBUIÇÃO GEOGRÁFICA")
    print("="*70)
    
    location_cols = [col for col in df_sinan.columns if any(term in col.lower() for term in ['uf', 'estado', 'municipio', 'cidade', 'regiao'])]
    print(f"Colunas de localização encontradas: {location_cols}")
    
    if location_cols:
        for col in location_cols:
            print(f"\nDistribuição por {col}:")
            value_counts = df_sinan[col].value_counts()
            print(value_counts.head(10))
    
    # Análise temporal
    print("\n" + "="*70)
    print("ANÁLISE TEMPORAL")
    print("="*70)
    
    date_cols = [col for col in df_sinan.columns if 'data' in col.lower() or 'dt_' in col.lower()]
    print(f"Colunas de data encontradas: {date_cols}")
    
    if date_cols:
        for col in date_cols:
            print(f"\nAnálise da coluna {col}:")
            print(f"Tipo de dados: {df_sinan[col].dtype}")
            print(f"Valores únicos: {df_sinan[col].nunique()}")
            print(f"Valores nulos: {df_sinan[col].isnull().sum()}")
            
            # Mostrar exemplos
            sample_values = df_sinan[col].dropna().head(5).tolist()
            print(f"Exemplos: {sample_values}")
            
            # Tentar converter para datetime
            try:
                if df_sinan[col].dtype == 'object':
                    df_sinan[f'{col}_parsed'] = pd.to_datetime(df_sinan[col], errors='coerce')
                    valid_dates = df_sinan[f'{col}_parsed'].dropna()
                    if len(valid_dates) > 0:
                        print(f"Datas válidas: {len(valid_dates)}")
                        print(f"Período: {valid_dates.min()} a {valid_dates.max()}")
                        
                        # Análise mensal
                        df_sinan['mes'] = df_sinan[f'{col}_parsed'].dt.month
                        df_sinan['ano'] = df_sinan[f'{col}_parsed'].dt.year
                        
                        casos_por_mes = df_sinan.groupby(['ano', 'mes']).size().reset_index(name='casos')
                        print(f"\nCasos por mês:")
                        print(casos_por_mes)
                        
            except Exception as e:
                print(f"Erro ao processar datas: {e}")
    
    # Salvar resumo
    print("\n" + "="*70)
    print("RESUMO FINAL")
    print("="*70)
    print(f"Total de registros: {len(df_sinan):,}")
    print(f"Colunas: {len(df_sinan.columns)}")
    print(f"Período dos dados: 2025")
    
    # Salvar arquivo de resumo
    summary_path = Path('data/processed/sinan_summary.txt')
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("RESUMO DOS DADOS SINAN - DENGUE 2025\n")
        f.write("="*50 + "\n")
        f.write(f"Total de registros: {len(df_sinan):,}\n")
        f.write(f"Colunas: {len(df_sinan.columns)}\n")
        f.write(f"Período: 2025\n\n")
        f.write("Colunas disponíveis:\n")
        for col in df_sinan.columns:
            f.write(f"  - {col}\n")
    
    print(f"✅ Resumo salvo em: {summary_path}")

if __name__ == "__main__":
    main()

