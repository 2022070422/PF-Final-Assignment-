from EmployeeManagement.Employee import Employee
from ClientandGuestManagement.Client import Client
from EventManagement.Event import Event
from ClientandGuestManagement.Guest import Guest
from EmployeeManagement.SalesManager import SalesManager
from DataStorage.FileHandler import FileHandler
from VenueManagement.Venue import Venue
from SupplierManagement.FurnitureSupplier import FurnitureSupplier
from  SupplierManagement.Caterer import Caterer
from SupplierManagement.Cleaner import Cleaner  # Import the Cleaner class from the Cleaner.py file

from SupplierManagement.Decorator import Decorator
from SupplierManagement.EntertainmentCompany import EntertainmentCompany

# Your test cases and main program logic follow here
# Test cases for Employee class
def test_employee():
    employee1 = Employee("John Doe", "EMP001", "Sales", "Salesperson", 50000, 30, "1992-05-15", "ABC123")
    employee2 = SalesManager("Alice Smith", "EMP002", "Marketing", "Marketing Manager", 60000, 35, "1987-10-20", "XYZ456", 10)
    
    print("Employee 1 Details:")
    employee1.display_details()
    print("\nEmployee 2 Details:")
    employee2.display_details()

# Test cases for Client class
def test_client():
    client1 = Client("CLI001", "ABC Company", "123 Main Street", "info@abccompany.com", 10000)
    client2 = Client("CLI002", "XYZ Corporation", "456 Elm Street", "info@xyzcorp.com", 15000)
    
    print("Client 1 Details:")
    client1.display_details()
    print("\nClient 2 Details:")
    client2.display_details()

# Test cases for Guest class
def test_guest():
    guest1 = Guest("GUEST001", "John Smith", "789 Oak Avenue", "john@example.com")
    guest2 = Guest("GUEST002", "Jane Doe", "101 Pine Street", "jane@example.com")
    
    print("Guest 1 Details:")
    guest1.display_details()
    print("\nGuest 2 Details:")
    guest2.display_details()

# Test cases for Supplier classes
def test_supplier():
    caterer = Caterer("SUP001", "Catering Pro", "789 Oak Avenue", "cateringpro@example.com", "Menu", 50, 200)
    cleaner = Cleaner("SUP002", "Cleaner Co", "123 Elm Street", "cleanerco@example.com", "Cleaning Services")
    decorator = Decorator("SUP003", "Decorator Deluxe", "456 Maple Avenue", "decoratordeluxe@example.com", "Theme", "Style")
    entertainment_company = EntertainmentCompany("SUP004", "Entertainment Enterprises", "789 Pine Street", "entertainment@example.com", "Type", "Services")
    furniture_supplier = FurnitureSupplier("SUP005", "Furniture Emporium", "101 Oak Street", "furniture@example.com", "Type", "Rental Options")

    print("Caterer Details:")
    caterer.display_details()
    print("\nCleaner Details:")
    cleaner.display_details()
    print("\nDecorator Details:")
    decorator.display_details()
    print("\nEntertainment Company Details:")
    entertainment_company.display_details()
    print("\nFurniture Supplier Details:")
    furniture_supplier.display_details()

# Test cases for Event class
def test_event():
    event1 = Event("EVT001", "Wedding", "Classic", "2024-06-15", "18:00", 4, "Grand Hotel", "CLI001", ["GUEST001", "GUEST002"], ["SUP001", "SUP002"])
    event2 = Event("EVT002", "Birthday", "Superhero", "2024-07-20", "14:00", 3, "City Park", "CLI002", ["GUEST001"], ["SUP002"])
    
    print("Event 1 Details:")
    event1.display_details()
    print("\nEvent 2 Details:")
    event2.display_details()

