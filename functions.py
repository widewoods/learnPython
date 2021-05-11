def print_n_times(msg, n=2):
    for i in range(n):
        print(msg)


print_n_times("3", n=2)


def mul(*values):
    result = 1
    for i in values:
        result *= i

    return result


print(mul(5,7,9,10))


def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i

    return output


print(factorial(6))


def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)


print(recursion_factorial(10))

count = 0


def fibonacci(n):
    global count
    count += 1
    if n == 1:
        return 1
    elif  n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
print(count)

dictionary = {1: 1, 2: 1}

count = 0


def memo_fibonacci(n):
    global count
    count += 1
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = memo_fibonacci(n-1) + memo_fibonacci(n-2)
        return dictionary[n]


print(memo_fibonacci(10))
print(count)

print("-" * 40)

#Problems


def flatten(data):
    output = []
    for elem in data:
        if type(elem) == list:
            output += flatten(elem)
        elif type(elem) == int:
            output.append(elem)

    return output


example = [[1,2,3], [4, [5, 6]], 7, [8, 9]]
print(example)
print(flatten(example))


min_people = 2
max_people = 10
total = 6
memo = {}


def ways_to_seat(remaining, seated):
    key = str([remaining, seated])

    if key in memo:
        return memo[key]
    if remaining < 0:
        return 0
    if remaining == 0:
        return 1

    count = 0
    for i in range(seated, max_people + 1):
        count += ways_to_seat(remaining - i, i)

    memo[key] = count

    return count


print(ways_to_seat(total, min_people))




