def first(gram):
    FIRST = {k: set() for k in gram}

    mudou = True
    while mudou:
        mudou = False

        for X in gram:
            for prod in gram[X]:

                if prod == ["ε"]:
                    if "ε" not in FIRST[X]:
                        FIRST[X].add("ε")
                        mudou = True
                    continue

                i = 0
                while i < len(prod):
                    s = prod[i]

                    if s not in gram:  # terminal
                        if s not in FIRST[X]:
                            FIRST[X].add(s)
                            mudou = True
                        break

                    antes = len(FIRST[X])
                    FIRST[X].update(FIRST[s] - {"ε"})

                    if len(FIRST[X]) != antes:
                        mudou = True

                    if "ε" not in FIRST[s]:
                        break

                    i += 1

                else:
                    if "ε" not in FIRST[X]:
                        FIRST[X].add("ε")
                        mudou = True

    return FIRST