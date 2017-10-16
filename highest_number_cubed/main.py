def highest_number_cubed(limit):
    x = 0
    while (x**3) < limit:
        x += 1
    return (x - 1)


limit = 30
testcode = highest_number_cubed(limit = 12000)
print(testcode)



def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
