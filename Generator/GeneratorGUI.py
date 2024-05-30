""" Start """
# Modules
import random, string, uuid, tkinter as tk  

""" UID """
# Function 1: A start up welcome message and ask user input
def startup_msg():
    print("Welcome!\nThis program will create a unique ID (UID) for you,\nin the form of random characters!", end="\n")   

# Function 2: Generate the UID , set to length 10 for default
def uid_generator(str_len = 10):
    uid_string = str(uuid.uuid4().hex) # convert into string format and .hex = hyphen removed
    uid_upper = uid_string.upper() # convert into upper case
    uid_short = uid_upper[0:str_len] # shorten generated ID to desired length using slicing
    
    label_uid_short = tk.Label(master = frame_b, text = uid_short, font = ("bold"))
    label_uid_short.grid(row = 1, column = 1, padx = 20, sticky = "")

""" Pass """ 
# Funtion 1: A start up welcome message and ask user input
def startup_msg_psw():
    print("Hi again! \nThis program will generate a unique password for you!", end="\n")

# Function 2: Funtion to generate the password
def password_generator(pass_len = 12):
    rand_characters = string.digits + string.punctuation + string.ascii_letters
    pass_word = "".join(random.choice(rand_characters) for _ in range(pass_len))
    
    label_pass_word = tk.Label(master = frame_c, text = pass_word, font = ("bold"))
    label_pass_word.grid(row = 2, column = 1, padx = 20, sticky = "")

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
    width = 18,
    command = uid_generator
)

# Section C:
butn_pass = tk.Button(
    master = frame_c,
    text = "Generate Password",
    width = 18,
    command = password_generator
)

# Entry
# UID:
entry_uid1 = tk.Entry(master = frame_b)
#entry_uid2 = entry_uid1.get(0, uid_short)

# Password:
#entry_password = tk.Entry().get(0, pass_word)

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