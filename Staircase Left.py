def staircase(j):
    for i in range(1, j + 1):
        print(str("#" * i).ljust(j))


if __name__ == "__main__":
    n = int(input("Enter a number (5):"))
    staircase(n)
