from models.parking_lot import ParkingLot
from models.vehicle import VehicleType
from models.parking_ticket import ParkingTicket
import datetime

class ParkingService(object):
    def __init__(self):
        pass

    def park_vehicle(self, vehicle, parking_lot, ticket_number):
        if vehicle.vehicle_type == VehicleType.BIKE:
            if len(parking_lot.two_wheeler_spots_free) > 0:
                parking_spot = parking_lot.two_wheeler_spots_free.pop()
                issued_at = datetime.datetime.now()
                ticket = ParkingTicket(ticket_number, vehicle.vehicle_id, parking_lot.parking_lot_id, issued_at)
                vehicle.set_active_ticket(ticket)
                parking_lot.two_wheeler_spots_occupied[ticket.ticket_number] = parking_spot 
                return ticket
            else:
                print("No parking spot free")
        elif vehicle.vehicle_type == VehicleType.CAR:
            if len(parking_lot.four_wheeler_spots_free) > 0:
                parking_spot = parking_lot.four_wheeler_spots_free.pop()
                ticket = ParkingTicket(ticket_number, vehicle.vehicle_id, parking_lot.parking_lot_id, datetime.datetime.now())
                vehicle.set_active_ticket(ticket)
                parking_lot.four_wheeler_spots_occupied[ticket.ticket_number] = parking_spot 
                return ticket
            else:
                print("No parking spot free")
        else:
            pass



    def exit_vehicle(self, ticket, parking_lot, vehicle):
        if vehicle.vehicle_type == VehicleType.BIKE:
            parking_spot = parking_lot.two_wheeler_spots_occupied[ticket.ticket_number]
            del parking_lot.two_wheeler_spots_occupied[ticket.ticket_number]
            parking_lot.two_wheeler_spots_free.append(parking_spot)
            parking_rate = parking_lot.rates[parking_spot.spot_type]
            paid_at = datetime.datetime.now()
            amount = parking_rate * ((paid_at - ticket.issued_at).seconds/60)
            ticket.paid_at  = paid_at
            ticket.paid_amount = amount
            vehicle.tickets[ticket.ticket_number] = ticket
            vehicle.set_active_ticket()
            return amount
        elif vehicle.vehicle_type == VehicleType.CAR:
            parking_spot = parking_lot.four_wheeler_spots_occupied[ticket.ticket_number]
            del parking_lot.four_wheeler_spots_occupied[ticket.ticket_number]
            parking_lot.four_wheeler_spots_free.append(parking_spot)
            parking_rate = parking_lot.rates[parking_spot.spot_type]
            paid_at = datetime.datetime.now()
            amount = parking_rate * ((paid_at - ticket.issued_at).seconds/60)
            ticket.paid_at  = paid_at
            ticket.paid_amount = amount
            vehicle.tickets[ticket.ticket_number] = ticket
            vehicle.set_active_ticket()
            return amount
        else:
            pass

    def show_history(self, vehicle):
        for ticket_nu, ticket in  vehicle.tickets.items():
            print("Vehicle: %s Parking Lot: %s Duration: %s hours Amount Paid: %s" % (vehicle.vehicle_id, ticket.parking_lot_id, ((ticket.paid_at - ticket.issued_at).seconds/60), ticket.paid_amount))


