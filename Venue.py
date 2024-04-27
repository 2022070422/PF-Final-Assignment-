class Venue:
    def __init__(self, venue_id, name, address, contact_details, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display_details(self):
        print("Venue ID:", self.venue_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)
        print("Minimum Guests:", self.min_guests)
        print("Maximum Guests:", self.max_guests)
