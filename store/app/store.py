import csv
import datetime
import hashlib

import dbmodel
from dbmodel import get_passwords
from config import configs


def get_random(chars=20):
    return hashlib.md5(str(datetime.datetime.now()).encode() + configs['salt'].encode()).hexdigest()[:chars]


def generate_csv(user):
    rand = get_random(10)
    fn = f'{user}_export_{rand}.csv'
    path = f'/tmp/{fn}'

    header = ['Site', 'Username', 'Password']

    passwords = [i[1:4] for i in get_passwords(user)]

    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows((i for i in passwords))

    return fn


def add_password(username, site, user, password):
    if site == '' or user == '' or password == '':
        return 'Empty Field'
    dbmodel.add_password(username, site, user, password)
    return 0


def del_password(password_id):
    dbmodel.del_password(password_id)
    return 0
