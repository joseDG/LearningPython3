
# This class allows us to minimize dependency between front end and backend
# it performs delegation behind the scene

from .api.flights.flights_mgr import FlightsManager
from .api.flights.flight_common import FlightRequest
from .api.hotels.hotels_mgr import HotelsManager
from .api.hotels.hotel_common import HotelRequest
from .api.common.reservation import IReservation, ItineraryReservation
from .api.payment.paypal_payment import PayPalPayment
from .common.exceptions import ExpediaPaymentException, ExpediaReservationException


class CustomerBackendManager:
    def __init__(self, customer):
        self.customer = customer
        self.flights_mgr = FlightsManager()
        self.hotels_mgr = HotelsManager()
        self.payment_api = PayPalPayment()      # only one payment method at a time

    def search_flights(self, request: FlightRequest):
        return self.flights_mgr.search(request)

    def search_hotels(self, request: HotelRequest):
        return self.hotels_mgr.search(request)

    def get_payment_choices(self):
        return [repr(card) for card in self.customer.payment_cards]

    def _make_payment(self, cost, card):
        self.payment_api.set_user_info(card.owner_name, card.address)
        self.payment_api.set_card_info(card.card_number, card.expiry_date, card.security_code)
        status, transaction_id = self.payment_api.make_payment(cost)
        return status, transaction_id

    def _cancel_payment(self, transaction_id):
        self.payment_api.cancel_payment(transaction_id)

    def _cancel_reservations(self, reservations):
        # For simplicity: assume cancellation will always work. In reality, no
        for reservation in reservations:
            reservation.mgr.cancel(reservation)

    def _reserve(self, reservations):
        """
        Reserve all the given reservations. If failed to reserve a some of them, then all are cancelled.

        :return: True if succeeded
        """
        if not isinstance(reservations, list):
            reservations = [reservations]   # let's always make a list

        reserved_items = [] # track whatever reserved
        for reservation in reservations:
            confirmation_id = reservation.mgr.reserve(reservation)
            if confirmation_id:
                reservation.confirmation_id = confirmation_id
                reserved_items.append(reservation)
            else:
                reservation.mgr.cancel(reserved_items)  # cancel all reserved SO FAR
                return False
        return True

    def pay_and_reserve(self, reservation: IReservation, payment_card_idx):
        payment_card = self.customer.payment_cards[payment_card_idx]
        total_cost = reservation.total_cost
        is_paid, transaction_id = self._make_payment(total_cost, payment_card)

        if is_paid:
            if isinstance(reservation, ItineraryReservation):
                is_reserved = self._reserve(reservation.reservations)
            else:
                is_reserved = self._reserve(reservation)

            if not is_reserved:
                self._cancel_payment(transaction_id)
                raise ExpediaReservationException

        else:
            raise ExpediaPaymentException



