""" The Tkinter GUI creation """
# Import
import tkinter as tk

# Window
window = tk.Tk()

""" Frames """
# Main frame:
frm_main = tk.Frame(
    master = window,
    height = 400,
    width = 500
)
frm_main.pack()

# UID frame
frm_uid = tk.Frame(
    master = frm_main
)
frm_uid.pack(fill = tk.BOTH)

# Password frame
frm_psw = tk.Frame(
    master = frm_main
)
frm_psw.pack(fill = tk.BOTH)

""" Labels """
# UID label 
lbl_uid = tk.Label(
    master = frm_uid,
    text = "UID",
    bg = "#feffbb",
    height = 200,
    width = 500
)
lbl_uid.pack()

# Password label 
lbl_psw = tk.Label(
    master = frm_psw,
    text = "Password",
    bg = "#cdebea",
    height = 200,
    width = 500
)
lbl_psw.pack(side = tk.TOP)

# Launch window
window.mainloop()
