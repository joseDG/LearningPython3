
from ..common.reservation import ReservationManagersProcessor
from .hilton_mgr import HiltonHotelManager
from .marriott_mgr import MarriottHotelManager


class HotelsManager(ReservationManagersProcessor):
    def __init__(self):
        # Create our managers and give to parent
        mgrs = [HiltonHotelManager(), MarriottHotelManager()]
        super().__init__(mgrs)
