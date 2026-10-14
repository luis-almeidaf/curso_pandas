# %%

import pandas as pd

idades = [12, 23, 24, 56, 123]
nomes = ["Luis", "Fernando", "Lucas", "Giulia", "Luis"]

series_idades = pd.Series(idades, name="teste")
series_nomes = pd.Series(nomes)

series_idades

# %%

df = pd.DataFrame()

df["idades"] = series_idades
df["nomes"] = series_nomes

# %%

df.iloc[1]["nomes"]
# o iloc retorna a serie na posição 1 do df
# e o ["nomes"] pega o valor dentro da coluna "nomes" da serie

# %%
df.loc[1]["nomes"]

#%%
df["nomes"][1]

# %%
df.iloc[1]["idades"]

# %%
df.loc[1]["idades"]

#%%
df["idades"][1]
