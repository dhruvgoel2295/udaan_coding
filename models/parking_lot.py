from models.vehicle import VehicleType

class ParkingLot(object):
    def __init__(self, parking_lot_id, two_wheeler_spots_free, four_wheeler_spots_free, rates=None):
        self.parking_lot_id = parking_lot_id
        self.two_wheeler_spots_free = two_wheeler_spots_free
        self.two_wheeler_spots_occupied = {}
        self.four_wheeler_spots_free = four_wheeler_spots_free
        self.four_wheeler_spots_occupied = {}
        self.rates = rates
        self.current_ticket_number = 0


    def check_free(self, vehicle_type):
        if vehicle_type == VehicleType.BIKE:
            return len(self.two_wheeler_spots_free) > 0
        elif vehicle_type ==  VehicleType.CAR:
            return len(self.four_wheeler_spots_free) > 0
        return False


