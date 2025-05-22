import hashlib


user_db = {}

session = {"user": None}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup():
    username = input("Choose a username: ")
    
    if username in user_db:
        print("Username already exists!")
        return
    password = input("Choose a password: ")
    user_db[username] = hash_password(password)
    print("Account created successfullly..")

def login():
    username = input("Username: ")
    password = input("Password: ")
    hashed = hash_password(password)
    
    if user_db.get(username) == hashed:
        session["user"] = username
        print(f"Welcome, {username}! You are now logged in.")
    else:
        print(f"Invalid username or password.")

def logout():
    if session["user"]:
        print(f"Goodbye, {session['user']}!")
        session['user'] = None
    else:
        print("You are not Logged in.")

def dashboard():
    if session['user']:
        print(f"Dashboard - Logged in as: {session['user']}")
    
    else:
        print("Please log in to access the dashboard.")
def run():
    while True:
        print("\n --- MENU ---")
        print("1. Sign Up")
        print("2.  Login")
        print("3.  Dashboard")
        print("4.  Logout")
        print("5.  Exit")
        
        choice  = input("Choose an option (1 - 5 ): ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            dashboard()
        elif choice == '4':
            logout()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid chioce!!!")

run()