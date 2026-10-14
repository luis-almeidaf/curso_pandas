# %%

idades = [12, 23, 24, 56, 23, 25]

media = sum(idades) / len(idades)
print("Média: ", media)

diffs = 0
for idade in idades:
    diffs += (idade - media)**2

variancia = diffs / (len(idades) - 1)

print("Variância: ", variancia)

# %%

import pandas as pd

#Criação de uma série
idades = [12, 56, 56, 14, 12, 30, 25]
series_idades = pd.Series(idades)
series_idades

# o ideal é que para séries todos o itens tenham o mesmo tipo, int, float

# %%
#Estatísticas da série
media_idades = series_idades.mean()  # media
var_idades = series_idades.var()  # variancia
summary_idades = series_idades.describe()  #resumo dos itens

summary_idades
