# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%
# é possível usar só o on=["nome da coluna"], se o noem for igual nos 2 dfs
# se for diferente, usar o left_on e right_on
# suffixes permite alterar o nome que vai ser exibido depois de colunas repetidas
# por padrão o how é inner, ou seja, vai trazer só os matches das chaves
# o left vai trazer tudo da esquerda,mais o que ter match da direita
# o right traz tudo da direita, mais os matches da esquerda
df = transacoes.merge(right=clientes,
                      how="left",
                      left_on=["IdCliente"],
                      right_on=["idCliente"],
                      suffixes=["Transacao", "Cliente"])
df

# %%
# exercício
# quem tem mais transações de Streak?

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")

produtos = pd.read_csv("../data/produtos.csv", sep=";")

# %%

cliente_trasacao_produto = transacoes.merge(transacao_produto,
                                            on="IdTransacao",
                                            how="left")
cliente_trasacao_produto[['IdTransacao', "IdCliente", "IdProduto"]]

# %%
df_final = cliente_trasacao_produto.merge(produtos, on="IdProduto", how='left')
df_final = df_final[df_final["DescNomeProduto"] == "Presença Streak"]
df_final

#%%
(df_final.groupby(by=["IdCliente"])["IdTransacao"].count().sort_values(
    ascending=False).head(1))

# %%
# pode ser feito dessa forma
# poderia ser um inner join no lugar do right
produtos = produtos[produtos["DescNomeProduto"] == "Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao", how="left")
           .merge(produtos, on=["IdProduto"],how="right")
           .groupby(by=["IdCliente"])["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1))
