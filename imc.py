# Importação da lib pandas
import pandas as pd


# Leitura do arquivo .csv
df = pd.read_csv('DATASET.CSV', sep=';')

df['Peso (kg)'] = df['Peso (kg)'].str.replace(',', '.').astype(float)
df['Altura (m)'] = df['Altura (m)'].str.replace(',', '.').astype(float)
df['Primeiro Nome'] = df['Primeiro Nome'].str.capitalize()

df['IMC'] = df[['Peso (kg)', 'Altura (m)']].apply(lambda x: round(x['Peso (kg)']/x['Altura (m)']**2,2), axis = 1)

df['Nome completo'] = df.apply(lambda x: x['Primeiro Nome'] + ' ' +  x['Sobrenomes'], axis = 1)

df['Nome completo'] = df['Nome completo'].str.upper()
df['Nome completo'] = df['Nome completo'].str.split()
df['Nome completo'] = df['Nome completo'].str.join(" ")
df['Nome completo'] = df['Nome completo'].str.strip()

df_final = df[['Nome completo', 'IMC']]

print(df_final)

df_final.to_csv('lucasFreireMota.txt', header = False, index=True, sep=" ")