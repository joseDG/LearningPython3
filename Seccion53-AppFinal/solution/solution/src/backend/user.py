

class User:
    def __init__(self, user_name, password, name, email):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.email = email


    def __repr__(self):
        return f'{self.name} | {type(self).__name__}'


class Customer(User):
    def __init__(self, user_name, password, name, email):
        super().__init__(user_name, password, name, email)
        # ReservationsSet reservations;
        self.payment_cards = []



class Admin(User):
    pass