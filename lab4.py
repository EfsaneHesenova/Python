import random

n = int(input("Massivin satir sayini daxil edin (n): "))
m = int(input("Massivin sutun sayini daxil edin (m): "))

A = []
for i in range(n):
    row = []
    for j in range(m):
        element = random.randint(1, 100)  
        row.append(element)
    A.append(row)

with open('massiv.txt', 'w') as file:
    for row in A:
        file.write(' '.join(map(str, row)) + '\n')
tek_ededler = []
with open('massiv.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = list(map(int, line.split()))
        for num in numbers:
            if num % 2 != 0:
                tek_ededler.append(num)
with open('tek_ededler.txt', 'w') as file:
    for num in tek_ededler:
        file.write(str(num) + '\n')

tek_ededler_cemi = sum(tek_ededler)

print("Tək ədədlər fayla yazıldı.")
print("Tək ədədlərin cəmi:", tek_ededler_cemi)
