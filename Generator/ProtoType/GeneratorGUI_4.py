""" Start """
# Modules
import tkinter as tk 

# Main Window
window = tk.Tk()
window.title("Generator: UID & Password")
window.resizable(width = 0, height = 0)
window.rowconfigure(3)
window.columnconfigure(2)

""" Main """
# Frames:
# Section A:
frame_a = tk.Frame(
    master = window,
    bg = "#439f7f",
    relief = tk.RIDGE,
    borderwidth = 2
)
# Section B:
frame_b = tk.Frame(
    master = window,
    bg = "#89bee8",
    relief = tk.RIDGE,
    borderwidth = 2
)
# Section C:
frame_c = tk.Frame(
    master = window,
    bg = "#89bee8",
    relief = tk.RIDGE,
    borderwidth = 2
)

# Lables:
# Section A:
label_intro = tk.Label(
    master = frame_a,
    text = "This is a random user ID & Password generator.\nPlease press the button for a unique key.",
    font = ("", 10, "bold"),
    #bg = "#439f7f"
)

# Buttons:
# Section B:
butn_uid = tk.Button(
    master = frame_b,
    text = "Generate ID",
    width = 18
)

# Section C:
butn_pass = tk.Button(
    master = frame_c,
    text = "Generate Password",
    width = 18
)

""" Run """
# Frames:
frame_a.grid(sticky = "n", padx = 15, pady = 15)
frame_b.grid(sticky = "w", padx = 5, pady = 5)
frame_c.grid(sticky = "w", padx = 5, pady = 5)

# Lables:
label_intro.grid(row = 0, column = 0, padx = 10, pady = 10)

# Buttons:
butn_uid.grid(row = 1, column = 0, padx = 2, pady= 2)
butn_pass.grid(row = 2, column = 0, padx = 2, pady = 2)

""" End """
# Run Window
window.mainloop()