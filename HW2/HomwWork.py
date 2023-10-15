a = int(input("вклад в разиере:"))
n = int(input("проценты:"))
years = int(input("годы:"))
for i in range(years):
    n = n / 100
    a = a + (a * n)
print(a)
