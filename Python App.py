import tkinter as tk
from tkinter import messagebox
from Hat Class import Hat



raw_data = [
    ["Dad Cap", "Brown", "100% Cotton", 15.80],
    ["Trucker Hat", "Red", "Polyvinyl", 13.90],
    ["Bowler Hat", "Black", "Rabbit Fur", 29.60],
    ["Chef Toque", "White", "Pleated Polyester and Cotton", 18.30],
    ["Beanie", "Orange", "Wool and Spandex", 36.50],
    ["Fedora", "Green", "Wool", 96.28],
    ["Sun Hat", "Beige", "Paper Straw", 68.86],
    ["Traveller Hat", "Khaki", "Recycled Cotton", 89.97],
]

hat_list = []  # required, list for all hat objects

def data_from_array():
    """Read all data from raw_data , create Hat objects and put into hat_list"""
    for data in raw_data:
        hat_list.append(Hat(*data))

data_from_array()

def main_menu():
    """Function to display the main menu"""
    # clear login window
    for widget in root.winfo_children():
        widget.destroy()

    # create main menu label
    menu_label = tk.Label(root, text="Main Menu")
    menu_label.grid(row=0, column=5, columnspan=2)

    # create main menu buttons
    display_all_button = tk.Button(root, text="SEE ALL HATS", command=display_all)
    display_details_button = tk.Button(root, text="SEE FULL DETAILS", command=display_details)
    create_new_button = tk.Button(root, text="CREATE NEW HAT", command=add_new_hat)
   

    # add buttons to the window
    display_all_button.grid(row=1, column=5, pady=10)
    display_details_button.grid(row=2, column=5, pady=10)
    create_new_button.grid(row=3, column=5, pady=10)
   
current_index = 0

def display_all():
    """Function to display a list of all available hats"""
    # clear main menu
    for widget in root.winfo_children():
        widget.destroy()


    # create label to display list of hats
    hat_list_label = tk.Label(root, text="List of Hats:")
    hat_list_label.grid(row=0, column=0, sticky='w')

    global current_index


    row=1
    for i, hat in enumerate(hat_list[current_index:current_index+3]):
        hat_number_label = tk.Label(root, text=f"{hat_list.index(hat)+1}.")
        hat_number_label.grid(row=row, column=5, sticky='W')

        name_label = tk.Label(root, text="Name:")
        name_label.grid(row=row, column=5, sticky='W', padx=10)

        name_result_label = tk.Label(root, text=hat.get_name())
        name_result_label.grid(row=row, column=6, sticky='W', padx=10)

        row += 1

        colour_label = tk.Label(root, text="Colour:")
        colour_label.grid(row=row, column=5, sticky='W', padx=10)

        colour_result_label = tk.Label(root, text=hat.get_colour())
        colour_result_label.grid(row=row, column=6, sticky='W', padx=10)

        row += 1

        material_label = tk.Label(root, text="Material:")
        material_label.grid(row=row, column=5, sticky='W', padx=10)

        material_result_label = tk.Label(root, text=hat.get_material())
        material_result_label.grid(row=row, column=6, sticky='W', padx=10)

        row += 1

        price_label = tk.Label(root, text="Price:")
        price_label.grid(row=row, column=5, sticky='W', padx=10)

        price_result_label = tk.Label(root, text=hat.get_price())
        price_result_label.grid(row=row, column=6, sticky='W', padx=10)

        row += 1

        priceGST_label = tk.Label(root, text="Price with GST:")
        priceGST_label.grid(row=row, column=5, sticky='W', padx=10)

        priceGST_result_label = tk.Label(root, text=round(hat.get_price_with_gst(),2))
        priceGST_result_label.grid(row=row, column=6, sticky='W', padx=10)

        row += 1
     


    # add previous and next buttons
    prev_button = tk.Button(root, text="Previous", command=display_prev)
    prev_button.grid(row=row, column=0, pady=10)
    next_button = tk.Button(root, text="Next", command=display_next)
    next_button.grid(row=row, column=10, pady=10)

    # create main button
    main_button = tk.Button(root, text="main", command=main_menu)
    main_button.grid(row=0, column=12, pady=0)


def display_prev():
    """Function to display previous 3 items"""
    global current_index
    if current_index - 3 >= 0:
        current_index -= 3
        display_all()
   


def display_next():
    """Function to display next 3 items"""
    global current_index
    if current_index + 3 <= len(hat_list):
        current_index += 3
        display_all()
  

