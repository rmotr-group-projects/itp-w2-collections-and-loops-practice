def highest_number_cubed(limit):
    num = 1
    answer = 0
    while True:
        answer = num ** 3
        if answer > limit: 
            num = num - 1
            break
        else:
            num = num + 1
    return num

print(highest_number_cubed(30))


def test_three():
    assert highest_number_cubed(30) == 3

def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
