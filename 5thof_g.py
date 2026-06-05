
# MAP FUNCTION IN PYTHON - Easy Explanation and Notes
#

# ============================================
# MAP FUNCTION IN PYTHON
# ============================================

# Definition:
# map() applies the same function to every element
# of a list, tuple, set, string, etc.

# Syntax:
# map(function, iterable)

# ============================================
# 1. MAP WITH LIST
# ============================================

# Add 1 to every number

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x + 1, numbers))

print("Original List:", numbers)
print("New List:", result)

# Output:
# [2, 3, 4, 5]


# ============================================
# 2. MAP WITH TUPLE
# ============================================

# Multiply every number by 2

# Note: Converting between list and tuple is possible without data loss
# list() and tuple() preserve all elements and their order
# Data loss occurs when converting to set (loses duplicates and order)
numbers = (1, 2, 3, 4)

result = tuple(map(lambda x: x * 2, numbers))

print("\nOriginal Tuple:", numbers)
print("New Tuple:", result)

# Output:
# (2, 4, 6, 8)


# ============================================
# 3. MAP WITH SET
# ============================================

# Square every number

# Warning: Converting list/tuple to set can cause data loss
# Sets remove duplicate values and don't maintain order
# Example: [1, 2, 2, 3] becomes {1, 2, 3} - one '2' is lost
numbers = {1, 2, 3}

result = set(map(lambda x: x * x, numbers))

print("\nOriginal Set:", numbers)
print("New Set:", result)

# Output:
# {1, 4, 9}


# ============================================
# 4. MAP WITH STRING
# ============================================

# Convert letters to uppercase

letters = ["a", "b", "c"]

result = list(map(str.upper, letters))

print("\nOriginal Letters:", letters)
print("Uppercase Letters:", result)

# Output:
# ['A', 'B', 'C']


# ============================================
# 5. MAP WITH TWO LISTS
# ============================================

# Add corresponding elements

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, list1, list2))

print("\nList 1:", list1)
print("List 2:", list2)
print("Sum:", result)

# Output:
# [5, 7, 9]


# ============================================
# 6. MAP WITH CUSTOM FUNCTION
# ============================================

# Custom function to find square

def square(num):
    return num * num

numbers = [2, 3, 4]

result = list(map(square, numbers))

print("\nNumbers:", numbers)
print("Squares:", result)

# Output:
# [4, 9, 16]


# ============================================
# MOST IMPORTANT EXAM EXAMPLE
# ============================================

# Double every number

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print("\nDoubled Numbers:", result)

# Output:
# [2, 4, 6, 8, 10]


# ============================================
# IMPORTANT POINTS
# ============================================

# 1. map() applies a function to every element.
#
# 2. It works with:
#    - List
#    - Tuple
#    - Set
#    - String
#
# 3. map() returns a map object.
#
# 4. Convert map object using:
#    list()
#    tuple()
#    set()
#
# 5. lambda is commonly used with map().
#
# 6. Multiple iterables can be passed to map().


# ============================================
# VIVA DEFINITION
# ============================================

# map() is a built-in Python function that applies
# the same function to every element of an iterable
# and returns the modified result.





# ============================================
# DIFFERENCE BETWEEN MAP AND LAMBDA
# ============================================

# MAP is a built-in function that applies a function to every element of an iterable
# LAMBDA is an anonymous (unnamed) function used to create small, one-line functions

# Key Difference: MAP is a function that takes another function as input
#                 LAMBDA is used to CREATE a function (often used WITH map)

# Example showing the difference:

numbers = [1, 2, 3, 4, 5]

# Using map WITH lambda (lambda creates the function, map applies it)
result_with_lambda = list(map(lambda x: x * 2, numbers))
print("Using map with lambda:", result_with_lambda)

# Using map WITH a regular function (function is defined separately)
def double(x):
    return x * 2

result_with_function = list(map(double, numbers))
print("Using map with regular function:", result_with_function)

# Lambda ALONE (just creates a function, doesn't apply it to anything)
my_lambda = lambda x: x * 2
print("Lambda alone (just a function):", my_lambda)
print("Calling lambda on one value:", my_lambda(5))

# MAP ALONE (needs a function to work)
# map(numbers) would give an error - map needs a function as first argument

# ============================================
# SUMMARY OF DIFFERENCES
# ============================================

# MAP:
# - Built-in function
# - Applies a function to all elements in an iterable
# - Syntax: map(function, iterable)
# - Returns a map object

# LAMBDA:
# - Creates anonymous functions
# - Used for simple, one-line operations
# - Syntax: lambda arguments: expression
# - Returns a function object

# TOGETHER:
# - Lambda is often used WITH map to create quick functions
# - Example: map(lambda x: x*2, numbers)



# Q.
s = ['10', '20', '30', '40']

result = list(map(int, s))  # yaha 2 chiz lege 1st per jo typecast karna hai and 2nd the variable where we inisilized the value

print("Original String List:", s)
print("Converted Integer List:", result)

# Q. 
string = [' hi ', ' hello ']

result = list(map(str.strip, string)) # this strip is defined in str this is called string method. same goes for list ass well...

print("Original List:", string)
print("Cleaned List:", result)




# Q.

c = ['523', 'hi', [1, 2, 3]]
result = [len(str(item)) for item in c]

print("Original Collection:", c)
print("Length List:", result) 


# Q. i want square of a number in a list with lambda keywaord
a = [1,2,3,4,5]
result = list(map(lambda x : x**2 , a))
print("Original List:", a)
print("Square List:", result)


# Q.
# Input: ['123', '345', '764']
# Output: [321, 543, 467]

numbers = ['123', '345', '764']
result = list(map(lambda x: int(x[::-1]), numbers))

print("Original String List:", numbers)
print("Reversed Integer List:", result)


# mam method to solve
l = [123,345,764]

def rev(n):
    var = 0
    while n > 0:
        d = n%10
        var = var*10 + d
        n //= 10

    return var
print(list(map(rev,l)))




# WA map function to calculate the sum of only +ve no. print
l = [1,-5,-6,23]
result = sum(list(map(lambda x: x if x > 0 else 0, l)))

print("Original List:", l)
print("Sum of +ve Numbers:", result) 
