# Modelo SARIMA (Seasonal Autoregressive Integrated Moving Average)

O modelo SARIMA (Seasonal Autoregressive Integrated Moving Average) é uma extensão do modelo ARIMA que suporta dados de séries temporais com um componente sazonal. É amplamente utilizado para previsão em séries temporais univariadas que exibem padrões sazonais.

## Componentes do Modelo

O SARIMA é denotado como $SARIMA(p, d, q)(P, D, Q)_s$, onde os parâmetros são divididos em partes não sazonais e sazonais.

### Parte Não Sazonal $(p, d, q)$
- **p (Autoregressive - AR):** O número de defasagens (lags) da própria série incluídas no modelo. Refere-se à dependência linear entre uma observação e suas observações anteriores.
- **d (Integrated - I):** O número de vezes que a série bruta foi diferenciada para torná-la estacionária. A diferenciação remove tendências.
- **q (Moving Average - MA):** O tamanho da janela de média móvel. Refere-se à dependência linear entre uma observação e os erros residuais de um modelo de média móvel aplicado a observações defasadas.

### Parte Sazonal $(P, D, Q)_s$
- **P (Seasonal Autoregressive - SAR):** O número de defasagens sazonais. Semelhante ao AR, mas para a componente sazonal.
- **D (Seasonal Integrated - SI):** O número de diferenciações sazonais. Remove a sazonalidade da série.
- **Q (Seasonal Moving Average - SMA):** O número de defasagens de erro sazonal. Semelhante ao MA, mas para a componente sazonal.
- **s (Sazonalidade):** O comprimento do ciclo sazonal (ex: 12 para dados mensais com ciclo anual, 7 para dados diários com ciclo semanal).

## Funcionamento

O modelo combina esses componentes para capturar a autocorrelação nos dados.
1.  **Diferenciação:** Primeiro, a série é diferenciada (se necessário) para remover tendências e sazonalidade, tornando-a estacionária (média e variância constantes ao longo do tempo).
2.  **Autoregressão e Média Móvel:** Em seguida, os componentes AR e MA modelam a relação entre as observações atuais, passadas e os erros passados.
3.  **Sazonalidade:** Os componentes sazonais (SAR, SI, SMA) tratam especificamente dos padrões que se repetem em intervalos fixos ($s$).

## Vantagens e Desvantagens

### Vantagens
- **Capacidade de Modelar Sazonalidade:** Excelente para dados com padrões sazonais claros e fortes.
- **Flexibilidade:** Pode modelar uma ampla variedade de padrões de séries temporais.
- **Bem Fundamentado:** Baseado em teoria estatística sólida.

### Desvantagens
- **Complexidade de Ajuste:** Requer a determinação de muitos parâmetros ($p, d, q, P, D, Q, s$), o que pode ser difícil e demorado.
- **Suposição de Linearidade:** Assume relações lineares, o que pode não ser adequado para todos os dados.
- **Dados Univariados:** Tradicionalmente focado em uma única variável (embora o SARIMAX permita variáveis exógenas).
- **Requer Estacionariedade:** A série deve ser transformada para ser estacionária, o que nem sempre é trivial.

## Aplicações

- Previsão de vendas mensais.
- Previsão de demanda de energia elétrica.
- Previsão de tráfego de passageiros em companhias aéreas.
- Previsão de casos de doenças sazonais (como Dengue).

## Exemplo de Implementação em Python (statsmodels)

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Definindo o modelo
# order=(p, d, q), seasonal_order=(P, D, Q, s)
model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))

# Ajustando o modelo
model_fit = model.fit(disp=False)

# Fazendo previsões
predictions = model_fit.predict(start=len(data), end=len(data)+10)
```
