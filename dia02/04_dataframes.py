# %%

import pandas as pd

df_clients = pd.read_csv("../data/clientes.csv", sep=";")

df_clients

# %%
# Amostras

df_clients.head(n=10)
# limita o tamanho do para exibição, é como o limit do sql
# trás as primeiras linhas

# %%
df_clients.tail(10)
# limita o tamanho do para exibição, é como o limit do sql
# trás as últimas linhas

# %%
df_clients.sample(10)
# limita o tamanho do para exibição, é como o limit do sql
# trás uma amostra aleatório, embaralhado

# %%
df_clients.shape
# retorna um tupla contendo o número de linhas e de colunas do df

# %%
df_clients.columns

# %%
df_clients.index

# %%
df_clients.info(memory_usage='deep')  # sem o paramentro memory_usage,
# faz a inferência do uso de memória, com o deep tras o valor real

# %%

df_clients.dtypes["idCliente"]  #dtypes retorna a tipagem de cada coluna
