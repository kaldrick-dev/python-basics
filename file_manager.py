def save_message(message):
    try:
        with open("messages.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")

def read_message():
    print("Reading saved message...")
    try:
        with open("messages.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No saved message found.")
    except Exception as e:
        print(f"An error occurred while reading the message: {e}")            