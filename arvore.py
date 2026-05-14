class No:

    def __init__(self, valor):

        self.valor = valor
        self.filhos = []

    def add(self, filho):

        self.filhos.append(filho)


def mostrar_arvore(no, nivel=0):

    print("   " * nivel + str(no.valor))

    for filho in no.filhos:

        mostrar_arvore(filho, nivel + 1)