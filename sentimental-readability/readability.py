text = input("Text: ")
cl, cw, cs = 0, 0, 0

for char in text:
    if char.isalpha():
        cl += 1
    elif char.isspace():
        cw += 1
    elif char in ['.', '!', '?']:
        cs += 1

if cl:
    if cs == 0:
        cs = 1
    cw += 1

L = cl / cw * 100
S = cs / cw * 100

index = round((0.0588 * L) - (0.296 * S) - 15.8)

if index <= 1:
    print("Before Grade 1")

elif index >= 16:
    print("Grade 16+")

else:
    print("Grade ", index)

