num = int(input("Give me a number: "))

list_range = list(range(1,num+1))

divisor_list = []

for number in list_range:
    if num % number == 0:
        divisor_list.append(number)

print(divisor_list)