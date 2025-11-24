import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.download_data import run_download
from scripts.process_data import run_processing
from scripts.analyze_data import analyze_correlations
from scripts.visualize_data import visualize_data
from scripts.update_docs import update_docs

def main():
    print("==================================================")
    print("   🚀 TCC1 AUTOMATED PIPELINE STARTED")
    print("==================================================")
    
    # 1. Download
    run_download()
    
    # 2. Process
    run_processing()
    
    # 3. Analyze
    analyze_correlations()
    
    # 4. Visualize
    visualize_data()
    
    # 5. Update Docs
    update_docs()
    
    print("\n==================================================")
    print("   ✅ PIPELINE COMPLETED SUCCESSFULLY")
    print("==================================================")
    print("Check 'data_processed/' for datasets.")
    print("Check 'docs/template/extracted/figuras/' for plots.")
    print("Check 'docs/template/extracted/editaveis/' for updated LaTeX.")

if __name__ == "__main__":
    main()

