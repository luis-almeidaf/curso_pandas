# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(
    url,
    storage_options={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) curso-pandas/1.0'
    },
)

df_uf = dfs[1]
df_uf


# %%
def str_to_float(valor: str):
    valor = valor.replace("\xa0", "").replace(" ", "").replace(",", ".")
    return float(valor)


# %%
df_uf["Área (km²)"] = df_uf["Área (km²)"].apply(str_to_float)
df_uf["População (Censo 2022)"] = df_uf["População (Censo 2022)"].apply(
    str_to_float)
df_uf["PIB per capita (R$) (2015)"] = df_uf[
    "PIB per capita (R$) (2015)"].apply(str_to_float)
df_uf["PIB (2015)"] = df_uf["PIB (2015)"].apply(str_to_float)

#%%


def exp_to_anos(exp):
    return float(exp.replace(",", ".").replace(" anos", ""))


# %%

df_uf["Expectativa de vida (2016)"] = df_uf[
    "Expectativa de vida (2016)"].apply(exp_to_anos)

# %%


def mortalidade_to_float(x: str):
    x = float(x.replace("‰", "").replace(",", "."))
    return x


# %%
df_uf["Mortalidade infantil (/1000)"] = df_uf[
    "Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%


def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000
            and linha["Mortalidade infantil (/1000)"] < 15
            and linha["IDH (2010)"] > 700)


# %%
# isso aplica a função em cada uma das linhas do df
# uma linha é uma serie do pandas com os valores da linha em questão
# axis = 0 são as colunas
# axis = 1 são as linhas
# sem nada especificado o padrão é 0
df_uf.apply(classifica_bom, axis=1)
