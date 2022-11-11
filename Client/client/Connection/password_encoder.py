from hashlib import md5



def passwEncode(password) -> str:
    return md5(password.encode()).hexdigest()