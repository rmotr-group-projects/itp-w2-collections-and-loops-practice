def create_box(height, width, character):
    new_height = 0
    a_width = 0
    a_width = [character] * width
    a_width = ''.join(a_width)
    # .join is a string method to concatenate lists to strings
       
    while new_height < height -1:
        a_width += '\n'
        a_width += character*width
        new_height += 1  #bug: new_height not incrementing
    a_width += '\n'   
    return(a_width)

"""
output   '****\n****\n****'
expected '****\n****\n****\n'
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
def test_Third_box():
    assert create_box(3, 24, 'x') == third_box_expected
