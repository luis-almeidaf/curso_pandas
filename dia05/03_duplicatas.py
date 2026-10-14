# %%
import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ["leo", 'luis', 'luis', 'lara'],
    "sobrenome": ["calvo", "faria", "faria", 'ataide']
})

df

# %%

# por padrão mantém a primeira ocorrência encontrada
# se passar o parametro keep='last' fica o ultimo no df
df.drop_duplicates()

# %%

df2 = pd.DataFrame({
    "nome": ["leo", 'luis', 'luis', 'lara'],
    "sobrenome": ["calvo", "faria", "faria", 'ataide'],
    "salario": [1234, 3245, 2344, 2356]
})

df2.drop_duplicates(keep="last", subset=["nome", "sobrenome"])

# %%
#pegar a primeira transação diaria de cada usuaria

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao")

#%%
# primeira e ultima transcoes do dia

first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"])

pd.concat([last, first])
