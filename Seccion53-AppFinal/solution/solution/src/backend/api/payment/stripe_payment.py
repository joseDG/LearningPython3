
from .payment_common import IPayment
from .stripe_external import *


class StripePayment(IPayment):
    def __init__(self):
        self.card = StripeCardInfo()
        self.user = StripeUserInfo()

    def set_user_info(self, name, address):
        self.user.name = name
        self.user.address = address

    def set_card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.card.ccv = ccv

    def make_payment(self, money):
        return StripePaymentAPI.withdraw_money(self.user, self.card, money)

    def cancel_payment(self, transaction_id):
        return StripePaymentAPI.cance_money(transaction_id)
