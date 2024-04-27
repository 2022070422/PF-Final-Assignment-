import tkinter as tk
from EmployeeGUI import EmployeeGUI
from EventGUI import EventGUI
from ClientGUI import ClientGUI
from GuestGUI import GuestGUI
from CatererGUI import CatererGUI
from CleanerGUI import CleanerGUI
from DecoratorGUI import DecoratorGUI
from EntertainmentCompanyGUI import EntertainmentCompanyGUI
from FurnitureSupplierGUI import FurnitureSupplierGUI

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        self.master.geometry("400x400")  # Set window dimensions
        
        # Set up buttons for accessing different screens
        self.setup_buttons()

    def setup_buttons(self):
        # Set up buttons for accessing different screens
        button_texts = [
            "Manage Employees", 
            "Manage Events", 
            "Manage Clients", 
            "Manage Guests", 
            "Manage Caterers",
            "Manage Cleaners",
            "Manage Decorators",
            "Manage Entertainment Companies",
            "Manage Furniture Suppliers"
        ]
        button_commands = [
            self.open_employee_gui, 
            self.open_event_gui, 
            self.open_client_gui, 
            self.open_guest_gui, 
            self.open_caterer_gui,
            self.open_cleaner_gui,
            self.open_decorator_gui,
            self.open_entertainment_company_gui,
            self.open_furniture_supplier_gui
        ]
        for i, text in enumerate(button_texts):
            button = tk.Button(self.master, text=text, command=button_commands[i])
            button.pack(pady=5)

    def open_employee_gui(self):
        # Open the EmployeeGUI screen
        employee_window = tk.Toplevel(self.master)
        employee_gui = EmployeeGUI(employee_window)

    def open_event_gui(self):
        # Open the EventGUI screen
        event_window = tk.Toplevel(self.master)
        event_gui = EventGUI(event_window)

    def open_client_gui(self):
        # Open the ClientGUI screen
        client_window = tk.Toplevel(self.master)
        client_gui = ClientGUI(client_window)

    def open_guest_gui(self):
        # Open the GuestGUI screen
        guest_window = tk.Toplevel(self.master)
        guest_gui = GuestGUI(guest_window)

    def open_caterer_gui(self):
        # Open the CatererGUI screen
        caterer_window = tk.Toplevel(self.master)
        caterer_gui = CatererGUI(caterer_window)

    def open_cleaner_gui(self):
        # Open the CleanerGUI screen
        cleaner_window = tk.Toplevel(self.master)
        cleaner_gui = CleanerGUI(cleaner_window)

    def open_decorator_gui(self):
        # Open the DecoratorGUI screen
        decorator_window = tk.Toplevel(self.master)
        decorator_gui = DecoratorGUI(decorator_window)

    def open_entertainment_company_gui(self):
        # Open the EntertainmentCompanyGUI screen
        entertainment_window = tk.Toplevel(self.master)
        entertainment_gui = EntertainmentCompanyGUI(entertainment_window)

    def open_furniture_supplier_gui(self):
        # Open the FurnitureSupplierGUI screen
        furniture_window = tk.Toplevel(self.master)
        furniture_gui = FurnitureSupplierGUI(furniture_window)

def main():
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
