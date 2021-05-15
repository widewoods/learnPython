tuple_test_a = (10, 20, 30)

print(tuple_test_a[0])
print(tuple_test_a[1])
print(tuple_test_a[2], "\n")

[a, b] = [10, 20]
(c, d) = (10, 20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d, "\n")

tuple_test_b = 10, 20, 30, 40
print("tuple_test_b:", tuple_test_b)
print("type(tuple_test_b):", type(tuple_test_b), "\n")

a, b, c = 10, 20, 30
print("a:", a)
print("b:", b)
print("c:", c, "\n")

# Swapping

a, b = 10, 20
print("a:", a)
print("b:", b)
print()

a, b = b, a
print("a:", a)
print("b:", b)
print()


def test(a, b):
    return a, b


a, b = test(40, 30)
print("a:", a)
print("b:", b)
print()

x, y = divmod(97, 40)
print(x, y)