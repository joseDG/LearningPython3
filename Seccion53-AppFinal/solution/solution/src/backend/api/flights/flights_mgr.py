
from ..common.reservation import ReservationManagersProcessor
from .aircanada_mgr import AirCanadaFlightsManager
from .turkish_mgr import TurkishFlightsManager


class FlightsManager(ReservationManagersProcessor):
    def __init__(self):
        # Create our managers and give to parent
        mgrs = [AirCanadaFlightsManager(), TurkishFlightsManager()]
        super().__init__(mgrs)
