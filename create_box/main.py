# Write a program that takes three inputs: height, width, and character.

# height: tells you how many rows
# width: tells you how many columns
# character: tells you what character to use

#___________understanding concepts part 1___________
width = 'xxx'
height = 'yyy'

print("this is an example:")
for r in height:
    print(width)

# what the code should do:
width = 3
height_or_repeat = 3
character = '*'
box = ''

print("this is an example of what we want:")
print(character * width)
print(character * width)
print(character * width)

'''returns
***
***
***
'''

#___________understanding concepts part 2___________
width = 3
height = 3
character = '*'
box = ''
repeat = 0

while True:
    row = character * width
    repeat += 1
    box = box + '\n' + row 
 
    if repeat == height:
        break

print("this is an example of what we want:")
print(box)


#___________turning this into a function:___________
def create_box(height, width, character):
    repeat = 0
    box = ''
    
    while True:
        row = character * width        
        repeat += 1
        box = box + '\n' + row
    
        if repeat == height:
            break

    return box

# testing the function:
test = create_box(3, 24, 'x')
print("testing with parameters {} and {} and {}: ".format(3, 24, 'x') + test)



#___________Extra credit challenge___________
# Add error checking to make sure the width and height is greater or equal to 1

def create_box(height, width, character):
    repeat = 0
    box = ''
    
    if width >= 1 and height >= 1:
    
        while True:
            row = character * width        
            repeat += 1
            box = box + '\n' + row
    
            if repeat == height:
                break

        return box
    
    else:
        return "You did not provide a valid height or width. Try again."

# testing the revised function, to see if it produces the error message when given an invalid parameter
test = create_box(0, 2, 'x')
print("testing with invalide parameters: \n" + test)




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
    