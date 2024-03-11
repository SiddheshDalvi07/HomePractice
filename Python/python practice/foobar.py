def foobar(n):
    for i in range(1,n+1):
        if (i%3==0 and i%5==0):
            print("foobar")
        elif (i%3==0):
            print("foo")
        elif (i%5==0):
            print("bar")
        else:
            print(i)


num = int(input("Enter the number :"))
foobar(num)