from addition import add
from multiplication import multiply
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
num4=int(input("enter the fourth number"))
if(num1%2!=0 and num2%2!=0 and num3%2!=0 and num4%2!=0):
    import sys
    sys.stdout = open(r'C:\Users\VIRAJ\Desktop\python assesment\output.txt',"a")
    print("no even number is present")
else:
    addres=add(num1,num2,num3,num4)
    mulres=multiply(num1,num2,num3,num4)
    import sys
    sys.stdout = open(r'C:\Users\VIRAJ\Desktop\python assesment\output.txt',"a")
    print("add of even numbers is:",addres)
    print("mul of even numbers is:",mulres)
