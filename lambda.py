#Function as a parameter

def call_10_times(func):
    for i in range(10):
        func()


def print_hello():
    print("Hello")


call_10_times(print_hello)
print()


def power(item):
    return item * item


def under_3(item):
    return item < 3


# map()

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map()")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))


# filter()

output_b = filter(under_3, list_input_a)
print("# filter()")
print("filter(under_3, list_input_a)", output_b)
print("filter(under_3, list_input_a)", list(output_b))
print()



# lambda
output_c = map(lambda x: x * x, list_input_a)
output_d = filter(lambda x: x < 3, list_input_a)

print(output_c)
print(list(output_c))
print(output_d)
print(list(output_d))

