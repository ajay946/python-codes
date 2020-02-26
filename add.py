#Adding of two numbers

num1 = input("Enter First number: ")
num2 = input("Enter second number: ")

sum = float(num1) + float(num2) #user might also enter float nmubers
print(f'The sum of {num1} + {num2} = {sum}') #using f function
print("The sum of {0} + {1} = {2} ".format(num1,num2,sum))#using format for print