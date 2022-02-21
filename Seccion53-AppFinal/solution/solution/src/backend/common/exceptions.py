


class ExpediaException(BaseException):
    pass

class ExpediaPaymentException(ExpediaException):
    pass

class ExpediaReservationException(ExpediaException):
    pass