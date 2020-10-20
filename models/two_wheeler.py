from models.vehicle import Vehicle
from models.vehicle import VehicleType

class TwoWheeler(Vehicle):
    def __init__(self, vehicle_id):
        super().__init__(vehicle_id, VehicleType.BIKE)

    
