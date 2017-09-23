def _is_prime(number):      # checks if the number is prime
    if number == 1:         # 1 is not prime by convention
        return False
    if number == 2 or number == 3 or number == 5 or number == 7:          # 2 and 3 are always prime
        return True
    for x in range(2,number):
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            return False # not prime
        else:
            return True     # prime

def list_of_prime_numbers(max_number):      # creates a list of primes
    primelist = []                          # empty list to be filled
    for x in range(max_number+1):   # check integers between 2 and max_number, inclusive
        test = _is_prime(x)         # send each integer to the prime-checking function
        if test:            
            primelist.append(x)     # if integer is prime, add to list of primes
    return primelist                    # end

# =================== #
# ====== Tests ====== #
# =================== #
print(_is_prime(19))
print(_is_prime(20))
print(_is_prime(2))
print(_is_prime(3))
print(_is_prime(4))
print(list_of_prime_numbers(19))
print(list_of_prime_numbers(2))
print(list_of_prime_numbers(0))


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
    
def test_five_prime():
    assert _is_prime(5) is True

def test_seven_prime():
    assert _is_prime(7) is True
    
def test_twentyfive_prime():
    assert _is_prime(25) is False 

# Test: `list_of_prime_numbers`
def test_big_number_list():
    assert list_of_prime_numbers(19) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_list_one():
    assert list_of_prime_numbers(2) == [2]

def test_list_zero():
    assert list_of_prime_numbers(0) == []
    
def test_list_forty_nine():
    assert list_of_prime_numbers(49) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]