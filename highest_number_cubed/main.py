def highest_number_cubed(limit):
    x = 0
    result = 0
    while result < limit:
        x = x + 1
        result = x ** 3
    x = x - 1
    return(x)


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
