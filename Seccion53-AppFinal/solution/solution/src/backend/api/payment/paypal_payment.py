
from .payment_common import IPayment
from .paypal_external import *

class PayPalPayment(IPayment):
    def __init__(self):
        self.paypal = PayPalOnlinePaymentAPI()
        self.card = PayPalCreditCard()

    def set_user_info(self, name, address):
        self.card.name = name
        self.card.address = address

    def set_card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.card.ccv = ccv

    def make_payment(self, money):
        self.paypal.card_info = self.card
        return self.paypal.pay_money(money)

    def cancel_payment(self, transaction_id):
        return self.paypal.cancel_money(transaction_id)