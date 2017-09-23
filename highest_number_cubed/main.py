def highest_number_cubed(limit):
    c = 1
    cubed = 0
    for i in range(limit):
      cubed = c * c * c
      if (cubed <= limit):
        c += 1
    return c-1
    # return int(limit**(1/3.0))


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
