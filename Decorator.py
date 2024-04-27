from SupplierManagement.Supplier import Supplier

class Decorator(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, decoration_theme, decoration_style):
        """
        Constructor method to initialize attributes of the Decorator class.
        
        Parameters:
            supplier_id (str): Unique identifier for the decorator.
            name (str): Name of the decorator.
            address (str): Address of the decorator.
            contact_details (str): Contact details of the decorator.
            decoration_theme (str): Theme of decoration offered by the decorator.
            decoration_style (str): Style of decoration offered by the decorator.
        """
        super().__init__(supplier_id, name, address, contact_details)
        self.decoration_theme = decoration_theme
        self.decoration_style = decoration_style

    def display_details(self):
        """
        Method to display the details of the decorator.
        """
        super().display_details()
        print("Decoration Theme:", self.decoration_theme)
        print("Decoration Style:", self.decoration_style)
