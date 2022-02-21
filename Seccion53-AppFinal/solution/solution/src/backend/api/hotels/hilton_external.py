
class HiltonCustomerInfo:
    def __init__(self, name, passport, birthdate):
        pass

class HiltonRoom:
    def __init__(self, room_type, available, price_per_night, date_from, date_to):
        self.room_type = room_type
        self.available = available
        self.price_per_night = price_per_night
        self.date_from = date_from
        self.date_to = date_to

class HiltonHotelAPI:
    @staticmethod
    def search_rooms(location, from_date, to_date, adults, children, needed_rooms):
        rooms = []
        rooms.append(HiltonRoom("Interior View", 6, 200.0, "29-01-2022", "10-02-2022"))
        rooms.append(HiltonRoom("City View", 3, 300.0, "29-01-2022", "10-02-2022"))
        rooms.append(HiltonRoom("Deluxe View", 8, 500.0, "29-01-2022", "10-02-2022"))
        return rooms

    @staticmethod
    def reserve_room(room: HiltonRoom, customers_info: list):
        confirmation_id = '45544HiltonHotelAPI4545'  # None for failure
        return confirmation_id

    @staticmethod
    def cancel_room(confirmation_id):
        return True
