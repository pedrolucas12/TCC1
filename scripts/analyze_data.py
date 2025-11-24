import pandas as pd
import numpy as np
import os
from statsmodels.tsa.stattools import grangercausalitytests
import warnings

warnings.filterwarnings("ignore")

INPUT_FILE = "data_processed/dataset_unificado.csv"
OUTPUT_CSV = "data_processed/TABELA_CORRELACAO_SINAN_INMET_ULTIMOS3ANOS.csv"
OUTPUT_MD = "data_processed/TABELA_CORRELACAO_SINAN_INMET_ULTIMOS3ANOS.md"

def analyze_correlations():
    print("--- STEP 3: STATISTICAL ANALYSIS ---")
    
    df = pd.read_csv(INPUT_FILE)
    df = df.sort_values('data')
    
    variables = {
        'chuva': 'Chuva',
        'umidade': 'Umidade',
        'temperatura_media': 'Temperatura Média',
        'pressao': 'Pressão'
    }
    
    results = []
    
    for var_col, var_name in variables.items():
        if var_col not in df.columns: continue
        
        print(f"    Analyzing {var_name}...")
        
        # 1. Correlations
        pearson = df['casos_dengue'].corr(df[var_col], method='pearson')
        spearman = df['casos_dengue'].corr(df[var_col], method='spearman')
        
        row = {
            'Variável': var_name,
            'Pearson': round(pearson, 4),
            'Spearman': round(spearman, 4)
        }
        
        # 2. Granger Causality (Climate -> Dengue)
        # Data: [Target, Predictor]
        data_gc = df[['casos_dengue', var_col]].dropna()
        
        max_lag = 4
        try:
            gc_res = grangercausalitytests(data_gc, maxlag=max_lag, verbose=False)
            
            for lag in range(1, max_lag + 1):
                # F-test p-value
                p_val = gc_res[lag][0]['ssr_ftest'][1]
                sig = "SIM" if p_val < 0.05 else "NÃO"
                
                row[f'Granger Lag {lag} (p-value)'] = round(p_val, 4)
                row[f'Sig Lag {lag}'] = sig
                
        except Exception as e:
            print(f"    ⚠️ Granger failed for {var_name}: {e}")
            
        results.append(row)
        
    # Create DF
    res_df = pd.read_json(pd.DataFrame(results).to_json(orient='records'), orient='records') # Hack to normalize order if needed, but Dict preserves insertion in Python 3.7+
    res_df = pd.DataFrame(results)
    
    # Save CSV
    res_df.to_csv(OUTPUT_CSV, index=False)
    print(f"✔ Table saved to {OUTPUT_CSV}")
    
    # Save Markdown
    md_content = res_df.to_markdown(index=False)
    with open(OUTPUT_MD, 'w') as f:
        f.write("# Tabela de Correlação e Causalidade (2022-2024)\n\n")
        f.write(md_content)
    print(f"✔ Markdown saved to {OUTPUT_MD}")
    
    return res_df

if __name__ == "__main__":
    analyze_correlations()

