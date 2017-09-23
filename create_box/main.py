def create_box(height, width, character):
    row = 0
    box = ''
    while row < height:
        printrow = ''
        column = 0
        printcolumn = ''
        while column < width:
            printcolumn += character
            column += 1
        printrow = printcolumn + "\n"
        row += 1 
        box += printrow   
    return box
print(create_box(3, 4, '*'))
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
