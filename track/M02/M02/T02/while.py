# Read the value of n
n = int(input())

# Initialize the counter and total
counter = 0
total = 0
# Loop while the counter is less than n
while counter <= n:
    total = total + counter
    counter += 1

# Display the total
print(f"Total: {total}")