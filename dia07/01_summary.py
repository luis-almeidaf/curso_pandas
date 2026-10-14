# %%

import pandas as pd

idades = [21, 24, 6, 42, 6, 4, 23]
idades = pd.Series(idades)

idades

idades.sum()
idades.max()
idades.min()
idades.mean()
idades.describe()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

#%%
redes_sociais = [
    "flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"
]
clientes[redes_sociais].sum()

# %%
# para obter todas as colunas numéricas no caso
num_columns = clientes.dtypes[~(clientes.dtypes == "str")].index.tolist()

clientes[num_columns].describe()
