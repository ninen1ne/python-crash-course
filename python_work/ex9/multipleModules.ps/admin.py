from user import User
from privileges import Privileges

class Admin(User):
    """Model a specific role of special user(admin)."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes from parent class.
        Then initialize attributes specific to admin role."""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


