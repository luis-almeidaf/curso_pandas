# %%

import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%


def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()

    return np.sqrt((amplitude - media)**2)


def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days


idades = pd.Series([12, 24, 23, 65, 76, 4, 12, 56])

# %%

summary = (transacoes.groupby(by=["IdCliente"], as_index=False).agg({
    "IdTransacao": ["count"],
    "QtdePontos": [
        "sum",
        "mean",
        diff_amp,
    ],
    "DtCriacao": [life_time]
}))

# %%

summary.columns = [
    "IdCliente", "QtdTransacao", "TotalPontos", "MediaPontos", "AmpMeanDiff",
    "LifeTime"
]
summary
