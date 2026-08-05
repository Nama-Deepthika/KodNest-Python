Marks = int(input())
Attendance = int(input())
Project_completion = input()

if Marks >= 60 and Attendance >= 75:
    if Project_completion == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")