import pandas as pd
import numpy as np
import os
from scripts.download_data import find_inmet_files

DATA_RAW = "data/raw"
DATA_PROCESSED = "data_processed"
OUTPUT_FILE = os.path.join(DATA_PROCESSED, "dataset_unificado.csv")

def process_inmet(files):
    print(">>> [PROCESSING] INMET Data...")
    all_data = []
    
    for file_path in files:
        try:
            # Try reading with common settings
            df = pd.read_csv(file_path, sep=';', encoding='latin1', skiprows=8, decimal=',', na_values=['-9999', 'null'])
        except:
            # Fallback
            df = pd.read_csv(file_path, sep=',', encoding='utf-8', skiprows=8, decimal='.', na_values=['-9999'])

        # Normalize Columns
        col_map = {}
        print(f"    DEBUG: Columns in {os.path.basename(file_path)}: {list(df.columns)}")
        for col in df.columns:
            c = col.upper()
            if "DATA" in c and "UTC" not in c: col_map[col] = "date"
            elif "HORA" in c and "UTC" in c: col_map[col] = "hour"
            elif "PRECIPITA" in c: col_map[col] = "chuva"
            elif "TEMPERATURA DO AR - BULBO SECO" in c: col_map[col] = "temp"
            elif "UMIDADE RELATIVA" in c: col_map[col] = "umidade"
            elif "PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO" in c: col_map[col] = "pressao"
        
        print(f"    DEBUG: Map {col_map}")
        df = df.rename(columns=col_map)
        
        # Keep only relevant
        needed = ['date', 'chuva', 'temp', 'umidade', 'pressao']
        available = [c for c in needed if c in df.columns]
        df = df[available]
        
        # Date conversion
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
        all_data.append(df)

    full_df = pd.concat(all_data, ignore_index=True)
    full_df = full_df.dropna(subset=['date'])
    
    # Ensure numeric
    for col in ['chuva', 'temp', 'umidade', 'pressao']:
        if col in full_df.columns:
            full_df[col] = pd.to_numeric(full_df[col], errors='coerce')

    # Calculate Week Start (Sunday)
    # Monday=0, Sunday=6. 
    # If Monday(0), week_start is prev Sunday (-1 day). (0+1)%7 = 1.
    # If Sunday(6), week_start is today (0 shift). (6+1)%7 = 0.
    full_df['data'] = full_df['date'] - pd.to_timedelta((full_df['date'].dt.dayofweek + 1) % 7, unit='D')
    
    # Aggregate Weekly
    weekly = full_df.groupby('data').agg({
        'chuva': 'sum',
        'temp': 'mean',
        'umidade': 'mean',
        'pressao': 'mean'
    }).reset_index()
    
    weekly = weekly.rename(columns={'temp': 'temperatura_media'})
    print(f"    ✔ INMET processed: {len(weekly)} weeks")
    return weekly

def process_sinan():
    print(">>> [PROCESSING] SINAN Data...")
    raw_path = os.path.join(DATA_RAW, "sinan_raw.csv")
    if not os.path.exists(raw_path):
        raise FileNotFoundError("SINAN raw data not found. Run download first.")
        
    df = pd.read_csv(raw_path)
    
    # Normalize
    # InfoDengue cols: 'data_iniSE', 'SE', 'casos', ...
    rename_map = {
        'data_iniSE': 'data',
        'SE': 'semana_epidemiologica',
        'casos': 'casos_dengue',
        'casos_est': 'casos_estimados' # Sometimes useful
    }
    
    df = df.rename(columns=rename_map)
    
    # Convert Date
    # Check if ms timestamp
    if pd.api.types.is_numeric_dtype(df['data']):
         df['data'] = pd.to_datetime(df['data'], unit='ms')
    else:
         df['data'] = pd.to_datetime(df['data'])
         
    # Keep relevant
    needed = ['data', 'semana_epidemiologica', 'casos_dengue']
    df = df[needed]
    
    # Add Year
    df['ano'] = df['data'].dt.year
    
    # Sort
    df = df.sort_values('data')
    
    print(f"    ✔ SINAN processed: {len(df)} weeks")
    return df

def run_processing():
    print("--- STEP 2: PROCESSING & MERGING ---")
    
    # Get files
    inmet_files = find_inmet_files()
    
    # Process
    df_inmet = process_inmet(inmet_files)
    df_sinan = process_sinan()
    
    # Merge
    # Left join on SINAN (our target)
    print(">>> [MERGING] Datasets...")
    merged = pd.merge(df_sinan, df_inmet, on='data', how='inner') # Inner to ensure we have climate data
    
    # Final Polish
    merged = merged.round(2)
    merged = merged.sort_values('data')
    
    # Fill small gaps if any (linear interpolation for climate)
    climate_cols = ['temperatura_media', 'umidade', 'pressao']
    merged[climate_cols] = merged[climate_cols].interpolate(method='linear', limit_direction='both')
    merged['chuva'] = merged['chuva'].fillna(0) # Rain usually 0 if missing in aggregation? Or interpolate? Better 0 or keep NaN. Let's assume 0 for safety in sums, but valid check needed.
    
    # Save
    merged.to_csv(OUTPUT_FILE, index=False)
    print(f"✔ DATASET FINAL UNIFICADO GERADO: {OUTPUT_FILE}")
    print(merged.head())
    
    return merged

if __name__ == "__main__":
    run_processing()

