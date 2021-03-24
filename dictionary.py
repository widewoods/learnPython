dict_a = {"name": "Woods", "age": 17}

print(dict_a["name"])
print(dict_a["age"])

dict_a["age"] = "Highschooler"  # Change value
print(dict_a["age"])

dict_b = {"list_a": [1, 2, 3, 4, 5]}

print(dict_b["list_a"][3])

dict_b["list_b"] = [7, 8, 9, 10]  # Add new key and value to dictionary
print(dict_b)

del dict_b["list_b"]
print(dict_b)

dict_c = {}
# print(dict_c["Not a real key"]) - KeyError

dict_d = {
    "name": "Dried Mango",
    "type": "Sweets",
    "ingredient": ["Mango", "Sugar", "Food Coloring"],
    "origin": "Philippines"
}

# key = input("Enter a key: ")
#
# if key in dict_d:
#     print(dict_d[key])
# else:
#     print("There is no key called", key)

value = dict_d.get("Key")  # Returns None if there is no key
print(value)
print()

for key in dict_d:
    print(key, ":", dict_d[key])


print("-" * 40)
# Simple Dictionary Problems
print("# Simple Dictionary Problems")

# 1
print("# 1")
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

for pet in pets:
    print(pet["name"], str(pet["age"]) + "살")

print()
# 2
print("# 2")
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
print()

# 3
# type("String") is str - check string
# type([]) is list - check list
# type({}) is list - check dict
print("# 3")
character = {
    "name": "Knight",
    "level": 12,
    "items": {
        "sword": "Sword of Fire",
        "armor": "Full Plated"
    },
    "skill": ["Slash", "Great Slash", "Perfect Slash"]
}

for key in character:
    if type(character[key]) is list:
        for elem in character[key]:
            print(key, ":", elem)
    elif type(character[key]) is dict:
        for k in character[key]:
            print(k, ":", character[key][k])
    else:
        print(key, ":", character[key])
