# WAP to program to create billing system in supermarket

total = 0
while True :
    name = input(" Enter your name : ")
    no = int ( input (" Enter your number : "))

    print()
    print("-"*40)
    print()

    while True:
        qty = int ( input (" Enter the quantity of the items : "))
        price = int ( input ( " Enter the price of 1 item : "))
        repeat = input ( " You want to add more items (y/n) : ")
        total+= qty*price

        if repeat == 'n':
            break
    
    print()
    print("-"*40)
    print()
    
    print("*"*5,"Thanks for Shopping","*"*5)
    print(name)
    print(no)
    print ("Total Billing Amount = ",total)

    print()
    print("-"*40)
    print()
    
    repeat1=input ( " You want to add more records (y/n) : ")
    if repeat == 'n':
            break