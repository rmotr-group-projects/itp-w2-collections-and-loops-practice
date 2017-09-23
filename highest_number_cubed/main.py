def highest_number_cubed(limit):
    if limit == 1:
        return 1
    else:
        number = 1
        while (number * number * number ) < limit:
            number = number + 1
        if (number ** number) > limit:
            return number -1
            #break
        else:
            return number
        
print(highest_number_cubed(1))
print(highest_number_cubed(7))
print(highest_number_cubed(8))
print(highest_number_cubed(27))
print(highest_number_cubed(28))

print("=========")
print(highest_number_cubed(30))
print(highest_number_cubed(12))
print(highest_number_cubed(3))
print(highest_number_cubed(12000))



def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
