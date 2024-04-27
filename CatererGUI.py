import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from SupplierManagement.Supplier import Supplier
from SupplierManagement.Caterer import Caterer

class CatererGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Caterer Supplier Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for caterer supplier details
        self.setup_caterer_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_caterer_widgets(self):
        # Set up labels and entry fields for caterer supplier details
        caterer_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Menu:", "Minimum Guests:", "Maximum Guests:"]
        self.caterer_entries = {}
        for i, label_text in enumerate(caterer_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.caterer_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        caterer_button_texts = ["Add Caterer Supplier", "Display Caterers", "Delete Caterer", "Modify Caterer"]
        caterer_button_commands = [self.add_caterer, self.display_caterers, self.delete_caterer, self.modify_caterer]
        for i, text in enumerate(caterer_button_texts):
            button = tk.Button(self.master, text=text, command=caterer_button_commands[i])
            button.grid(row=7 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_caterer(self):
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        # Check if a caterer supplier with the same ID already exists
        try:
            existing_caterers = FileHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A caterer supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing caterers, so no need to check
        
        # Get other caterer supplier details from entry fields
        name = self.caterer_entries["Name:"].get()
        address = self.caterer_entries["Address:"].get()
        contact_details = self.caterer_entries["Contact Details:"].get()
        menu = self.caterer_entries["Menu:"].get()
        min_guests = self.caterer_entries["Minimum Guests:"].get()
        max_guests = self.caterer_entries["Maximum Guests:"].get()

        # Create a Caterer object
        caterer = Caterer(supplier_id, name, address, contact_details, menu, min_guests, max_guests)

        # Load existing caterer supplier data or create an empty list if not found
        try:
            existing_caterers = FileHandler.load_data("caterers_data.pkl")
        except FileNotFoundError:
            existing_caterers = []

        # Add the new caterer supplier to the existing list
        existing_caterers.append(caterer)

        # Save the updated caterer supplier data
        FileHandler.save_data(existing_caterers, "caterers_data.pkl")

        messagebox.showinfo("Success", "Caterer supplier added successfully.")

    def display_caterers(self):
        # Display functionality for caterer suppliers
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = FileHandler.load_data("caterers_data.pkl")
            display_text = ""
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {caterer.supplier_id}\n"
                    display_text += f"Name: {caterer.name}\n"
                    display_text += f"Address: {caterer.address}\n"
                    display_text += f"Contact Details: {caterer.contact_details}\n"
                    display_text += f"Menu: {caterer.menu}\n"
                    display_text += f"Minimum Guests: {caterer.min_guests}\n"
                    display_text += f"Maximum Guests: {caterer.max_guests}\n"
                    break  # Exit loop once the caterer supplier is found
            else:
                messagebox.showinfo("Error", "Caterer supplier not found.")
                return
            messagebox.showinfo("Caterer Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Caterers", "No caterer suppliers found.")

    def delete_caterer(self):
        # Delete functionality for caterer suppliers
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = FileHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    existing_caterers.remove(caterer)
                    FileHandler.save_data(existing_caterers, "caterers_data.pkl")
                    messagebox.showinfo("Success", "Caterer supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Caterer supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No caterer suppliers found.")

    def modify_caterer(self):
        # Modify functionality for caterer suppliers
        supplier_id = self.caterer_entries["Supplier ID:"].get()
        try:
            existing_caterers = FileHandler.load_data("caterers_data.pkl")
            for caterer in existing_caterers:
                if caterer.supplier_id == supplier_id:
                    # Update caterer supplier details
                    caterer.name = self.caterer_entries["Name:"].get()
                    caterer.address = self.caterer_entries["Address:"].get()
                    caterer.contact_details = self.caterer_entries["Contact Details:"].get()
                    caterer.menu = self.caterer_entries["Menu:"].get()
                    caterer.min_guests = self.caterer_entries["Minimum Guests:"].get()
                    caterer.max_guests = self.caterer_entries["Maximum Guests:"].get()
                    FileHandler.save_data(existing_caterers, "caterers_data.pkl")
                    messagebox.showinfo("Success", "Caterer supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Caterer supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No caterer suppliers found.")

def main():
    root = tk.Tk()
    app = CatererGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
