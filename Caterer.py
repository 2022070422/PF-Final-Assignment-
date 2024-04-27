from SupplierManagement.Supplier import Supplier
class Caterer(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        super().__init__(supplier_id, name, address, contact_details)
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display_details(self):
        super().display_details()
        print("Menu:", self.menu)
        print("Minimum Guests:", self.min_guests)
        print("Maximum Guests:", self.max_guests)

