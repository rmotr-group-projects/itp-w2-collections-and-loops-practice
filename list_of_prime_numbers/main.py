
def _is_prime(number):
    if number <= 1:
      return False
    for n in range(2, number):
      if number%n == 0:
        return False
    return True


def list_of_prime_numbers(max_number):
    l = [] #empty list
    for i in range(2, max_number):
        if _is_prime(i):
            l.append(i)
            i+=1
        else:
            i+=1
    print l
    
    
    


''' ```python
>>> _is_prime(5)
True
>>> _is_prime(4)
False
>>> list_of_prime_numbers(10)
[2, 3, 5, 7]
>>> list_of_prime_numbers(19)
[2, 3, 5, 7, 11, 13, 17, 19]
```
'''


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
