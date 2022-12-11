R, c = map(int, input("Enter a number (11 33):").split(" "))
for i in range(1, R, 2):
    print((".|." * i).center(c, "-"))
print("WELCOME".center(c, "-"))
for i in range(R - 2, -1, -2):
    print((".|." * i).center(c, "-"))
