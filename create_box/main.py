def create_box(height, width, character):
    rows = character * width
    boxybox = (rows + '\n') * height 
    return boxybox

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