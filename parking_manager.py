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

class ParkingManager(object):
    def __init__(self):
        self.parking_lots = {}
        self.vehicles = {}
        self.tickets = {}
        self.current_ticket_id = 1
        self.service = ParkingService()

    def add_vehicle(self, vehicle_id, vehicle_type):
        if vehicle_type == VehicleType.CAR:
            self.vehicles[vehicle_id] = FourWheeler(vehicle_id)

        elif vehicle_type == VehicleType.BIKE:
            self.vehicles[vehicle_id] = TwoWheeler(vehicle_id)

        else:
            raise Exception("VehicleType not supported.")

    def add_parking_lot(self, parking_lot_id, two_wheeler_capacity, four_wheeler_capacity, two_wheeler_rate, four_wheeler_rate):
        spots = {}
        spot_id = 1
        two_spots = []
        four_spots = []
        rates = {}
        for capacity in range(two_wheeler_capacity):
            two_spots.append(TwoWheelerSpot(spot_id))
            spot_id += 1
        for capacity in range(four_wheeler_capacity):
            four_spots.append(FourWheelerSpot(spot_id))
            spot_id += 1
        rates[ParkingSpotType.BIKE] = two_wheeler_rate
        rates[ParkingSpotType.CAR] = four_wheeler_rate



        self.parking_lots[parking_lot_id] = ParkingLot(parking_lot_id, two_spots, four_spots, rates)

    def check_free_parking(self, vehicle):
        for parking_lot_id, parking_lot in self.parking_lots.items():
            if parking_lot.check_free(vehicle.vehicle_type):
                return parking_lot
        return None

    def park_vehicle(self, vehicle_id):
        parking_lot = self.check_free_parking(self.vehicles[vehicle_id])
        if not parking_lot:
            print("No space")
            return None
        ticket_id = self.current_ticket_id
        self.current_ticket_id += 1
        ticket = self.service.park_vehicle(self.vehicles[vehicle_id], parking_lot, ticket_id)
        self.tickets[ticket.ticket_number] = ticket 
        return ticket.ticket_number

    def exit_vehicle(self, ticket_number):
        ticket = self.tickets[ticket_number]
        amount = self.service.exit_vehicle(ticket, self.parking_lots[ticket.parking_lot_id], self.vehicles[ticket.vehicle_id])
        return amount

    def show_history(self, vehicle_id):
        self.service.show_history(self.vehicles[vehicle_id])

