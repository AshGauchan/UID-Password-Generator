# testing Tkinter

import tkinter as tk 

window = tk.Tk() # window

frame_a = tk.Frame()
frame_b = tk.Frame()

lable_a = tk.Label(
    master = frame_a,
    text = "I am in Frame A"
)
lable_a.pack()

lable_b = tk.Label(
    master = frame_b,
    text = "I am in Frame B"
)
lable_b.pack(
    
)


# frame pack
frame_b.pack()
frame_a.pack()


window.mainloop() # open window

