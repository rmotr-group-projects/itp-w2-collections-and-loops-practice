def highest_number_cubed(limit):
    for num in range(limit): 
        if num % 3 == 0:
         num = max(range(limit)) 
         root = num ** (1./3) 
    return int(root)     


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
