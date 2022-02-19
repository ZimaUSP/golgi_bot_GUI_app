import pandas as pd

#df = pd.read_excel("Golgi_v0.1\dados\Cadastro dos comprimidos unitarizados.xls")
#df = df.set_index('id')
#df.to_csv('Golgi_v0.1\dados\drug_data.csv')
df = pd.read_csv("Golgi_v0.1\dados\drug_data.csv")
df = df.set_index('id')

print(df)

del(df["photo_path"])

print(df)

df.to_csv('Golgi_v0.1\dados\drug_data.csv')

