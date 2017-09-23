def highest_number_cubed(limit):
    for i in range(limit):
        if (i ** 3) >= limit:
            break
    #limit < 8 should return output = 1 (2**3 = 8)
    output = 1 if (limit < 8) else (i - 1)
    return output


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
