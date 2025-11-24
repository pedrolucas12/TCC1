import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from statsmodels.tsa.seasonal import seasonal_decompose

INPUT_FILE = "data_processed/dataset_unificado.csv"
OUTPUT_DIR = "docs/template/extracted/figuras" # Official LaTeX dir
ALT_OUTPUT_DIR = "docs/figuras" # User requested dir
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ALT_OUTPUT_DIR, exist_ok=True)

def save_plot(fig, name):
    path1 = os.path.join(OUTPUT_DIR, name)
    path2 = os.path.join(ALT_OUTPUT_DIR, name)
    fig.savefig(path1, dpi=300, bbox_inches='tight')
    fig.savefig(path2, dpi=300, bbox_inches='tight')
    print(f"    Saved {name}")

def visualize_data():
    print("--- STEP 4: VISUALIZATION ---")
    
    df = pd.read_csv(INPUT_FILE)
    df['data'] = pd.to_datetime(df['data'])
    df = df.sort_values('data')
    
    sns.set_theme(style="whitegrid")
    
    # 1. Série Temporal (Casos vs Chuva)
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    color = 'tab:red'
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Casos de Dengue', color=color, fontsize=12)
    ax1.plot(df['data'], df['casos_dengue'], color=color, linewidth=2, label='Casos')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(False)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Precipitação (mm)', color=color, fontsize=12)
    ax2.bar(df['data'], df['chuva'], color=color, alpha=0.3, width=5, label='Chuva')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.grid(False)
    
    plt.title('Evolução Temporal: Dengue vs Chuva no DF (2022-2024)', fontsize=14)
    save_plot(fig, "evolucao_temporal_combinada.png")
    plt.close()
    
    # 2. Heatmap
    cols = ['casos_dengue', 'chuva', 'umidade', 'temperatura_media', 'pressao']
    labels = ['Casos', 'Chuva', 'Umidade', 'Temp. Média', 'Pressão']
    corr = df[cols].corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", 
                xticklabels=labels, yticklabels=labels)
    plt.title('Matriz de Correlação (Pearson)', fontsize=14)
    save_plot(plt.gcf(), "heatmap_correlacao_oficial.png")
    plt.close()
    
    # 3. STL Decomposition (Casos)
    # Need index as datetime
    df_stl = df.set_index('data')
    # Period = 52 weeks
    res = seasonal_decompose(df_stl['casos_dengue'], model='additive', period=52)
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
    res.observed.plot(ax=ax1, color='black')
    ax1.set_ylabel('Observado')
    ax1.set_title('Decomposição STL: Casos de Dengue')
    
    res.trend.plot(ax=ax2, color='blue')
    ax2.set_ylabel('Tendência')
    
    res.seasonal.plot(ax=ax3, color='green')
    ax3.set_ylabel('Sazonalidade')
    
    res.resid.plot(ax=ax4, color='gray', linestyle='none', marker='.')
    ax4.set_ylabel('Resíduo')
    ax4.set_xlabel('Data')
    
    save_plot(fig, "decomposicao_stl_casos.png")
    plt.close()
    
    # 4. Cross Correlation (Lags Plot)
    fig, ax = plt.subplots(figsize=(10, 5))
    lags = range(0, 13)
    rhos = [df['casos_dengue'].corr(df['chuva'].shift(lag)) for lag in lags]
    
    ax.stem(lags, rhos)
    ax.set_xlabel('Defasagem (Semanas)')
    ax.set_ylabel('Correlação (Pearson)')
    ax.set_title('Correlação Cruzada: Chuva (Defasada) vs Casos', fontsize=14)
    save_plot(fig, "analise_lags_crosscorr.png")
    plt.close()

    print("✔ Figures generated.")

if __name__ == "__main__":
    visualize_data()

