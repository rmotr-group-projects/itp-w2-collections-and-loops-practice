def create_box(height, width, character):
    result = ''
    h = 0
    while h < height:
        line = width * character
        result += line + '\n'
        h += 1
    return result


print (create_box(3, 4, '*'))
print (create_box(1, 1, '@'))
print (create_box(3, 24, 'x'))



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
    assert create_box(3, 24, 'x') == third_box_expected

