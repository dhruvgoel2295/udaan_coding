from models.parking_spot import ParkingSpot
from models.parking_spot import ParkingSpotType


class FourWheelerSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, ParkingSpotType.CAR)

    
