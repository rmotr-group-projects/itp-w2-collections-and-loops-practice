def highest_number_cubed(limit):
    number = 0
    while (number ** 3) < int(limit):
        number += 1
    number = number - 1
    return number


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
