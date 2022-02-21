
from abc import ABC, abstractmethod

class IPayment(ABC):    # I for interface
    @abstractmethod
    def set_user_info(self, name, address):
        pass

    @abstractmethod
    def set_card_info(self, id, expire_date, ccv):
        pass

    @abstractmethod
    def make_payment(self, money):
        pass

    @abstractmethod
    def cancel_payment(self, transaction_id):
        pass


class PaymentCard:
    def __init__(self, owner_name, card_number, expiry_date, security_code, address):
        self.owner_name = owner_name
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.security_code = security_code
        self.address = address

    def __repr__(self):
        return f'{self.__class__.__name__}- Name: {self.owner_name}, Number: {self.card_number}, Expiry Date: {self.expiry_date}'


class DebitCard(PaymentCard):
    def __init__(self, owner_name, card_number, expiry_date, security_code, address):
        super().__init__(owner_name, card_number, expiry_date, security_code, address)


class CreditCard(PaymentCard):
    def __init__(self, owner_name, card_number, expiry_date, security_code, address):
        super().__init__(owner_name, card_number, expiry_date, security_code, address)



