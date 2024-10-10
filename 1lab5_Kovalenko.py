hat_list = [1, 2, 3, 4, 5]

number = int(input("Enter a number: "))

hat_list[int(len(hat_list) // 2)] = number
print(hat_list)

del hat_list [-1]

print(hat_list)