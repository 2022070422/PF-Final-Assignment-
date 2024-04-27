import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from SupplierManagement.Supplier import Supplier
from SupplierManagement.Cleaner import Cleaner

class CleanerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cleaner Supplier Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for cleaner supplier details
        self.setup_cleaner_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_cleaner_widgets(self):
        # Set up labels and entry fields for cleaner supplier details
        cleaner_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Cleaning Services:"]
        self.cleaner_entries = {}
        for i, label_text in enumerate(cleaner_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.cleaner_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        cleaner_button_texts = ["Add Cleaner Supplier", "Display Cleaners", "Delete Cleaner", "Modify Cleaner"]
        cleaner_button_commands = [self.add_cleaner, self.display_cleaners, self.delete_cleaner, self.modify_cleaner]
        for i, text in enumerate(cleaner_button_texts):
            button = tk.Button(self.master, text=text, command=cleaner_button_commands[i])
            button.grid(row=6 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_cleaner(self):
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        # Check if a cleaner supplier with the same ID already exists
        try:
            existing_cleaners = FileHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A cleaner supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing cleaners, so no need to check
        
        # Get other cleaner supplier details from entry fields
        name = self.cleaner_entries["Name:"].get()
        address = self.cleaner_entries["Address:"].get()
        contact_details = self.cleaner_entries["Contact Details:"].get()
        cleaning_services = self.cleaner_entries["Cleaning Services:"].get()

        # Create a Cleaner object
        cleaner = Cleaner(supplier_id, name, address, contact_details, cleaning_services)

        # Load existing cleaner supplier data or create an empty list if not found
        try:
            existing_cleaners = FileHandler.load_data("cleaners_data.pkl")
        except FileNotFoundError:
            existing_cleaners = []

        # Add the new cleaner supplier to the existing list
        existing_cleaners.append(cleaner)

        # Save the updated cleaner supplier data
        FileHandler.save_data(existing_cleaners, "cleaners_data.pkl")

        messagebox.showinfo("Success", "Cleaner supplier added successfully.")

    def display_cleaners(self):
        # Display functionality for cleaner suppliers
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = FileHandler.load_data("cleaners_data.pkl")
            display_text = ""
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {cleaner.supplier_id}\n"
                    display_text += f"Name: {cleaner.name}\n"
                    display_text += f"Address: {cleaner.address}\n"
                    display_text += f"Contact Details: {cleaner.contact_details}\n"
                    display_text += f"Cleaning Services: {cleaner.cleaning_services}\n"
                    break  # Exit loop once the cleaner supplier is found
            else:
                messagebox.showinfo("Error", "Cleaner supplier not found.")
                return
            messagebox.showinfo("Cleaner Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Cleaners", "No cleaner suppliers found.")

    def delete_cleaner(self):
        # Delete functionality for cleaner suppliers
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = FileHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    existing_cleaners.remove(cleaner)
                    FileHandler.save_data(existing_cleaners, "cleaners_data.pkl")
                    messagebox.showinfo("Success", "Cleaner supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Cleaner supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No cleaner suppliers found.")

    def modify_cleaner(self):
        # Modify functionality for cleaner suppliers
        supplier_id = self.cleaner_entries["Supplier ID:"].get()
        try:
            existing_cleaners = FileHandler.load_data("cleaners_data.pkl")
            for cleaner in existing_cleaners:
                if cleaner.supplier_id == supplier_id:
                    # Update cleaner supplier details
                    cleaner.name = self.cleaner_entries["Name:"].get()
                    cleaner.address = self.cleaner_entries["Address:"].get()
                    cleaner.contact_details = self.cleaner_entries["Contact Details:"].get()
                    cleaner.cleaning_services = self.cleaner_entries["Cleaning Services:"].get()
                    FileHandler.save_data(existing_cleaners, "cleaners_data.pkl")
                    messagebox.showinfo("Success", "Cleaner supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Cleaner supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No cleaner suppliers found.")

def main():
    root = tk.Tk()
    app = CleanerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
