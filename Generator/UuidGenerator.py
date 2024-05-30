""" The uuid generator class """

# Import modules
import uuid

# Define functions

# Function 1: A start up welcome message and ask user input
def startup_msg():
    global ask_user_uid

    print("Welcome!\nThis program will create a unique ID (UID) for you,\nin the form of random characters!", end="\n")   
    ask_user_uid = str(input("Would you like a UID, yes or no? :"))
    

# Function 2: Generate the UID , set to length 10 for default
def uid_generator(str_len = 10):
    startup_msg() # calling start up message
    if ask_user_uid == "yes":
        uid_string = str(uuid.uuid4().hex) # convert into string format and .hex = hyphen removed
        #print(uid_string)
        uid_upper = uid_string.upper() # convert into upper case
        #print(uid_up)
        uid_short = uid_upper[0:str_len] # shorten generated ID to desired length using slicing
        print(uid_short)
    elif ask_user_uid == "no":
        print("UID was not generated...")
    else:
        print("Please type yes or no...")
        uid_generator()
    
uid_generator() # call function
