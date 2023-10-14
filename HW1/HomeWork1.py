# два числа.второе число больше первого. 1 - x; 2 - y 
# найти числа которые имеют ровно 5 делителей, 
# среди чисел в диапозоне от x до y включительно.
# вывести их и количество этих чисел 

num1 = int(input())
num2 = int(input())
count = 0
for i in range(num1, num2+1):
    count2 = 0
    for a in range(2, i):
        if i % a == 0:
            count2 += 1
    if count2 == 5:
        count += 1
        print(i)
print(count)      
        














