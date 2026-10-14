#%%

import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")

filtro = (df["IdProduto"] == '5') | (df["IdProduto"] == '11')
df[filtro]

# %%

#faz a mesma coisa, que o filtro de cima, é só passar a lista
# retorna um série de bool que pode ser usado como filtro
filtro = df["IdProduto"].isin(['5', '11'])
df[filtro]

#%%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

#%%
filtro = clientes["DtCriacao"].notna()
clientes[filtro]

#%%
filtro = clientes["DtCriacao"].notnull()
clientes[filtro]

#%%
#tudo a mesma coisa, o ~ é a negação da expressão
clientes["DtCriacao"].notna()
~clientes["DtCriacao"].isna()

clientes["DtCriacao"].notnull()
~clientes["DtCriacao"].isnull()

# %%
# um filtro é uma view, é só uma vizualição dos dados filtrados
# uma nova variavel com os dados filtrados
