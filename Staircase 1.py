def staircase(n):
    for i in range(1, n + 1):
        print(str("#" * i).rjust(n))


if __name__ == "__main__":
    n = int(input("Enter a number (5):"))
    staircase(n)
