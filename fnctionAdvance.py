def add(a,b,c):
    d = a+b+c
    print("sum is "+ str(d))

# x=int(input("enter first no "))
# y =int(input("enter second no "))
# z =int(input("enter third no "))

# add(x,y,z)
#Done-Simple
#voting
# def canVote(username,age):
#     if(age>=18):
#         print(username+" you are eligible for voting")
#     else:
#         print(username+ " you are not eligible for voting")
#
# n = input("enter your name")
# a = int(input("enter your age"))
# canVote(n,a)



def canVote(username,age):
    if(age>=18 and age<=120):
        print(username+" you are eligible for voting")
    else:
        if (age > 0 and age<121):
            print(username + "you are not eligible for voting")
        else:
            print("Invalid age, try again")


n = input("enter your name")
a = int(input("enter your age"))
canVote(n,a)

