"""
SARIMA - Seasonal AutoRegressive Integrated Moving Average
==========================================================

Modelo estatístico clássico para séries temporais com sazonalidade.

BASEADO EM: Xavier et al. (2021) - PLOS ONE
"Analysis of climate factors and dengue incidence"

O paper usa ARMAX (similar ao SARIMA com variáveis exógenas) e identifica:
- Sazonalidade anual (ciclo de 52 semanas)
- Lag de 1-2 meses (4-8 semanas) para precipitação
- Temperatura >22°C como threshold crítico

ESTRUTURA SARIMA(p,d,q)(P,D,Q)[s]:
- p: ordem AR (auto-regressivo)
- d: diferenciação (tornar série estacionária)
- q: ordem MA (média móvel)
- P,D,Q: componentes sazonais
- s: período sazonal (52 semanas para dengue)

Autor: Pedro Lucas Santana
Data: Outubro 2025
TCC: Predição de Surtos de Dengue usando Machine Learning
"""

import pandas as pd
import numpy as np
import warnings
from pathlib import Path
import json
from datetime import datetime

import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tools.eval_measures import rmse, meanabs

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

warnings.filterwarnings('ignore')

# Configuração de visualização
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (15, 8)
plt.rcParams['font.size'] = 10


class SARIMADengueModel:
    """
    Modelo SARIMA para previsão de casos de dengue usando variáveis climáticas
    
    Parâmetros baseados em Xavier et al. (2021):
    - Sazonalidade: 52 semanas (anual)
    - Variáveis exógenas: precipitação acumulada 8 semanas, temperatura, umidade
    - Lag temporal: 1-2 meses (4-8 semanas)
    """
    
    def __init__(self, order=(1,1,1), seasonal_order=(1,1,1,52), output_dir='../data/processed/models'):
        """
        Inicializa o modelo SARIMA
        
        Args:
            order (tuple): (p,d,q) - parâmetros não-sazonais
            seasonal_order (tuple): (P,D,Q,s) - parâmetros sazonais
            output_dir (str): Diretório para salvar resultados
        """
        self.order = order
        self.seasonal_order = seasonal_order
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.model = None
        self.results = None
        self.forecast_results = {}
        
    def check_stationarity(self, series, significance=0.05):
        """
        Testa estacionariedade usando Augmented Dickey-Fuller
        
        Série estacionária: média e variância constantes no tempo
        Necessário para ARIMA funcionar bem
        
        Args:
            series (pd.Series): Série temporal
            significance (float): Nível de significância
            
        Returns:
            dict: Resultados do teste ADF
        """
        result = adfuller(series.dropna(), autolag='AIC')
        
        output = {
            'test_statistic': result[0],
            'p_value': result[1],
            'n_lags': result[2],
            'n_obs': result[3],
            'critical_values': result[4],
            'is_stationary': result[1] < significance
        }
        
        print(f"\n{'='*70}")
        print("TESTE DE ESTACIONARIEDADE (Augmented Dickey-Fuller)")
        print(f"{'='*70}")
        print(f"Estatística ADF: {output['test_statistic']:.4f}")
        print(f"P-valor: {output['p_value']:.4f}")
        print(f"Número de lags: {output['n_lags']}")
        print(f"Número de observações: {output['n_obs']}")
        print("\nValores críticos:")
        for key, value in output['critical_values'].items():
            print(f"  {key}: {value:.3f}")
        
        if output['is_stationary']:
            print("\n✅ SÉRIE É ESTACIONÁRIA (p-valor < 0.05)")
        else:
            print("\n⚠️  SÉRIE NÃO É ESTACIONÁRIA - considere diferenciação (d > 0)")
        
        return output
    
    def plot_diagnostics(self, series, title="Série Temporal de Dengue"):
        """
        Plota diagnósticos da série temporal
        
        1. Série temporal original
        2. ACF (autocorrelação) - identifica padrões temporais
        3. PACF (autocorrelação parcial) - identifica ordem AR
        
        Args:
            series (pd.Series): Série temporal
            title (str): Título do gráfico
        """
        fig, axes = plt.subplots(3, 1, figsize=(15, 12))
        
        # Série original
        axes[0].plot(series)
        axes[0].set_title(f'{title} - Evolução Temporal')
        axes[0].set_xlabel('Semana Epidemiológica')
        axes[0].set_ylabel('Casos de Dengue')
        axes[0].grid(True, alpha=0.3)
        
        # Número de lags (máximo 40 ou metade do tamanho da série)
        max_lags = min(52, len(series) // 2)
        
        # ACF - Autocorrelação
        plot_acf(series.dropna(), lags=max_lags, ax=axes[1])
        axes[1].set_title('ACF - Função de Autocorrelação (identifica MA e sazonalidade)')
        
        # PACF - Autocorrelação Parcial
        plot_pacf(series.dropna(), lags=max_lags, ax=axes[2])
        axes[2].set_title('PACF - Função de Autocorrelação Parcial (identifica AR)')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / f'diagnostics_{title.lower().replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
        print(f"\n📊 Diagnósticos salvos: {self.output_dir / f'diagnostics_{title.lower().replace(' ', '_')}.png'}")
        plt.close()
        
    def prepare_data(self, df, target_col='casos_dengue', exog_cols=None, test_size=12):
        """
        Prepara dados para treinamento SARIMA
        
        Args:
            df (pd.DataFrame): DataFrame com dados
            target_col (str): Coluna target (casos de dengue)
            exog_cols (list): Colunas de variáveis exógenas (clima)
            test_size (int): Número de semanas para teste (padrão: 12 = 3 meses)
            
        Returns:
            tuple: (y_train, X_train, y_test, X_test)
        """
        print(f"\n{'='*70}")
        print("PREPARAÇÃO DOS DADOS")
        print(f"{'='*70}")
        
        # Ordenar por tempo
        df = df.sort_values(['ano', 'semana_epi']).reset_index(drop=True)
        
        # Target
        y = df[target_col]
        
        # Variáveis exógenas
        X = None
        if exog_cols:
            X = df[exog_cols]
            print(f"Variáveis exógenas: {exog_cols}")
        
        # Split temporal (NUNCA usar shuffle em séries temporais!)
        split_idx = len(y) - test_size
        
        y_train = y[:split_idx]
        y_test = y[split_idx:]
        
        X_train = X[:split_idx] if X is not None else None
        X_test = X[split_idx:] if X is not None else None
        
        print(f"\nTreino: {len(y_train)} semanas ({len(y_train)/52:.1f} anos)")
        print(f"Teste: {len(y_test)} semanas ({len(y_test)/52:.1f} anos)")
        print(f"Período treino: semana {df.loc[0, 'semana_epi']}/{df.loc[0, 'ano']} a {df.loc[split_idx-1, 'semana_epi']}/{df.loc[split_idx-1, 'ano']}")
        print(f"Período teste: semana {df.loc[split_idx, 'semana_epi']}/{df.loc[split_idx, 'ano']} a {df.loc[len(df)-1, 'semana_epi']}/{df.loc[len(df)-1, 'ano']}")
        
        return y_train, X_train, y_test, X_test
    
    def train(self, y_train, X_train=None, verbose=True):
        """
        Treina modelo SARIMA
        
        Args:
            y_train (pd.Series): Série temporal de treino
            X_train (pd.DataFrame): Variáveis exógenas (opcional)
            verbose (bool): Imprimir progresso
            
        Returns:
            statsmodels.tsa.statespace.sarimax.SARIMAXResultsWrapper: Modelo treinado
        """
        print(f"\n{'='*70}")
        print("TREINAMENTO SARIMA")
        print(f"{'='*70}")
        print(f"Ordem não-sazonal (p,d,q): {self.order}")
        print(f"Ordem sazonal (P,D,Q,s): {self.seasonal_order}")
        print(f"Variáveis exógenas: {'Sim' if X_train is not None else 'Não'}")
        
        print("\n⏳ Treinando modelo SARIMA...")
        
        try:
            self.model = SARIMAX(
                y_train,
                exog=X_train,
                order=self.order,
                seasonal_order=self.seasonal_order,
                enforce_stationarity=False,
                enforce_invertibility=False
            )
            
            self.results = self.model.fit(disp=verbose)
            
            print("\n✅ Modelo treinado com sucesso!")
            
            if verbose:
                print("\n" + "="*70)
                print("SUMÁRIO DO MODELO")
                print("="*70)
                print(self.results.summary())
            
            return self.results
            
        except Exception as e:
            print(f"\n❌ ERRO no treinamento: {e}")
            raise
    
    def evaluate(self, y_test, X_test=None, forecast_steps=None):
        """
        Avalia modelo no conjunto de teste
        
        Args:
            y_test (pd.Series): Série temporal de teste
            X_test (pd.DataFrame): Variáveis exógenas de teste
            forecast_steps (int): Número de passos à frente (padrão: len(y_test))
            
        Returns:
            dict: Métricas de avaliação
        """
        if self.results is None:
            raise ValueError("Modelo não treinado! Execute train() primeiro.")
        
        if forecast_steps is None:
            forecast_steps = len(y_test)
        
        print(f"\n{'='*70}")
        print("AVALIAÇÃO DO MODELO")
        print(f"{'='*70}")
        print(f"Passos à frente: {forecast_steps}")
        
        # Previsão
        forecast = self.results.forecast(steps=forecast_steps, exog=X_test)
        
        # Métricas
        mae = mean_absolute_error(y_test[:forecast_steps], forecast)
        rmse_val = np.sqrt(mean_squared_error(y_test[:forecast_steps], forecast))
        mape = np.mean(np.abs((y_test[:forecast_steps] - forecast) / y_test[:forecast_steps])) * 100
        r2 = r2_score(y_test[:forecast_steps], forecast)
        
        metrics = {
            'mae': mae,
            'rmse': rmse_val,
            'mape': mape,
            'r2': r2
        }
        
        print(f"\n📊 MÉTRICAS DE DESEMPENHO:")
        print(f"  MAE (Mean Absolute Error): {mae:.2f} casos")
        print(f"  RMSE (Root Mean Squared Error): {rmse_val:.2f} casos")
        print(f"  MAPE (Mean Absolute Percentage Error): {mape:.2f}%")
        print(f"  R² (Coeficiente de Determinação): {r2:.4f}")
        
        self.forecast_results = {
            'forecast': forecast,
            'actual': y_test[:forecast_steps],
            'metrics': metrics
        }
        
        return metrics
    
    def plot_forecast(self, y_train, y_test, X_test=None, title="Previsão SARIMA - Dengue"):
        """
        Plota previsões vs valores reais
        
        Args:
            y_train (pd.Series): Série de treino
            y_test (pd.Series): Série de teste
            X_test (pd.DataFrame): Variáveis exógenas de teste
            title (str): Título do gráfico
        """
        if not self.forecast_results:
            raise ValueError("Execute evaluate() primeiro!")
        
        forecast = self.forecast_results['forecast']
        
        plt.figure(figsize=(15, 6))
        
        # Treino
        plt.plot(range(len(y_train)), y_train, label='Treino (Observado)', color='blue', alpha=0.7)
        
        # Teste
        test_idx = range(len(y_train), len(y_train) + len(y_test))
        plt.plot(test_idx, y_test, label='Teste (Observado)', color='green', linewidth=2)
        
        # Previsão
        forecast_idx = range(len(y_train), len(y_train) + len(forecast))
        plt.plot(forecast_idx, forecast, label='Previsão SARIMA', color='red', linestyle='--', linewidth=2)
        
        # Intervalo de confiança (apenas se não houver variáveis exógenas)
        try:
            if X_test is not None:
                pred = self.results.get_forecast(steps=len(forecast), exog=X_test)
            else:
                pred = self.results.get_forecast(steps=len(forecast))
            ci = pred.conf_int()
            plt.fill_between(
                forecast_idx,
                ci.iloc[:, 0],
                ci.iloc[:, 1],
                color='red',
                alpha=0.2,
                label='IC 95%'
            )
        except:
            pass  # Se falhar, continua sem IC
        
        plt.axvline(x=len(y_train), color='black', linestyle=':', linewidth=2, label='Início Teste')
        plt.xlabel('Semana Epidemiológica')
        plt.ylabel('Casos de Dengue')
        plt.title(f'{title}\nMAE: {self.forecast_results["metrics"]["mae"]:.2f} | RMSE: {self.forecast_results["metrics"]["rmse"]:.2f} | R²: {self.forecast_results["metrics"]["r2"]:.4f}')
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(self.output_dir / f'forecast_{title.lower().replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
        print(f"\n📊 Gráfico de previsão salvo: {self.output_dir / f'forecast_{title.lower().replace(' ', '_')}.png'}")
        plt.close()
    
    def save_model(self, filename='sarima_model.pkl'):
        """
        Salva modelo treinado
        
        Args:
            filename (str): Nome do arquivo
        """
        if self.results is None:
            raise ValueError("Modelo não treinado!")
        
        filepath = self.output_dir / filename
        self.results.save(filepath)
        print(f"\n💾 Modelo salvo: {filepath}")
        
        # Salvar metadados
        metadata = {
            'order': self.order,
            'seasonal_order': self.seasonal_order,
            'aic': float(self.results.aic),
            'bic': float(self.results.bic),
            'metrics': {k: float(v) for k, v in self.forecast_results['metrics'].items()} if self.forecast_results else {},
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        with open(self.output_dir / f'{filename}.json', 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"📋 Metadados salvos: {self.output_dir / f'{filename}.json'}")
        
    @staticmethod
    def load_model(filepath):
        """
        Carrega modelo salvo
        
        Args:
            filepath (str): Caminho do arquivo .pkl
            
        Returns:
            SARIMAXResultsWrapper: Modelo carregado
        """
        from statsmodels.iolib.smpickle import load_pickle
        return load_pickle(filepath)


def grid_search_sarima(y_train, X_train=None, p_range=(0,3), d_range=(0,2), q_range=(0,3), 
                       P_range=(0,2), D_range=(0,2), Q_range=(0,2), s=52):
    """
    Busca em grade para encontrar melhores parâmetros SARIMA
    
    ATENÇÃO: Pode demorar muito! Use rangos pequenos.
    
    Args:
        y_train (pd.Series): Série de treino
        X_train (pd.DataFrame): Variáveis exógenas
        p_range, d_range, q_range: Rangos não-sazonais
        P_range, D_range, Q_range: Rangos sazonais
        s (int): Período sazonal
        
    Returns:
        tuple: (melhor_order, melhor_seasonal_order, melhor_aic)
    """
    print(f"\n{'='*70}")
    print("GRID SEARCH SARIMA")
    print(f"{'='*70}")
    print("⚠️  AVISO: Isso pode demorar bastante tempo!")
    print(f"Combinações a testar: ~{len(range(*p_range)) * len(range(*d_range)) * len(range(*q_range)) * len(range(*P_range)) * len(range(*D_range)) * len(range(*Q_range))}")
    
    best_aic = np.inf
    best_order = None
    best_seasonal_order = None
    results_list = []
    
    total = 0
    for p in range(*p_range):
        for d in range(*d_range):
            for q in range(*q_range):
                for P in range(*P_range):
                    for D in range(*D_range):
                        for Q in range(*Q_range):
                            try:
                                model = SARIMAX(
                                    y_train,
                                    exog=X_train,
                                    order=(p,d,q),
                                    seasonal_order=(P,D,Q,s),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False
                                )
                                
                                results = model.fit(disp=False)
                                aic = results.aic
                                
                                results_list.append({
                                    'order': (p,d,q),
                                    'seasonal_order': (P,D,Q,s),
                                    'aic': aic,
                                    'bic': results.bic
                                })
                                
                                if aic < best_aic:
                                    best_aic = aic
                                    best_order = (p,d,q)
                                    best_seasonal_order = (P,D,Q,s)
                                    print(f"✅ Novo melhor: SARIMA{best_order}x{best_seasonal_order} | AIC: {best_aic:.2f}")
                                
                                total += 1
                                
                            except Exception as e:
                                continue
    
    print(f"\n{'='*70}")
    print(f"GRID SEARCH COMPLETO - {total} modelos testados")
    print(f"{'='*70}")
    print(f"\n🏆 MELHOR MODELO:")
    print(f"  Ordem: SARIMA{best_order}x{best_seasonal_order}")
    print(f"  AIC: {best_aic:.2f}")
    
    # Top 5
    results_df = pd.DataFrame(results_list).sort_values('aic').head(5)
    print(f"\n📊 TOP 5 MODELOS:")
    print(results_df.to_string(index=False))
    
    return best_order, best_seasonal_order, best_aic


def main():
    """
    Exemplo de uso do modelo SARIMA
    
    NOTA: Como ainda não temos dados de dengue do SINAN,
    este exemplo usa dados simulados. Quando os dados reais
    estiverem disponíveis, substitua a seção de simulação.
    """
    print("="*70)
    print("MODELO SARIMA PARA PREVISÃO DE DENGUE")
    print("="*70)
    print("Baseado em: Xavier et al. (2021) - PLOS ONE")
    print("TCC: Predição de Surtos de Dengue")
    print("Autor: Pedro Lucas Santana")
    print("="*70)
    
    # Carregar dados climáticos processados
    print("\n📂 Carregando dados climáticos...")
    data_path = Path('../data/processed/inmet/inmet_weekly_lagged_2025.parquet')
    
    if not data_path.exists():
        print(f"❌ ERRO: Arquivo não encontrado: {data_path}")
        print("Execute primeiro: python scripts/data/process_inmet_bulk.py")
        return
    
    df_climate = pd.read_parquet(data_path)
    print(f"✅ Dados climáticos carregados: {df_climate.shape}")
    
    # ====================================================================
    # SIMULAÇÃO DE DADOS DE DENGUE (REMOVER QUANDO TIVER DADOS REAIS)
    # ====================================================================
    print("\n⚠️  SIMULANDO DADOS DE DENGUE (dados reais virão do SINAN)")
    
    # Agregar por semana (média de todas as estações)
    df_weekly = df_climate.groupby(['ano', 'semana_epi']).agg({
        'precip_acum_8sem': 'mean',
        'temp_favoravel': 'mean',
        'indice_risco_dengue': 'mean',
        'TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)_mean': 'mean',
        'UMIDADE RELATIVA DO AR, HORARIA (%)_mean': 'mean'
    }).reset_index()
    
    # Simular casos de dengue correlacionados com clima
    np.random.seed(42)
    baseline = 100
    temp_effect = df_weekly['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)_mean'] * 5
    precip_effect = df_weekly['precip_acum_8sem'] * 0.5
    seasonal = 50 * np.sin(2 * np.pi * df_weekly['semana_epi'] / 52)
    noise = np.random.normal(0, 20, len(df_weekly))
    
    df_weekly['casos_dengue'] = (baseline + temp_effect + precip_effect + seasonal + noise).clip(lower=0).astype(int)
    
    print(f"✅ Dados simulados: {len(df_weekly)} semanas")
    print(f"   Período: {df_weekly['ano'].min()}/{df_weekly['semana_epi'].min()} a {df_weekly['ano'].max()}/{df_weekly['semana_epi'].max()}")
    print(f"   Casos: média={df_weekly['casos_dengue'].mean():.0f}, min={df_weekly['casos_dengue'].min()}, max={df_weekly['casos_dengue'].max()}")
    
    # ====================================================================
    # ANÁLISE E MODELAGEM
    # ====================================================================
    
    # Inicializar modelo
    model = SARIMADengueModel(
        order=(1,1,1),           # (p,d,q) - parâmetros não-sazonais
        seasonal_order=(1,1,1,52) # (P,D,Q,s) - 52 semanas = sazonalidade anual
    )
    
    # Verificar estacionariedade
    model.check_stationarity(df_weekly['casos_dengue'])
    
    # Diagnósticos
    model.plot_diagnostics(df_weekly['casos_dengue'])
    
    # Preparar dados
    exog_cols = ['precip_acum_8sem', 'temp_favoravel', 'indice_risco_dengue']
    y_train, X_train, y_test, X_test = model.prepare_data(
        df_weekly,
        target_col='casos_dengue',
        exog_cols=exog_cols,
        test_size=12  # 12 semanas = ~3 meses de teste
    )
    
    # Treinar
    model.train(y_train, X_train, verbose=True)
    
    # Avaliar
    metrics = model.evaluate(y_test, X_test)
    
    # Visualizar
    model.plot_forecast(y_train, y_test, X_test)
    
    # Salvar
    model.save_model('sarima_dengue_v1.pkl')
    
    print("\n" + "="*70)
    print("✅ TREINAMENTO CONCLUÍDO COM SUCESSO!")
    print("="*70)
    print("\nPRÓXIMOS PASSOS:")
    print("1. Baixar dados reais de dengue do SINAN")
    print("2. Fazer join espacial (estações → municípios)")
    print("3. Re-treinar modelo com dados reais")
    print("4. Comparar com outros modelos (XGBoost, LSTM)")
    print("="*70)


if __name__ == '__main__':
    main()
