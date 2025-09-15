num=int((input("Enter a number: ")))
temp=num
sum=0
#pow=len(str(num))
while num!=0:
    digit=num%10
    sum+=digit**len(str(temp))
    num//=10
if sum==temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")