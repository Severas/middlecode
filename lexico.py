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
    ("CHAVES", r"\{|\}"),
    ("DOIS_PONTOS", r":"),

    ("KEYWORD", r"\banel\b|\bouro\b|\bprata\b|\btexto\b|\bdestino\b|\bse\b|\bsenao\b|\benquanto\b|\bpalantir\b|\bverdadeiro\b|\bfalso\b"),

    ("IDENTIFICADOR", r"[a-zA-Z][a-zA-Z0-9]*"),
    ("ESPACO", r"\s+"),
]

DFA = {

    "start": {
        "a-z": "id",
        "A-Z": "id",
        "0-9": "num",

        "+": "opnum",
        "-": "opnum",
        "*": "opnum",
        "/": "opnum",
        "^": "opnum",

        "<": "rel_lt",
        ">": "rel_gt",
        "=": "assign",
        "!": "rel_not"
    },

    "id": {
        "a-z": "id",
        "A-Z": "id",
        "0-9": "id"
    },

    "num": {
        "0-9": "num",
        ".": "float_start"
    },

    "float_start": {
        "0-9": "float"
    },

    "float": {
        "0-9": "float"
    },

    "rel_lt": {
        "=": "rel_le"
    },

    "rel_gt": {
        "=": "rel_ge"
    },

    "assign": {
        "=": "rel_eq"
    },

    "rel_not": {
        "=": "rel_ne"
    }
}

ACCEPT_STATES = {
    "id",
    "num",
    "float",
    "opnum",
    "rel_lt",
    "rel_gt",
    "rel_le",
    "rel_ge",
    "rel_eq",
    "rel_ne",
    "assign"
}


def categoria_char(c):

    if c.islower():
        return "a-z"

    elif c.isupper():
        return "A-Z"

    elif c.isdigit():
        return "0-9"

    return c


def validar_dfa(lexema):

    estado = "start"

    for c in lexema:

        categoria = categoria_char(c)

        if categoria not in DFA[estado]:
            return False

        estado = DFA[estado][categoria]

    return estado in ACCEPT_STATES


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

                    if tipo in [
                        "IDENTIFICADOR",
                        "NUM_INT",
                        "NUM_FLOAT",
                        "OPNUM",
                        "OPREL",
                        "ATRIBUICAO"
                    ]:

                        if not validar_dfa(valor):

                            raise Exception(
                                f"o conselho branco rejeitou o lexema: '{valor}'"
                            )

                    tokens.append((tipo, valor))

                pos = match.end(0)
                break

        if not match:

            if codigo[pos] == '"':

                raise Exception(
                    "as runas da string nunca foram fechadas"
                )

            raise Exception(
                f"simbolo proibido pelos magos: '{codigo[pos]}'"
            )

    return tokens


def normalizar_token(tipo, valor):

    if tipo == "IDENTIFICADOR":
        return "id"

    elif tipo in ["NUM_INT", "NUM_FLOAT"]:
        return "num"

    elif tipo == "STRING":
        return "string"

    elif tipo == "KEYWORD":
        return valor.lower()

    elif tipo == "LOGICO":
        return valor

    elif tipo == "OPNUM":
        return valor

    elif tipo == "OPREL":
        return "OPREL"

    else:
        return valor