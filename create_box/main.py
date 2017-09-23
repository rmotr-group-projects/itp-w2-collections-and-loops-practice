def create_box(height, width, character):
    box = ''
    for y in range(height):
        box += character * width + '\n'
    return box

def create_border(height, width, character):
    box = ''
    for y in range(height):
        if y == 0 or y == height - 1:
            box += character * width + '\n'
        else:
            box += character + ' ' * (width - 2)+ character + '\n'
    return box

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

fourth_test = """
#####
#   #
#   #
#   #
#   #
#   #
#   #
#   #
#####
""".lstrip()

fifth_test = """
ooooooooooo
o         o
o         o
o         o
o         o
o         o
ooooooooooo
""".lstrip()


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

def third_test_box():
    assert create_box(3, 24, 'x') == third_box_expected
    
def test_first_border():
    assert create_border(9, 5, '#') == fourth_test

def test_second_border():
    assert create_border(7, 11, 'o') == fifth_test
