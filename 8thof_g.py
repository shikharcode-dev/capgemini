# Generator: A generator is a special type of function in Python that returns an iterator object.
# Instead of returning all values at once using 'return', it uses 'yield' to return values one at a time.
# This makes generators memory-efficient as they generate values on-the-fly rather than storing them all in memory.
# 
# Key characteristics:
# - Uses 'yield' keyword instead of 'return'
# - Maintains state between calls
# - Can be iterated only once
# - Saves memory by generating values lazily (one at a time)
#
# Example:
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count  # Returns count and pauses here
#         count += 1
#
# Usage:
# counter = count_up_to(5)
# for num in counter:
#     print(num)  # Prints: 1, 2, 3, 4, 5
#
# In this example, count_up_to() is a generator that yields numbers from 1 to n.
# Each time yield is called, it returns a value and pauses, resuming from that point on the next iteration. 






#mam ex=
# def number():
#     for i in range(1,6):
#         yield i
# for j in number():
#     print(j)

# create a genrator to genrates the squre of numbers from 1 to 5 and diaplay then by using for loop
# def square():
#     for i in range(1,6):
#         yield i*i 
# for j in square():
#     print(j) 






#Expceptation handling

# try:
#     n1 = int(input("Enter first number: "))
#     n2 = int(input("Enter second number: "))
#     result = n1/n2

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")



# Problem: Get a number from user and handle exceptions when user provides invalid input (non-integer)
# Example outputs:
# If user enters "42":
#   You entered: 42
# If user enters "hello":
#   Error: Please enter a valid integer
# If user enters "3.14":
#   Error: Please enter a valid integer
# If user enters "":
#   Error: Please enter a valid integer
# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Error: Please enter a valid integer")


# try to handle value error by using generic expectation handlling
# try:
#     num = int(input("Enter a number: "))

#     print("You entered:", num)

# except Exception as e:
#     print("Error occurred:", e)




# import time
# try:
#     while True:
#         print("progrm runing... press ctrl+c to stop.")
#         time.sleep(1)

# except:
#     print("unexpected error occured")

# finally:
#     print("program stopped.")



