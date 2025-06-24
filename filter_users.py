import json


def filter_users_by_name(name):
    """
    Filter users from a JSON file by their name (case insensitive).

    Parameters:
    name (str): The name to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """
    Filter users from a JSON file by their age.

    Parameters:
    age (int): The age to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    # Filter users whose age matches the provided age
    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """
    Filter users from a JSON file by their email address (case insensitive).

    Parameters:
    email (str): The email address to filter users by.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    # Prompt the user for a filtering option
    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    if filter_option == "name":
        # Prompt the user for a name to search
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        # Prompt the user for an age to search
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Invalid input. Please enter a numeric age.")

    else:
        # Inform the user that the filter option is not supported
        print("Sorry, filtering by that option isn't available. Supported options: 'name', 'age'.")
