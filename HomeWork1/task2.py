value_predikat = (True, False)
for x in value_predikat:
    for y in value_predikat:
        for z in value_predikat:
            print(f"¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для значений x = {x}, y = {y}, z = {z}" )
            if not (x or y or z) == (not x) and (not y) and (not z):
                print("Истина")
            else:
                print("Ложь")
