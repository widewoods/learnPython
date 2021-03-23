import datetime

now = datetime.datetime.now()

# if now.hour < 12:
#     print("It's {} A.M. in the morning".format(now.hour))
#
# if now.hour >= 12:
#     print("It's {} P.M. in the afternoon".format(now.hour - 12))

# Use else instead of another if

if now.hour < 12:
    print("It's {} A.M. in the morning".format(now.hour))

else:
    print("It's {} P.M. in the afternoon".format(now.hour - 12))

print("-" * 40)

score = int(input("Enter a score: "))

if score == 100:
    print("100!")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

print("-" * 40)

number = input("Enter an integer: ")
number = int(number)

if number > 0:
    raise NotImplementedError
# Can use pass for not implemented code as well
# NotImplemented error is better to remember
else:
    raise NotImplementedError
