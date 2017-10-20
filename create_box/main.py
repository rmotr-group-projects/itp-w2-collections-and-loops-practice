def create_box(height, width, character):
    line = ''
    para = ''
    for x in range(height):
        for x in range(width):
            line = line + character
        line = line + '\n'
         
    return line


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
<3<3<3
<3<3<3
<3<3<3
<3<3<3
""".lstrip()



def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected


# Write your own test using the `third_box_expected` box
def test_third_box():
    assert create_box(4, 3, '<3') == third_box_expected