def display_hat_details(hat_name, name_label, color_label, material_label, price_label, priceGST_label):
    """Function to display the details of a selected hat"""
    hat = None
    # find the hat object based on the hat name
    for h in hat_list:
        if h.get_name() == hat_name:
            hat = h
            break
        
    # update the details labels with the hat details
    name_label["text"] = "Name: " + hat.get_name()
    color_label["text"] = "Colour: " + hat.get_colour()
    material_label["text"] = "Material: " + hat.get_material()
    price_label["text"] = "Price: " + str(hat.get_price())
    priceGST_label["text"] = "Price with GST: " + str(hat.get_price_with_gst())
    return hat


def display_details():
    """Function to display the details of a selected hat"""
    # clear main menu
    for widget in root.winfo_children():
        widget.destroy()

    # create first frame for hat selection
    selection_frame = tk.Frame(root,height=800)
    selection_frame.grid(row=0, column=0, padx=10)

    # create label for hat selection
    select_label = tk.Label(selection_frame, text="Select a hat:")
    select_label.grid(row=0, column=0, sticky="W", pady=20)

    # create Listbox for hat selection
    hat_list_box = tk.Listbox(selection_frame)
    hat_list_box.grid(row=1, column=0, padx=10)

    # populate Listbox with hat names
    for hat in hat_list:
        hat_list_box.insert(tk.END, hat.get_name())

   # bind selection event to the Listbox
    hat_list_box.bind("<<ListboxSelect>>", lambda event: display_hat_details(hat_list_box.get(hat_list_box.curselection()), name_label, color_label, material_label, price_label,priceGST_label))

    # create second frame for hat details
    details_frame = tk.Frame(root,height=800)
    details_frame.grid(row=0, column=1, padx=10)

    # create empty label for hat details
    name_label = tk.Label(details_frame, text="Name:")
    name_label.grid(row=1, column=0, sticky="W", padx=20)
    color_label = tk.Label(details_frame, text="Color:")
    color_label.grid(row=2, column=0, sticky="W", padx=20)
    material_label = tk.Label(details_frame, text="Material:")
    material_label.grid(row=3, column=0, sticky="W", padx=20)
    price_label = tk.Label(details_frame, text="Price:")
    price_label.grid(row=4, column=0, sticky="W", padx=20)
    priceGST_label = tk.Label(details_frame, text="Price with GST:")
    priceGST_label.grid(row=5, column=0, sticky="W", padx=20)

    #add Edit button in details frame
    edit_button = tk.Button(details_frame, text="Edit", command=lambda: open_edit_window(display_hat_details(hat_list_box.get(hat_list_box.curselection()), name_label, color_label, material_label, price_label, priceGST_label)))
    edit_button.grid(row=6, column=0, pady=10)

    # create main button
    main_button = tk.Button(root, text="main", command=main_menu)
    main_button.grid(row=1, column=10, pady=0)

#function to open edit window
def open_edit_window(hat):
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Hat")
   
    # create labels for name, color, material, and price
    name_label = tk.Label(edit_window, text="Name:")
    name_label.grid(row=0, column=0, sticky="W", padx=20)
    color_label = tk.Label(edit_window, text="Color:")
    color_label.grid(row=1, column=0, sticky="W", padx=20)
    material_label = tk.Label(edit_window, text="Material:")
    material_label.grid(row=2, column=0, sticky="W", padx=20)
    price_label = tk.Label(edit_window, text="Price:")
    price_label.grid(row=3, column=0, sticky="W", padx=20)

    # create entry boxes for name, color, material, and price
    name_entry = tk.Entry(edit_window)
    name_entry.grid(row=0, column=1, padx=20)
    name_entry.insert(0, hat.get_name())
    color_entry = tk.Entry(edit_window)
    color_entry.grid(row=1, column=1, padx=20)
    color_entry.insert(0, hat.get_colour())
    material_entry = tk.Entry(edit_window)
    material_entry.grid(row=2, column=1, padx=20)
    material_entry.insert(0, hat.get_material())
    price_entry = tk.Entry(edit_window)
    price_entry.grid(row=3, column=1, padx=20)
    price_entry.insert(0, hat.get_price())

    # create a save button
    save_button = tk.Button(edit_window, text="Save", command=lambda: save_changes(hat))
    save_button.grid(row=4, column=0, columnspan=2, pady=10)

    #create function to save changes
    def save_changes(hat):
        hat.set_name(name_entry.get())
        hat.set_colour(color_entry.get())
        hat.set_material(material_entry.get())
        hat.set_price(price_entry.get())
        messagebox.showinfo("Success", "Hat details updated successfully")
        display_details()
        edit_window.destroy() 


