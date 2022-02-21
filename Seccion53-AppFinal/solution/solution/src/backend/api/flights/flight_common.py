from ..common.reservation import IReservation


class FlightRequest:
    def __init__(self, datetime_from, from_loc, datetime_to, to_loc, infants, children, adults):
        self.datetime_from = datetime_from
        self.from_loc = from_loc
        self.datetime_to = datetime_to
        self.to_loc = to_loc
        # Counts for
        self.infants = infants
        self.children = children
        self.adults = adults

    def __repr__(self):
        return f'From: {self.from_loc} on {self.datetime_from} - To {self.to_loc} ' \
               f'on {self.datetime_to} - #infants {self.infants} #children {self.children} # adults {self.adults}'


class Flight:
    def __init__(self, airline_name, total_cost, request: FlightRequest, flight_mgr):
        """
        :param flight_mgr: The manager that created this flight. It maybe used later for reservation
        """
        self.airline_name = airline_name
        self.total_cost = total_cost
        self.request = request
        self.flight_mgr = flight_mgr

    def __repr__(self):
        return f'{self.airline_name}: Cost {self.total_cost} - {self.request}'





class FlightReservation(IReservation):
    def __init__(self, flight: Flight, customers_info: list):
        super().__init__()
        self.flight = flight
        self.customers_info = customers_info

    @property
    def total_cost(self):
        return self.flight.total_cost

    @property
    def mgr(self):
        return self.flight.flight_mgr

    def __repr__(self):
        return repr(self.flight)

