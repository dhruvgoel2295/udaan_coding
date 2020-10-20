import enum
class ParkingSpotType(enum.Enum):
    BIKE, CAR = 1, 2

class ParkingSpot(object):
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type

    
