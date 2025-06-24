import json
import re    # import Regex for email input validation


def load_users(filepath="users.json"):
    """
    Load users from a JSON file.

    Parameters:
    filepath (str): Path to the JSON file containing users.
    """
    with open(filepath, "r") as file:
        users = json.load(file)
    return users


def filter_users_by_name(users, name):
    """
    Filter users by their name (case insensitive).

    Parameters:
    users (list): List of user dictionaries.
    name (str): The name to filter users by.
    """
    return [user for user in users if user.get("name", "").lower() == name.strip().lower()]


def filter_users_by_age(users, age):
    """
    Filter users by their age.

    Parameters:
    users (list): List of user dictionaries.
    age (int): The age to filter users by.
    """
    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(users, email):
    """
    Filter users by their email address (case insensitive).

    Parameters:
    users (list): List of user dictionaries.
    email (str): The email address to filter users by.
    """
    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    users = load_users()

    filter_option = input("What would you like to filter by? ('name' or 'age' or 'email'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        if not name_to_search:
            print("Error: Name input cannot be empty.")
        elif not re.match(r"^[A-Za-zÄÖÜäöüß\s'-]{2,}$", name_to_search):
            print("Error: Invalid name. Only letters, spaces, hyphens, and apostrophes are allowed.")
        else:
            results = filter_users_by_name(users, name_to_search)
            if results:
                for user in results:
                    print(user)
            else:
                print(f"No users found with name: {name_to_search}")


    elif filter_option == "age":
        try:
            age_input = input("Enter an age to filter users: ").strip()
            if not age_input:
                print("Error: Age input cannot be empty.")
            else:
                age_to_search = int(age_input)
                filter_users_by_age(users, age_to_search)
        except ValueError:
            print("Invalid input. Please enter a numeric age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        if not email_to_search:
            print("Error: Email input cannot be empty.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_to_search):
            print("Error: Invalid email format.")
        else:
            results = filter_users_by_email(users, email_to_search)
            if results:
                for user in results:
                    print(user)
            else:
                print(f"No users found with email: {email_to_search}")


    else:
        print("Sorry, filtering by that option isn't available. Supported options: 'name', 'age'.")
