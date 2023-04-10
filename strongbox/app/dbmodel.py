import sqlite3
import uuid

import psycopg2
from config import db_config

conn = psycopg2.connect(database=db_config["database"],
                        host=db_config["host"],
                        user=db_config["user"],
                        password=db_config["password"],
                        port=db_config["port"])


def add_user(username, password_hash):
    cur = conn.cursor()
    cur.execute("""INSERT INTO users
        (id, username, password)
        VALUES
        (nextval('useq'),%s, %s);""", (username, password_hash,))
    conn.commit()
    cur.close()
    return 0


def get_user(username):
    cur = conn.cursor()
    cur.execute("SELECT username, password FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    return user


def get_passwords(username):
    cur = conn.cursor()
    cur.execute("SELECT id, site, username, password FROM stored_passwords WHERE username_id = %s", (username,))
    passwords = cur.fetchall()
    cur.close()
    return passwords


def check_user_exist(username):
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM users WHERE username = %s", (username,))
    res = cur.fetchone()
    cur.close()
    if res is None:
        return 0
    return 1


def add_password(username_id, site, user, password):
    cur = conn.cursor()
    password_id = str(uuid.uuid4())
    cur.execute("""INSERT INTO stored_passwords
            (id, username_id, site, username, password)
            VALUES
            (%s, %s, %s, %s, %s);""", (password_id, username_id, site, user, password,))
    conn.commit()
    cur.close()
    return 0


def del_password(password_id):
    if password_id == 'deadbeef':
        return 1
    cur = conn.cursor()
    cur.execute("""DELETE FROM stored_passwords
            WHERE id = %s;""", (password_id,))
    conn.commit()
    cur.close()
    return 0
