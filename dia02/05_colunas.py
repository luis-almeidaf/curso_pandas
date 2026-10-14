# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df

# %%
df.shape

# %%

df.info(memory_usage='deep')

# %%
df.dtypes

#%%
renamed_columns = {"pontos": "QtdPontos", "DescSistemaOrigem": "SistemaOrigem"}

df = df.rename(columns=renamed_columns)
#para alterar o nome de uma coluna permanentemente
# é preciso reatribuir o dataframe com a chamada do rename

df.columns

# %%
# outra forma de renomar
# sem precisar reatribuir o df
renamed_columns2 = {"DtCriacao": "DataCriacao"}
df.rename(columns=renamed_columns2, inplace=True)

df

# %%

df["IdCliente"]  #retorna a série, ou seja a coluna

# %%
#passando uma lista como argumento é possivel buscar várias colunas
colunas = ["IdCliente", "DataCriacao", "SistemaOrigem"]
df[colunas]  # retorna um df

# %%
df[["IdCliente"]]  #retorna um df com uma coluna só

# %%
#Comparação com sql
# SELECT * FROM df

df

# %%
# SELECT idCliente FROM df

df[["IdCliente"]]

# %%
# SELECT IdCliente, QtdPontos FROM df LIMIT 5

df[["IdCliente", "QtdPontos"]].head(5)

# %%
# Reordenando colunas

# SELECT IdCliente, IdTransacao, QtdPontos
# FROM df
# LIMIT 5

#forma 1
df[["IdCliente", "IdTransacao", "QtdPontos"]].head(5)
# isso já reorderna o retorno

# %%
# forma 2
# Pegue as colunas e transforme em lista
# ordene por ordem alfabética
# reatribua as colunas ordenadas ao dataframe
colunas = df.columns.to_list()
colunas.sort()

df = df[colunas]
df
