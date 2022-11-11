from hashlib import md5





def passwEncode(password):
    return md5(password.encode()).hexdigest()