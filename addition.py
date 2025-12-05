def addition():
    while True:
        try:
            number1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a integer")
    while True:
        try:    
            number2 = int(input("Enter another number: "))
            break
        except ValueError:
            print("PLease enter a integer")

    print(number1 + number2)
        

addition()
