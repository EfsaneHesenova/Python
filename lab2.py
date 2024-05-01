import random
n = int(input("Say: "))
siyahi = [random.randint(-3, 10) for _ in range(n)]
print(siyahi)

ededi_orta = 0
cem = 0
say = 0
netice = 0
for i in siyahi:
    if siyahi[0] < 0:
        print("Ilk reqem menfidir")
        break
        netice = 0
    else:
        netice = 1
        if i >= 0:
            cem += i
            say += 1
        else:
            break

if netice == 1:
    ededi_orta = cem / say
    print("Ededi orta: ", ededi_orta)
