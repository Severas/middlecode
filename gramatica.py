# meio basicona sem inventar muita coisa, pra nao complicar dps kkk agora com ordem de precedencia

GRAMATICA = {

    "PROG": [["CMD", "PROG"], ["ε"]],

    "CMD": [["DECL"], ["ATR"], ["IF"], ["WHILE"], ["PRINT"]],

    "DECL": [["anel", "TIPO", "id", "=", "EXPR"]],

    "TIPO": [["ouro"], ["prata"], ["texto"], ["destino"]],

    "ATR": [["id", "=", "EXPR"]],

    "IF": [["se", "(", "EXPR_LOG", ")", ":", "CMD", "senao", ":", "CMD"]],

    "WHILE": [["enquanto", "(", "EXPR_LOG", ")", ":", "CMD"]],

    "PRINT": [["palantir", "(", "EXPR", ")"]],

    "EXPR": [["EXPR_LOG"]],

    # logico
    "EXPR_LOG": [["EXPR_LOG", "ou", "EXPR_AND"], ["EXPR_AND"]],
    "EXPR_AND": [["EXPR_AND", "e", "EXPR_NOT"], ["EXPR_NOT"]],
    "EXPR_NOT": [["nao", "EXPR_NOT"], ["EXPR_REL"]],

    "EXPR_REL": [
        ["EXPR_NUM", "OPREL", "EXPR_NUM"],
        ["EXPR_NUM"],
        ["verdadeiro"],
        ["falso"]
    ],

    # numerico com precedencia
    "EXPR_NUM": [["EXPR_NUM", "+", "TERM"], ["EXPR_NUM", "-", "TERM"], ["TERM"]],
    "TERM": [["TERM", "*", "FATOR"], ["TERM", "/", "FATOR"], ["FATOR"]],
    "FATOR": [["BASE", "^", "FATOR"], ["BASE"]],

    "BASE": [
        ["(", "EXPR_NUM", ")"],
        ["num"],
        ["id"]
    ]
}