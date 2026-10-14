# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

# %%
# nesse exemplo, aplica o count para cada uma das linhas
# cria um novo dataframe agrupando pela chave que foi passada
# aplicando a função chamada, onde cada linha do df é o resultado dessa função
# para cada agrupamento
transacoes.groupby(by=["IdCliente"]).count()

#%%
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

#%%
# qtde_pontos
# total_pontos
# pontos/transacoes
# isso retorna um df multiindex
summary = transacoes.groupby(by=["IdCliente"], as_index=False).agg({
    "IdTransacao": ["count"],
    "QtdePontos": ['sum', 'mean']
})

summary

# %%
# para acessar um df multiindex pode ser feitos das 2 maneiras abaixo
summary["QtdePontos"]["mean"]

# %%

summary[("QtdePontos", "sum")]

# %%
# você pode renomear as colunas de  um df multiindex seguindo a ordem das colunas
summary.columns = ["IdCliente", "QtdTransacao", "TotalPontos", "AvgPontos"]
summary
