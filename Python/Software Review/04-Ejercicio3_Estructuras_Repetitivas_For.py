for iP in range(680):
    for iQ in range(680):
        if (iP ** 3 + iQ ** 4 - 2 * iP) ** 2 < 680:
            print(f"Los numeros posibles de P, son:"
                  f"",iP, end=", ")
            print(f"Los numeros posibles de Q, son:"
                  f"",iP, end=", ")