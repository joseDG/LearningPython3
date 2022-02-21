
# In practice, you may download their code here to contact remotely Paypal
# This is external code. It knows NOTHING about ur project.
# We use it. It doesn't use our code base

class PayPalCreditCard:
    def __init__(self, name = None, address= None,
          id= None, expire_date= None, ccv= None):
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv

class PayPalOnlinePaymentAPI:
    def __init__(self, card_info : PayPalCreditCard = None):
        self.card_info = None

    def pay_money(self, money):
        print(f'PayPalOnlinePaymentAPI pay_money')
        return True, '12345PayPal'    # Call PayPal backend
        # Switch it to False to see failulres and their handling

    def cancel_money(self, transaction_id):
        print(f'PayPalOnlinePaymentAPI cancel_money')
        return True