def create_box(height, width, character):
    string = ""
    if height >= 1 and width >= 1:
        for h in range(height):
            for w in range(width):
                string += character
            string += "\n"
            
        return string
    else:
        return 'invalid size'

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