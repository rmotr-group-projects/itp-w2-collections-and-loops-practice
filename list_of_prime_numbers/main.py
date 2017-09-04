def _is_prime(number):
# setting up the variable to test if a number is prime or not
  var = 2                   
  while var < number:
#while the var is lower then the number the test should continue
    if number % var == 0:
      return False
# while the provided number divided by the test variable does not result in a remainder (i.e. number not prime)
#the test should return false
    elif number % var == 0:
      break
# another elif with the same test but this time it breaks out of the loop
    var = var + 1
  
  return True



def list_of_prime_numbers(number):
    answer_list = []
    for i in range(2, number+1):
        if _is_prime(i) == True:
            answer_list.append(i)
    return answer_list

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
