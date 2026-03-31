import json
import os
import hashlib

USERS_FILE = "users.json"


# =========================
#  HASH FUNCTION
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
#  LOAD USERS
# =========================
def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# =========================
#  SAVE USERS
# =========================
def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# =========================
#  SIGNUP
# =========================
def signup():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if user exists
    for user in users:
        if user["username"] == username:
            print(" User already exists")
            return None

    # Store hashed password
    users.append({
        "username": username,
        "password": hash_password(password)
    })

    save_users(users)
    print(" Signup successful!")
    return username


# =========================
#  LOGIN
# =========================
def login():
    users = load_users()

    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_input = hash_password(password)

    for user in users:
        if user["username"] == username and user["password"] == hashed_input:
            print(" Login successful!")
            return username

    print(" Invalid credentials")
    return None
