from Modules import Functions
import time

now = time.strftime("%A, %b %d, %Y   %H:%M:%S IST")
print("It is", now)
# Main Menu ------------------------------------------------------------------------------------------------- Main Menu
while True:
    items = Functions.read_write('r')
    Functions.prnt_lst(items)
    user_action = input("Choose your action with correct serial number...\n"
                        "1 or \"Add\" - Add an item\n"
                        "2 or \"Edit\" - Edit an item\n"
                        "3 or \"Complete\" - Mark complete and remove from the list\n"
                        "* or \"Clear\" - Clear the list\n"
                        "# or \"Exit\" - Exit the program\n"
                        "************************************************\n").strip().lower()
# Adding an item to the list --------------------------------------------------------------- Adding an item to the list
    if user_action.startswith('1') or user_action.startswith('add'):

        if ((user_action.startswith("1") and not user_action[1:]) or
                (user_action.startswith("add") and not user_action[4:])):
            item = input("Enter an item name: ").strip().capitalize() + '\n'
            items.append(item)
            Functions.read_write("w", items)
            continue

        elif user_action.startswith("1") and user_action[1].isspace():
            item = user_action[1:].strip().capitalize() + '\n'
            items.append(item)

        elif user_action.startswith("add") and user_action[3].isspace():
            item = user_action[3:].strip().capitalize() + '\n'
            items.append(item)

        else:
            print("Wrong command...")
            continue
        Functions.read_write("w", items)
# Edit an item in the list ------------------------------------------------------------------- Edit an item in the list
    elif user_action.startswith('2') or user_action.startswith('edit'):

        if ((user_action.startswith("2") and not user_action[1:]) or
                (user_action.startswith("edit") and not user_action[4:])):
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(input("Which one you want to edit? (Choose the Serial number): "), items))
                items.__setitem__(int(j)-1, input('Write the new item name: ').strip().capitalize() + '\n')
                print('Updated..!!')
                Functions.read_write("w", items)
                continue

        elif user_action.startswith("2") and user_action[1].isspace():
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(user_action[1:].strip().capitalize(), items))
                items.__setitem__(j - 1, input('Write the new item name: ').strip().capitalize() + '\n')
                print('Updated..!!')

        elif user_action.startswith("edit") and user_action[4].isspace():
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(user_action[4:].strip().capitalize(), items))
                items.__setitem__(j - 1, input('Write the new item name: ').strip().capitalize() + '\n')
                print('Updated..!!')

        else:
            print("Wrong command...")
            continue
        Functions.read_write("w", items)
# To mark an item complete ------------------------------------------------------------------- To mark an item complete
    elif user_action.startswith('3') | user_action.startswith('complete'):

        if ((user_action.startswith("3") and not user_action[1:]) |
                (user_action.startswith("complete") and not user_action[8:])):
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(input("Which item do you want to mark complete and remove from the list? "
                                                "(Choose the Serial number): "), items))
                removed = items[j - 1]
                items.pop(j - 1)
                print(f"Updated..!!\n"
                      f"{removed.strip()} has been removed from the list")
                Functions.read_write("w", items)
                continue

        elif user_action.startswith("3") and user_action[1].isspace():
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(user_action[1:].strip().capitalize(), items))
                removed = items[j - 1]
                items.pop(j - 1)
                print(f"Updated..!!\n"
                      f"{removed.strip()} has been removed from the list")

        elif user_action.startswith("complete") and user_action[8].isspace():
            if not items:
                continue
            else:
                j = int(Functions.srl_chk(user_action[8:].strip().capitalize(), items))
                removed = items[j - 1]
                items.pop(j - 1)
                print(f"Updated..!!\n"
                      f"{removed.strip()} has been removed from the list")

        else:
            print("Wrong command...")
            continue
        Functions.read_write("w", items)
# Clearing the list --------------------------------------------------------------------------------- Clearing the list
    elif user_action in ["*", "clear"]:
        items = Functions.read_write('r')
        Functions.read_write("w")
        user_choice = input("List Cleared...\n"
                            "Backup created...!! Do you want to retrieve? (Yes or No): ").strip().capitalize()
        while user_choice not in ["Yes", "No"]:
            user_choice = input("Enter valid choice (Yes or No): ").strip().capitalize()
        if user_choice == "Yes":
            Functions.read_write("w", items)
            print("List retrieved..")
        else:
            print('List Cleared...')
# Exiting the program ----------------------------------------------------------------------------- Exiting the program
    elif user_action in ["#", "exit"]:
        Functions.prnt_lst(items)
        print("Exiting... Bye..!!")
        exit()
# Wrong command ----------------------------------------------------------------------------------------- Wrong command
    else:
        print("Wrong command...")
# End of program --------------------------------------------------------------------------------------- End of program
