from .utils import get_menu_choice
from ..backend.user import Customer
from ..backend.api.common.reservation import ItineraryReservation
from ..backend.api.common.customer_info import CustomerInfo
from ..backend.api.flights.flight_common import FlightRequest, FlightReservation
from ..backend.api.hotels.hotel_common import HotelRequest, HotelReservation
from ..backend.customer_backend_mgr import CustomerBackendManager
from ..backend.common.exceptions import ExpediaPaymentException, ExpediaReservationException


class CustomerFrontendManager:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.customer_backend_mgr = CustomerBackendManager(customer)
        self.current_itinerary = ItineraryReservation()
        self.itineraries = []

        #self._load_data()

    def _load_data(self):
        s = '1'
        request = FlightRequest(s, s, s, s, s, s, s)
        flights = self.customer_backend_mgr.search_flights(request)
        customer = CustomerInfo(self.customer.name, None, None)  # temp. in practice build
        reservation = FlightReservation(flights[0], [customer])
        status = self.customer_backend_mgr._reserve(reservation)
        self.current_itinerary.reservations.append(reservation)

        s = '2'
        request = FlightRequest(s, s, s, s, s, s, s)
        flights = self.customer_backend_mgr.search_flights(request)
        customer = CustomerInfo(self.customer.name, None, None)  # temp. in practice build
        reservation = FlightReservation(flights[1], [customer])
        self.current_itinerary.reservations.append(reservation)
        self.reserve_itinerary()

        s = '2'
        request = FlightRequest(s, s, s, s, s, s, s)
        flights = self.customer_backend_mgr.search_flights(request)
        customer = CustomerInfo(self.customer.name, None, None)  # temp. in practice build
        reservation = FlightReservation(flights[2], [customer])
        status = self.customer_backend_mgr._reserve(reservation)
        self.current_itinerary.reservations.append(reservation)

        s = '4'
        request = FlightRequest(s, s, s, s, s, s, s)
        flights = self.customer_backend_mgr.search_flights(request)
        customer = CustomerInfo(self.customer.name, None, None)  # temp. in practice build
        reservation = FlightReservation(flights[3], [customer])
        self.current_itinerary.reservations.append(reservation)

        s = '5'
        request = HotelRequest(s, s, s, s, s, s, s)
        hotels = self.customer_backend_mgr.search_hotels(request)
        customer = CustomerInfo(self.customer.name, None, None)  # temp. in practice build
        reservation = HotelReservation(hotels[0], [customer])
        self.current_itinerary.reservations.append(reservation)

        self.reserve_itinerary()

        self.list_itineraries()

    def print_menu(self):
        msgs = ['View profile [NA]', 'Make itinerary', 'List my itineraries', 'Logout']
        return get_menu_choice(f'Welcome {self.customer}:', msgs)

    def run(self):
        funcs = [self.view_profile, self.make_itinerary, self.list_itineraries]

        while True:
            choice = self.print_menu()
            if choice == 4:
                self.customer = None
                return
            else:
                funcs[choice - 1]()

    def view_profile(self):
        raise NotImplementedError

    def make_itinerary(self):
        self.current_itinerary = ItineraryReservation()
        funcs = [self.add_flight, self.add_hotel, self.reserve_itinerary, self.cancel_itinerary]

        def print_menu():
            msgs = ['Add Flight', 'Add Hotel', 'Reserve itinerary', 'Cancel itinerary']
            return get_menu_choice(f'Create your itinerary:', msgs)

        while True:
            choice = print_menu()
            funcs[choice - 1]()

            if choice >= 3:
                return

    def list_itineraries(self):
        if not self.itineraries:
            print('No itineraries at the moment')
            return

        print(f'Listing {len(self.itineraries)} itineraries')
        for itin in self.itineraries:
            print(repr(itin), '\n')

    def add_flight(self):
        def read_flight_request():
            from_loc = input('Enter from: ')
            from_dte = input('Enter From Date (dd-mm-yy): ')
            to_loc = input('Enter To: ')
            to_dte = input('Enter Return Date (dd-mm-yy): ')
            # In practice we need to make sure valid int are given
            infants = int(input('Enter # of infants: '))
            children = int(input('Enter # of children: '))
            adults = int(input('Enter # of adults: '))

            return FlightRequest(from_dte, from_loc, to_dte, to_loc, infants, children, adults)

        request = read_flight_request()
        flights = self.customer_backend_mgr.search_flights(request)

        choice = get_menu_choice(f'Select a flight:', flights)

        customer = CustomerInfo(self.customer.name, None, None)    # temp. in practice build
        reservation = FlightReservation(flights[choice-1], [customer])
        self.current_itinerary.reservations.append(reservation)

    def add_hotel(self):
        def read_hotel_request():
            room_type = input('Enter room type: ')
            datetime_from = input('Enter From Date (dd-mm-yy): ')
            datetime_to = input('Enter To Date (dd-mm-yy): ')
            location = input('Enter location: ')
            num_rooms = int(input('Enter # of rooms: '))
            children = int(input('Enter # of children: '))
            adults = int(input('Enter # of adults: '))

            return HotelRequest(room_type, datetime_from, datetime_to, location, num_rooms, children, adults)

        request = read_hotel_request()
        hotels = self.customer_backend_mgr.search_hotels(request)

        choice = get_menu_choice(f'Select a hotel:', hotels)

        customer = CustomerInfo(self.customer.name, None, None)
        reservation = HotelReservation(hotels[choice-1], [customer])
        self.current_itinerary.reservations.append(reservation)

    def reserve_itinerary(self):
        if self.current_itinerary.reservations:
            choices = self.customer_backend_mgr.get_payment_choices()
            choice = get_menu_choice(f'Which payment card:', choices)
            try:
                self.customer_backend_mgr.pay_and_reserve(self.current_itinerary, choice-1)
            except ExpediaPaymentException as e:
                print(e)
                print('Failed to pay. Review your balance')
            except ExpediaReservationException as e:
                print(e)
                print('Failed to complete reservation. Money will be returned shortly. Try again later')
            else:
                self.itineraries.append(self.current_itinerary)
                self.current_itinerary = ItineraryReservation()
                print('Successfully paid and reserved the trip')

        else:
            print('Nothing is added to reserve')

    def cancel_itinerary(self):
        # Iterate on each reservation: cancel it
        self.current_itinerary = ItineraryReservation()


