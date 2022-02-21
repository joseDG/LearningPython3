from .utils import get_menu_choice
from ..backend.users_mgr import UsersManager

class SiteAccessManager:
    def __init__(self):
        self.users_mgr = UsersManager()     # backend object

    def print_menu(self):
        return get_menu_choice('System Access:', ['Login', 'Sign up [NA]'])

    def get_accessed_user(self):
        funcs = [self.login, self.signup]

        while True:
            choice = self.print_menu()
            user = funcs[choice-1]()

            if user is not None:
                return user
            else:
                print('Try again')

    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')

        user = self.users_mgr.get_user(username, password)
        if user is None:
            print('\nInvalid Username or Password')
        return user

    def signup(self):
        raise NotImplementedError



