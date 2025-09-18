#break and continue statement in python
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i==5:
        continue#it will stop the loop when i is equal to 5
    print(i)
else:
    print("hello") #it will not print hello because the loop is terminated by break statement