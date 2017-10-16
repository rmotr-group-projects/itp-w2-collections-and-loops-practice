"""
read code on this link to know various functions which are faster -
https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
and
https://www.daniweb.com/programming/software-development/code/462120/isprime-function-python - info on how to use a
output from 1 function into another.

def _is_prime(number):
    if number == 2 or number == 3: return True
    if number < 2 or number % 2 == 0: return False
    if number < 9: return True
    if number % 3 == 0: return False
    r = int(number ** 0.5)
    f = 5
    while f <= r:
        print
        '\t', f
        if number % f == 0: return False
        if number % (f + 2) == 0: return False
        f += 6
    return True
"""


def _is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for n in range(2, number):
        if number % n ==0:
            return False
    return True


number = 19
testcode = _is_prime(number)
print(testcode)


def list_of_prime_numbers(max_number):
    primes_list = []
    new_max = max_number + 1
    for n in range(2, new_max):
        if _is_prime(n):
            primes_list.append(n)
    return primes_list







max_number = 55
testcode = list_of_prime_numbers(max_number)
print(testcode)


# =================== #
# ====== Tests ====== #
# =================== #

# Test: `is_prime`


def test_big_number_prime_true():
    assert _is_prime(19) is True


def test_big_number_prime_false():
    assert _is_prime(20) is False


def test_two_prime():
    assert _is_prime(2) is True


def test_three_prime():
    assert _is_prime(3) is True


def test_four_prime():
    assert _is_prime(4) is False


# Test: `list_of_prime_numbers`

def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_list_one():
    assert list_of_prime_numbers(2) == [2]


def test_list_zero():
    assert list_of_prime_numbers(0) == []
