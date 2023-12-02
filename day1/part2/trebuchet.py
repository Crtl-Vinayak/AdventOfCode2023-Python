file = open("input.txt")
txt = file.read()
lijst = txt.split()

str = "twone1sixseven3"

first_digit = None
last_digit = None
num_numeric_lijst = ['1','2','3','4','5','6','7','8','9']
num_alphabetic_lijst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def is_letter(char):
    if char in num_numeric_lijst:
        return False
    return True

flag = True
for char in str: 
    if first_digit == None:
        flag = True
    else:
        flag = False

    if is_letter(char):
        if str in num_alphabetic_lijst:

        
    else:
        print('1')
        
