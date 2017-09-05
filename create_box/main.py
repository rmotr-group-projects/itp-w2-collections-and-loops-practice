def create_box(height, width, character):
  
    #Ernesto's Solution
    box_height = 0
    my_box = ''

    while box_height < height:
        my_box += (width * character) + '\n'
        box_height += 1
        
    return my_box

    """
    # Gagan's solution
    if height < 1 or width < 1:
        return "Invalid input"
    h = 0
    w = 0
    my_box = ''
    while w < width:
        my_box = my_box + character
        w += 1
        # my_box = height * (my_box + '\n')
        # print(my_box)
    return height * (my_box + '\n')
    """


# Tests:

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

# Write your own test using the `third_box_expected` box
def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected
