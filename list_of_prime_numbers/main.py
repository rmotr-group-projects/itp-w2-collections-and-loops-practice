
def _is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True   

def list_of_prime_numbers(max_number):
    list_prime = []
    for item in range(max_number+1):
        print(item)
        if _is_prime(item):
            list_prime.append(item)
    return list_prime
    


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
