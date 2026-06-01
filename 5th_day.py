'''age = input("Please enter your age: ")
if(age>=18):
    print("You are eligible to vote.")
else:
    print("baccha hai chalaja.")'''

#write a program to check if number is even or odd
'''num = int(input("Enter a number: "))
if(num%2==0):
    print("Even number.")
else:
    print("Odd number.")'''

#write a program to check if number is divisible by 5 or not, if not divisible by 5 then check if it is divisible by 3 or not check if it is divisible by 3 or not

'''num = int(input("Enter a number: "))
if(num%5==0):
    print("Divisible by 5.")

elif(num%3==0):
    print("Divisible by 3.")   

else:
    print("Not divisible by 5 or 3.")'''

#write a program to check grade of students above 50 grade d, avove 70 grade c, above 80 grade b, above 90 grade a

'''grade = int(input("Enter your grade: "))
if(grade>=90): 
    print("Grade A.")
elif(grade>=80):
    print("Grade B.")
elif(grade>=70):
    print("Grade C.")
elif(grade>=50):
    print("Grade D.")'''  #if agar opposit likhta to 50 per hi check karke bahar aajayega wo aage check nhi karega so we have to write in this order only i.e. increasing order. thus is apply on if i added if added a range between that like
#elif(grade>=50 and grade<70):
    #print("Grade D.") so we uing that.

#Nested and Nested if else statement.

#Write a program to check if the number is two digit or not and if it is two digit then check if it is even or odd. if it is not two digit then divide it by ten and print the remainder.
'''num = int(input("Enter a number: "))
if(num>=10 and num<100):
    if(num%2==0):
        print("Even number.")
    else:
        print("Odd number.")
else:
    remainder = num % 10
    print("Not a two digit number. Remainder when divided by 10:", remainder)'''

#write a program to check if it is a week day or not if it is a week day then check if the employee have worked for seven hours or not. if he had worked for seven hours salleary = 20000. else deduct the sailry. if it is not a week day then print happy holiday. if it is not holiday check if he has woke up before 10 am or not. if he woke up before 10 am then print good morning. else happy holidays

day = input("Enter the day of the week: ")
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    hours_worked = int(input("Enter the number of hours worked: "))
    if hours_worked >= 7:
        print("Salary: 20000")
    else:
        print("Salary deducted.")
else:
    print("Happy holiday.")
    wake_up_time = input("Enter the time you woke up: ")
    if wake_up_time < "10:00":
        print("Good morning.")
    else:
        print("Happy holidays.")