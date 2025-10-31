num = int(input())
temp = num
power = 1
while temp >= 10:
    temp //= 10
    power *= 10
first = temp             
last = num % 10          
middle = (num % power) // 10
new_num = last * power + middle * 10 + first
print(new_num)
