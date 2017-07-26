def highest_number_cubed(limit):
    condition = 0
    num = 0
    count = 2
    while condition == 0:
        num = count**3
        if num < limit:
            count+=1
        else:
            condition = 1
    count = count - 1
    return count

# For testing and troubleshooting purposes
print(highest_number_cubed(30))
print(highest_number_cubed(12))
print(highest_number_cubed(3))
print(highest_number_cubed(12000))

# Provided test cases
def test_three():
    assert highest_number_cubed(30) == 3

def test_two():
    assert highest_number_cubed(12) == 2

def test_one():
    assert highest_number_cubed(3) == 1

def test_big():
    assert highest_number_cubed(12000) == 22
