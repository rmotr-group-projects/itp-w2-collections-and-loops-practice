def highest_number_cubed(limit):
    x_var = 1
    y_var = x_var + 1
    while y_var**3 < limit:
        y_var += 1
    return y_var - 1
        


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
