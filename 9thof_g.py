# #c
# # CUSTOM EXCEPTIONS AND EXCEPTION HANDLING IN PYTHON

# # 1. CREATING CUSTOM EXCEPTIONS
# # Syntax: class CustomExceptionName(Exception):
# #         Custom exception classes inherit from the Exception base class

# class InsufficientBalanceError(Exception):
#     """Custom exception for insufficient balance in bank account"""
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         self.message = f"Insufficient balance. Available: ${balance}, Required: ${amount}"
#         super().__init__(self.message)

# class InvalidAgeError(Exception):
#     """Custom exception for invalid age"""
#     def __init__(self, age):
#         self.age = age
#         self.message = f"Invalid age: {age}. Age must be between 0 and 120"
#         super().__init__(self.message)

# # 2. RAISING EXCEPTIONS
# # Syntax: raise ExceptionName("error message")
# # The 'raise' keyword is used to manually trigger an exception

# def withdraw_money(balance, amount):
#     """Function demonstrating raising custom exception"""
#     if amount > balance:
#         # Raising our custom exception
#         raise InsufficientBalanceError(balance, amount)
#     return balance - amount

# def validate_age(age):
#     """Function demonstrating raising custom exception with validation"""
#     if age < 0 or age > 120:
#         raise InvalidAgeError(age)
#     return True

# # 3. HANDLING EXCEPTIONS
# # Syntax: try:
# #             # code that might raise exception
# #         except ExceptionName as e:
# #             # handle the exception
# #         finally:
# #             # always executes

# # Example 1: Handling custom exception
# try:
#     current_balance = 1000
#     withdrawal_amount = 1500
#     new_balance = withdraw_money(current_balance, withdrawal_amount)
#     print(f"Withdrawal successful. New balance: ${new_balance}")
# except InsufficientBalanceError as e:
#     print(f"Error: {e.message}")
#     print(f"You tried to withdraw ${e.amount} but only have ${e.balance}")

# # Example 2: Handling multiple exceptions
# try:
#     user_age = -5
#     validate_age(user_age)
#     print("Age is valid")
# except InvalidAgeError as e:
#     print(f"Error: {e.message}")
# except Exception as e:
#     print(f"Unexpected error: {e}")

# # Example 3: Try-except-else-finally
# try:
#     age = 25
#     validate_age(age)
# except InvalidAgeError as e:
#     print(f"Validation failed: {e}")
# else:
#     # Executes only if no exception was raised
#     print(f"Age {age} is valid!")
# finally:
#     # Always executes regardless of exception
#     print("Validation process completed")

# # Example 4: Re-raising exceptions
# def process_transaction(balance, amount):
#     try:
#         return withdraw_money(balance, amount)
#     except InsufficientBalanceError as e:
#         print(f"Transaction failed: {e.message}")
#         # Re-raising the same exception to be handled at higher level
#         raise

# # Example 5: Chaining exceptions (Python 3+)
# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # Raising a new exception while preserving the original
#     raise ValueError("Cannot perform calculation") from e 





# Q. create an error if even so ok if odd so error will occur
class OddError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num % 2 != 0:
        raise OddError

    print("OK")

except OddError:
    print("Error: Odd number entered")

finally:
    print("End of program.")




# MODULES IN PYTHON - DETAILED EXPLANATION 

# What is a Module?
# A module is a file containing Python definitions, functions, classes, and statements.
# Modules help organize code into reusable components and avoid naming conflicts.
# Any Python file (.py) can be used as a module.

# 1. TYPES OF MODULES
# - Built-in modules: Pre-installed with Python (e.g., math, os, sys, datetime)
# - Third-party modules: Installed via pip (e.g., numpy, pandas, requests)
# - User-defined modules: Custom modules created by developers

# 2. IMPORTING MODULES - DIFFERENT WAYS

# Method 1: Import entire module
# Syntax: import module_name
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793

# Method 2: Import specific items from module
# Syntax: from module_name import item1, item2
from math import sqrt, pi
print(sqrt(25))  # Output: 5.0
print(pi)  # Output: 3.141592653589793

# Method 3: Import all items from module (not recommended)
# Syntax: from module_name import *
from datetime import *
print(datetime.now())  # Current date and time

