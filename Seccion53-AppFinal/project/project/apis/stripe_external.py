

class StripeUserInfo:
    def __init__(self, name = None, address = None):
        self.name = name
        self.address = address


class StripeCardInfo:
    def __init__(self, id = None, expire_date = None):
        self.id = id
        self.expire_date = expire_date


class StripePaymentAPI:
    @staticmethod
    def withdraw_money(user_info, card_info, money):
        print(f'StripePaymentAPI request')
        return True, '12345Stripe'           # Call Stripe backend


    @staticmethod
    def cancel_money(transaction_id):
        return True