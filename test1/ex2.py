import random
import re
import string


def check_validity(password):
    if len(re.findall("[a-z]", password)) < 4:
        return False
    elif len(re.findall("[A-Z]", password)) < 2:
        return False
    elif len(re.findall("[0-9]", password)) < 1:
        return False
    elif len(re.findall("[$#!%@]", password)) < 1:
        return False
    elif len(password) > 20:
        return False
    elif len(password) < 8:
        return False
    return True


def random_password():
    password = ""
    arr_password = random.sample(string.digits, 1) + random.sample(string.ascii_lowercase, 4) + random.sample(
        string.ascii_uppercase, 2) + random.sample(['$', '#', '!', '%', '@'], 1)
    arr_password += [random.choice("$#!%@" + string.digits + string.ascii_letters) for i in range(random.randint(0, 20 - 8))]
    random.shuffle(arr_password)
    for symbol in arr_password:
        password += symbol
    return password