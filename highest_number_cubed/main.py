def highest_number_cubed(limit):
    index = 1
    total = 0
    
    while total < limit:
        total = index * index * index
        index = index + 1
    return index - 2


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
