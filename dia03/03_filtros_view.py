# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1

# %%
clientes

## FILTROS E COPIAS

# no pandas em versões menores que 3..
# quando fazemos um filtroele não retorna um copia do df anterior só com as linhas filtradas
# chamamos isso de wiew, ele aponta para as linhas do df original, onde o filtro é verdadeiro
# uma view é uma variavel que aponta para as linhas do filtro

# no pandas 3 para frente
# Uma nota para as pessoas que estão a ver isto e a usar o Pandas 3.0:
# aquilo que o Téo mostra aqui já não se aplica em Pandas 3.0,
# em que o modelo Copy-on-Write passou a ser o default.
# Quando há um assignment, a DF é copiada.

# %%

#PONTEIROS E REFERENCIAS NO PYTHON

A = [1, 2]
B = A
print("A: ", A)
print("B: ", B)

B.append(3)
print("A: ", A)
print("B: ", B)
# Quando fazemos a associação "B = A" passamos o endereço de A para B
# Para onde a variavel aponta na memória
# o que permite a variável B alterar o que está nesse endereço de memória

# VARIAVEIS EM PYTHON
# No python as variaveis não são caixinhas, mas sim post its, ou seja,
# A variavel "cola" em um objeto, endereço de memória
# Tudo em python é tratado como ponteiros ou referências por de baixo dos panos

# %%

A = [1, 2]
B = A.copy()
print("A: ", A)
print("B: ", B)

B.append(3)
print("A: ", A)
print("B: ", B)

# com o .copy() criamos um novo endereço de memória para o a variavel B
# o que permite alterar um objeto sem impactar o outro
# em DF é preciso fazer a mesma coisa, usar o .copy()
# aumenta o custo em memória
