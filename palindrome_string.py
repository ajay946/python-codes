#program to check if a string is a palindrome
mystr = str(input("Enter the string: "))#takes input from user
mystr = mystr.casefold()#Caseless comparision
revstr = reversed(mystr) # to reverse the string
if list(mystr) == list(revstr):# to check if reverse is same as actual string
    print("String is a palindrome ")
else:
    print("String is not a palindrome")

#using inbuilt method
x= input("Enter a string: ")
if (x == x[::-1]):
    print("String is palindrome")
else:
    print("String is not a palindrome")