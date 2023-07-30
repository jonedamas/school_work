from Oving_2 import oppgave_2_f


def perf_tall(tall):
    tot_sum = 1

    for i in range(2, int(tall / 2 + 1)):
        if oppgave_2_f.delelig(tall, i):
            tot_sum += int(tall / i)

    if tot_sum == 1:
        return False
    elif tot_sum == tall:
        return True
    else:
        return False


value = perf_tall()
print(value)
