storage = ""

def encode(password):
    newstr = ""
    for c in password:
        newstr += str(int(c) + 3)
    return newstr


def decode(password):
    int_password = []
    for num in password:
        if int(num) > 2:
            int_password.append(int(num) - 3)
        elif int(num) <= 2:
            int_password.append((int(num) + 10) - 3)
    decoded_password = ""
    for i in int_password:
        decoded_password += str(i)
    return decoded_password
