x=int(input("Enter the starting number of the interval: "))
y=int(input("Enter the ending number of the interval: "))

for n in range(x, y+1):
    if n<=1:
        continue
    flag=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag=False
            break

    if flag:
        print(n)