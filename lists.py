# Getting elements in a list
list_a = [273, 32, 103, "String", True, False]

print(list_a)
print(list_a[0])
print(list_a[2])
print(list_a[1:3])

print(list_a[-1])
print(list_a[-2])

print(list_a[3][0:3])

print("-" * 40)

# List operators
list_b = [1, 2, 3]
list_c = [4, 5, 6]

print("list_b = ", list_b)
print("list_c = ", list_c, "\n")

print("list_b + list_c = ", list_b + list_c)
print("list_b * 3 = ", list_b * 3)

print(len(list_b))

print("-" * 40)

# Adding new elements
list_d = [1, 2, 3]

list_d.append(4)
list_d.append(5)
print(list_d)

list_d.insert(0, 10)
print(list_d)

list_d.extend(list_c)
print(list_d)

print("-" * 40)

# Removing elements
list_e = [0, 1, 2, 3, 4, 5]

del list_e[1]
print(list_e)

a = list_e.pop(2)
print(list_e)
print(a)

del list_e[:2]
print(list_e)

list_e.remove(5)
print(list_e)

list_e.clear()
print(list_e)

print("-" * 40)

list_f = [273, 32, 103, 57, 52]
print(273 in list_f)
print(100 in list_f)

print(273 not in list_f)
