#more condition elif ladder
num1=int(input("enter a 1 number:"))
num2=int(input("enter a 2 number:"))
num3=int(input("enter a 3 number:"))
if(num1>num2 and num1>num3):
    print(f"number {num1}is the greatest")
elif(num2>num1 and num2>num3):
        print(f"number {num2}is the greatest")
else:
            print(f"number {num3}is the greatest")