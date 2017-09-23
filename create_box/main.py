def create_box(height, width, character):
    box = ""
    for i in range(height):
        box += character * width
        box += '\n'
    return box

#With a for nested loop
"""

def create_box(height, width, character):
    box = ""
    for i in range(height):
      for j in range(width):
        box += character
      box += '\n'
    return box
"""

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
