# %%

import pandas as pd

idades = [12, 23, 24, 56, 23, 25]

series_idades = pd.Series(idades)
series_idades

# %%

print(idades[0])
print(series_idades[0])

# %%
series_idades = series_idades.sort_values()
series_idades

series_idades[3]
# o indice 3 é o 56, mesmo que pela ordenação ele seja o último

# %%
print(series_idades.iloc[0])
print(series_idades.iloc[-1])
print(series_idades)
print(series_idades[:3])  #3 primeiros elementos
print(series_idades.iloc[:-1])  # do primeiro elemento até o penultimo
print(series_idades.iloc[::-1])  # do último elemento até o primeiro

# %%
# dessa forma você meio que cria um dict dentro do indice com a chave que você quer
idades = [12, 23, 24, 56, 123]
indexes = ["Luis", "Fernando", "Lucas", "Giulia", "Luis"]

series_idades = pd.Series(idades, index=indexes)

series_idades["Luis"]  # traz todos os valores encontrados com chave "Luis"

# %%
series_idades.loc["Luis"]

# %%
series_idades.iloc[[-1]]
