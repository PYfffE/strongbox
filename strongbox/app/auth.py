from flask import session
from dbmodel import add_user, check_user_exist, get_user
import dbmodel
from hashlib import sha1


def check_login(username, password):
    if check_user_exist(username):
        if len(username) > 20:
            return "Incorrect login or password"
        creds = get_user(username)
        if (username == creds[0]) and (sha1(password.encode()).hexdigest() == creds[1]):
            return 0
    return "Incorrect login or password"

def check_register(username, password):
    if len(password) < 6:
        return "Password must contain 6 symbols minimum"
    elif len(username) > 20:
        return "Too long username"
    elif check_user_exist(username):
        return "User already exist"
    add_user(username, sha1(password.encode()).hexdigest())
    return 0


def get_passwords(username):
    passwords = dbmodel.get_passwords(username)
    if not passwords:
        return []
    return passwords



