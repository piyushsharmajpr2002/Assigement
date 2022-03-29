def find(str,length):
    # str=list(tr)
    no_of_lower=0
    no_of_upper=0
    for i in range(length):
        if str[i]==' '  or  bool(str[i].isdigit)==str[i].isdigit():
            continue
        elif   str[i]== str[i].upper():
             no_of_upper+=1
        
        elif str[i]==str[i].lower():
             no_of_lower+=1
        
        else:
            pass
    print("the no of upper case letter is ",no_of_upper)
    print("the no of lower case letter is ",no_of_lower)
    
print("calculate the Upper and Lower case letter")
str=input("enter a string  ")
length=len(str)
find(str,length)
# str=input("enter a string ")
# print(str.isdigit())  <--- true / false