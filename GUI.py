from Modules import Functions
import PySimpleGUI as Gui
import time
import os

if not os.path.exists("ShoppingList.txt"):
    with open("ShoppingList.txt", 'w') as file:
        pass

Gui.theme("Black")

add = 'add_item'
edt = 'edit_item'
res = 'result'
clr = 'clear'
t = "time"

time_display = Gui.Text(time.strftime("%A, %b %d, %Y   [%H:%M:%S IST]"), key=t)

add_label = Gui.Text("Enter an item to add or edit:")
input_box = Gui.InputText(tooltip="Enter an item", key=add, size=(45, 2), border_width=5)
add_button = Gui.Button(image_source="Icons/add.png", mouseover_colors="Yellow",
                        tooltip="Add item", key="Add", image_size=(70, 35))

list_display = Gui.Listbox(values=Functions.read_write("r"), key=edt,
                           enable_events=True, size=(45, 10))

edit_button = Gui.Button(image_source="Icons/edit.png", mouseover_colors="Yellow",
                         tooltip="Edit item", key="Edit", image_size=(70, 35))

exit_button = Gui.Button(image_source="Icons/exit.png", mouseover_colors="Yellow",
                         tooltip="Exit", key="Exit", image_size=(70, 35))

remove_button = Gui.Button(image_source="Icons/remove.png", mouseover_colors="Yellow",
                           tooltip="Remove item", key="Remove", image_size=(70, 35))

clear_button = Gui.Button(image_source="Icons/clear.png", mouseover_colors="Yellow",
                          tooltip="Clear list", key="Clear", image_size=(70, 35))

result_display = Gui.Text(key=res, text_color='Orange')


window = Gui.Window("Shopping list",
                    layout=[[time_display],
                            [add_label],
                            [input_box, add_button],
                            [list_display, edit_button, remove_button],
                            [result_display],
                            [clear_button, exit_button]],
                    font=("Cambria", 13), resizable=True)

while True:
    event, values = window.read(timeout=1000)
    print(event)
    print(values)
    window[t].update(value=time.strftime("%A, %b %d, %Y   [%H:%M:%S IST]"))

    match event:
        case "Add":
            if not values[add]:
                Gui.popup("Please write an item to add in the input field.",
                          title="Alert..!!",
                          font=("Cambria", 13))
                continue
            else:
                items = Functions.read_write("r")
                new_item = values[add].strip().capitalize() + "\n"
                if new_item in items:
                    Gui.popup(f"{new_item.strip()} is already existing in the list",
                              title="Alert..!!",
                              font=("Cambria", 13))
                    window[add].update(value="")
                    continue
                else:
                    items.append(new_item)
                    Functions.read_write("w", items)
                    window[edt].update(values=Functions.read_write('r'))
                    window[add].update(value="")
                    window[res].update(value="Item added..!!")

        case "Edit":
            if not values[edt]:
                window[add].update(value="")
                Gui.popup("Please select an item to edit in the displayed list.",
                          title="Alert..!!",
                          font=("Cambria", 13))
                continue
            else:
                items = Functions.read_write("r")
                item_to_edit = values[edt][0]
                item_tobe_added = values[add].strip().capitalize() + '\n'
                if not values[add].strip().capitalize():
                    Gui.popup("Please write an item to add in the input field.",
                              title="Alert..!!",
                              font=("Cambria", 13))
                    continue
                elif item_tobe_added in items:
                    Gui.popup(f"{item_tobe_added.strip()} is already existing in the list",
                              title="Alert..!!",
                              font=("Cambria", 13))
                    window[add].update(value="")
                    continue
                else:
                    item_to_edit = values[edt][0]
                    index = items.index(item_to_edit)
                    items[index] = item_tobe_added
                    Functions.read_write("w", items)
                    window[edt].update(values=Functions.read_write('r'))
                    window[add].update(value="")
                    window[res].update(value=f"{item_to_edit.strip()} replaced with {item_tobe_added.strip()}..!!")

        case "edit_item":
            if not values[edt]:
                continue
            else:
                window[add].update(value=values[edt][0].strip())

        case "Remove":
            if not values[edt]:
                Gui.popup("Please select an item to remove in the displayed list.",
                          title="Alert..!!",
                          font=("Cambria", 13))
                continue
            else:
                items = Functions.read_write("r")
                item_to_remove = values[edt][0]
                items.remove(item_to_remove)
                Functions.read_write("w", items)
                window[edt].update(values=Functions.read_write('r'))
                window[add].update(value="")
                window[res].update(value=f"{item_to_remove.strip()} has been removed..!!")

        case "Clear":
            items = []
            Functions.read_write("w", items)
            window[edt].update(values=Functions.read_write('r'))
            window[add].update(value="")
            window[res].update(value=f"List has been cleared..!!")

        case Gui.WIN_CLOSED | "Exit":
            break

window.close()
