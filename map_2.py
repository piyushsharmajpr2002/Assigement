def square(x):
    return x*x

print("Program using Map function ")
list_user=list()
for i in range(4):
    no=eval(input("enter a no "))
    list_user.append(no)
print(list_user)
output_list=map(square,list_user)
print(list(output_list))
