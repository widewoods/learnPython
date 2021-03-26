# min(), max(), sum()

numbers = [103, 52, 273, 32, 77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(min(103, 52, 273))
print(max(103, 52, 273))

print("-" * 40)

# reversed()

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print(list_reversed)  # iterator - will learn later
print(list(list_reversed))

for i in reversed(list_a):
    print(i)

print("Hello"[::-1])  # another way to reverse

print("-" * 40)

# enumerate()

ex_list = ["Item1", "Item2", "Item3"]

print(enumerate(ex_list))
print(list(enumerate(ex_list)))

for i, value in enumerate(ex_list):
    print("Item at index {} is {}".format(i, value))

print("-" * 40)

# items()

ex_dict = {
    "KeyA" : "ValueA",
    "KeyB" : "ValueB",
    "KeyC" : "ValueC"
}

print(ex_dict.items())

for key, value in ex_dict.items():
    print("dictionary[{}] = {}".format(key, value))

print("-" * 40)

# list comprehension

array = [i * i for i in range(0, 20, 2)]

print(array)

array = ["Apple", "Plum", "Chocolate", "Banana", "Cherry"]
output = [fruit for fruit in array if fruit != "Chocolate"]

print(output)

print("-" * 40)

# Iterator
# Use next() to get elements one by one

num = [1, 2, 3, 4, 5, 6]
r_num = reversed(num)

print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
