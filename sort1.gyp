import os
import sys

list1 =[]

def check ():
    k = int(input("input 0 to stop adding numbers: "))
    if k != 0:
        list1.append(k)
        check()
    else: 
        print("These are the results: ")
        
def sol ():
    list1.sort(reverse = True)
    y = list1[0] * list1[1] * list1[2]
    print(str(list1[0])+ " x " +str(list1[1])+ " x " +str(list1[2])+ " = " +str(y))

print("\nEnter your numbers and we will calculate the product for the highest 3 values.")

check()
sol()




    








