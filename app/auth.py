import sqlite3
import bcrypt

# ---------------- DATABASE CONNECTION ----------------

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ---------------- SIGNUP FUNCTION ----------------

def signup(username, password):

    # Check if username exists
    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        return False

    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )

    # Insert user
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password)
    )

    conn.commit()

    return True


# ---------------- LOGIN FUNCTION ----------------

def login(username, password):

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()

    if result:

        stored_password = result[0]

        if bcrypt.checkpw(
            password.encode('utf-8'),
            stored_password
        ):
            return True

    return False