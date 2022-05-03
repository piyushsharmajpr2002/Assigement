print("oops exercise ")
class Power:
    def __init__(self,x):
        print("find the power of no??  ",x)
    
    def find(self,base,expo):
        #print("hello")
        i=1
        f=1
        while i<=expo:
            f=f*base
            i+=1
        print(f' the power of no  is {f}')    

expo=eval(input("enter a expo of no "))
base=eval(input("enter a pow "))
# create class object 
obj=Power(base)
obj.find(base,expo)


          