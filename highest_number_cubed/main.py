def highest_number_cubed(limit):
    cubed_list = []
    x = 0
    while x**3 < limit:
        cubed_list.append(x)
        x += 1
    return max(cubed_list)
    
    
print (highest_number_cubed(30))
print (highest_number_cubed(12))
print (highest_number_cubed(3))
print (highest_number_cubed(12000))


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
