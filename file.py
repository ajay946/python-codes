
def binary_srch(lst, n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid= (l + u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False

pos=-1
lst=[1,5,3,28,267,15,2,524,21,11]
print("values are: ", lst)
lst.sort()
print("sorted list is: ", lst)
n=int(input("Enter a number to find in the list "))
if binary_srch(lst,n):
    print("Value found in the list ",pos+1)
else:
    print("Number is not in the list")
