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

df_uf.to_csv("../data/ufs.csv", sep=",", index=False)

df_uf
