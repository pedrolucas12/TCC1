import os
import pandas as pd
import requests
import time
import re
import glob

# Configuration
DATA_RAW = "data/raw"
DATA_PROCESSED = "data_processed"
os.makedirs(DATA_RAW, exist_ok=True)
os.makedirs(DATA_PROCESSED, exist_ok=True)

INMET_DIR = "dadosINMET"
TARGET_YEARS = [2022, 2023, 2024]
STATION_CODE = "A001" # Brasília
SINAN_GEOCODE = 5300108 # Brasília
SINAN_API_URL = "https://info.dengue.mat.br/api/alertcity"

def find_inmet_files():
    print(">>> [INMET] Searching for local files...")
    found_files = []
    
    # Recursive search for CSVs
    for root, dirs, files in os.walk(INMET_DIR):
        for file in files:
            if file.lower().endswith(".csv") and STATION_CODE in file.upper():
                # Check year in filename
                for year in TARGET_YEARS:
                    if str(year) in file:
                        full_path = os.path.join(root, file)
                        print(f"    Found: {file}")
                        found_files.append(full_path)
                        break
    
    if not found_files:
        print("❌ [INMET] No files found! Please check 'dadosINMET' folder.")
    
    return sorted(list(set(found_files)))

def fetch_sinan_data():
    print(">>> [SINAN] Fetching data from InfoDengue API...")
    all_data = []
    
    for year in TARGET_YEARS:
        print(f"    Fetching {year}...")
        params = {
            "geocode": SINAN_GEOCODE,
            "disease": "dengue",
            "format": "json",
            "ew_start": 1,
            "ew_end": 53,
            "ey_start": year,
            "ey_end": year
        }
        
        try:
            response = requests.get(SINAN_API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data:
                df = pd.DataFrame(data)
                all_data.append(df)
            else:
                print(f"    ⚠️ No data for {year}")
        
        except Exception as e:
            print(f"    ❌ Error fetching {year}: {e}")
            
        time.sleep(1)

    if all_data:
        full_df = pd.concat(all_data, ignore_index=True)
        output_path = os.path.join(DATA_RAW, "sinan_raw.csv")
        full_df.to_csv(output_path, index=False)
        print(f"    ✔ SINAN raw data saved to {output_path}")
        return output_path
    else:
        print("❌ [SINAN] Failed to fetch data.")
        return None

def run_download():
    print("--- STEP 1: DOWNLOAD & LOCATE DATA ---")
    
    # 1. Locate INMET
    inmet_files = find_inmet_files()
    
    # 2. Fetch SINAN
    sinan_file = fetch_sinan_data()
    
    return inmet_files, sinan_file

if __name__ == "__main__":
    run_download()

