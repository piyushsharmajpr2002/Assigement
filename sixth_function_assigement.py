def total_sum(list_game):
    """this is calculate the sum of list"""
    sum=0
    for i in list_game:
        sum+=i
    print("the total sum is ",sum)

print("Game of function ")
list_game=[]
# print(type(list_game))
for i in range(0,5):
    no=int(input("enter a no "))
    list_game.append(no)
total_sum(list_game)
