def highest_number_cubed(limit):
    result = 0
    x = 1
    while x**3 < limit:
        x += 1
        result +=1
    return result
        


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
