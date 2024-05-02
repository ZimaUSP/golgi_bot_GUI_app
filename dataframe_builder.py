import pandas as pd
from config import *

#df = pd.read_excel("Golgi_v0.1\dados\Cadastro dos comprimidos unitarizados.xls")
#df = df.set_index('id')
#df.to_csv('Golgi_v0.1\dados\drug_data.csv')
if in_linux:
    df = pd.read_csv("Golgi_v0.1/dados/drug_data.csv")
else:
    df = pd.read_csv("Golgi_v0.1\dados\drug_data.csv")
df = df.set_index('id')

print(df)

del(df["photo_path"])

print(df)
if in_linux:
    df.to_csv('Golgi_v0.1/dados/drug_data.csv')
else:
    df.to_csv('Golgi_v0.1\dados\drug_data.csv')

