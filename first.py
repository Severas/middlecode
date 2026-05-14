def compute_first(gramatica):
    first = {nt: set() for nt in gramatica}

    mudou = True

    while mudou:
        mudou = False

        for X in gramatica:
            for prod in gramatica[X]:

                # epsilon
                if prod == ["ε"]:
                    if "ε" not in first[X]:
                        first[X].add("ε")
                        mudou = True
                    continue

                for i, simbolo in enumerate(prod):

                    # terminal
                    if simbolo not in gramatica:
                        if simbolo not in first[X]:
                            first[X].add(simbolo)
                            mudou = True
                        break

                    # nao terminal
                    antes = len(first[X])

                    first[X] |= (first[simbolo] - {"ε"})

                    if len(first[X]) > antes:
                        mudou = True

                    # para se nao tiver epsilon
                    if "ε" not in first[simbolo]:
                        break

                    # todos possuem epsilon
                    if i == len(prod) - 1:
                        if "ε" not in first[X]:
                            first[X].add("ε")
                            mudou = True

    return first