# %%

import pandas as pd

df = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5],
    "nome": ["luis", "lu", "fer", "nah", "ads"]
})

df2 = pd.DataFrame({
    "cliente": [6, 7, 8],
    "nome": ["almeida", "faria", "silva"],
    "idade": [32, 45, 23]
})

df3 = pd.DataFrame({"idade": [32, 45, 23, 17, 24]})

# %%

dfs = [df, df2]
# o ignore index, cria novos indices para o df mergeado
# sem isso ele mantem os indices de cada df
pd.concat(dfs, ignore_index=True)

# %%
# se você ordenar um df e depois fizer um concat com ele, não vai manter a order
# é preciso usar o reset_index com drop = true
df3 = df3.sort_values(by="idade").reset_index(drop=True)
df3
# %%

# por padrao o concat simplemente empilha os dfs, um abaixo do outro
# com o axis = 1, eles ficam lado a lado
# a associação é feita por indice
pd.concat([df, df3], axis=1)
