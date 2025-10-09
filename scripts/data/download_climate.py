#!/usr/bin/env python3
"""
Script para download de dados climáticos (NASA POWER)

Este script faz download de dados meteorológicos usando a API NASA POWER.
Para CHIRPS e ERA5, ver notebooks específicos devido à complexidade.

Autor: Filippo Ferrari
Projeto: TCC - Previsão de Surtos de Dengue
Data: Outubro 2025
"""

import requests
import pandas as pd
import json
from pathlib import Path
from datetime import datetime
import time


def get_nasa_power(lat, lon, start_date, end_date, parameters=None):
    """
    Baixa dados NASA POWER para uma coordenada
    
    Args:
        lat (float): Latitude
        lon (float): Longitude
        start_date (str): Data inicial (formato YYYYMMDD)
        end_date (str): Data final (formato YYYYMMDD)
        parameters (list): Lista de parâmetros (padrão: temperatura, precipitação, umidade)
    
    Returns:
        pd.DataFrame: DataFrame com os dados climáticos
    """
    if parameters is None:
        parameters = ["T2M", "PRECTOTCORR", "RH2M"]  # Temp, Precip, Umidade
    
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    params = {
        "parameters": ",".join(parameters),
        "community": "AG",  # Agricultural community
        "longitude": lon,
        "latitude": lat,
        "start": start_date,
        "end": end_date,
        "format": "JSON"
    }
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Baixando dados para ({lat:.4f}, {lon:.4f})...")
    
    try:
        response = requests.get(url, params=params, timeout=120)
        response.raise_for_status()
        
        data = response.json()
        
        # Extrair parâmetros
        param_data = data['properties']['parameter']
        
        # Converter para DataFrame
        df = pd.DataFrame(param_data)
        df.index = pd.to_datetime(df.index, format='%Y%m%d')
        df.index.name = 'date'
        
        # Adicionar coordenadas
        df['lat'] = lat
        df['lon'] = lon
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ {len(df)} dias baixados")
        
        return df
    
    except Exception as e:
        print(f"[ERRO] Falha no download: {e}")
        raise


def download_for_municipalities(municipios_file, start_date, end_date, output_dir="../../data/raw/climate"):
    """
    Baixa dados climáticos para múltiplos municípios
    
    Args:
        municipios_file (str): Arquivo CSV com colunas: ibge_municipio, lat, lon
        start_date (str): Data inicial (YYYYMMDD)
        end_date (str): Data final (YYYYMMDD)
        output_dir (str): Diretório de saída
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Ler municípios
    print(f"\n{'='*60}")
    print("Download de Dados Climáticos - NASA POWER")
    print(f"{'='*60}\n")
    
    municipios = pd.read_csv(municipios_file)
    print(f"Total de municípios: {len(municipios)}")
    print(f"Período: {start_date} a {end_date}\n")
    
    all_data = []
    errors = []
    
    for idx, row in municipios.iterrows():
        ibge = row['ibge_municipio']
        lat = row['lat']
        lon = row['lon']
        
        print(f"[{idx+1}/{len(municipios)}] Município {ibge}...", end=" ")
        
        try:
            df = get_nasa_power(lat, lon, start_date, end_date)
            df['ibge_municipio'] = ibge
            all_data.append(df)
            
            # Pausa para não sobrecarregar a API
            time.sleep(0.5)
            
        except Exception as e:
            errors.append({'ibge': ibge, 'error': str(e)})
            print(f"❌ ERRO: {e}")
            continue
    
    # Concatenar todos os dados
    if all_data:
        df_final = pd.concat(all_data, ignore_index=False)
        
        # Salvar como Parquet
        output_file = output_path / f"nasa_power_{start_date}_{end_date}.parquet"
        df_final.to_parquet(output_file, engine='pyarrow', compression='snappy')
        
        print(f"\n{'='*60}")
        print(f"✅ Dados salvos em: {output_file}")
        print(f"Total de registros: {len(df_final):,}")
        print(f"Municípios com sucesso: {len(all_data)}/{len(municipios)}")
        
        if errors:
            print(f"Municípios com erro: {len(errors)}")
            error_file = output_path / f"nasa_power_errors_{start_date}_{end_date}.json"
            with open(error_file, 'w') as f:
                json.dump(errors, f, indent=2)
            print(f"Log de erros: {error_file}")
        
        print(f"{'='*60}\n")
    
    else:
        print("\n❌ Nenhum dado foi baixado com sucesso.")


def download_single_location(lat, lon, start_date, end_date, output_dir="../../data/raw/climate"):
    """
    Baixa dados para uma única localização (útil para testes)
    
    Args:
        lat (float): Latitude
        lon (float): Longitude
        start_date (str): Data inicial (YYYYMMDD)
        end_date (str): Data final (YYYYMMDD)
        output_dir (str): Diretório de saída
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    df = get_nasa_power(lat, lon, start_date, end_date)
    
    # Salvar
    output_file = output_path / f"nasa_power_{lat}_{lon}_{start_date}_{end_date}.parquet"
    df.to_parquet(output_file, engine='pyarrow')
    
    print(f"\n✅ Dados salvos em: {output_file}")
    print(f"Resumo estatístico:")
    print(df.describe())


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Download de dados climáticos via NASA POWER API'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comando')
    
    # Comando: single (uma localização)
    single_parser = subparsers.add_parser('single', help='Download para uma localização')
    single_parser.add_argument('--lat', type=float, required=True, help='Latitude')
    single_parser.add_argument('--lon', type=float, required=True, help='Longitude')
    single_parser.add_argument('--start-date', type=str, required=True, help='Data inicial (YYYYMMDD)')
    single_parser.add_argument('--end-date', type=str, required=True, help='Data final (YYYYMMDD)')
    single_parser.add_argument('--output-dir', type=str, default='../../data/raw/climate')
    
    # Comando: batch (múltiplos municípios)
    batch_parser = subparsers.add_parser('batch', help='Download para múltiplos municípios')
    batch_parser.add_argument('--municipios-file', type=str, required=True, 
                             help='Arquivo CSV com colunas: ibge_municipio, lat, lon')
    batch_parser.add_argument('--start-date', type=str, required=True, help='Data inicial (YYYYMMDD)')
    batch_parser.add_argument('--end-date', type=str, required=True, help='Data final (YYYYMMDD)')
    batch_parser.add_argument('--output-dir', type=str, default='../../data/raw/climate')
    
    args = parser.parse_args()
    
    if args.command == 'single':
        download_single_location(
            args.lat, args.lon, 
            args.start_date, args.end_date, 
            args.output_dir
        )
    elif args.command == 'batch':
        download_for_municipalities(
            args.municipios_file,
            args.start_date, args.end_date,
            args.output_dir
        )
    else:
        # Exemplo de uso (Brasília)
        print("Exemplo de uso:")
        print("\n# Para uma localização (Brasília):")
        print("python download_climate.py single --lat -15.8 --lon -47.9 --start-date 20200101 --end-date 20241231")
        print("\n# Para múltiplos municípios:")
        print("python download_climate.py batch --municipios-file municipios_coords.csv --start-date 20200101 --end-date 20241231")


if __name__ == "__main__":
    main()

