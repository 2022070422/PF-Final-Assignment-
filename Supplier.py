class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display_details(self):
        print("Supplier ID:", self.supplier_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)



