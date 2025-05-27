#clears terminal using ANSI escape sequence to improve readability of terminal output
def clear_screen():
    print("\033c", end="")

#requires user input before immediately returning to the main menu
def wait_for_enter():
    while True:
        if input("\nPress Enter to return to the menu...") == "":
            break

#hardcoded property detials from table 1
property_details = {
    "B12-3AB": {"Original cost": 153450, "Residual mortgage": 112345, "Entries": []},
    "B13-4CD": {"Original cost": 212130, "Residual mortgage": 180234, "Entries": []},
    "B14-5GH": {"Original cost": 120100, "Residual mortgage": 85980, "Entries": []},
    "B15-6JK": {"Original cost": 135230, "Residual mortgage": 101321, "Entries": []},
    "B16-7MO": {"Original cost": 183230, "Residual mortgage": 130234, "Entries": []}
}

#asks for input, validates property id key, removing whitespace, handles incorrect capatilisation, avoids key errors
def property_data():
    clear_screen()
    while True:
        property_id = input("Enter Property ID: ").strip().upper()
        property_info = property_details.get(property_id) #safelookup 
        if property_info:
            print("\nProperty found")
            break
        else:
            print("Please Enter a Valid Property ID")
    #ask for user input for values in new keys
    description = input("\nEnter Entry Description: ").strip() 
    #asks for value input, and handles value errors
    while True:
        try:
            amount = float(input("\nEnter Amount: "))
            break
        except ValueError:
            print("Please enter a number")    
    #appends the new keys to the dictionary
    property_info["Entries"].append((description, amount))
    print("Entry added")
    wait_for_enter()
        
    
#view stored data in list
def summary_data():
    clear_screen() 
    print()
    #placeholder
    print("placeholder")   
    wait_for_enter()

#displays menu and handles user selection
def rental_management_menu():
    while True:
        clear_screen()
        print("Rental Managment Menu")
        print("1. Enter rental property details")
        print("2. Display summary for rentals")
        print("3. Exit")
        
        #maybe remove the prompt from this input
        selection = input("\nEnter your Selection: ")

        if selection == "1":
            property_data()
        elif selection == "2":
            summary_data()
        elif selection == "3":
            print("\nExiting Program...")
            break
        else:
            print("Invalid choice, please select 1,2 or 3")
            wait_for_enter()
           
rental_management_menu()



