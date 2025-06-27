module_list = []

def data_entry_and_storage():
    while True:
        module_code = input("Enter Module code: ").upper()
        if module_code == "":
            verification_input = input("Are you sure you want to exit? Press Enter to continue")
            if verification_input == "":
                break
        else:
            module_mark = int(input("Enter your mark: "))
        module_list += (module_code, module_mark)
        
def display_menu():
    print("Menu")
    print("\t1. Show average mark")
    print("\t2. Show best module with its mark" )
    print("\t3. End program")

def average_mark():
    marks = module_list[1::2]
    total_mark = sum(marks)
    average = total_mark / len(marks) 
    print(f"{average:.2f}")

def best_module_and_mark():
    highest = module_list[0]
    for module in module_list[]

def main_program():
    data_entry_and_storage()
    display_menu()
    while True:
        selection = input("Enter your selection")

        if selection == "1":
            average_mark()
        elif selection == "2":
            best_module_and_mark()
        elif selection == "3":
            break
        else:
            print("enter valid response")

main_program()