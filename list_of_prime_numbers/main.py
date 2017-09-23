
def _is_prime(num):
    # Prime Number must be greater than 1
    if num > 1:
        # Need to check every number between 2 and num for a factor
        for i in range(2,num):
            # If the number modulo i is 0 it is dividable 
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                # if this is the case we aren't prime and need to bail 
                return False
                break
        else:
            #if nothing is modulo 0 above we are ok
            return True
            print(num,"is a prime number")
    # else the number isn't prime
    else:
        print(num,"is not a prime number")
        return False
     
def list_of_prime_numbers(max_number):
    #given a number print all of the prime numbers less than or equal to it
    # if the number is 0 just return []
    
    
    #make an empty collection for the answer 
    answer = []
   
    counter = 2
    
    # if the number is 0 do nothing 
    if max_number == 0:
        return answer
    else:
        #count up to the max_number including it
        for i in range(2,max_number+1):
            if _is_prime(i):
                answer.append(i)
        return answer
           

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
