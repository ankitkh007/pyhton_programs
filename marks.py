m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))

total = m1 + m2 + m3 + m4
average = total / 4

print("Total Marks =", total)
print("Average Marks =", average)

if average > 90:
    print("Grade = O")
elif average >= 80 and average <= 90:
    print("Grade = A")
elif average >= 70 and average <= 79:
    print("Grade = B")
elif average >= 60 and average <= 69:
    print("Grade = C")
else:
    print("Grade = Fail")