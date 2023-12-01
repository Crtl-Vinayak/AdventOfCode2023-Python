file = open("day1_example.txt", "r")
txt = file.read()
print(txt)

lijst = txt.split()
print(txt.split())

digit_lijst = []
for i in range(len(lijst)):
    
    flag = True
    first_digit = None
    last_digit = None

    print(lijst[i], end="\n\n")
    for j in range(len(lijst[i])):
        if lijst[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if flag:
                first_digit = lijst[i][j]
                flag = False
            else:
                last_digit = lijst[i][j]
    if last_digit == None:
        last_digit = first_digit

    digit_lijst.append(first_digit + last_digit)


print(digit_lijst)
sum = 0
for i in digit_lijst:
    sum += int(i)

print(f"sum = {sum}")
