def smart_div(func):
    print("I am Smart_div")
    # this is a decorator which add more functionality to the actual div function
    def inner(a,b):
        #we compare if numerator is smaller than denominator if yes we swap values
        if a<b:
            a,b =b,a
        return func(a,b)
    return inner
#this is the way we create a ON/OFF switch for the decorator by just commenting the @smart_div
@smart_div
def div(a,b):
    print("i am div")
    print(a/b)
# so here when we call the div method the smart_div will take div as a parameter and will
# first run smart_div than the original div method
div(2,4)