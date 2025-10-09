#!/usr/bin/env python3
"""
Script para download de dados SINAN de dengue do OpenDataSUS

Autor: Filippo Ferrari
Projeto: TCC - Previsão de Surtos de Dengue
Data: Outubro 2025
"""

import requests
import zipfile
import io
import json
import pandas as pd
import os
from pathlib import Path
from datetime import datetime


def download_sinan_dengue(year, output_dir="../../data/raw/sinan"):
    """
    Baixa dados SINAN de dengue do OpenDataSUS
    
    Args:
        year (int): Dois dígitos do ano (ex: 24 para 2024)
        output_dir (str): Diretório para salvar os dados
    
    Returns:
        pd.DataFrame: DataFrame com os dados de dengue
    """
    # Criar diretório se não existir
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # URL do S3 do OpenDataSUS
    url = f"https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/json/DENGBR{year:02d}.json.zip"
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Baixando dados de 20{year:02d}...")
    print(f"URL: {url}")
    
    try:
        # Download do arquivo
        response = requests.get(url, timeout=300)
        response.raise_for_status()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Download concluído. Extraindo...")
        
        # Extrair ZIP
        z = zipfile.ZipFile(io.BytesIO(response.content))
        
        # Encontrar arquivo JSON dentro do ZIP
        json_files = [name for name in z.namelist() if name.endswith('.json')]
        
        if not json_files:
            raise ValueError("Nenhum arquivo JSON encontrado no ZIP")
        
        json_file = json_files[0]
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Arquivo encontrado: {json_file}")
        
        # Ler JSON
        with z.open(json_file) as f:
            data = json.load(f)
        
        # Converter para DataFrame
        df = pd.json_normalize(data)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Total de registros: {len(df):,}")
        
        # Salvar como Parquet (mais eficiente que CSV)
        output_file = output_path / f"dengue_20{year:02d}.parquet"
        df.to_parquet(output_file, engine='pyarrow', compression='snappy')
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Salvo em: {output_file}")
        
        # Também salvar metadados
        metadata = {
            'year': f"20{year:02d}",
            'download_date': datetime.now().isoformat(),
            'url': url,
            'records': len(df),
            'columns': list(df.columns),
            'file_size_mb': os.path.getsize(output_file) / (1024 * 1024)
        }
        
        metadata_file = output_path / f"dengue_20{year:02d}_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Metadados salvos em: {metadata_file}")
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha no download: {e}")
        raise
    except Exception as e:
        print(f"[ERRO] {e}")
        raise


def download_multiple_years(start_year, end_year, output_dir="../../data/raw/sinan"):
    """
    Baixa dados de múltiplos anos
    
    Args:
        start_year (int): Ano inicial (dois dígitos)
        end_year (int): Ano final (dois dígitos)
        output_dir (str): Diretório para salvar
    """
    print(f"\n{'='*60}")
    print(f"Download de dados SINAN - Dengue")
    print(f"Período: 20{start_year:02d} a 20{end_year:02d}")
    print(f"{'='*60}\n")
    
    results = {}
    
    for year in range(start_year, end_year + 1):
        try:
            df = download_sinan_dengue(year, output_dir)
            results[f"20{year:02d}"] = {
                'success': True,
                'records': len(df)
            }
        except Exception as e:
            results[f"20{year:02d}"] = {
                'success': False,
                'error': str(e)
            }
        
        print()  # Linha em branco entre downloads
    
    # Resumo
    print(f"\n{'='*60}")
    print("RESUMO DO DOWNLOAD")
    print(f"{'='*60}")
    
    for year, result in results.items():
        if result['success']:
            print(f"✅ {year}: {result['records']:,} registros")
        else:
            print(f"❌ {year}: FALHOU - {result['error']}")
    
    print(f"{'='*60}\n")


def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Download de dados SINAN de dengue do OpenDataSUS'
    )
    parser.add_argument(
        '--year',
        type=int,
        help='Ano para download (dois dígitos, ex: 24 para 2024)'
    )
    parser.add_argument(
        '--start-year',
        type=int,
        help='Ano inicial para download em lote'
    )
    parser.add_argument(
        '--end-year',
        type=int,
        help='Ano final para download em lote'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='../../data/raw/sinan',
        help='Diretório de saída (padrão: ../../data/raw/sinan)'
    )
    
    args = parser.parse_args()
    
    if args.year:
        # Download de um ano específico
        download_sinan_dengue(args.year, args.output_dir)
    elif args.start_year and args.end_year:
        # Download de múltiplos anos
        download_multiple_years(args.start_year, args.end_year, args.output_dir)
    else:
        # Download padrão: últimos 5 anos
        current_year = datetime.now().year % 100
        download_multiple_years(current_year - 4, current_year, args.output_dir)


if __name__ == "__main__":
    main()

