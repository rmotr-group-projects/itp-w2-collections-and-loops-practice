def highest_number_cubed(limit):#max version
    testing = 1
    testing_state = True
    
    while testing_state == True:
        if testing ** 3 < limit:
            testing +=1
        elif testing ** 3 == limit:
            testing_state = False
            return testing
        else:
            testing_state = False
            return testing-1

def highest_number_cubed(limit):
  results = []
  for i in range(limit):
    test = i ** 3
    if test <= limit:
      results.append(i)
      i += 1
  return max(results)   


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
