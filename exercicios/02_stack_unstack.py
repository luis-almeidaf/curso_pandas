#%%

import pandas as pd

#%%

df = pd.read_csv("homicidios_consolidados.csv")
df.head()

#%%
# isso altera o agrupamento do df
# o .stack retorna um série
# sem o set_index  ele não agrupa corretamente
df = df.set_index(["nome", "período"]).stack()

#%%
# o .reset_index() faz com que volte a ser um df
# é mais fácil fazer isso que alterar a tabela, adicionar colunas
# para não precisar alterar o schema do banco

df_stack = df.reset_index()
df_stack.columns = ["nome", "período", "métrica", "valor"]

df_stack

# %%

# isso cria um multi series, que é estranho de trabalhar
# as colunas ficam empilhadas
df_unstack = df_stack.set_index(["nome", "período",
                                 "métrica"]).unstack().reset_index()
df_unstack

#%%
# para resolver é possível dropar os levels
# drop_level, passando o indice que vocÊ quer remover 0 é o padrão
# conventendo isso em lista é possível pegar só o que você quer
# o [2:] começa do segundo indice da lista
metricas = df_unstack.columns.droplevel(0).to_list()[2:]
metricas

#%%
df_unstack.columns = ["nome", "perído"] + metricas
df_unstack
