from SupplierManagement.Supplier import Supplier
class FurnitureSupplier(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, furniture_type, rental_options):
        super().__init__(supplier_id, name, address, contact_details)
        self.furniture_type = furniture_type
        self.rental_options = rental_options
                                                      
    def display_details(self):
        super().display_details()
        print("Furniture Type:", self.furniture_type)
        print("Rental Options:", self.rental_options)
