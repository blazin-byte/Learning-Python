# These are just some basic Python concepts

# This is print(f) which prints whatevers in curly braces as a string
num = 72
print(f"Num is {num}!")

# Practice with Lists
test_list = [
    num,
    "String",
    44,
    45,
]
# Use For Loop to run through List
for i in test_list:
    print(i)
print("\n")
# Use For Indexed Loop to run through List
for index, value in enumerate(test_list):
    print(f"Index: {index}, Value: {value}")

# Dictionaries for control flow
dict_a = {
    "A": 1,
    'B': 2,
    'C': 3,
    'D': 4,
    "A": 5
}
for key, value in dict_a.items():
    print(f"{key},{value}")
