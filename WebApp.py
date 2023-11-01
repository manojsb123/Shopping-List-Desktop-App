import streamlit as st
from Modules import Functions
import os

from Modules.Functions import add_item

items = Functions.read_write('r')
n = "add item"
o = "option"
if not os.path.exists("ShoppingList.txt"):
    with open("ShoppingList.txt", 'w') as file:
        pass

st.title("Shopping List")
st.subheader("Enter new item to add in the input box below...")

if not items:
    pass
else:
    st.write("Current items in the list are....")
    for i in items:
        st.checkbox(i, key=i)
    st.text("")
    st.button("Remove", on_click=Functions.remove_item)
    st.button("Clear", on_click=Functions.clear_items)
    st.text("")

st.text_input(label="Enter a new item to add in the list", placeholder="Enter a new item and press \"Enter\"", key=n,
              on_change=add_item)

# st.session_state
