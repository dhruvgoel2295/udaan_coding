from models.parking_lot import ParkingLot
from models.vehicle import VehicleType
from models.parking_spot import ParkingSpot
from models.two_wheeler_spot import TwoWheelerSpot
from models.four_wheeler_spot import FourWheelerSpot
from models.parking_spot import ParkingSpotType
from models.two_wheeler import TwoWheeler
from models.four_wheeler import FourWheeler
from models.parking_ticket import ParkingTicket
from services.parking_service import ParkingService
from parking_manager import ParkingManager

class Driver(object):
    def __init__(self):
        self.manager = ParkingManager()

    def read_from_json(self, file_name):
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        return data

    def main(self):
        self.manager.add_parking_lot("abc", 2, 10, 20, 30)
        self.manager.add_parking_lot("bcd", 10, 10, 20, 30)
        self.manager.add_vehicle("123", VehicleType.CAR)
        self.manager.add_vehicle("456", VehicleType.BIKE)
        self.manager.add_vehicle("098", VehicleType.BIKE)
        self.manager.add_vehicle("099", VehicleType.BIKE)
        ticket1 = self.manager.park_vehicle("123")
        ticket2 = self.manager.park_vehicle("456")
        ticket3 = self.manager.park_vehicle("098")
        ticket4 = self.manager.park_vehicle("099")
        #ticket3 = self.manager.park_vehicle("456", "bcd")
        self.manager.exit_vehicle(ticket1)
        self.manager.exit_vehicle(ticket2)
        self.manager.exit_vehicle(ticket3)
        self.manager.exit_vehicle(ticket4)
        #self.manager.exit_vehicle(ticket3)
        self.manager.show_history("123")
        self.manager.show_history("456")
        self.manager.show_history("098")
        self.manager.show_history("099")


driver = Driver()
driver.main()