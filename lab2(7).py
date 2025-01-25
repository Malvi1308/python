def check():
    a=int(input("enter the value of a"))
    if a%400==0:
        if a%100==0:
            if a%4==0:
               print ("a is the leap year")
    else:
        print("a is not leap year")
check()
          
