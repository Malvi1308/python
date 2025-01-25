def compare():

    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    c=int(input("enter the value of c"))
    l=a
    if b>l:
      l=b
    if c>l:
      l=c
    s=a
    if s>c:
     s=c
    if s>b:
     s=b
    if l==s:
        print("all values are same")
    else:
        print(l,"largest",s,"smallest")
compare()
