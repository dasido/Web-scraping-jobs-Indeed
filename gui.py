from tkinter import *
import tkinter as tk
from tkinter import ttk
from webScrap import process_manager, init_user_filters


root = tk.Tk()
root.title('Automate your job search')
root.geometry("600x500")


# Initialize a Label to display the User Input
label = Label(root)
label.pack()

# Create widgets for user filters input
title = Entry(root)
title.insert(0, "title, skill or company")                     
title.pack()

location = Entry(root)
location.insert(0, "location")
location.pack()

# Create a button to validate
tk.Button(root, text="set", command=lambda: init_user_filters(title.get(), location.get())).pack()


# Add some style
style = ttk.Style()

# Pick a theme
style.theme_use("classic")

# Configure our treeview colors
style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
# Change selected color
style.map('Treeview', background=[('selected', 'blue')])
# Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(fill='x')

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, selectmode="extended", yscrollcommand=tree_scroll.set)
my_tree.pack()


# Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Job Title", "Company Name", "Location")

# Format Our Columns
my_tree.column("#0", width=0, minwidth=25)
my_tree.column("Job Title", anchor=W, width=120)
my_tree.column("Company Name", anchor=CENTER, width=80)
my_tree.column("Location", anchor=W, width=120)

# Create Headings 
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Job Title", text="Job Title", anchor=W)
my_tree.heading("Company Name", text="Company Name", anchor=CENTER)
my_tree.heading("Location", text="Location", anchor=W)

btn_expand = Button(root, text="Search")
btn_expand = tk.Button(root, text="Search", bg='#000000', fg='#b7f731', command=lambda:wake_up(), font="Raleway", height=2, width=10).pack(expand=YES)


def wake_up():
    df = process_manager()
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)


my_tree.pack(fill='x')
root.mainloop()