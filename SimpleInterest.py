#To calculate simple interest given principle amount, time and rate of interest

p = float(input("Enter the principle amount: "))
t = float(input("Enter the time(yrs): "))
r = float(input("Enter the rate of interest: "))
# to find simple interest multiple all three values and divide by 100
SI = (p * r * t)/100
print(f"Simple Interest is {}".format(SI))
