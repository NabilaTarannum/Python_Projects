for digit in range(256):
    print("%d = %c" % (digit, chr(digit)))

# another way

for i in range(256):
    ch = chr(i)
    print("ASCII value of", i, "is =", ch)
