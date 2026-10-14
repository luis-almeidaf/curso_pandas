# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

# %%
idCliente = clientes["idCliente"]


def get_last_id_part(id: str):
    return id.split("-")[-1]


get_last_id_part("001ebba5-5491-400a-ad05-d9204ea11cca")

# %%
ultima_parte_ids = []

for i in idCliente:
    ultima_parte = get_last_id_part(i)
    ultima_parte_ids.append(ultima_parte)

clientes["novoId"] = ultima_parte_ids

clientes.head()

# %%
# o apply aplica uma função que recebe 1 elemento, que vai ser o elemento da série
# já faz a chamada automaticamente, sem precisar fazer um for
clientes["idCliente"].apply(get_last_id_part)
