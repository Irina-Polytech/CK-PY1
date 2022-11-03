import random
import string

alphabet = f'{string.ascii_letters}{string.digits}'

def get_random_password(len_password=8) -> str: # TODO написать функцию генерации случайных паролей
    password = ''.join(random.sample(alphabet, len_password))
    return password

print(get_random_password())
