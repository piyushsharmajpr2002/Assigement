print("Fun with lists and tuples")
sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
length=len(sample_list)
# print(length)
for i in range(0,length):
    # key=sample_list[i][1]
    for j in range(0,length-1):
     if    sample_list[j][1] > sample_list[j+1][1]:
          temp=sample_list[j]
          sample_list[j]=sample_list[j+1]
          sample_list[j+1]=temp

         

                                        
print(sample_list)
              