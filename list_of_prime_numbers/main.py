import math
def _is_prime(number):
    square_root = math.sqrt(number) # I'm taking the square root of the given number - pls check http://www.counton.org/explorer/primes/checking-if-a-number-is-prime/ for more explanation :)
    i = 2
    count_list = []
    isprime = "none"
    if number == 1: # I needed to hard-code the first 3 numbers
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    while i <= square_root: # here I add all numbers from square root till 2. So if you number is 5, this list will contains 5,4,3,2
        count_list.append(i)
        i += 1
    
    
    for num in count_list: # here I check what happens if I modulo the original number with the numbers in the previously made list.
        if number % num == 0: # if modulo = 0, then we can divide that number with num, so it won't be prime
            isprime = False # else? it's prime and voila :)
            return isprime
        else:
            isprime = True
    return isprime
    
 #        if ....
 # Hi there! I'll take care of the is prime number list if that's fine with you :)
 # I need to work on this a little bit more, but it will be ready latest by tomorrow :)
 # -----
 # Hi Zsofia! Sorry I was a little busy today! 
 #
 # I think I figured out a _is_prime function that works by using modulo (%) and
 # incrementing a while loop. I think you'll learn more by trying to make it work on
 # your own, but I'm happy to walk you through my solution if you don't figure it out
 # by Monday ;)
 #
 # Once the _is_prime function is written, list_of_prime_numbers should work

def list_of_prime_numbers(max_number):
    results_list = [] # creating a list that I can add each prime number to
    counter = 1 # counter to increment from 1 up to the max_number parameter
    while counter <= max_number:
        if _is_prime(counter): # using above function to test if the current number is prime
            results_list.append(counter) # if the number is prime, append to our list
        counter = counter + 1 # increment counter up to the next number to loop through
    return results_list # spits out the fully populated list of prime numbers
    
        
        
    

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
