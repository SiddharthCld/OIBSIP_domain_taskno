# cli_auth.py

# Simple dictionary to store user credentials (Username: Password)
users_db = {}

def register():
    print("\n--- Register ---")
    username = input("Enter a new username: ")
    if username in users_db:
        print("Error: Username already exists!")
        return
    
    password = input("Enter a new password: ")
    users_db[username] = password
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists and password matches
    if users_db.get(username) == password:
        print("\nLogin successful!")
        secure_page(username)
    else:
        print("\nError: Invalid credentials.")

def secure_page(username):
    # This page can only be reached if login is successful
    print(f"\n*** SECURED PAGE ***")
    print(f"Welcome, {username}! You now have access to the secure area.")
    print("Type 'logout' to return to the main menu.")
    
    while True:
        action = input("> ")
        if action.lower() == 'logout':
            print("Logging out...")
            break

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()