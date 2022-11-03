import random

def get_unique_list_numbers() -> list[int]:
    list_number = []
    i = 0
    while i < 15:
        number = random.randint(-10, 10)
        i += 1
        if number not in list_number:
            list_number.append(number) # TODO написать функцию для получения списка уникальных целых чисел
        else:
            i -= 1
    return list_number

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
