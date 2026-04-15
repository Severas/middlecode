import re

TOKENS = [
    ("COMENTARIO", r"#.*"),
    ("NUM_FLOAT", r"\d+\.\d+"),
    ("NUM_INT", r"\d+"),
    ("STRING", r'"[^"]*"'),

    ("OPNUM", r"\+|\-|\*|\/|\^"),
    ("LOGICO", r"\be\b|\bou\b|\bnao\b"),
    ("OPREL", r"==|!=|>=|<=|>|<"),

    ("ATRIBUICAO", r"="),
    ("PARENTESES", r"\(|\)"),
    ("DOIS_PONTOS", r":"),

    # palavras chave da terra media
    ("KEYWORD", r"\banel\b|\bouro\b|\bprata\b|\btexto\b|\bdestino\b|\bse\b|\bsenao\b|\benquanto\b|\bpalantir\b|\bverdadeiro\b|\bfalso\b"),

    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("ESPACO", r"\s+"),
]

def lexer(codigo):
    tokens = []
    pos = 0

    while pos < len(codigo):
        match = None

        for tipo, regex in TOKENS:
            pattern = re.compile(regex)
            match = pattern.match(codigo, pos)

            if match:
                valor = match.group(0)

                if tipo != "ESPACO" and tipo != "COMENTARIO":
                    tokens.append((tipo, valor))

                pos = match.end(0)
                break

        if not match:
            raise Exception(f"erro lexico em: {codigo[pos]}")

    return tokens


def normalizar_token(tipo, valor):
    if tipo == "IDENTIFICADOR":
        return "id"
    elif tipo in ["NUM_INT", "NUM_FLOAT"]:
        return "num"
    elif tipo == "STRING":
        return "texto"
    elif tipo == "KEYWORD":
        return valor.lower()
    elif tipo == "LOGICO":
        return valor
    elif tipo == "OPNUM":
        return valor
    elif tipo == "OPREL":
        return valor
    else:
        return valor