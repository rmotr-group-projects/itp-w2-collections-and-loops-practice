def highest_number_cubed(limit):
    for num in range(limit):
        cubed_num = num ** 3
        if cubed_num <= limit:
            num_cubed_lst = []
            num_cubed_lst.append(num)
            
    return max(num_cubed_lst)
    
    
# __________________________________________________ #

def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
    


