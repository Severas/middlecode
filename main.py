from lexico import lexico, toTerm
from sintatico import first
from gramatica import gramatica

codigo = """
# declaracao
anel ouro frodo = 10
anel prata gandalf = 2.5
anel texto anelUnico = "Um Anel"
anel destino jornada = verdadeiro

# conta
frodo = frodo + 5 * gandalf ^ 2

# if
se (frodo > 10 e jornada):
    palantir("forte")
senao:
    palantir("fraco")

# loop
enquanto (frodo < 20):
    frodo = frodo + 1
"""

tks = lexico(codigo)
terms = toTerm(tks)

print("tokens:")
for t in tks:
    print(t)

print("\nterminais:")
print(terms)

f = first(gramatica)

print("\nFIRST:")
for k in f:
    print(k, "=", f[k])