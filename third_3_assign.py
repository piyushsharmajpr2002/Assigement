print("find odd no && even no ")
start_no=int(input("enter a starting  no "))
last_no=int(input("enter a last no "))
odd_count=even_count=0
print("before finding the no of odd is :",odd_count,"and even is :",even_count)
i=start_no
for  i in range(i,last_no+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
    i+=1
print("the numbers of odd is :",odd_count)
print("the numbers of even is :",even_count)


