import pandas as pd

df = pd.read_csv('DATASET.CSV', delimiter=';')

df['Peso (kg)'] = df['Peso (kg)'].str.replace(',', '.').astype(float)
df['Altura (m)'] = df['Altura (m)'].str.replace(',', '.').astype(float)
df['Primeiro Nome'] = df['Primeiro Nome'].str.capitalize()

df['IMC'] = df[['Peso (kg)', 'Altura (m)']].apply(lambda x: round(x['Peso (kg)']/x['Altura (m)']**2,2), axis = 1)
df['Nome completo'] = df.apply(lambda x: x['Primeiro Nome'] + ' ' +  x['Sobrenomes'], axis = 1)
df['Nome completo'] = df['Nome completo'].str.upper()
df_final = df[['Nome completo', 'IMC']]


df_final.to_csv('LUCASFREIREMOTA.txt', index=False)