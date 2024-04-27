class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def display_details(self):
        print("Client ID:", self.client_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)
        print("Budget:", self.budget)
