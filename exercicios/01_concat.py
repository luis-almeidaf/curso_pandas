# %%

import pandas as pd


def criar_dataframes(nome_arquivo: str):
    df = (pd.read_csv(f"../data/ipea/{nome_arquivo}.csv",
                      sep=";").rename(columns={
                          "valor": nome_arquivo
                      }).set_index(["nome", "período"]).drop(["cod"], axis=1))
    return df


# %%

import os


def montar_lista_de_dfs(arquivos: list[str]) -> list[pd.DataFrame]:
    dfs = []

    for arquivo in arquivos:
        nome_arquivo = arquivo.split(".")[0]
        dfs.append(criar_dataframes(nome_arquivo))
    return dfs


# %%
arquivos_ipea = os.listdir("../data/ipea")

dfs = montar_lista_de_dfs(arquivos_ipea)
df_completo = pd.concat(dfs,
                        axis=1).reset_index().sort_values(["período", "nome"])

df_completo.to_csv("homicidio.csv", index=False)
