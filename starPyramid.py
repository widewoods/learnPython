def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " *" * i)


if __name__ == '__main__':
    pyramid(7)
    print("Pyramid from main:" + __name__)
else:
    print("Pyramid from import:" + __name__)