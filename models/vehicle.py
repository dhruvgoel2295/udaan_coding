import enum
class VehicleType(enum.Enum):
    BIKE, CAR = 1, 2

class Vehicle(object):
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.tickets = {}
        self.active_ticket = None

    def set_active_ticket(self, ticket=None):
        self.active_ticket = ticket

        
