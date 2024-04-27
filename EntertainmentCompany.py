from SupplierManagement.Supplier import Supplier

class EntertainmentCompany(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, entertainment_type, services_offered):
        """
        Constructor method to initialize attributes of the EntertainmentCompany class.
        
        Parameters:
            supplier_id (str): Unique identifier for the entertainment company.
            name (str): Name of the entertainment company.
            address (str): Address of the entertainment company.
            contact_details (str): Contact details of the entertainment company.
            entertainment_type (str): Type of entertainment offered by the company.
            services_offered (str): Description of services offered by the company.
        """
        super().__init__(supplier_id, name, address, contact_details)
        self.entertainment_type = entertainment_type
        self.services_offered = services_offered
        
    def display_details(self):
        """
        Method to display the details of the entertainment company.
        """
        super().display_details()
        print("Entertainment Type:", self.entertainment_type)
        print("Services Offered:", self.services_offered)
