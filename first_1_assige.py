print("Fibonacci Series Between 0 to 50")
num_till=int(input("enter a no which you want to stop fibonacci series  "))
i=0
a,b=0,1
while i!=num_till:
    a=a+b
    b=a-b
    print(a,end=" ")
    i+=1
print("\n program end")    

