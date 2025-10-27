def validate_input(user_input):
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    else:
        return False

def convert_to_binary(text):
    if text.isdigit():
        return bin(int(text))[2:]
    else:
        binaryName = []
        for char in text:
            partBinary = bin(ord(char))[2:]
            binaryName.append(partBinary)
        return ' '.join(binaryName)
    
def create_message(name, age, name_binary, age_binary):
    return(
        f"Hello {name}, your age {age} years old.\n"
        f"Name in binary is: {name_binary}\n"
        f"Age in binary is: {age_binary}"
    )