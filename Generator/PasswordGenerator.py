""" The password generator class """

# Import modules
import random
import string

# Funtion 1: A start up welcome message and ask user input
def startup_msg_psw():
    global ask_user_pass
    print("Hi again! \nThis program will generate a unique password for you!", end="\n")
    ask_user_pass = str(input("Would you like a password to be generated, yes or no? :")) 

#startup_msg_psw()

# Function 2: Funtion to generate the password
def password_generator(pass_len = 12):
    startup_msg_psw()
    if ask_user_pass == "yes":
        rand_characters = string.digits + string.punctuation + string.ascii_letters
        pass_word = "".join(random.choice(rand_characters) for _ in range(pass_len))
        print(pass_word)
    elif ask_user_pass == "no":
        print("Password was not generated...")
    else:
        print("Please type yes or no...")
        password_generator()

password_generator()