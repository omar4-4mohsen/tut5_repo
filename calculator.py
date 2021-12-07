x= input("enter first number ")
y= input ("enter second number")
operation=input("choose opersation")
again = True
while(again):
    if(operation=="+"):
        again=False
        result=x+y
        print("result is : "+result)
    elif(operation=="-"):
        again=False
        result=x-y
        print("result is : "+result )
    else:
        print("undefined operation")