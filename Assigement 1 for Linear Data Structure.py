#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question 1 :-

arr=[5,6,4,7,6,3]
target_no=11
pair_array=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        sum=arr[i]+arr[j]
        if sum == target_no:
            pair_array.append([arr[i],arr[j]])
            
        
print(pair_array)


# In[28]:


# QUESTION  2 :-

arr=[4,1,0,9,4,5,8] #6
arr.reverse()
print(arr)


# In[31]:


# Question 3.

str1=input("enter a string 1")
str2=input("enter a string 2")
if len(str1) == len(str2):
    temp=str1+str1
    if str2 in temp:
        print("rotation")
    else :
        print("no rotation")
else :
    print("no rotation ")
    


# In[35]:


# Question 4
# aagcdefccb

str=input("enter a string ")
#str="aagcdefccb"
count=0
d={}
for i in range(len(str)):
    if str[i] in d.keys():
        continue
    for j in range(i+1,len(str),1):
        if str[i] == str[j]:
            #print("yes",str[j])
            count+=1
    d[str[i]]=count
    count=0

for i in d:
    if d[i]==0:
        print("First Non-repeated value is ",i)
        break
    
print(d)


# In[44]:


# Question 5 :-

class Stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.stack3=[]
    
    def push1(self,data):
        self.stack1.append(data)
    
    def pop1(self):
        if len(self.stack1)==0:
            return "Empty stack1"
        return self.stack1.pop(len(self.stack1)-1)
    
    def push2(self,data):
        self.stack2.append(data)
    
    def pop2(self):
        if len(self.stack2)==0:
            return "Empty stack2"
        return self.stack2.pop(len(self.stack2)-1)
    
    def push3(self,data):
        self.stack3.append(data)
    
    def pop3(self):
        if len(self.stack3)==0:
            return "Empty stack3"
        return self.stack3.pop(len(self.stack3)-1)
    
    def peek(self):
        return self.stack3[len(self.stack3)-1]
        

obj=Stack()
obj.push1(3)
obj.push1(2)
obj.push1(1)
#  retrive from stack1 (3)
value=obj.pop1()
# push into stack2 3
obj.push3(value)

# retrive from stack1 2
val=obj.pop1()
# push into stack2 (2)
obj.push2(val)

# retrive from stack3 3
value=obj.pop3()
# push into stack2 (3)
obj.push2(value)

# retrive from stack1 (1)
value=obj.pop1()
obj.push3(value)

# retrive from stack2  (2)
value=obj.pop2()
obj.push1(value)

# retrive from stack2 (1)
value=obj.pop2()
obj.push3(value)

# retrive from stack1 ()
value=obj.pop1()
obj.push3(value)


    


# In[70]:


# Question 6 :-    AND    Question 7 : As Well 

"""
Infix   :-  a+b
Postfix :-  ab+
Prefix  :-  +ab
"""

class Stack :
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value
    
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]
    
    def postfix_to_prefix(self,exp):
        str=""
        for i in range(len(exp)):
            
            if i==len(exp)-1:          
                while len(self.stack) != 0:
                        value1=self.pop()
                        value2=self.pop()
                        print("yes")
                        str=str+exp[i]+value2+value1
                        return str
        
            elif exp[i].isalpha():
                 self.push(exp[i])
                
            elif exp[i]=='/' or exp[i]=='+' or  exp[i]=='*' or exp[i]=='-':
                 if len(self.stack)!=0:
                    value1=self.pop()
                    value2=self.pop()
                    str=str+exp[i]+value2+value1
                    self.push(str)
                    str=""
    
            
            
    def  prefix_to_infix(self,exp): # EDC/BA*-+
        exp=exp[::-1]
        str=""
        for i in range(len(exp)):
            
            if i==len(exp)-1:          
                while len(self.stack) != 0:
                        value1=self.pop()
                        value2=self.pop()
                        #print("yes")
                        str=str+value1+exp[i]+value2
                        return str
        
            elif exp[i].isalpha():
                 self.push(exp[i])
                
            elif exp[i]=='/' or exp[i]=='+' or  exp[i]=='*' or exp[i]=='-':
                 if len(self.stack)!=0:
                    value1=self.pop()
                    value2=self.pop()
                    str=str+value1+exp[i]+value2
                    self.push(str)
                    str=""
         
        
                

obj=Stack()
# POSTFIX TO PREFIX 

result=obj.postfix_to_prefix("ABC/-AK/L-*")
print("Prefix expression is =",result)

# PREFIX TO INFIX
print(obj.prefix_to_infix("+-*AB/CDE"))


# In[73]:


# Question 8 :-

class Stack :
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]

    def check_same(self,i,j):
        if j == '{' and i == '}':
            return 1
        elif j == '[' and i == ']':
            return 1
        elif j == '(' and i == ')':
            return 1
        return 0

# {[()]}
    def parenthesis_balanced(self,str):
        for i in str:
            if i == '{' or i == '[' or i == '(':
                self.push(i)
            elif i == '}' or i == ']' or i == ')':
                if len(self.stack) == 0:
                    return 0
                value = self.peek()

                if(self.check_same(i,value)):
                    self.pop()
                else:
                     return 0
        if len(self.stack) == 0:
               return 1
        return 0



s=Stack()
if s.parenthesis_balanced("()[({})]"):
    print("balanced")
else:
    print("not balanced ")


# In[76]:


# Question 9 :-   And     Question 10 :-                 As Well
class Using_stack:
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]

    def reverse_a_stack(self):
        temp=self.stack[::-1]
        return temp
    
    def find_smallest_no(self):
        min_value=999999
        for i in range(len(self.stack)):
            if self.stack[i] < min_value:
                min_value=self.stack[i]
        return min_value
        
        

obj=Using_stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(f"Before Reverse {obj.stack}")
print(f"After Reverse {obj.reverse_a_stack()}")

# SMALLEST NO function Call

print(f"SMALLEST NUMBER IS  {obj.find_smallest_no()}")


# In[ ]:


# END THE ASSIEGEMENT MA'AM SOME QUESTION I MERGED PLEASE CHECK CAREFULLY LIKE...
    #    QUESTION : 6 AND 7
    #    QUESTION  : 9 AND 10
    
    
    # BUT IT'S WORKING 

