from random import randint
def lottery():
    # returns 6 numbers between 20 and 40
    for i in range(6):
        yield randint(20, 40)

    # returns a 7th number between 1 and 15 and then again a number between 1 and 2
    yield randint(1,15)
    yield randint(1, 2)
for random_number in lottery():
       print("And the next number is... %d" %(random_number))