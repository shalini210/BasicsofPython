
def calc(n):

    if (n == '+'):
        print("addition ")
        n = a + b
        print(n)
    else:
        if (n == "-"):
            print("difference")
            n = a - b
            print(n)
        else:
            if (n == "*"):
                print("Multipy")
                n = a * b
                print(n)
            else:
                if (n == "/"):
                    print("DIivsion")
                    n = a / b
                    print(n)

a= int(input("enter first no "))
b = int(input("enter second no "))
n=""
while(n!="x"):
    print("press:")
    print("+ for addition ")
    print("- for difference ")
    print("* for difference ")
    print("/ for difference ")
    print("r for new inputs")
    print("x for exit")
    n = input()
    calc(n)
    if(n=="r"):
        a = int(input("enter first no "))
        b = int(input("enter second no "))
        n = ""
