def highest_number_cubed(limit):
    test_values = []
    test_value = 1
    cubed_number = test_value

    def cube_number(value):
        import math

        return math.pow(value, 3)

    while cubed_number <= limit:
        test_values.append(test_value)
        test_value += 1
        cubed_number = cube_number(test_value)

    return max(test_values)

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22


highest_number_cubed(30)
highest_number_cubed(12)
highest_number_cubed(3)
highest_number_cubed(12000)