def save_message(message):
    try:
        with open("messages.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")