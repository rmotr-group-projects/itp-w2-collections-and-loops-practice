def create_box(height, width, character):
    if width >= 1 and height >= 1:
        diagram = ""
        for row in range(height):
            for column in range(width):
                diagram += character
            diagram = diagram + '\n'
        return diagram

# I've added the if statement to test if the given height and width are <= 1, otherwise thows an error.
# I'm working on the last enhancement 'only the outer border of the box shows and it is not filled in', but it's difficult. 

    
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