class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        """
        Constructor method to initialize attributes of the Guest class.
        
        Parameters:
            guest_id (str): Unique identifier for the guest.
            name (str): The name of the guest.
            address (str): The address of the guest.
            contact_details (str): Contact details of the guest.
        """
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display_details(self):
        """
        Method to display the details of the guest.
        """
        print("Guest ID:", self.guest_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)
