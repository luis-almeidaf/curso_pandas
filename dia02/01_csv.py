# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

df.to_csv("clientes.csv", index=False)

#df.to_parquet("clientes.parquet", index=False)

#dfparquet = pd.read_parquet("clientes.parquet")

#df.to_excel("clientes.xlsx")

#df = pd.read_excel("clientes.xlsx")
df
