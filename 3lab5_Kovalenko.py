my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Видалення дублікатів
unique_set = set(my_list)

# Перетворення списку та його відсортування
unique_list = sorted(list(unique_set))

print("The list with unique elements only:")
print(unique_list)