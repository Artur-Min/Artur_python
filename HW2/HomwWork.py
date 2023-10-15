
a = int(input("вклад в разиере:"))
n = int(input("проценты:"))
year = int(input("годы:"))
for i in range(year+1):
    n = n / 100
    a = a + (a * n)
print(a)
