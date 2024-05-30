""" ---The Tkinter GUI creation--- """
# Import
import tkinter as tk 

# Main Window 
window = tk.Tk()
window.title("Generator: UID & Password ")
window.geometry('600x400') # width x height of window
window.resizable(width = 0, height = 0) # window set to not resizeable

window.rowconfigure(0) # = 1 row 
window.columnconfigure(2) # = 3 columns >> index starts at [0, 1, 2] >> 3 in total 

""" ---Frames--- """
# Section A: 
frame_section_a = tk.Frame(
    master = window,
    height = 500,
    width = 500,
    bg = "yellow"
)

# Section B: 
frame_section_b = tk.Frame(
    master = window,
    height = 500,
    width = 500,
    bg = "red"
)

# Section C: 
frame_section_c = tk.Frame(
    master = window,
    height = 500,
    width = 500,
    bg = "blue"
)

""" ---Labels--- """ 
    # row = i & column = j
# Section A: Intro msg
label_intro_msg = tk.Label(
    master = frame_section_a,
    text = "This program will generate a\nrandom User ID & Password.\nPlease press each button to generate a key.",
    font = ("", 9,"bold"),
    bg = "#fffbae"
)
#label_intro_msg.grid(row = 0, column = 0)

# Section B: UID 
label_uid = tk.Label(
    master = frame_section_b,
    text = "UID Generator",
    bg = "#ffb1cd"
)
#label_uid.grid(row = 1, column = 0)

# Section C: Password
label_password = tk.Label(
    master = frame_section_c,
    text = "Password Generator",
    bg = "#cde2d7"
)
#label_password.grid(row = 2, column = 0)

""" ---RUN--- """
# Frames
frame_section_a.pack(fill = tk.BOTH)
frame_section_b.pack(fill = tk.BOTH)
frame_section_c.pack(fill = tk.BOTH)

# Labels
label_intro_msg.grid() # fill only used with .pack()
label_uid.grid(row = 0, column = 2, sticky = "e")
label_password.grid(sticky = "e") # sticky only used with .grid()




""" ---LAUNCH WIN--- """
# Launch window
window.mainloop()