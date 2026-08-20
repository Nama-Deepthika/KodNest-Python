# Read marks, attendance and project completion status
Marks = int(input())
Attendance = int(input())
Project_completion = input()

# Check the academic requirements
if Marks >= 60 and Attendance >= 75:

    # Check the project completion status
    if Project_completion == "Yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")