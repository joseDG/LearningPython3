
class MarriottCustomerInfo:
    def __init__(self, name, passport, birthdate):
        pass

class MarriottRoom:
    def __init__(self, room_type, available, price_per_night, date_from, date_to):
        self.room_type = room_type
        self.available = available
        self.price_per_night = price_per_night
        self.date_from = date_from
        self.date_to = date_to


class MarriottHotelAPI:
    @staticmethod
    def search_available_rooms(location, from_date, to_date, adults, children, needed_rooms):
        rooms = []
        rooms.append(MarriottRoom("City View", 5, 444.0, "24-01-2022", "12-02-2022"))
        rooms.append(MarriottRoom("Deluxe View", 3, 350.0, "28-01-2022", "190-02-2022"))
        return rooms

    @staticmethod
    def do_room_reservation(room: MarriottRoom, customers_info: list):
        confirmation_id = '45544MarriottHotelAPI4545'  # None for failure
        return confirmation_id

    @staticmethod
    def cancel_room(confirmation_id):
        return True
