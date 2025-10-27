#!/usr/bin/env

from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    while True:
        name = input("Enter your name: ")
        if validate_input(name):
            break
        print("Invali name! Try again.")

    while True:
            age = int(input("Enter your age: "))
            if validate_input(age):
                break
            print("Invalid age! Try again.")

    return name, age

if __name__=="__main__":
    show_intro()
    name,age = get_user_info()
    nameBin = convert_to_binary(name)
    ageBin = convert_to_binary(age)
    
    message = create_message(name,age,nameBin,ageBin)
    print(message)
    save_message(message)
    read_message()
    show_exit_message()
