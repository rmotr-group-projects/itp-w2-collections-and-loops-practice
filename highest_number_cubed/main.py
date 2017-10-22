def highest_number_cubed(limit):
    value = 0
    value2 = 0
    while (value ** 3) <= limit:
        value += 1
        value2 = value -1
    return value2


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
