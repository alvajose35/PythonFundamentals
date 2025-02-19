def login(database, username, password):

    if username in database and database[username] == password:
        print(f"\nWelcome back {username}!")
        return username
    
    elif username in database and not(database[username] == password):
        print(f"\nPassword for {username} does not match.")
        return ""
    
    else:
        print(f"\n{username} does not exist in the database. Please register.")
        return ""

def register(database, username):
    
    if username in database:
        print("\nUsername already registered.")
        return ""
    
    else:
        print(f"\n{username} has been registered.")
        return username
