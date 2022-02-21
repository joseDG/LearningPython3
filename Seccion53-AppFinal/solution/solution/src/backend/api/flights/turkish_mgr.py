from .flight_common import Flight, FlightRequest, FlightReservation
from .turkish_external import TurkishOnlineAPI, TurkishFlight, TurkishCustomerInfo
from ..common.reservation import IReservationManager
from ..common.customer_info import CustomerInfo

class TurkishFlightsManager(IReservationManager):
    def __init__(self):
        self.api = TurkishOnlineAPI()

    def search(self, request: FlightRequest):

        self.api.set_from_to_info(request.datetime_from, request.from_loc, request.datetime_to, request.to_loc)
        self.api.set_passengers_info(request.infants, request.children, request.adults)

        flights_external = self.api.get_available_flights()

        # Convert from the API flight format to a unified project format
        flights = []
        for flight_external in flights_external:
            flight =  Flight('Turkish Airline', flight_external.cost, request, self)
            flights.append(flight)
        return flights

    @staticmethod
    def _to_turkish_flight_external(flight: Flight):
        return TurkishFlight(flight.total_cost, flight.request.datetime_from, flight.request.datetime_to)

    @staticmethod
    def _to_turkish_customers_info_external(customers_info: list):
        result = []
        for customer in customers_info:
            customer: CustomerInfo = customer
            result.append(TurkishCustomerInfo(customer.passport_id, customer.name, customer.birthdate))
        return result

    def reserve(self, reservation: FlightReservation):
        # convert from our unified project format to airlines API
        flight = self._to_turkish_flight_external(reservation.flight)
        customers_info = self._to_turkish_customers_info_external(reservation.customers_info)
        return TurkishOnlineAPI.reserve_flight(customers_info, flight)

    def cancel(self, reservation):
        return TurkishOnlineAPI.cancel_flight(reservation.confirmation_id)