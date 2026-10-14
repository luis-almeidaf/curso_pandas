# %%
import pandas as pd

# %%

pontos = [101, 3, 5, 7, 30, 100, 50, 52, 600]

filtro = []
valores_50_mais = []

for i in pontos:
    filtro.append(i >= 50)

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%
df_teste = pd.DataFrame({
    "nome": ["teo", "nah", "luis"],
    "idade": [13, 23, 33],
    "uf": ["sp", "rj", "sp"]
})

filtro = df_teste["uf"] != "sp"
print(filtro)
# isso gera uma série de bool do mesmo length do df, validando a condição
# o que permite utilizar isso como parametro no df para filtrar

df_teste[filtro]  #retorna só as linhas que passam na condição lógica
#retorna só o que for true na série do filtro

#%%

filtro_fodase = [False, True, False]
df_teste[filtro_fodase]

#%%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

#%%
#filtros

#valores menores que 50
filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
#valores entre 50 e 100 (inclusivo)
filtro_real = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)
# filtro_real = (df["QtdePontos"] >= 75) * (df["QtdePontos"] <= 100)
# pode usar tanto o & ou * multiplicação
#precisa dos parenteses para cada condição

df[filtro_real]

#%%
#filtrando 1 ou 100
filtro = (df["QtdePontos"] == 1) + (df["QtdePontos"] == 100)
# pode usar tanto | ou +
# baseado na tabela verdade
df[filtro]

#%%
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) & (df["DtCriacao"]
                                                              <= "2025-01-01")
df[filtro]
