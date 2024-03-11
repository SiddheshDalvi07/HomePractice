def fibonaci(n):
    n1=0
    n2=1
    sum=""
    print(n1)
    print(n2)
    for i in range(1,n):
        sum = n1+n2
        print(sum)
        n1=n2
        n2=sum
        
        

num = int(input("Enter the number :"))
fibonaci(num)