# WAP to print a series "1 + 2 + .....+ n"

n = int(input("Enter a number: "))

# Print the series
for i in range(1, n + 1):
    print(i, end="")  # Print the current number
    if i < n:  # If not the last number, print a "+" after it
        print(" + ", end="")

# Calculate and print the sum
print(" =", sum(range(1, n + 1)))
