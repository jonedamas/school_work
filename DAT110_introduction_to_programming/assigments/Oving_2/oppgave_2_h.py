from Oving_2 import oppgave_2_g

print('Perfekte tall mellom 1 og 10000:')

for tall in range(10001):
    if oppgave_2_g.perf_tall(tall):
        print(tall)
