""" ---The Tkinter GUI creation--- """
# Import
import tkinter as tk
#import UuidGenerator, PasswordGenerator

# Main Window
window = tk.Tk()
window.title("Generator: UID & Password")

#window.geometry("400x200") # w x h
window.resizable(width = 0, height = 0)

window.rowconfigure(2)
window.columnconfigure(1)

""" Frame """
frame_main = tk.Frame(
    master = window,
    bg = "#fffbae",
    padx = 15,
    pady = 15
)

""" Widgets """
# Section A:
label_intro_msg = tk.Label(
    master = frame_main,
    text = "This is a random user ID & Password generator.\nPlease press the buttons to generate.",
    font = ("", 10, "bold"),
    padx = 20,
    pady = 20
)

# Section B:
button_uid = tk.Button(
    master = frame_main,
    text = "Generate UID",
    width = 20,
    height = 1
)
entry_uid = tk.Entry(master = frame_main, width = 30)

# Section C:
button_password = tk.Button(
    master = frame_main,
    text = "Generate Password",
    width = 20,
    height = 1,
    padx = 1,
    pady = 1
)
entry_password = tk.Entry(master = frame_main, width = 30)


""" Run Widgets """
# Frames:
frame_main.grid()

# Lables:
label_intro_msg.grid(row = 0, column = 0, sticky = "e")

# Buttons:
button_uid.grid(row = 1, column = 0, sticky = "w")
button_password.grid(row = 2, column = 0, sticky = "w")

# Entry:
entry_uid.grid(row = 1, column = 1, sticky = "n")
entry_password.grid(row = 2, column = 1, sticky = "n")


""" Run loop """
window.mainloop()