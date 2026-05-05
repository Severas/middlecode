GRAMATICA = {

    "PROG": [["CMD", "PROG2"]],

    "PROG2": [["CMD", "PROG2"], ["ε"]],

    "CMD": [["DECL"], ["ATR"], ["IF"], ["WHILE"], ["PRINT"]],

    "DECL": [["anel", "TIPO", "id", "=", "EXPR"]],
    "TIPO": [["ouro"], ["prata"], ["texto"], ["destino"]],

    "ATR": [["id", "=", "EXPR"]],

    "IF": [["se", "(", "EXPR_LOG", ")", ":", "CMD", "senao", ":", "CMD"]],
    "WHILE": [["enquanto", "(", "EXPR_LOG", ")", ":", "CMD"]],

    "PRINT": [["palantir", "(", "EXPR", ")"]],

    "EXPR": [["EXPR_LOG"]],

    # logico
    "EXPR_LOG": [["EXPR_AND", "EXPR_LOG2"]],
    "EXPR_LOG2": [["ou", "EXPR_AND", "EXPR_LOG2"], ["ε"]],

    "EXPR_AND": [["EXPR_NOT", "EXPR_AND2"]],
    "EXPR_AND2": [["e", "EXPR_NOT", "EXPR_AND2"], ["ε"]],

    "EXPR_NOT": [["nao", "EXPR_NOT"], ["EXPR_REL"]],

    "EXPR_REL": [
        ["EXPR_NUM", "OPREL", "EXPR_NUM"],
        ["EXPR_NUM"],
        ["verdadeiro"],
        ["falso"],
        ["string"]
    ],

    # numerico
    "EXPR_NUM": [["TERM", "EXPR_NUM2"]],
    "EXPR_NUM2": [["+", "TERM", "EXPR_NUM2"], ["-", "TERM", "EXPR_NUM2"], ["ε"]],

    "TERM": [["FATOR", "TERM2"]],
    "TERM2": [["*", "FATOR", "TERM2"], ["/", "FATOR", "TERM2"], ["ε"]],

    "FATOR": [["BASE", "FATOR2"]],
    "FATOR2": [["^", "FATOR"], ["ε"]],

    "BASE": [["(", "EXPR_NUM", ")"], ["num"], ["id"]]
}