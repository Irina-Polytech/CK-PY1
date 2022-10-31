def get_count_char(str_): # TODO посчитать количество каждой буквы в строке в аргументе str_
    letter_dict = {}
    for letter in ''.join(str_.lower().split(' ')):
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def percent(dict_):
    sum_value = 0
    for key,value in dict_.items():
        sum_value += value
    for key,value in dict_.items():
        value = (value/sum_value) * 100
        dict_[key] = value
    return dict_
