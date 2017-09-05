def highest_number_cubed(limit):

    # Gagan's solution
    num = 0
    cube_result = 0
    while cube_result <= limit:
        num = num + 1
        cube_result = (num * num * num)
        #print(num)
    return (num - 1)

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22