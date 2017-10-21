
def _is_prime(number):
    flag = True
    if number > 1:
       for i in range(2,number):
            if (number % i) == 0:
               flag = False
               break
            else:
               flag = True
    else:
        flag = False
    return flag
    
    
    
def list_of_prime_numbers(max_number):
    lista = []
    for i in range(max_number+1):
        if _is_prime(i):
            lista.append(i)
    return lista

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
