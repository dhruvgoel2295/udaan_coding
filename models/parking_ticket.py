

class ParkingTicket(object):
    def __init__(self, ticket_number, vehicle_id, parking_lot_id, issued_at, paid_at=None, paid_amount=None):
        self.ticket_number = ticket_number
        self.vehicle_id = vehicle_id
        self.parking_lot_id = parking_lot_id
        self.issued_at = issued_at
        self.paid_at = None
        self.paid_amount = None

    
