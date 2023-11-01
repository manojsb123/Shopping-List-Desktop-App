# Shopping List ----------------------------------------------------------------------------------------- Shopping List
import streamlit as st
n = "add item"


def read_write(mode, obj=None):
    """
    Reads the text file and returns a list
    and
    Writes the input list to the same text document
    based on input file opening mode
    :param mode:
    :param obj:
    :return:
    """
#    location = r"C:\Users\manoj\OneDrive - Consumers Food and Drug\2-Manoj Docs\5-Learning\PythonProgramming\
    #    TextFiles\ShoppingList.txt"
    location = "ShoppingList.txt"
    if obj is None:
        obj = []
    if mode == "r":
        with open(location, mode) as file:
            obj = file.readlines()
        return obj
    else:
        with open(location, mode) as file:
            file.writelines(obj)


def srl_chk(k, objs=None):
    if objs is None:
        objs = []
    """
    Checks for the availability of the serial number entered by user 
    in the list
    :param k: 
    :return: 
    """
    while not k[0].isdigit() or int(k) > len(objs) or int(k) <= 0:
        k = input("Enter a valid serial number from the list only...!!: ")
    return k


def prnt_lst(items_list):
    """
    Prints the list contents
    :param items_list:
    :return:
    """
    if not items_list:
        print("************************************************\n"
              "Currently No items in the shopping list...\n"
              "************************************************")
    else:
        print('************************************************\n'
              'Here is the current shopping list...')
        [print(f"{index + 1} - {x.strip()}")
         for index, x in enumerate(items_list)]
        print("************************************************")


def clear_items():
    read_write('w')


def add_item():
    item = st.session_state[n]
    if not st.session_state[n]:
        pass
    else:
        items = read_write('r')
        item_to_add = st.session_state[n].strip(' ').capitalize() + '\n'
        if item_to_add in items:
            st.write("Item is already existing in the list")
        else:
            items.append(item_to_add)
            read_write('w', items)
            st.session_state[n] = ''


def remove_item():
    items = read_write('r')
    items_removed = []
    for i in items:
        if st.session_state[i]:
            items_removed.append(i)
    if not items_removed:
        st.write("Select at least one item from the list to remove")
    else:
        st.write("Items removed are")
        for i in items_removed:
            items.remove(i)
            st.write(i)

    read_write('w', items)