# Method 4: Import with alias
# Syntax: import module_name as alias
import numpy as np  # Common practice for numpy
import pandas as pd  # Common practice for pandas

# Method 5: Import specific item with alias
# Syntax: from module_name import item as alias
from math import sqrt as square_root
print(square_root(36))  # Output: 6.0

# 3. CREATING CUSTOM MODULES
# Example: Create a file named 'mymodule.py' with the following content:
# def greet(name):
#     return f"Hello, {name}!"
# 
# def add(a, b):
#     return a + b
# 
# PI = 3.14159
#
# Then import and use it:
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.add(5, 3))
# print(mymodule.PI)

# 4. MODULE SEARCH PATH - HOW PYTHON FINDS MODULES
# When you import a module, Python searches for it in the following order:

# Step 1: Current directory (where the script is running)
# Step 2: PYTHONPATH environment variable directories
# Step 3: Standard library directories
# Step 4: Site-packages directory (third-party modules)

# You can view the search path using sys.path:
import sys
print("Python Module Search Path:")
for path in sys.path:
    print(path)

# 5. MODIFYING THE MODULE SEARCH PATH
# You can add custom directories to the search path:
import sys
sys.path.append('/path/to/your/modules')  # Add directory to search path
sys.path.insert(0, '/priority/path')  # Add directory at the beginning (highest priority)

# 6. USEFUL MODULE ATTRIBUTES
# __name__: Name of the module
# __file__: Path to the module file
# __doc__: Documentation string of the module
# __package__: Package name (for packages)

import math
print(f"Module name: {math.__name__}")  # Output: math
print(f"Module file: {math.__file__}")  # Output: path to math module
print(f"Module doc: {math.__doc__[:50]}...")  # First 50 chars of documentation

# 7. THE __name__ VARIABLE
# When a Python file is run directly, __name__ is set to "__main__"
# When imported as a module, __name__ is set to the module name
# This allows code to behave differently when run directly vs imported

# Example in a module file:
# if __name__ == "__main__":
#     # This code runs only when file is executed directly
#     print("Running as main program")
# else:
#     # This code runs when imported as module
#     print("Imported as module")

# 8. PACKAGES
# A package is a collection of modules organized in directories
# Packages contain a special __init__.py file (can be empty)
# Example package structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py

# Importing from packages:
# import mypackage.module1
# from mypackage import module2
# from mypackage.subpackage import module3

# 9. COMMONLY USED BUILT-IN MODULES

# os module - Operating system interface
import os
print(f"Current directory: {os.getcwd()}")
print(f"List files: {os.listdir('.')}")

# sys module - System-specific parameters and functions
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")