def add_new_hat():
    """Function to add a new hat to the list"""
    # clear main menu
    for widget in root.winfo_children():
        widget.destroy()

    # create first frame for new hat data entry
    entry_frame = tk.Frame(root, height=800)
    entry_frame.grid(row=0, column=0, padx=10)

    # create labels for hat data entry
    name_entry_label = tk.Label(entry_frame, text="Enter name:")
    name_entry_label.grid(row=0, column=0, sticky="W", padx=20, pady=10)
    color_entry_label = tk.Label(entry_frame, text="Enter color:")
    color_entry_label.grid(row=1, column=0, sticky="W", padx=20, pady=10)
    material_entry_label = tk.Label(entry_frame, text="Enter material:")
    material_entry_label.grid(row=2, column=0, sticky="W", padx=20, pady=10)
    price_entry_label = tk.Label(entry_frame, text="Enter price:")
    price_entry_label.grid(row=3, column=0, sticky="W", padx=20, pady=10)

    # create entry widgets for hat data entry
    name_entry = tk.Entry(entry_frame)
    name_entry.grid(row=0, column=1, padx=10)
    color_entry = tk.Entry(entry_frame)
    color_entry.grid(row=1, column=1, padx=10)
    material_entry = tk.Entry(entry_frame)
    material_entry.grid(row=2, column=1, padx=10)
    price_entry = tk.Entry(entry_frame)
    price_entry.grid(row=3, column=1, padx=10)

    # create 'Add' button
    add_button = tk.Button(entry_frame, text="Add", command=lambda: create_new_hat(name_entry.get(), color_entry.get(), material_entry.get(), price_entry.get()))
    add_button.grid(row=4, column=2, pady=10)

    # create main button
    main_button = tk.Button(entry_frame, text="main", command=main_menu)
    main_button.grid(row=5, column=3, pady=10)

    

def create_new_hat(name, color, material, price):
    """Function to create a new hat object and add it to the hat_list"""
    new_hat = Hat(name, color, material, price)
    hat_list.append(new_hat)
    messagebox.showinfo("Success", "New hat added successfully!")
    display_details()



def search_name_category_description(search_string: str, hat_list: list) -> list:
        search_string = search_string.lower()
        found_hats = []
        for hat in hat_list:
            if (
                search_string in hat.get_name().lower()
                or search_string in hat.get_colour().lower()
                or search_string in hat.get_material().lower()
            ):
                found_hats.append(hat)
        return found_hats


def search():
        """Function to search for hats by name, color, or material"""
        display_search_result(search_var.get())


def display_search_result(search_string: str):
        """Function to search for hats by name, color, and material and display the result"""
        found_hats = search_name_category_description(search_string, hat_list)
        result_text = ""
        if len(found_hats) == 0:
            result_text = "=====No results found====="
        else:
            for hat in found_hats:
                result_text += f"{hat.get_name()}\n"
                result_text += f"Color: {hat.get_colour()}\n"
                result_text += f"Material: {hat.get_material()}\n"
                result_text += f"Price: ${hat.get_price()}\n"
                result_text += "-----------------------------------\n"
        search_result_label["text"] = result_text




root = tk.Tk()
root.title("Main Menu")

# create search frame
search_frame = tk.Frame(root)
search_frame.pack(pady=10, anchor="w")

# create label for search input
search_label = tk.Label(search_frame, text="Enter search term:")
search_label.grid(row=0, column=0, sticky="W")

# create entry for search input
search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var)
search_entry.grid(row=1, column=0, padx=10)

# create 'search' button
search_button = tk.Button(search_frame, text="Search", command=search)
search_button.grid(row=1, column=1, pady=10)

# create result frame
result_frame = tk.Frame(root)
result_frame.pack(pady=10, anchor="w")

# create label to display search result
search_result_label = tk.Label(result_frame, text="")
search_result_label.grid(row=4, column=0,sticky="W")
search_result_label.config(anchor="w")




    
#function to check for login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Alvin" and password == "123sp":
        messagebox.showinfo("Login", "Login successful!")
        main_menu()
    else:
        messagebox.showerror("Login", "Invalid credentials. Please try again.")
    return


#create login window 
root = tk.Tk()
root.title("Hat Shop Login")
root.geometry("400x400+{}+{}".format(
    int((root.winfo_screenwidth() - 400) / 2),
    int((root.winfo_screenheight() - 400) / 2)
))

# create label for username
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, sticky="W")

# create entry for username
username_var = tk.StringVar()
username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=10)

# create label for password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky="W")

# create entry for password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1, padx=10)

# create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, pady=10)


# start GUI
root.mainloop()