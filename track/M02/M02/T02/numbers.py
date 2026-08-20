# Read how many numbers will be entered
number_count = int(input())

# Initialize the counters and total
positive = 0
negative = 0
zero = 0
total = 0

# Read and analyze each number
for i in range(number_count):
    num = int(input())
    total = total + num
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1
    else:
        zero = zero + 1

# Display the final analysis
print(f"Positive Count: {positive}")
print(f"Negative Count: {negative}")
print(f"Zero Count: {zero}")
print(f"Total: {total}")



    
    

