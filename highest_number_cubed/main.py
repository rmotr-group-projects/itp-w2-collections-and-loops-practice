# take an input and find the highest number which when cubed is less than the input
# ** is exponentiation operation in python
def highest_number_cubed(limit):
    # start at the top of the range and count down 
    for i in reversed(range(1,(limit+1))):
        if i**3 >=limit:
            print("%s too big" % i)
        else:
            print("%s is just right" % (i))
            return i


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
