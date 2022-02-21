
class TurkishCustomerInfo:
    def __init__(self, passport, name, birthdate):
        pass


class TurkishFlight:
    def __init__(self, cost, datetime_from, datetime_to):
        self.cost = cost
        self.datetime_from = datetime_from
        self.datetime_to = datetime_to


class TurkishOnlineAPI:
    def set_from_to_info(self, datetime_from, from_loc, datetime_to, to_loc):
        pass

    def set_passengers_info(self, infants, childern, adults):
        pass

    def get_available_flights(self):
        flights = []
        flights.append(TurkishFlight(400, "10-01-2022", "10-03-2022"))
        flights.append(TurkishFlight(431, "18-01-2022", "27-03-2022"))
        return flights

    @staticmethod
    def reserve_flight(customers_info: list, flight: TurkishFlight):
        confirmation_id = '1234TTTTT'  # None for failure
        return confirmation_id
        # return None     # Try None

    @staticmethod
    def cancel_flight(confirmation_id):
        return True
