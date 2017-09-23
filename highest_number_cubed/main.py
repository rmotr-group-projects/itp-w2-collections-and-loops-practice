def highest_number_cubed(limit): 
    #return int(limit**(1/3))

    i = 0
    for i in limit:
        if i ** 3 < limit:
            return i + 1
        else:
            return i - 1
def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