# datetime module - Date and time operations
from datetime import datetime, timedelta
now = datetime.now()
print(f"Current time: {now}")
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# random module - Random number generation
import random
print(f"Random number: {random.randint(1, 100)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

# json module - JSON encoding and decoding
import json
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# 10. RELOADING MODULES
# Modules are loaded only once per interpreter session
# To reload a module after changes, use importlib.reload()
import importlib
# importlib.reload(mymodule)  # Reloads the module

# 11. BEST PRACTICES
# - Import modules at the top of the file
# - Use specific imports (from module import item) for clarity
# - Avoid wildcard imports (from module import *) to prevent naming conflicts
# - Use aliases for long module names (import numpy as np)
# - Group imports: standard library, third-party, local modules
# - One import per line for better readability






# MODULES AND LIBRARIES IN PYTHON - DEFINITIONS AND EXAMPLES

# DEFINITION OF MODULE:
# A module is a single Python file (.py) that contains Python code including functions, classes, and variables.
# It helps organize code into logical, reusable components.
# Example: math.py, os.py, datetime.py are all modules

# EXAMPLE OF MODULE:
# Using the built-in 'math' module
import math
result = math.sqrt(16)  # Using sqrt function from math module
print(f"Square root of 16: {result}")  # Output: 4.0
print(f"Value of PI: {math.pi}")  # Output: 3.141592653589793

# DEFINITION OF LIBRARY:
# A library is a collection of related modules bundled together to provide extended functionality.
# It's a broader term that encompasses multiple modules working together for a common purpose.
# Libraries can contain packages (directories with multiple modules) and sub-packages.
# Example: NumPy, Pandas, Requests are libraries that contain multiple modules

# EXAMPLE OF LIBRARY:
# Using the 'datetime' library which contains multiple modules (datetime, date, time, timedelta, etc.)
from datetime import datetime, timedelta
current_time = datetime.now()  # Using datetime module from datetime library
print(f"Current date and time: {current_time}")
future_date = current_time + timedelta(days=7)  # Using timedelta module
print(f"Date after 7 days: {future_date}")

# KEY DIFFERENCE:
# Module = Single file with Python code
# Library = Collection of multiple modules/packages working together for a broader purpose







# EXPLANATION OF THE sys MODULE IN PYTHON
# The 'sys' module provides access to system-specific parameters and functions
# It allows interaction with the Python interpreter and the runtime environment
# 'sys' stands for "system" and is a built-in module (no installation required)

# Key features and commonly used functions of the sys module:

# 1. sys.argv - Command line arguments
#    Returns a list of command line arguments passed to the script
#    sys.argv[0] is the script name, sys.argv[1:] are the arguments

# 2. sys.path - Module search path
#    A list of strings that specifies the search path for modules
#    Can be modified to add custom module directories

# 3. sys.version - Python version information
#    Returns a string containing the Python version number and build information

# 4. sys.platform - Platform identifier
#    Returns the platform name (e.g., 'win32', 'linux', 'darwin' for macOS)

# 5. sys.exit() - Exit the program
#    Terminates the Python program with an optional exit status code

# 6. sys.stdin, sys.stdout, sys.stderr - Standard I/O streams
#    File objects for standard input, output, and error streams

# 7. sys.modules - Dictionary of loaded modules
#    Contains all modules that have been imported in the current session

# 8. sys.maxsize - Maximum integer size
#    Returns the largest integer supported by the platform

# Example usage of sys module functions:
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Module search paths: {sys.path}")
print(f"Maximum integer size: {sys.maxsize}")






# sys.exit() - Exit the program
# The exit() function terminates the Python program immediately
# It raises a SystemExit exception which can be caught if needed
# Syntax: sys.exit([status_code])
# - status_code is optional (default is 0)
# - 0 means successful termination
# - Non-zero values (typically 1) indicate an error or abnormal termination
# - Can also pass a string message which will be printed to stderr

# Example 1: Exit with default status code (0)
import sys
# sys.exit()  # Program terminates here with status 0

# Example 2: Exit with custom status code
# sys.exit(1)  # Program terminates with error status 1

# Example 3: Exit with error message
# sys.exit("An error occurred!")  # Prints message and exits with status 1

# Example 4: Conditional exit
age = 15
if age < 18:
    sys.exit("Access denied: Must be 18 or older")  # Exits if condition is true
print("Access granted")  # This line won't execute if exit() is called

# Example 5: Exit in exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    sys.exit(1)  # Exit with error code

# Example 6: Catching SystemExit exception
try:
    sys.exit("Attempting to exit")
except SystemExit as e:
    print(f"Exit was called with: {e}")
    # Program continues instead of exiting




# sys.version - Returns detailed Python version information as a string
# This includes the version number, build date, compiler used, and other details
# Format: 'major.minor.micro releaseLevel serialNumber (build info) [compiler]'
import sys
print(sys.version)

# sys.path - Explanation
# sys.path is a list that contains the directories where Python searches for modules when you use import statements
# When you import a module, Python looks through each directory in sys.path in order until it finds the module
# This list determines the module search path and can be modified to include custom directories
# By default, sys.path includes:
#   1. The directory containing the script being run (or current directory in interactive mode)
#   2. Directories listed in the PYTHONPATH environment variable
#   3. Standard library directories
#   4. Site-packages directory (where third-party packages installed via pip are stored)
# You can view sys.path to see all directories Python searches for modules
# You can also modify sys.path by appending or inserting directories to add custom module locations






class Resume10th:

    def __init__(self, name, age, marks10):
        self.name = name
        self.age = age
        self.marks10 = marks10

    def show10(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("10th Marks:", self.marks10)

class Resume12th(Resume10th):
