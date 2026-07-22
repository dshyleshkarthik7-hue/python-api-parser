from api import get_user
from parser import UserParser


def main():
    response = get_user()

    user = UserParser.from_dict(response)

    print(user)
    print()
    print(f"Username : {user.username}")
    print(f"Email    : {user.email}")
    print(f"City     : {user.city}")
    print(f"Zip Code : {user.zipcode}")


if __name__ == "__main__":
    main()
