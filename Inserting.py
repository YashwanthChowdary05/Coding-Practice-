# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of -> 
# commands where each command will be of the  types listed above. Iterate ->
# through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    myList =[]
    for i in range(0,N):
        myCommand = input().split()
        if len(myCommand) == 3:
            myList.insert(int(myCommand[1]),int(myCommand[2]))     
        elif len(myCommand)==2:
            if myCommand[0] =="append":
                myList.append(int(myCommand[1]))
            elif myCommand[0]=="remove":
                myList.remove(int(myCommand[1]))
        else:
            if myCommand[0] =="sort":
                myList.sort()
            elif myCommand[0]=="pop":
                myList.pop()
            elif myCommand[0]=="reverse":
                myList.reverse()
            elif myCommand[0]=="print":
                print(myList)


# Input
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print             