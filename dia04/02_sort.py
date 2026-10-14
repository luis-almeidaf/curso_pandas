#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

max_pontos = df["qtdePontos"].max()
filtro = df["qtdePontos"] == max_pontos
df[filtro]

# %%

# o sort_values, retorna um df nova, não uma view
df.sort_values(by="qtdePontos", ascending=False).head(5)

#%%
#pegando só o id do cliente, retornando a coluna
top_5 = (df.sort_values(by="qtdePontos", ascending=False).head(5)["idCliente"])
top_5

#%%
# exemplo com empate

empate = pd.DataFrame({
    "nome": ["luis", "Lucas", "jose", "hasd"],
    "idade": [23, 24, 52, 26],
    "salario": [1422, 2455, 1900, 2455]
})

# passando uma lista, você ordena pelo primeiro
# caso de empate considera o segundo item da lista
# para o ascending é a mesma coisa
empate.sort_values(by=["salario", "idade"], ascending=[False, True])
