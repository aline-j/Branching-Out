import json


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
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


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
        filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(users, age_to_search)
        except ValueError:
            print("Invalid input. Please enter a numeric age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users, email_to_search)

    else:
        print("Sorry, filtering by that option isn't available. Supported options: 'name', 'age'.")
