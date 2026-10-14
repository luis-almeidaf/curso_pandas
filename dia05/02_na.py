# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

# isso remove qualquer linha que tenha valores faltantes
# cria uma view, precisa reatriabuir para a variavel do df
clientes.dropna(how="all")  # precisa que a coluna toda seja na
clientes.dropna(how="any")  # se houver um NA na coluna dropa

# %%

df = pd.DataFrame({
    "nome": ["luis", None, "jose", "hasd"],
    "idade": [None, None, 52, 26],
    "salario": [1422, 2455, None, 2455]
})

#df.dropna(how="all", subset=["idade"])
# subset indica o critério
# nesse caso indica que deve remover somente se a coluna idade tiver na

df.dropna(how="all", subset=["idade", "nome"])
# aqui precisa que as 2 colunas do subset sejam na/none para remover

# %%

# substitui os valores na, por 0 nesse caso, pode ser qualquer valor
# aqui estamos substituindo diretamente na serie
#df["idade"].fillna(0)

# aqui no df inteiro
df.fillna({"nome": "ze", "idade": 0})

medias = df[["idade", "salario"]].mean()
df.fillna(medias)
