
class Privileges():
    """This class only contain prvileges attribute."""

    def __init__(self):
        """Initialize previleges attribute."""
        self.privileges = ['can delete post', 'can ban user', 'can inspect user activities.']

    def show_privileges(self):
        """Show administrator privileges"""
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}.')
