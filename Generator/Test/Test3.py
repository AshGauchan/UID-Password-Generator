# import module
import tkinter as tk

# create window
window = tk.Tk()

# code
frame_1 = tk.Frame(
    master = window,
    height = 100,
    width = 200,
    bg = "red"
)
frame_1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

frame_2 = tk.Frame(
    master = window,
    height = 100,
    width = 100,
    bg = "yellow"
)
frame_2.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

frame_3 = tk.Frame(
    master = window,
    height = 100,
    width = 50,
    bg = "blue"
)
frame_3.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

# run loop
window.mainloop()
