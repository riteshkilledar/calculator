#Name: Riteshsingh Killedar

#Email: 

def start():

    print()

    print("\t\tSimple Calculator")

    print()

    print("1: Addition")

    print("2: Substraction")

    print("3: Multiplication")

    print("4: Division")

    print("5: Percentage")

    print("6: Close")

    print()

    choice = int(input('Select any one option from above: '))

    if choice==1:

        N1 = int(input('Enter First number: '))

        N2 = int(input('Enter Second number: '))

        print(N1,"+",N2,"=",add(N1,N2))

        start()

    elif choice==2:

        N1 = int(input('Enter First number: '))

        N2 = int(input('Enter Second number: '))

        print(N1,"-",N2,"=",sub(N1,N2))

        start()

    elif choice==3:

        N1 = int(input('Enter First number: '))

        N2 = int(input('Enter Second number: '))

        print(N1,"*",N2,"=",mul(N1,N2))

        start()

    elif choice==4:

        N1 = int(input('Enter First number: '))

        N2 = int(input('Enter Second number: '))

        print(N1,"/",N2,"=",div(N1,N2))

        start()

    elif choice==5:

        N1 = int(input('Enter First number: '))

        N2 = int(input('Enter Second number: '))

        print(N1,"%",N2,"=",per(N1,N2),"%")

        start()

    elif choice==6:

        print("\t\tCalculator closed.")

    else:

        print("Select Correct option.")

        start()

start()

#Calculation functions

def add(a,b):

    c=a + b

    return c

def sub(a,b):

    c=a - b

    return c

def mul(a,b):

    c=a * b

    return c

def div(a,b):

    c = b/a

    return c

def per(a,b):

    c = (b/a)*100

    return c

#End of Code
