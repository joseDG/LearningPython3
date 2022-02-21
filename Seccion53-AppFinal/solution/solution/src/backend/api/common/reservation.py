from abc import ABC, abstractmethod


class IReservation(ABC):
    @property
    @abstractmethod
    def total_cost(self):
        pass

    @property
    @abstractmethod
    def mgr(self):  # The (flight/hotel) manager that is responsible for reserve/cancel this reservation
        pass

    @abstractmethod
    def __repr__(self):
        pass


class ItineraryReservation(IReservation):
    """
    ItineraryReservation is just collection of reservations, so follows same interface
    """
    def __init__(self):
        super().__init__()
        self.reservations = []

    @property
    def total_cost(self):
        return sum([reservation.total_cost for reservation in self.reservations])

    @property
    def mgr(self):
        return None     # Each internal reservation has its own manager

    def __repr__(self):
        res = f'Itinerary Total Cost {self.total_cost}\n\t' + \
              '\n\t'.join([repr(reservation) for reservation in self.reservations])
        return res


class IReservationManager(ABC):
    """
    Represents a single reservation manager that does basic functionalities
    E.g. a canadian flights reservation manager searches CanadaAirlines for flights
    """
    @abstractmethod
    def search(self, request):
        pass

    @abstractmethod
    def reserve(self, reservation: IReservation):
        pass

    @abstractmethod
    def cancel(self, reservation: IReservation):
        pass


class ReservationManagersProcessor(IReservationManager):
    """
    Represents a group of (e.g. flights/hotels) managers.
    The class e.g. iterates on the managers to pass a request and send back answer
    """
    def __init__(self, mgrs):
        super().__init__()
        self.mgrs = mgrs

    def search(self, request):
        aggregated_result = []

        for mgr in self.mgrs:
            aggregated_result.extend(mgr.search(request))

        return aggregated_result

    def reserve(self, reservation: IReservation):
        return reservation.mgr.reserve(reservation) # get responsible manager and ask him

    def cancel(self, reservation: IReservation):
        return reservation.mgr.cancel(reservation)
