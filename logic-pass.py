# #Task1
# ##Programe to remove Character from word
# def remove():
#     #input Data from user
#     word=input("enter word : ")
#     char=input("enter char : ")
#     #loop to check char
#     for i in word :
#         if i == char:
#             #replace char by empty
#            word2= word.replace(i,'')
#     print(word2)
# remove()
 

# #Task2

# Program to check if a number is prime or not
# # To take input from the user
# num = int(input("Enter a number: "))
# # define a flag variable
# flag = False
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")


#task3
#Programe to count repeat of Char
def Count():
    #take data from user
    word=input("enter word : ")
    char=input("enter char : ")
    #variable count to store value for later
    count=0
    #loop to check
    for i in word :
        if i == char:
         count+=1
    print(f"count number of {char} is {count}")
Count()