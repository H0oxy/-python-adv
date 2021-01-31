'''
1. Написать валидацию даты на чистом python (без re)
2, 3. Написать валидатор для вещественных чисел: 1.32 или 1,32 (с re и на чистом python)
'''
import re

RE_REAL_NUMBERS_VALIDATOR = re.compile(r'^[\d]{1,}[.|,][\d]+$')

def number_is_valid(number):
    return RE_REAL_NUMBERS_VALIDATOR.match(number)

assert not number_is_valid('1.d2')
assert not number_is_valid('d.32')
assert not number_is_valid('132')
assert number_is_valid('1.32')
assert number_is_valid('1,32')
