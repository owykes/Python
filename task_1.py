#clears terminal using ANSI escape sequence to improve readability of terminal output
def clear_screen():
    print("\033c", end="")

#requires user input before immediately returning to the main menu
def wait_for_enter():
    while True:
        if input("\nPress Enter to return to the menu...") == "":
            break

#placeholder subroutine for property data
def property_data():
    clear_screen()
    print("Enter Property Details")
    wait_for_enter()
        
#placeholder subroutine for summary data
def summary_data():
    clear_screen()
    print("Property Summary")  
    wait_for_enter()
 
#displays menu and handles user selection
def rental_management_menu():
    while True:   
        clear_screen()
        print("Rental Management Menu")
        print("1. Enter rental property details")
        print("2. Display summary for rentals")
        print("3. Exit")
        
        #prompts user for selection
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



