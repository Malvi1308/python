def check():
    a=int(input("enter the lenght"))
    b=int(input("enter the bredth"))
    area=a*b
    perimeter=2*(a+b)
    if area>perimeter:
          print("the area is greater than the perimeter")
    else:
         print("the area is smaller than the perimeter")
check()    
