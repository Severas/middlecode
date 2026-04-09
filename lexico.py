import re

TOKENS = [
    ("COMENT", r"#.*"),

    # palavras chave
    ("DECL", r"\banel\b"),
    ("TIPO", r"\bouro\b|\bprata\b|\btexto\b|\bdestino\b"),
    ("IF", r"\bse\b"),
    ("ELSE", r"\bsenao\b"),
    ("WHILE", r"\benquanto\b"),
    ("PRINT", r"\bpalantir\b"),

    # valores
    ("BOOL", r"\bverdadeiro\b|\bfalso\b"),
    ("FLOAT", r"\d+\.\d+"),
    ("INT", r"\d+"),
    ("STR", r'"[^"]*"'),

    # operadores
    ("OPNUM", r"\+|\-|\*|\/|\^"),
    ("OPREL", r"==|!=|>=|<=|>|<"),
    ("OPLOG", r"\be\b|\bou\b|\bnao\b"),

    # simbolos
    ("ATRIB", r"="),
    ("LP", r"\("),
    ("RP", r"\)"),
    ("DP", r":"),
    
    ("ID", r"[a-zA-Z][a-zA-Z0-9_]*"),
    ("SPACE", r"\s+"),
]


def lexico(cod):
    tks = []
    i = 0

    while i < len(cod):
        ok = False

        for tp, rg in TOKENS:
            m = re.match(rg, cod[i:])
            if m:
                v = m.group(0)

                if tp not in ["SPACE", "COMENT"]:
                    tks.append((tp, v))

                i += len(v)
                ok = True
                break

        if not ok:
            raise Exception("erro lexico -> " + cod[i])

    return tks


def norm(tp, v):
    if tp == "DECL":
        return "decl"
    if tp == "TIPO":
        return "tipo"
    if tp == "ID":
        return "id"
    if tp in ["INT", "FLOAT"]:
        return "num"
    if tp == "STR":
        return "string"
    if tp == "BOOL":
        return "bool"
    if tp == "OPNUM":
        return "opnum"
    if tp == "OPREL":
        return "oprel"
    if tp == "OPLOG":
        return "oplog"
    if tp == "IF":
        return "if"
    if tp == "ELSE":
        return "else"
    if tp == "WHILE":
        return "while"
    if tp == "PRINT":
        return "print"

    return v


def toTerm(tks):
    return [norm(t, v) for t, v in tks]