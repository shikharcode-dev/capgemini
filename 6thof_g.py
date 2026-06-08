# FILE HANDLING IN PYTHON - Easy Notes

# What is File Handling?
# File handling allows us to work with files on our computer
# We can read data from files, write data to files, or modify existing files

# Why use File Handling?
# - Store data permanently (data remains even after program ends)
# - Read large amounts of data
# - Share data between programs

# HOW TO OPEN A FILE
# Syntax: file_object = open(filename, mode)

# COMMON FILE MODES:
# 'r' - Read mode (default) - opens file for reading
# 'w' - Write mode - creates new file or overwrites existing file
# 'a' - Append mode - adds data to end of file
# 'r+' - Read and Write mode

# # EXAMPLE 1: Opening and Reading a file
# file = open('example.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# # EXAMPLE 2: Writing to a file
# file = open('output.txt', 'w')
# file.write('Hello, this is a test!')
# file.close()

# # EXAMPLE 3: Using 'with' statement (RECOMMENDED - automatically closes file)
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# # File automatically closes after this block

# # EXAMPLE 4: Reading line by line
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line)

# # EXAMPLE 5: Appending to a file
# with open('output.txt', 'a') as file:
#     file.write('\nThis is a new line!')

# IMPORTANT: Always close files after use or use 'with' statement



# mam ex =
# f1 = open("text.txt","w")
# f1.write("this is my first line")
# f1.close()
# print("file written successfully")


#WAP to write one line i.e. your name to a file student.txt with using open function and write my name 
# f = open("student.txt", "w")
# f.write("Shikhar")
# f.close()


# l = ["shikhar\n", "shukla\n", "python\n"]
# f = open("text.txt", "w+")
# f.write("dofvnfvn\n")
# f.writelines(l)
# f.seek(0)
# print(f.read())
# f.close()
# print("end")

# write ex=
# l1 = ["shikhar\n", "shukla\n", "python\n"]
# f = open("text.txt", "w")

# f.write("this is first line\n")
# f.writelines(l1)
# f.seek(0)
# f.close()

# f1 = open("text.txt", "r")
# print(f1.readlines())
# print(f1.read()) # that give me blank after readline 
# f1.seek(0) # using that i got all data cze i move my cursor to starting
# f1.close()
# print("done")



# Write name, age, city in 3 different lines and read using different methods
# f = open("mydata.txt", "w")
# f.write("Shikhar\n")
# f.write("25\n")
# f.write("Delhi\n")
# f.close()

# f = open("mydata.txt", "r")
# print(f.read()) 
# f.seek(0)  # Reset file pointer to beginning

# f.readline() 
# print(f.readline())
# f.seek(0)  # Reset file pointer to beginning

# print(f.readlines())
# f.close()

# print("done") 




#
# APPEND MODE ('a') - DETAILED EXPLANATION

# What is Append Mode?
# - Append mode adds new data to the END of an existing file
# - It does NOT delete or overwrite existing content
# - If file doesn't exist, it creates a new file
# - File pointer is positioned at the end of the file

# Difference between Write ('w') and Append ('a'):
# 'w' mode - Deletes all existing content and writes fresh data
# 'a' mode - Keeps existing content and adds new data at the end

# EXAMPLE 1: Basic Append
# First, let's create a file with some initial content
# f = open("notes.txt", "w")
# f.write("Line 1: Python is easy\n")
# f.write("Line 2: I love coding\n")
# f.close()

# # Now append new content without deleting existing lines
# f = open("notes.txt", "a")
# f.write("Line 3: Append mode is useful\n")
# f.write("Line 4: Old data is safe\n")
# f.close()

# # Read and verify all content is preserved
# f = open("notes.txt", "r")
# print(f.read())
# f.close()

# # EXAMPLE 2: Append with 'with' statement (RECOMMENDED)
# with open("notes.txt", "a") as f:
#     f.write("Line 5: Using with statement\n")
# # File automatically closes

# # EXAMPLE 3: Appending multiple lines using writelines()
# new_lines = ["Line 6: First new line\n", "Line 7: Second new line\n", "Line 8: Third new line\n"]
# with open("notes.txt", "a") as f:
#     f.writelines(new_lines)

# # EXAMPLE 4: Real-world use case - Adding log entries
# with open("activity_log.txt", "a") as f:
#     f.write("User logged in at 10:30 AM\n")
#     f.write("User viewed dashboard\n")
#     f.write("User logged out at 11:00 AM\n")

# # KEY POINTS TO REMEMBER:
# # 1. Append ('a') preserves old data, Write ('w') deletes it
# # 2. Always use '\n' for new lines when appending
# # 3. Perfect for logs, records, and continuous data collection
# # 4. Use 'with' statement to auto-close files

# print("Append examples completed!")










f = open("mydata.txt", "w")
f.write("Shikhar\n")
f.write("25\n")
f.write("Delhi\n")
f.close()

f = open("mydata.txt", "r")
print(f.read()) 
f.seek(0)  # Reset file pointer to beginning

f.readline() 
print(f.readline())
f.seek(0)  # Reset file pointer to beginning

print(f.readlines())
f.close()

print("done") 


f1 = open("mydata.txt", "a+")
f1.write("this is append mode")
f1.seek(0)
print(f1.read())
f1.close()





