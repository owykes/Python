#clears terminal using ANSI escape sequence to improve readability of terminal output
def clear_screen():
    print("\033c", end="")

#requires user input before immediately returning to the main menu
def wait_for_enter():
    while True:
        if input("\nPress Enter to return to the menu...") == "":
            break

def display_menu():
        print("Rental Management Menu")
        print("\t1. Enter rental property details")
        print("\t2. Display summary for rentals")
        print("\t3. Exit")

#hardcoded property detials from table 1 in dictionary
property_details = {
    "B12-3AB": {"Original cost": 153450, "Residual mortgage": 112345},
    "B13-4CD": {"Original cost": 212130, "Residual mortgage": 180234},
    "B14-5GH": {"Original cost": 120100, "Residual mortgage": 85980},
    "B15-6JK": {"Original cost": 135230, "Residual mortgage": 101321},
    "B16-7MO": {"Original cost": 183230, "Residual mortgage": 130234}
}
#asks for input, validates property id key, removing whitespace, handles incorrect capatilisation, avoids key errors
def property_data():
    while True:
        clear_screen()
        property_id = input("Enter Property#: ").strip().upper()
        property_info = property_details.get(property_id) #safelookup 
        if property_info:
            print("\nProperty found")
            clear_screen()
            break
        else:
            print("Please Enter a Valid Property#")
    #ask for user input for description dictionary 
    description = input("Enter Entry Description: ").strip() 
    #asks for value input, and handles value errors
    while True:
        try:
            amount = float(input("\nEnter Amount: "))
            break
        except ValueError:
            print("\nPlease enter a valid amount")    
    #appends directly into the dictionary
    property_info[description] = amount
    print("\nEntry added")
    wait_for_enter()
        
#placeholder subroutine for summary data
def summary_data():
    clear_screen()
    print(f"{'Property#'}")
    print("=" * 90)
    
    wait_for_enter()
 
#displays menu and handles user selection
def rental_management_menu():
    while True:   
        clear_screen()
        display_menu()
        #prompts user for selection
        selection = input("\nEnter your Selection: ")

        if selection == "1":
            property_data()
        elif selection == "2":
            summary_data()
        elif selection == "3":
            clear_screen()
            print("Exiting Program...")
            break
        else:
            print("Invalid choice, please select 1,2 or 3")
            wait_for_enter()
                      
rental_management_menu()
