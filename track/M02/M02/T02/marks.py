# Read the number of students
student = int(input())

# Initialize the total and counters
total = 0
passed = 0
failed = 0

# Read and process each mark
for i in range(student):
    mark = int(input())
    tatal = total + mark
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

# Calculate average and display
print(f"Total Marks: {total}")
print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}")

# Display the batch result
if failed == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")

