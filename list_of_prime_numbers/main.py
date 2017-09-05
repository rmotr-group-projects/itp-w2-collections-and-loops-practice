def _is_prime(number):

# Gagan's Solution
    if number == 2:
        result = True
    elif number % 2 == 0:
        result = False
    elif number <= 1:
        result = False
    else:
        n = 2
        while n < number:
            remainder = number % n
            if remainder == 0:
                result = False
                break
            else:
                result = True
            n += 1
    return result

def list_of_prime_numbers(number):
    n = 2
    prime_list = []
    if number < 2:
        return prime_list
    elif number >= 2:
        while n <= number:
            if _is_prime(n) == True:
                prime_list.append(n)
                # print(prime_list)
            n += 1
        return prime_list

""" Szilvia's Solution
    for i in (2, number):
            while number:
               if number == 2:
                   return True
               elif number%i == 0:
                   return False
               else:
                   return True


def list_of_prime_numbers(max_number):
    pass
   
"""

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
