#1. Built-in constants
print("First constant", True)
print("Second constant", False)
print("Third constant", None)

# 2. Python functions

my_list = [3, 14, 8, 11, 5]

def filterFunction(obj):
    if obj > 8:
        return True
    else:
        return False

filtered = list(filter(filterFunction,my_list))

print(filtered)

# 3. Loops and Branching.

for obj in my_list:
    print(obj)

print(my_list[0] if my_list[0] != my_list[1] else my_list[1])

# 4. Exception.

my_list1 = [1, 2, 3, 4, 5]

try:
    my_list1 [6]
except IndexError:
    print("That index is not in the list!")

# 5. Context manager.

with open ("text.txt", 'r') as file:
    print (file.read())

# 6. Lambda

test_lambda = lambda x: x+7
y = 10
print(test_lambda(y))