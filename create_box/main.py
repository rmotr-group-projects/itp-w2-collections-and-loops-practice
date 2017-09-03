def create_box(height, width, character):
    if width >= 1 and height >= 1: 
        line = (width * character)+"\n"
        return line * height
    else:
        return "Please make sure height and width is greater than 1"
 

# idea for this function using a while loop below
#
# def create_box(height, width, character):
#         line = '' 
#         while height >= 1:
#             line = line + (width * character)+"\n"
#             height = height - 1
#         return line



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
    
def test_third_box_expected():
    assert create_box(0,0,"&") == "Please make sure height and width is greater than 1"

# Write your own test using the `third_box_expected` box
