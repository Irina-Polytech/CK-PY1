list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
for number in range(len(list_numbers)):
    max_number = list_numbers[max_index]
    current_number = list_numbers[number]
    if current_number > max_number:
        max_index = number
# TODO Оформить решение
list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
