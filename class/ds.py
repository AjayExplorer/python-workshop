#list is a collection which is ordered and changeable. Allows duplicate members.
#tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#set is a collection which is unordered and unindexed. No duplicate members.
#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#we can store different data types in a single list, tuple, set or dictionary.
#add element by using append() function in list and set
#add element by using add() function in set
#add element by using update() function in set

#write  a program to sum of  even element in a list
a=list()
n=int(input("enter the umber of elements"))
print("enter the elements")
for i in range(0,n):
    k=int(input())
    a.append(k)
s=0
for i in range(0,n):
        if(a[i]%2==0):
         s=s+a[i]
print("sum of elements in the list is:",s)