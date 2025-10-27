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