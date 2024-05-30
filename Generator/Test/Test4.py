import tkinter as tk 

# Window:
window = tk.Tk()

# Frame:
fram_main = tk.Frame(
    master = window,
    height = 400,
    width = 400
)
fram_main.pack()

# Labels 1:
label_1 = tk.Label(
    text = "I am at x: 0 and y: 0",
    bg = "red"
)
label_1.place(
    x = 0,
    y = 0
)

# Label 2:
label_2 = tk.Label(
    text = "I am at x: 130 and y: 130",
    bg = "yellow"
)
label_2.place(
    x = 130,
    y = 130
)

# Launch window:
window.mainloop()