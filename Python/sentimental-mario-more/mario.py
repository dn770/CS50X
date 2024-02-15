h = input("height: ")
while not h.isdigit() or int(h) > 8 or int(h) < 1:
    h = input("height: ")

h = int(h)
for i in range(1, 1 + h ):
    for j in range(h):
        if j >= (h - i):
            print("#", end ="")
        else:
            print(" ", end="")

    print("  ",end ="")

    for j in range(i):
        print("#", end ="")

    print()


