'''
analisador sintatico

usei parser LL(1) top-down recursivo
ficou mais facil de integrar com a gramatica e com o FIRST
integrado com o lexico
o lexer gera os tokens e o parser consome eles
se nao der erro gera a arvore sintatica
se der erro mostra mensagem da linguagem tipo magia falhou
algumas coisas da gramatica/token foram alteradas
separei expressao numerica e logica
removi recursao a esquerda
normalizei id e num pra simplificar o parser
tambem adicionei blocos com {}
pq o parser nao sabia onde if/while terminava
ficou mais organizado pro LL(1)
'''

from lexico import lexer, normalizar_token
from gramatica import GRAMATICA
from first import compute_first
from parser import Parser
from arvore import mostrar_arvore


codigo1 = '''
anel prata a = 1.0
anel prata b = 3.0
anel prata c = 2.0

anel destino jornada = verdadeiro
anel texto mensagem = "invocando magia antiga"

palantir(mensagem)

anel prata destinoDelta = b ^ 2 - 4 * a * c

se (destinoDelta < 0 ou nao jornada): {

    palantir("as visoes do palantir nao revelam raizes reais")

} senao: {

    anel prata raizDestino = destinoDelta ^ 0.5

    anel prata caminho1 = (b + raizDestino) / (2 * a)

    anel prata caminho2 = (b - raizDestino) / (2 * a)

    palantir("primeiro caminho")
    palantir(caminho1)

    palantir("segundo caminho")
    palantir(caminho2)

}

enquanto (a < 2): {

    a = a + 0.5

}

se (destinoDelta >= 0 e a != 0): {

    palantir("os caminhos foram revelados na terra media")

} senao: {

    palantir("as sombras esconderam os caminhos")

}

se (caminho1 == caminho2): {

    palantir("um unico destino foi encontrado")

} senao: {

    palantir("destinos diferentes apareceram")

}
'''


codigo2 = '''
# declaracoes

anel ouro frodo = 10
anel prata gandalf = 2.5
anel texto anelUnico = "Um Anel"
anel destino jornada = verdadeiro

# operacoes
frodo = frodo + 5 * gandalf ^ 2

gandalf = (gandalf + 1.5) / 2

# if else
se (frodo > 10 e jornada): {

    palantir("frodo esta forte")

} senao: {

    palantir("frodo esta fraco")

}

# operador nao
se (nao jornada): {

    palantir("jornada falhou")

} senao: {

    palantir("a sociedade continua")

}

# loop
enquanto (frodo < 20): {

    frodo = frodo + 1

}

# comparacao
se (frodo >= 20 ou gandalf > 3): {

    palantir("objetivo alcancado")

} senao: {

    palantir("mordor continua distante")

}

# comparacoes extras
se (frodo == 20): {

    palantir("frodo chegou ao limite")

} senao: {

    palantir("frodo ainda caminha")

}

se (frodo != 0): {

    palantir("frodo ainda ativo")

} senao: {

    palantir("frodo desapareceu")

}

# bool
jornada = falso

# final
se (jornada == falso): {

    palantir("fim da jornada")

} senao: {

    palantir("a jornada continua")

}
'''

codigo_erro1 = '''
anel enquanto frodo = 10
'''

codigo_erro2 = '''
anel texto mensagem = "o olho de sauron

palantir(mensagem)
'''

codigo_erro3 = '''
anel ouro frodo$ = 10
'''

codigo_erro4 = '''
se (frodo > 10: {

    palantir("erro")

}
'''

codigo_erro5 = '''
se (frodo > 10): {

    palantir("frodo forte")

'''

codigo_erro6 = '''
se (frodo > 10):

    palantir("erro")

}
'''

codigo_erro7 = '''
anel ouro frodo = 10 +

palantir(frodo)
'''

codigo_erro8 = '''
palantir(("teste"))
'''

codigo_erro9 = '''
anel enquanto frodo = 10
'''

try:
    # alterar aqui para testar outros codigos ou erros
    tokens = lexer(codigo_erro1)

    print("\nTOKENS\n")

    for i, token in enumerate(tokens):
        print(f"{i+1:02d} -> {token}")

    normalizados = [
        normalizar_token(t, v)
        for t, v in tokens
    ]

    print("\nTOKENS NORMALIZADOS\n")

    for i, token in enumerate(normalizados):
        print(f"{i+1:02d} -> {token}")

    first = compute_first(GRAMATICA)

    print("\nFIRST\n")

    for nt, conjunto in first.items():
        print(f"{nt:12} -> {conjunto}")

    parser = Parser(normalizados)

    arvore = parser.parse()

    print("\nARVORE SINTATICA\n")

    mostrar_arvore(arvore)

except Exception as erro:

    print("\nmagia falhou...\n")
    print(erro)