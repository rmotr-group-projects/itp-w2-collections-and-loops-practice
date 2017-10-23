def create_box(height, width, character):
    a = ''
    index = 0
    for i in range(height):
        for i in range(width):
            a = a + character
            index = index + 1
        a = a + '\n'
        index = 0
    return a
    


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

def test_thrid_box():
    assert create_box(3,24,'x') == third_box_expected