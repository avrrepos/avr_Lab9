storage = ""

def encode(password):
    newstr = ""
    for c in password:
        newstr += str(int(c) + 3)
    return newstr

