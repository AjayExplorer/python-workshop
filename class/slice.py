#tuple  =>  immutable sequence types
#list   =>  mutable sequence types
a=()
n=int(input("enter the number of elements:"))
for i in range(0,n):
    no=int(input())
    a=a+(no,)
print(a)
s=0
for i in range(0,n):
    s=s+a[i]
print("sum of elements in the tuple is:",s)
