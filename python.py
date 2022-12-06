a=str(input("student name :"))
b=int(input("enter the english mark :"))
c=int(input("enter the tamil mark :"))
d=int(input("enter the maths mark :"))
e=b+c+d
f=e/3
print("total marks :",e)
print("avg :",f)
if b>=35 and c>=35 and d>=35:
    print("PASS")
else:
    print("FAIL")
