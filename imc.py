# Importação da biblioteca 'pandas'
import pandas as pd

# Leitura do arquivo .csv
df = pd.read_csv('DATASET.CSV', sep=';', encoding='utf-8')

# Removendo linhas com valores vazios
df = df.dropna()

# Convertendo de String para float, para usar no calculo do IMC
df['Peso (kg)'] = df['Peso (kg)'].str.replace(',', '.').astype(float)
df['Altura (m)'] = df['Altura (m)'].str.replace(',', '.').astype(float)

# Invertendo os valores da linha 66, colunas peso e altura
auxiliar1 = df['Altura (m)'][66]
auxiliar2 = df['Peso (kg)'][66]

df['Altura (m)'][66] = auxiliar2
df['Peso (kg)'][66] = auxiliar1

# Função para o cálculo do IMC
df['IMC'] = df[['Peso (kg)', 'Altura (m)']].apply(lambda x: round(x['Peso (kg)']/x['Altura (m)']**2, 2), axis=1)

# Juntando as colunas 'Primeiro nome' e 'Sobrenomes' em uma única chamada 'Nome completo'
df['Nome completo'] = df.apply(lambda x: x['Primeiro Nome'] + ' ' +  x['Sobrenomes'], axis = 1)

# Tratando nomes escritos de forma errada
if 'rrrrrr' in df['Nome completo'][82]:
  df['Nome completo'] = df['Nome completo'].str.replace('rrrrrr', "rr")

if 'Sregio' in df['Nome completo'][52]:
  df['Nome completo'] = df['Nome completo'].str.replace("Sregio", "sergio")

# Nomes em maiúsculo
df['Nome completo'] = df['Nome completo'].str.upper()

# Quebrando os nomes em pedaços e juntado para remover os espaços em excesso
df['Nome completo'] = df['Nome completo'].str.split()
df['Nome completo'] = df['Nome completo'].str.join(" ")
 
# Juntando nome e IMC 
df_final = df[['Nome completo', 'IMC']]

# Imprimindo no terminal
print(df_final.to_string(header=False, index=False).replace('.',','))

# Gerando o arquivo .txt
df_final.to_csv('lucasFreireMota.txt', header=False, index=False, sep=" ", float_format='%.2f')

recriado = []

# Abrindo o arquivo txt e pegando as informações
with open("lucasFreireMota.txt", "r", encoding="utf-8") as arquivo:
  linhas = arquivo.readlines()
  for linha in linhas:
    recriado.append(linha.replace('"','').replace('.',','))        
arquivo.close()

# Adicionando as informações ao txt, com virgula ao inves de ponto, como separador e sem aspas nos nomes
with open("lucasFreireMota.txt", "w", encoding="utf-8") as arquivo:
  for linha in recriado:
    arquivo.write(linha)
arquivo.close()