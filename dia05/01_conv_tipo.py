# %%

import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
#converte para float

df["qtdePontos"] = df["qtdePontos"].replace({25086: 0})
df["qtdePontos"]
# %%

df["DtCriacao"].replace({"2025-11-13 12:03:56.114": "2004:02-01 09:00:00.000"})

#%%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])

# %%
df["DtCriacao"].dt.year
