def highest_number_cubed(limit):
    #calculate limit's cubic root
    number = limit ** (1.0 / 3.0)
    #convert result to integer
    return int(number)

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
