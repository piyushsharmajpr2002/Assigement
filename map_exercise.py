def triple(a):
    return a*2+a

print("Program triple all no ")
list_given=[1,2,3,4,5,6,7]
print("the expected output")
new_list=map(triple,list_given)
print(list(new_list))
