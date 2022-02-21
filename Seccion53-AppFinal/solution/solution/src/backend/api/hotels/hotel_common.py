from ..common.reservation import IReservation


class HotelRequest:
    def __init__(self, room_type, datetime_from, datetime_to, location, num_rooms, children, adults):
        self.room_type = room_type
        self.datetime_from = datetime_from
        self.datetime_to = datetime_to
        self.location = location
        self.num_nights = 5     # compute it from the from-to dates
        self.children = children
        self.adults = adults
        self.num_rooms = num_rooms


    def __repr__(self):
        return f'From: {self.location} on {self.datetime_from} - ' \
               f'#num nights {self.num_nights} - #num rooms {self.num_rooms} - #children {self.children} #adults {self.adults}'


class Hotel:
    def __init__(self, hotel_name, price_per_night, request: HotelRequest, hotel_mgr):
        """
        :param hotel_mgr: The manager that created this Hotel. It maybe used later for reservation
        """
        self.hotel_name = hotel_name
        self.price_per_night = price_per_night
        self.request = request
        self.hotel_mgr = hotel_mgr

    @property
    def total_cost(self):
        return self.price_per_night * self.request.num_nights

    def __repr__(self):
        return f'{self.hotel_name}: Per night: {self.price_per_night} - Total cost {self.total_cost} - {self.request}'


class HotelReservation(IReservation):
    def __init__(self, hotel: Hotel, customers_info: list):
        super().__init__()
        self.hotel = hotel
        self.customers_info = customers_info

    @property
    def total_cost(self):
        return self.hotel.total_cost

    @property
    def mgr(self):
        return self.hotel.hotel_mgr

    def __repr__(self):
        return repr(self.hotel)