# Test cases for Venue class
def test_venue():
    venue1 = Venue("VEN001", "Grand Hotel", "123 Broadway", "info@grandhotel.com", 50, 200)
    venue2 = Venue("VEN002", "City Park", "456 Park Avenue", "info@citypark.com", 100, 500)
    
    print("Venue 1 Details:")
    venue1.display_details()
    print("\nVenue 2 Details:")
    venue2.display_details()

# Main program logic
if __name__ == "__main__":
    # Perform testing
    test_employee()
    test_client()
    test_guest()
    test_supplier()
    test_event()
    test_venue()
    # Sample event data
    events_data = [
    Event("E001", "Conference", "Tech Summit", "2024-05-15", "09:00", "1 day", "Convention Center", "C001", ["John Doe", "Jane Smith"], ["Supplier1", "Supplier2"]),
    Event("E002", "Workshop", "Data Science Workshop", "2024-06-20", "10:00", "4 hours", "Training Center", "C002", ["Alice Johnson", "Bob Brown"], ["Supplier3"]),
    Event("E003", "Seminar", "Leadership Seminar", "2024-07-25", "14:00", "2 hours", "Auditorium", "C003", ["Eva Garcia", "Michael Wang"], ["Supplier4"]),
    Event("E004", "Product Launch", "New Product Launch Event", "2024-08-30", "11:00", "3 hours", "Exhibition Hall", "C004", ["Sophia Lee", "David Wilson"], ["Supplier5", "Supplier6"])
]
    clients_data=[Client("CLI001", "ABC Company", "123 Main Street", "info@abccompany.com", 10000)
   , Client("CLI002", "XYZ Corporation", "456 Elm Street", "info@xyzcorp.com", 15000)]
    guest_data=[Guest("GUEST001", "John Smith", "789 Oak Avenue", "john@example.com")
    , Guest("GUEST002", "Jane Doe", "101 Pine Street", "jane@example.com")]
    cleaner_data=[Cleaner("SUP002", "Cleaner Co", "123 Elm Street", "cleanerco@example.com", "Cleaning Services"),
                  Cleaner("SUP003", "Cleaner Bo", "123 Elm Street", "cleanerbo@example.com", "Cleaning Services2")]
    carterer_data=[Caterer("SUP001", "Catering Pro", "789 Oak Avenue", "cateringpro@example.com", "Menu", 50, 200),Caterer("SUP005", "Catering Pro", "789 Oak Avenue", "cateringpro@example.com", "Menu", 2000, 300)]
    decorators_data=[
        Decorator("SUP005", "Decorator Deluxe", "456 Maple Avenue", "decoratordeluxe@example.com", "Theme", "Style"),Decorator("SUP005", "Decorator Deluxe", "456 Maple Avenue", "decoratordeluxe1@example.com", "Theme", "Style")
    ]
    entertainment_companies_data=[ EntertainmentCompany("SUP0028", "Entertainment Enterprises", "789 Pine Street", "entertainment@example.com", "Type", "Services"), EntertainmentCompany("SUP0020", "Entertainment Enterprises", "789 Pine Street", "entertainment@example.com", "Type", "Services")]

    furniture_suppliers_data=[
        FurnitureSupplier("SUP007", "Furniture Emporium", "101 Oak Street", "furniture@example.com", "Type", "Rental Options"),
        FurnitureSupplier("SUP008", "Furniture Emporium", "101 Oak Street", "furniture@example.com", "Type", "Rental Options")

    ]
# Saving data to the file
    FileHandler.save_data(events_data, "events_data.pkl")
    FileHandler.save_data( clients_data, "clients_data.pkl")
    FileHandler.save_data( guest_data, "guests_data.pkl")
    FileHandler.save_data( cleaner_data, "cleaners_data.pkl")
    FileHandler.save_data( carterer_data, "caterers_data.pkl")
    FileHandler.save_data( decorators_data, "decorators_data.pkl")
    FileHandler.save_data( entertainment_companies_data, "entertainment_companies_data.pkl")
    FileHandler.save_data( furniture_suppliers_data, "furniture_suppliers_data.pkl")


