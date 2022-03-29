# ord => takes character  and  chr=> takes value
from unittest.loader import VALID_MODULE_NAME


print("make your own mini dictionary")
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dict_list=dict()
# print(type(dict_list))
length=len(list)
for i in range(length):
    dict_list[list[i]]=ord(list[i])

print(dict_list)

