def create_box(height, width, character):
    
    # Initializing box with empty string 
    box = ''
    
    # Create a for loop that will loop the number of times in height
    # the _ means that no variable name is needed in the for loop
    for _ in range(height):
        
        # Multiplying the width by character and the endline
        box += character*width +'\n'
    
    # Returning newly created box    
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

# Tests
# print (create_box (3,4, "*"))
# print (create_box (2,10, "erica"))


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected
    
# Write your own test using the `third_box_expected` box
