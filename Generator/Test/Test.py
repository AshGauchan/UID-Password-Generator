""" The Tkinter GUI creation """

# Import Tkinter module from Python & declaring containter i.e window
import tkinter as tk

window = tk.Tk() # creates the window

""" Adding some widgets """

# 1: Welcome message
label_greetings = tk.Label(
    text = "Hello, this program is a simple generator \nto create unique and random ID's and Password .", # key:value pair
    foreground = "black", # set text color to white
    background = "yellow", # set background color to black
    width = 50,
    height = 3
) 
label_greetings.pack() # Pushing this widget into the window

label_msg_1 = tk.Label(
    text = "Please click each button to generate a random key.",
    fg = "black",
    bg = "pink",
    width = 50,
    height = 3
)
label_msg_1.pack()

# 2: Button widget
btn_1 = tk.Button(
    text = "Generate UID",
    fg = "black",
    bg = "#81ecec",
    width = 20,
    height = 2
)
btn_1.pack()

# 3: Entry widget
ent_usr = tk.Entry(
    width = 40,
)
ent_usr.pack()

ent_usr.insert(0, "What is you name?")


""" Main event loop = tells python to run tkinter event loop """

# Run the whole event and show widgets added
window.mainloop()

 # window.destroy() # Closes the window created