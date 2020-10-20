from models.parking_spot import ParkingSpot
from models.parking_spot import ParkingSpotType

class TwoWheelerSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(id, ParkingSpotType.BIKE)

    
