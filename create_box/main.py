def create_box(height, width, character):
    var = ""
    for i in range(width):
        var += character
    box = ""
    if height > 0:
        for i in range(height):
            box += var + "\n"
        return box
    else:
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


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

def test_third_box():
    assert create_box(3,24,"x") == third_box_expected