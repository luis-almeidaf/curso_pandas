# %%

import numpy as np
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

#%%
df["qtdePontos"] = df["qtdePontos"] + 100
# isso é uma operação scalar, você está adiocionando esse valor diretamente
# a cada item nesse coluna/serie

#%%
#mais rapido que fazer um for

nova_coluna = []

for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)

coluna_atualizada = pd.Series(nova_coluna)
df["pontos_100_com_for"] = coluna_atualizada

df

#%%
# isso soma linha por linha
# desde que as séries tenham o mesmo tamanho
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

#%%
df["flEmail"] * df["flTwitch"]
#para saber se tem um ou outro
#%%
#soma quantas redes sociais a pessoa tem cadastrada
df["qtdSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df[
    "flBlueSky"] + df["flInstagram"]
df

#%%

# nesse caso se algum valor for 0, indica que a pessoa não tem todas as redes conectadas
df["todasSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df[
    "flBlueSky"] * df["flInstagram"]
df["todasSocial"]

#%%
# o numpy é mais rápido que usar o apply() do pandas e passar operação matematica
df["logPontos"] = np.log(df["qtdePontos"] + 1)
df["logPontos"].describe()
