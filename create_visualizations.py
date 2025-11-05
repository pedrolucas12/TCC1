#!/usr/bin/env python3
"""
Script para criar visualizações dos dados de dengue
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
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def create_visualizations():
    print("="*70)
    print("CRIANDO VISUALIZAÇÕES DOS DADOS DE DENGUE")
    print("="*70)
    
    # Carregar dados
    sinan_path = Path('data/raw/sinan/dengue_2025.parquet')
    df = pd.read_parquet(sinan_path)
    
    # Criar diretório para salvar gráficos
    output_dir = Path('data/processed/visualizations')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Distribuição geográfica por UF
    print("1. Criando gráfico de distribuição por UF...")
    plt.figure(figsize=(15, 8))
    uf_counts = df['SG_UF_NOT'].value_counts().head(15)
    uf_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribuição de Casos de Dengue por UF - 2025', fontsize=16, fontweight='bold')
    plt.xlabel('UF', fontsize=12)
    plt.ylabel('Número de Casos', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'distribuicao_por_uf.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. Evolução temporal dos casos
    print("2. Criando gráfico de evolução temporal...")
    df['DT_NOTIFIC_parsed'] = pd.to_datetime(df['DT_NOTIFIC'])
    df['mes'] = df['DT_NOTIFIC_parsed'].dt.month
    df['ano'] = df['DT_NOTIFIC_parsed'].dt.year
    
    casos_por_mes = df.groupby(['ano', 'mes']).size().reset_index(name='casos')
    
    plt.figure(figsize=(15, 8))
    plt.plot(casos_por_mes['mes'], casos_por_mes['casos'], marker='o', linewidth=2, markersize=6)
    plt.title('Evolução Temporal dos Casos de Dengue - 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Mês', fontsize=12)
    plt.ylabel('Número de Casos', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'evolucao_temporal.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 3. Distribuição por faixa etária
    print("3. Criando gráfico de distribuição por idade...")
    plt.figure(figsize=(12, 8))
    df['NU_IDADE_N'].hist(bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
    plt.title('Distribuição de Casos por Idade - 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Idade (anos)', fontsize=12)
    plt.ylabel('Número de Casos', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'distribuicao_idade.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. Distribuição por sexo
    print("4. Criando gráfico de distribuição por sexo...")
    plt.figure(figsize=(8, 6))
    sexo_counts = df['CS_SEXO'].value_counts()
    colors = ['lightblue', 'lightpink']
    plt.pie(sexo_counts.values, labels=['Masculino', 'Feminino'], autopct='%1.1f%%', 
            colors=colors, startangle=90)
    plt.title('Distribuição de Casos por Sexo - 2025', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_dir / 'distribuicao_sexo.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 5. Análise de sintomas
    print("5. Criando gráfico de sintomas...")
    sintomas = ['FEBRE', 'MIALGIA', 'CEFALEIA', 'EXANTEMA', 'VOMITO', 'NAUSEA']
    sintomas_data = {}
    
    for sintoma in sintomas:
        if sintoma in df.columns:
            sintomas_data[sintoma] = df[sintoma].value_counts().get(1, 0)
    
    plt.figure(figsize=(12, 8))
    sintomas_df = pd.DataFrame(list(sintomas_data.items()), columns=['Sintoma', 'Casos'])
    sintomas_df = sintomas_df.sort_values('Casos', ascending=True)
    
    plt.barh(sintomas_df['Sintoma'], sintomas_df['Casos'], color='lightgreen', edgecolor='black')
    plt.title('Frequência de Sintomas em Casos de Dengue - 2025', fontsize=16, fontweight='bold')
    plt.xlabel('Número de Casos', fontsize=12)
    plt.ylabel('Sintomas', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'sintomas.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 6. Análise de gravidade
    print("6. Criando gráfico de gravidade...")
    gravidade_cols = ['HOSPITALIZ', 'EVOLUCAO']
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Hospitalização
    if 'HOSPITALIZ' in df.columns:
        hosp_counts = df['HOSPITALIZ'].value_counts()
        axes[0].pie(hosp_counts.values, labels=['Não', 'Sim'], autopct='%1.1f%%', 
                    colors=['lightcoral', 'lightblue'], startangle=90)
        axes[0].set_title('Casos Hospitalizados', fontsize=14, fontweight='bold')
    
    # Evolução
    if 'EVOLUCAO' in df.columns:
        evol_counts = df['EVOLUCAO'].value_counts()
        axes[1].pie(evol_counts.values, labels=evol_counts.index, autopct='%1.1f%%', 
                    startangle=90)
        axes[1].set_title('Evolução dos Casos', fontsize=14, fontweight='bold')
    
    plt.suptitle('Análise de Gravidade dos Casos de Dengue - 2025', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_dir / 'gravidade.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 7. Heatmap de correlação entre sintomas
    print("7. Criando heatmap de correlação...")
    sintomas_df = df[sintomas].fillna(0)
    correlation_matrix = sintomas_df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, linewidths=0.5)
    plt.title('Correlação entre Sintomas de Dengue - 2025', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_dir / 'correlacao_sintomas.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 8. Resumo estatístico
    print("8. Criando resumo estatístico...")
    resumo = {
        'Total de Casos': len(df),
        'Período': f"{df['DT_NOTIFIC_parsed'].min().strftime('%d/%m/%Y')} a {df['DT_NOTIFIC_parsed'].max().strftime('%d/%m/%Y')}",
        'UFs com Casos': df['SG_UF_NOT'].nunique(),
        'Média de Idade': df['NU_IDADE_N'].mean(),
        'Casos Hospitalizados': df['HOSPITALIZ'].value_counts().get(1, 0),
        'Óbitos': df['EVOLUCAO'].value_counts().get(5, 0) if 'EVOLUCAO' in df.columns else 0
    }
    
    print("\n" + "="*70)
    print("RESUMO ESTATÍSTICO")
    print("="*70)
    for key, value in resumo.items():
        print(f"{key}: {value:,}" if isinstance(value, (int, float)) else f"{key}: {value}")
    
    # Salvar resumo em arquivo
    with open(output_dir / 'resumo_estatistico.txt', 'w', encoding='utf-8') as f:
        f.write("RESUMO ESTATÍSTICO DOS DADOS DE DENGUE - 2025\n")
        f.write("="*50 + "\n")
        for key, value in resumo.items():
            f.write(f"{key}: {value:,}\n" if isinstance(value, (int, float)) else f"{key}: {value}\n")
    
    print(f"\n✅ Visualizações salvas em: {output_dir}")
    print("✅ Gráficos criados:")
    print("  - distribuicao_por_uf.png")
    print("  - evolucao_temporal.png") 
    print("  - distribuicao_idade.png")
    print("  - distribuicao_sexo.png")
    print("  - sintomas.png")
    print("  - gravidade.png")
    print("  - correlacao_sintomas.png")
    print("  - resumo_estatistico.txt")

if __name__ == "__main__":
    create_visualizations()
