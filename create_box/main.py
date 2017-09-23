def create_box(height, width, character):
    result = ''
    if height < 1 and width < 1:
        return "bad dimension"
        
    for row in range(height):
        for column in range(width):
           result += character 
            
        result+='\n'
    return result


# py.test -v --tb=short create_box

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
