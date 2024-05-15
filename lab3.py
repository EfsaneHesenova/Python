import random

n = int(input("Massivin satir sayini daxil edin (n): "))
m = int(input("Massivin sutun sayini daxil edin (m): "))

A = []
for i in range(n):
    row = []
    for j in range(m):
        element = random.randint(1, 9)
        row.append(element)
    A.append(row)

print("Massivin elementləri:")

for row in A:
    print(row)

hasil = [1] * m

for j in range(m):
    for i in range(n):
        hasil[j] *= A[i][j]

print("Her sutunun hasilı:", hasil)
