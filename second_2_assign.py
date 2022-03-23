print("Reverse a word ")
word_name=input("enter a word which you want to print reverse ")
# print(word_name[::-1])
#print(len(word_name))
for i in range((len(word_name)-1),-1,-1):
    print(word_name[i],end=" ")