
from users import User, Privileges, Admin

class User:
    def __init__(self, first_name, last_name, username, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Information:")
        print(f"\tFirst Name: {self.first_name.title()}")
        print(f"\tLast Name: {self.last_name.title()}")
        print(f"\tUsername: {self.username}")
        print(f"\tEmail: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back!")


class Privileges:
    """A class to store a list of privileges."""

    def __init__(self, privileges=None):
        """Initialize the privileges attribute."""
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges assigned.")


class Admin(User):
    """Represents an administrator, a special kind of user."""

    def __init__(self, first_name, last_name, username, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges() # Admin has an instance of Privileges


# Create an instance of User (though not strictly required by the prompt for direct testing)
user1 = User("john", "doe", "johndoe", "john.doe@example.com")

# Create an instance of Privileges
admin_privileges = Privileges()

# Create an instance of Admin
admin_user = Admin("alice", "smith", "asmith", "alice.smith@example.com")

# Call the user description and greeting methods through the Admin instance
# (since Admin inherits from User, it has these methods)
print("--- Admin User Information ---")
admin_user.describe_user()
admin_user.greet_user()

# Call the show_privileges() method through the Admin instance's privileges attribute
print("\n--- Admin Privileges ---")
admin_user.privileges.show_privileges()

# You can also test with custom privileges
print("\n--- Another Admin with Custom Privileges ---")
custom_privs = ["can edit content", "can manage users", "can access logs"]
another_admin = Admin("bob", "johnson", "bjohnson", "bob.j@example.com")
another_admin.privileges = Privileges(custom_privs) # Assigning custom privileges
another_admin.describe_user()
another_admin.privileges.show_privileges()