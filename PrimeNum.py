# To find prime number in a given range

start = int(input("Start: "))
end = int(input("End: "))
for i in range(start, end +1):

    # if number is divisible by any number between 2 and i it is not prime
    if i >1 :
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)
