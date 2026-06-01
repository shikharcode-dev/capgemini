
#write a program to check if it is a week day or not if it is a week day then check if the employee have worked for seven hours or not. if he had worked for seven hours salleary = 20000. else deduct the sailry. if it is not a week day then print happy holiday. if it is not holiday check if he has woke up before 10 am or not. if he woke up before 10 am then print good morning. else happy holidays

day = input("Enter the day: ")
if day.lower() in ["monday",'tuesday','wednesday','thrusday','friday']:

    hours_worked = int(input("enter a hours worked: "))
    if hours_worked >= 7:
        print("sailary = 20000")
    else:
        print("sailary deduct")

else:
    print("happy hollyday")
    woke_up_time = int(input("enter wokeup time:"))
    if woke_up_time > 10:
        print("good morning")
    else:
        print("happy hollyday")



