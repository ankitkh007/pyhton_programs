num = int(input("Enter a number: "))

fact = 1

# Loop to calculate factorial
for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is:", fact)