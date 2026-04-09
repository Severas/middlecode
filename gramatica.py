# meio basicona sem inventar muita coisa, pra nao complicar dps kkk
gramatica = {

    "S": [["CMD_LIST"]],

    "CMD_LIST": [["CMD", "CMD_LIST"], ["ε"]],

    "CMD": [
        ["decl", "tipo", "id", "=", "E"],
        ["id", "=", "E"],

        ["print", "(", "E", ")"],

        ["if", "(", "E", ")", ":", "CMD"],
        ["if", "(", "E", ")", ":", "CMD", "else", ":", "CMD"],

        ["while", "(", "E", ")", ":", "CMD"]
    ],

    "E": [["T", "E'"]],

    "E'": [["opnum", "T", "E'"], ["ε"]],

    "T": [
        ["id"],
        ["num"],
        ["string"],
        ["bool"]
    ]
}