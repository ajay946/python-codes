# Simple python program to implement enum
from enum import Enum
class Cricket(Enum):
    T20 = 20
    ODI = 50
    TEST = 90
    IPL = 20

print("Is IPL considered as T20 ?")
print(Cricket.IPL==Cricket.T20)
print ("Is ODI match same as TEST match?")
print(Cricket.ODI==Cricket.TEST)

