from arvore import No


class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.pos = 0

    def token_atual(self):

        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    def avancar(self):

        self.pos += 1

    def match(self, esperado):

        atual = self.token_atual()

        if atual == esperado:

            no = No(atual)

            self.avancar()

            return no

        raise Exception(
            f"esperava '{esperado}' mas encontrou '{atual}'"
        )

    def parse(self):

        arvore = self.PROG()

        if self.token_atual() is not None:

            raise Exception(
                f"token perdido nas terras medias: '{self.token_atual()}'"
            )

        return arvore

    def PROG(self):

        no = No("PROG")

        no.add(self.CMD())
        no.add(self.PROG2())

        return no

    def PROG2(self):

        no = No("PROG2")

        atuais = [
            "anel",
            "id",
            "se",
            "enquanto",
            "palantir"
        ]

        if self.token_atual() in atuais:

            no.add(self.CMD())
            no.add(self.PROG2())

        else:

            no.add(No("ε"))

        return no

    def CMD(self):

        atual = self.token_atual()

        if atual == "anel":
            return self.DECL()

        elif atual == "id":
            return self.ATR()

        elif atual == "se":
            return self.IF()

        elif atual == "enquanto":
            return self.WHILE()

        elif atual == "palantir":
            return self.PRINT()

        raise Exception(
            f"comando desconhecido nas terras medias: '{atual}'"
        )

    def DECL(self):

        no = No("DECL")

        no.add(self.match("anel"))
        no.add(self.TIPO())
        no.add(self.match("id"))
        no.add(self.match("="))
        no.add(self.EXPR())

        return no

    def TIPO(self):

        atual = self.token_atual()

        if atual in [
            "ouro",
            "prata",
            "texto",
            "destino"
        ]:

            return self.match(atual)

        raise Exception(
            f"tipo desconhecido pelos magos: '{atual}'"
        )

    def ATR(self):

        no = No("ATR")

        no.add(self.match("id"))
        no.add(self.match("="))
        no.add(self.EXPR())

        return no

    def IF(self):

        no = No("IF")

        no.add(self.match("se"))
        no.add(self.match("("))

        no.add(self.EXPR_LOG())

        no.add(self.match(")"))
        no.add(self.match(":"))
        no.add(self.match("{"))

        no.add(self.PROG())

        no.add(self.match("}"))

        # senao opcional
        if self.token_atual() == "senao":

            no.add(self.match("senao"))
            no.add(self.match(":"))
            no.add(self.match("{"))

            no.add(self.PROG())

            no.add(self.match("}"))

        return no

    def WHILE(self):

        no = No("WHILE")

        no.add(self.match("enquanto"))
        no.add(self.match("("))

        no.add(self.EXPR_LOG())

        no.add(self.match(")"))
        no.add(self.match(":"))
        no.add(self.match("{"))

        no.add(self.PROG())

        no.add(self.match("}"))

        return no

    def PRINT(self):

        no = No("PRINT")

        no.add(self.match("palantir"))
        no.add(self.match("("))

        no.add(self.EXPR())

        no.add(self.match(")"))

        return no

    def EXPR(self):

        no = No("EXPR")

        no.add(self.EXPR_LOG())

        return no

    def EXPR_LOG(self):

        no = No("EXPR_LOG")

        no.add(self.EXPR_AND())

        while self.token_atual() == "ou":

            no.add(self.match("ou"))
            no.add(self.EXPR_AND())

        return no

    def EXPR_AND(self):

        no = No("EXPR_AND")

        no.add(self.EXPR_NOT())

        while self.token_atual() == "e":

            no.add(self.match("e"))
            no.add(self.EXPR_NOT())

        return no

    def EXPR_NOT(self):

        no = No("EXPR_NOT")

        if self.token_atual() == "nao":

            no.add(self.match("nao"))
            no.add(self.EXPR_NOT())

        else:

            no.add(self.EXPR_REL())

        return no

    def EXPR_REL(self):

        no = No("EXPR_REL")

        atual = self.token_atual()

        if atual in ["verdadeiro", "falso"]:

            no.add(self.match(atual))

            return no

        elif atual == "string":

            no.add(self.match("string"))

            return no

        no.add(self.EXPR_NUM())

        if self.token_atual() == "OPREL":

            no.add(self.match("OPREL"))

            prox = self.token_atual()

            if prox in ["verdadeiro", "falso"]:

                no.add(self.match(prox))

            elif prox == "string":

                no.add(self.match("string"))

            else:

                no.add(self.EXPR_NUM())

        return no

    def EXPR_NUM(self):

        no = No("EXPR_NUM")

        no.add(self.TERM())

        while self.token_atual() in ["+", "-"]:

            no.add(self.match(self.token_atual()))
            no.add(self.TERM())

        return no

    def TERM(self):

        no = No("TERM")

        no.add(self.FATOR())

        while self.token_atual() in ["*", "/"]:

            no.add(self.match(self.token_atual()))
            no.add(self.FATOR())

        return no

    def FATOR(self):

        no = No("FATOR")

        no.add(self.BASE())

        if self.token_atual() == "^":

            no.add(self.match("^"))
            no.add(self.FATOR())

        return no

    def BASE(self):

        no = No("BASE")

        atual = self.token_atual()

        if atual == "(":

            no.add(self.match("("))
            no.add(self.EXPR_NUM())
            no.add(self.match(")"))

            return no

        elif atual == "num":

            no.add(self.match("num"))

            return no

        elif atual == "id":

            no.add(self.match("id"))

            return no

        raise Exception(
            f"expressao proibida por sauron: '{atual}'"
        )