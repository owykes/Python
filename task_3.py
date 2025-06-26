#Clears terminal to improve readability of terminal output
def clear_screen():
    print("\033c", end="")

#Requires user input before immediately returning to the main menu
def wait_for_enter():
    while True:
        if input("\nPress Enter to return to the menu...") == "":
            break

#Displays menu options
def display_menu():
        print("Rental Management Menu")
        print("\t1. Enter rental property details")
        print("\t2. Display summary for rentals")
        print("\t3. Exit")

#Hardcoded property details from table 1 in a dictionary of dictionaries
property_details = {
    "B12-3AB": {"Original cost": 153450, "Residual mortgage": 112345},
    "B13-4CD": {"Original cost": 212130, "Residual mortgage": 180234},
    "B14-5GH": {"Original cost": 120100, "Residual mortgage": 85980},
    "B15-6JK": {"Original cost": 135230, "Residual mortgage": 101321},
    "B16-7MO": {"Original cost": 183230, "Residual mortgage": 130234}
}
#Empty list for entries
entries = []

def property_data():
    """
    Handles user input for property entries.
    Accepts a property ID, description, and amount,
    and appends the inputs to the entries list 
    
    """
    clear_screen()
    while True:
        property_id = input("Enter Property#: ").strip().upper()
        #Rejects blank input so users can't submit to an empty property ID
        if not property_id:
            print("\nYou must enter a Property#\n")
            continue
        #Warns user if property is not part of the original dataset
        if property_id not in property_details:
            print("\nNote - this property is not in the original dataset, however the entry will still be stored.")
        while True:
            #Asks for user input for description dictionary and handles no input
            description = input("\nEnter entry description: ").strip()
            if not description:
                print("\nYou must enter a description.")
            else:
                break
        #Asks for value input, and handles value errors
        while True:
            try:
                amount = int(input("\nEnter Amount: "))
                break
            except ValueError:
                print("\nPlease enter a valid amount")    
        #Saves entry to entries
        entries.append({
            "Property#": property_id,
            "description": description,
            "amount": amount
        })
        wait_for_enter()
        break
        
#Placeholder subroutine for summary data
def summary_data():
    clear_screen()
    total_original_cost = 0
    total_residual_mortgage = 0
    Repairs = 0
    
    for property in property_details.values():
        total_original_cost += property["Original cost"]
        total_residual_mortgage += property["Residual mortgage"]
    print("Property#\tOriginal cost\tRepairs\tAmended cost\tResidual mortgage\tRents\tRents as % of Mortgage")
    print(f"Total\t\t{total_original_cost}\t\t\t\t\t{total_residual_mortgage}")
          
    
    print()
    wait_for_enter()
 
#Displays menu and handles user selection
def rental_management_menu():
    while True:   
        clear_screen()
        display_menu()
        #Prompts user for selection
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

#Initiates the main loop                       
if __name__ == "__main__":
    rental_management_menu()
