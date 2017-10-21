def highest_number_cubed(limit):
    number = 0
    valormax = 0
    valor = 0
    flag = 'true'
    
    while flag == 'true':
        if valor > limit:
            if valor > valormax:
                valormax = valor
            else:
                flag = 'false'
                return number-1
        else:
            number +=1        
            valor = number * number * number
            
    return number 


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
