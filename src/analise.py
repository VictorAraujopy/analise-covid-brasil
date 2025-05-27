import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import os

# Lê o arquivo CSV com os dados de COVID
df = pd.read_csv(r'C:\Users\vicit\Desktop\analise-covid-brasil\dados\brasil_covid.csv')

# Converte a coluna 'data' para o formato de data do Pandas
df['data'] = pd.to_datetime(df['data'])

# Agrupa os dados por data e soma os casos de todos os estados
casos_por_dia = df.groupby('data')['casosNovos'].sum()
obitos_por_dia = df.groupby('data')['obitosNovos'].sum()

# Gera o gráfico de casos por dia
plt.figure(figsize=(10, 5))
casos_por_dia.plot(color='blue')
plt.title('📈 Casos diários de COVID-19 no Brasil')
plt.xlabel('Data')
plt.ylabel('Número de Casos')
plt.grid(True)
plt.tight_layout()
plt.savefig('graficos/casos_por_dia.png')  # Salva o gráfico
plt.close()  # Fecha o gráfico atual

# Gera o gráfico de óbitos por dia
plt.figure(figsize=(10, 5))
obitos_por_dia.plot(color='red')
plt.title('☠️ Óbitos diários de COVID-19 no Brasil')
plt.xlabel('Data')
plt.ylabel('Número de Óbitos')
plt.grid(True)
plt.tight_layout()
plt.savefig(r'C:\Users\vicit\Desktop\analise-covid-brasil\graficos/obitos_por_dia.png')  # Salva o gráfico
plt.close()

print("✅ Gráficos gerados com sucesso na pasta 'graficos'")
