#set is a collection which is unordered and unindexed. No duplicate members.
#we can store different data types in a single list, tuple, set or dictionary.
#add element by using add() function in set
#set can creae by using set() function or by using {}
a=set()
n=int(input("enter the number of elements:"))
print("enter the elements:")
for i in range(0,n):
    no=int(input())
    a.add(no)
print(a)
s=0
for x in a:
    s=s+i
print("sum of elements in the set is:",s)