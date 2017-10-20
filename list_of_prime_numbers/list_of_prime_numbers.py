import math

def _is_prime(number):
    if number < 2:
        return(False)
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return(False)
    return(True)    


def list_of_prime_numbers(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.
     primes = []
     
     if sieveSize == 0:
         return primes
     
     if sieveSize == 2:
         primes.append(2)
         return primes


     sieve = [True] * sieveSize #creates a list of True values
     sieve[0] = False # changes these elements to false zero and one are not prime numbers
     sieve[1] = False
     # create the sieve
     
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:  #why does this logic work?
             sieve[pointer] = False
             pointer += i

     # compile the list of primes
     
     
     
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)
     return primes

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
