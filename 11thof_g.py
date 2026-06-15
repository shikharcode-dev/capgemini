# Regular Expression (RegEx)
# 
# Regular expressions are powerful patterns used for matching and manipulating text.
# They allow you to search, match, and replace text based on specific patterns.
# 
# In Python, we use the 're' module to work with regular expressions.
# 
# Common RegEx Patterns:
# - '.' : Matches any single character except newline
# - '^' : Matches the start of a string
# - '$' : Matches the end of a string
# - '*' : Matches 0 or more repetitions
# - '+' : Matches 1 or more repetitions
# - '?' : Matches 0 or 1 repetition
# - '\d' : Matches any digit (0-9)
# - '\w' : Matches any word character (letters, digits, underscore)
# - '\s' : Matches any whitespace character
# - '[abc]' : Matches any character in the set (a, b, or c)
# - '[^abc]' : Matches any character NOT in the set
# - '(pattern)' : Groups patterns together
# 
# Example 1: Basic pattern matching
# import re
# text = "My phone number is 123-456-7890"
# pattern = r'\d{3}-\d{3}-\d{4}'  # Pattern for phone number
# match = re.search(pattern, text)
# if match:
#     print(match.group())  # Output: 123-456-7890
# 
# Example 2: Finding all email addresses
# import re
# text = "Contact us at info@example.com or support@test.org"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# emails = re.findall(pattern, text)
# print(emails)  # Output: ['info@example.com', 'support@test.org']
# 
# Example 3: Replacing text
# import re
# text = "The price is $100 and $200"
# pattern = r'\$\d+'
# result = re.sub(pattern, 'PRICE', text)
# print(result)  # Output: The price is PRICE and PRICE
# 
# Example 4: Validating input
# import re
# def validate_password(password):
#     # Password must be 8+ chars, contain uppercase, lowercase, digit, and special char
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
#     return bool(re.match(pattern, password))
# 
# Example 5: Splitting strings
# import re
# text = "apple,banana;orange|grape"
# result = re.split(r'[,;|]', text)
# print(result)  # Output: ['apple', 'banana', 'orange', 'grape']






import re

text = 'Hi I am sam'
re.findall('[a-z]*', text)
print(text) 


import re 
text = 'Shikhar '