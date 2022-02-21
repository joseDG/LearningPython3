from .flight_common import Flight, FlightRequest, FlightReservation
from .aircanada_external import AirCanadaOnlineAPI, AirCanadaFlight, AirCanadaCustomerInfo
from ..common.reservation import IReservationManager
from ..common.customer_info import CustomerInfo


class AirCanadaFlightsManager(IReservationManager):
    def __init__(self):
        pass

    def search(self, request: FlightRequest):
        flights_external = AirCanadaOnlineAPI.get_flights(request.from_loc, request.datetime_from,
                                       request.to_loc, request.datetime_to,
                                       request.adults, request.children)

        # Convert from the API flight format to a unified project format
        flights = []
        for flight_external in flights_external:
            # pass self as the generating manager
            flight = Flight('AirCanada', flight_external.price, request, self)
            flights.append(flight)
        return flights

    def reserve(self, reservation: FlightReservation):
        # convert from our unified project format to airlines API
        flight = self._to_aircanda_flight_external(reservation.flight)
        customers_info = self._to_aircanda_customers_info_external(reservation.customers_info)
        return AirCanadaOnlineAPI.reserve_flight(flight, customers_info)

    def cancel(self, reservation):
        return AirCanadaOnlineAPI.cancel_flight(reservation.confirmation_id)

    @staticmethod
    def _to_aircanda_flight_external(flight: Flight):
        return AirCanadaFlight(flight.total_cost, flight.request.datetime_from, flight.request.datetime_to)

    @staticmethod
    def _to_aircanda_customers_info_external(customers_info: list):
        result = []
        for customer in customers_info:
            customer: CustomerInfo = customer
            result.append(AirCanadaCustomerInfo(customer.name, customer.passport_id, customer.birthdate))
        return result