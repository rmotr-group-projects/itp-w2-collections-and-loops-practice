# my thinking: this seems like a good fit for a while loop rather than a for
# loop due to the unknown and variable number of iterations that the loop will
# be making.

def highest_number_cubed(limit):
    
    # setting up the counter (number) and answer variable (total)
    
    total = 0
    number = 0
    
    # while loop takes the total (result of the cube operation) and compares it
    # against the provided limit. When total exceeds limit, the loop will no
    # longer run. the number counter increased by one before running the 
    # cube operation.
    
    while total < limit:
        number += 1
        total = number ** 3 
        
    # The final "return number" is decreased by 1 because the while loop exceeds
    # the limit and then stops, which results in the number variable being 1
    # larger than the correct answer.
        
    return number - 1


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
