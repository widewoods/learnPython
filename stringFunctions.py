format_a = "{}".format("Hello, World!")
format_b = "{}".format(1000)
format_c = "{} / {} : {}".format(100, 200, 300)
format_d = "{} {} {}".format(3.14, 100, True)  # Can format other types

print(format_a)
print(format_b)
print(format_c)
print(format_d)

a = "{}".format(100)
int_a = int(a)

print(type(a), a, type(int_a), int_a, "\n")
print("-" * 40)

output_a = "{:d}".format(5)
output_b = "{:5d}".format(5)
output_c = "{:05d}".format(5)  # Fills empty spaces with 0s


print(output_a)
print(output_b)
print(output_c)

output_d = "{:.3f}".format(3.14592)  # Automatically rounds to nearest
output_e = "{:g}".format(4.00)

print(output_d)
print(output_e)

print("-" * 40)

b = "Hello, World!"
print(b.upper())
print(b.lower())

c = "     Unnecessary Spaces      "
print(c.strip())
print(c.rstrip())
print(c.lstrip())

print("-" * 40)

print("Nickname".isalpha())
print("Password123".isalnum())
print("321".isdecimal())  # Use before casting

print("-" * 40)

d = "HelloHello"
print(d.find("Hello"))  # Search from left to right
print(d.rfind("Hello"))

print("Bye" in d)
print("Hello" in d)

e = "10 20 30 40 50".split(" ")  # Saved as a list
print(e)
e = "10,20,30,40,50".split(",")
print(e)

