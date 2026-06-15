
# # DECORATORS IN PYTHON - COMPLETE EXPLANATION

# # What is a Decorator?
# # A decorator is a design pattern in Python that allows you to modify or enhance
# # the behavior of functions or methods without permanently modifying them.
# # Decorators wrap another function to extend its behavior.

# # Key Concepts:
# # 1. Functions are first-class objects in Python (can be passed as arguments)
# # 2. Functions can be defined inside other functions
# # 3. Functions can return other functions

# # ============================================================================
# # BASIC EXAMPLE: Understanding the concept
# # ============================================================================

# def simple_decorator(func):
#     # This is the decorator function that takes a function as argument
#     def wrapper():
#         # This inner function wraps the original function
#         print("Before function execution")
#         func()  # Call the original function
#         print("After function execution")
#     return wrapper  # Return the wrapper function

# # Using the decorator with @ syntax
# @simple_decorator
# def say_hello():
#     print("Hello!")

# # When you call say_hello(), it actually calls wrapper() which wraps say_hello()
# # say_hello()  # Output: Before... Hello! After...


# # ============================================================================
# # DECORATOR WITH ARGUMENTS
# # ============================================================================

# def decorator_with_args(func):
#     # Wrapper accepts any number of positional and keyword arguments
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)  # Call original function with its arguments
#         print(f"Function {func.__name__} returned: {result}")
#         return result  # Return the result of original function
#     return wrapper

# @decorator_with_args
# def add(a, b):
#     return a + b

# # add(5, 3)  # Will print arguments and result


# # ============================================================================
# # DECORATOR WITH PARAMETERS (Decorator Factory)
# # ============================================================================

# def repeat(times):
#     # This is a decorator factory - it returns a decorator
#     def decorator(func):
#         # This is the actual decorator
#         def wrapper(*args, **kwargs):
#             # This wrapper executes the function multiple times
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(times=3)  # Decorator with parameter
# def greet(name):
#     print(f"Hello, {name}!")

# # greet("Alice")  # Will print greeting 3 times


# # ============================================================================
# # PRACTICAL EXAMPLE: Timer Decorator
# # ============================================================================

# import time

# def timer_decorator(func):
#     # Measures execution time of a function
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper

# @timer_decorator
# def slow_function():
#     time.sleep(1)
#     return "Done"


# # ============================================================================
# # PRACTICAL EXAMPLE: Authentication Decorator
# # ============================================================================

# def require_auth(func):
#     # Simulates authentication check
#     def wrapper(*args, **kwargs):
#         # In real scenario, check if user is authenticated
#         is_authenticated = True  # Placeholder
#         if is_authenticated:
#             return func(*args, **kwargs)
#         else:
#             print("Access denied: Authentication required")
#             return None
#     return wrapper

# @require_auth
# def sensitive_operation():
#     return "Sensitive data accessed"


# # ============================================================================
# # PRESERVING FUNCTION METADATA with functools.wraps
# # ============================================================================

# from functools import wraps

# def better_decorator(func):
#     # @wraps preserves the original function's name, docstring, etc.
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Enhanced behavior")
#         return func(*args, **kwargs)
#     return wrapper

# @better_decorator
# def documented_function():
#     """This is the docstring"""
#     pass

# # print(documented_function.__name__)  # Will print 'documented_function' not 'wrapper'


# # ============================================================================
# # CLASS-BASED DECORATORS
# # ============================================================================

# class CountCalls:
#     # Decorator implemented as a class
#     def __init__(self, func):
#         self.func = func
#         self.count = 0
    
#     def __call__(self, *args, **kwargs):
#         # __call__ makes the instance callable like a function
#         self.count += 1
#         print(f"Call {self.count} of {self.func.__name__}")
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hi():
#     print("Hi!")

# # say_hi()  # Call 1 of say_hi
# # say_hi()  # Call 2 of say_hi


# # ============================================================================
# # CHAINING MULTIPLE DECORATORS
# # ============================================================================

# def decorator_one(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Decorator 1")
#         return func(*args, **kwargs)
#     return wrapper

# def decorator_two(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Decorator 2")
#         return func(*args, **kwargs)
#     return wrapper

# @decorator_one
# @decorator_two
# def my_function():
#     print("Original function")

# # Execution order: decorator_one -> decorator_two -> my_function
# # my_function()  # Prints: Decorator 1, Decorator 2, Original function


# # ============================================================================
# # PRACTICAL EXAMPLE: Caching/Memoization Decorator
# # ============================================================================

# def memoize(func):
#     # Caches function results to avoid redundant calculations
#     cache = {}
#     @wraps(func)
#     def wrapper(*args):
#         if args in cache:
#             print(f"Returning cached result for {args}")
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
#     return wrapper

# @memoize
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)


# # ============================================================================
# # SUMMARY OF HOW TO CREATE DECORATORS:
# # ============================================================================

# # 1. Basic decorator structure:
# #    def my_decorator(func):
# #        def wrapper(*args, **kwargs):
# #            # Do something before
# #            result = func(*args, **kwargs)
# #            # Do something after
# #            return result
# #        return wrapper

# # 2. Use @wraps(func) to preserve metadata

# # 3. For decorators with parameters, use a decorator factory (nested function)

# # 4. Use *args and **kwargs to handle any function signature

# # 5. Always return the result of the original function (unless intentionally changing behavior)






# Decorator for WhatsApp-like authentication - checks authentication before and after function execution

# def decorator(func):

#     def auth():
#         print("User Authenticated")

#         func()

#         print("Action Completed")

#     return auth


# @decorator
# def send_message():
#     print("Message Sent")


# send_message() 



# create a decrotor with the pre task check the attendance, check any backlog or not, now with the main task can sit for the exam post task is get the result

# def exam(func):

#     def check():
#         attendance = True
#         backlog = False

#         if attendance and not backlog:
#             print("Eligible for Exam")

#             func()

#             print("Result Declared")

#         else:
#             print("Not Eligible for Exam")

#     return check


# @exam
# def sit_exam():
#     print("Student can sit for the exam")

# sit_exam() 