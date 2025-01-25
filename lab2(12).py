def check():
    x=int(input("enter the value of x"))
    y=int(input("enter the value of y"))
    x1=int(input("enter the value of x1"))
    y1=int(input("enter the value of y1"))
    r=int(input("enter the value of r"))
    if (x*x1)+(y*y1)==r*r:
        print("the points are lying on circle")
    else:
        print("the points are not lying on circle")
check()
