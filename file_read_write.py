file1 = open("basic1.txt", "w")

file1.write("Hello Python!")

file1.close()

with open("basic2.txt", "w") as file2:
    file2.write("Hello Python!")

with open("basic2.txt", "r") as file:
    contents = file.read()
print(contents)

import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file:
    for line in file:

        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        bmi = round(bmi, 2)
        result = ""
        if 25 <= bmi:
            result = "Overweight"
        elif 18.5 <= bmi:
            result = "Average"
        else:
            result = "Underweight"

        print('\n'.join([
            "Name: {}",
            "Weight: {}",
            "Height: {}",
            "BMI: {}",
            "Result: {}"
        ]).format(name, weight, height, bmi, result))
        print()


