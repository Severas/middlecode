from lexico import lexer, normalizar_token
from first import compute_first
from gramatica import GRAMATICA

codigo = '''
anel ouro frodo = 10
anel prata gandalf = 2.5
anel texto anelUnico = "Um Anel"
anel destino jornada = verdadeiro

frodo = frodo + 5 * gandalf ^ 2

se (frodo > 10 e jornada):
    palantir("forte")
senao:
    palantir("fraco")

enquanto (frodo < 20):
    frodo = frodo + 1
'''

# lexico
tokens = lexer(codigo)
print("TOKENS:")
print(tokens)

# normaliza
normalizados = [normalizar_token(t, v) for t, v in tokens]
print("\nTOKENS NORMALIZADOS:")
print(normalizados)

# FIRST
first = compute_first(GRAMATICA)
print("\nFIRST:")
for k, v in first.items():
    print(k, ":", v)