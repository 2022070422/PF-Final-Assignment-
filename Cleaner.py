from SupplierManagement.Supplier  import Supplier

class Cleaner(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, cleaning_services):
        super().__init__(supplier_id, name, address, contact_details)
        self.cleaning_services = cleaning_services

    def display_details(self):
        super().display_details()
        print("Cleaning Services:", self.cleaning_services)
