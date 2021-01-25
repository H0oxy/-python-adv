import re

RE_EMAIL_VALIDATOR = re.compile(r'^[A-Za-z0-9._-]+@([a-z0-9._-]+\.)+[a-z]{2,}$')  # \n\r, .com .org .su


def data_is_valid(data):
    return RE_DATA_VALIDATOR.match(data)

assert data_is_valid('25.01.2021')
assert data_is_valid('25-01-2021')
assert data_is_valid('25/01/2021')
assert not data_is_valid('5.01.2021')
assert not data_is_valid('05.01.21')
assert not data_is_valid('05,01,2021')
