import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from SupplierManagement.Supplier import Supplier
from SupplierManagement.Decorator import Decorator

class DecoratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Decorator Supplier Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for decorator supplier details
        self.setup_decorator_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_decorator_widgets(self):
        # Set up labels and entry fields for decorator supplier details
        decorator_labels = ["Supplier ID:", "Name:", "Address:", "Contact Details:", "Decoration Theme:", "Decoration Style:"]
        self.decorator_entries = {}
        for i, label_text in enumerate(decorator_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.decorator_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        decorator_button_texts = ["Add Decorator Supplier", "Display Decorators", "Delete Decorator", "Modify Decorator"]
        decorator_button_commands = [self.add_decorator, self.display_decorators, self.delete_decorator, self.modify_decorator]
        for i, text in enumerate(decorator_button_texts):
            button = tk.Button(self.master, text=text, command=decorator_button_commands[i])
            button.grid(row=6 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_decorator(self):
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        # Check if a decorator supplier with the same ID already exists
        try:
            existing_decorators = FileHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    messagebox.showerror("Error", "A decorator supplier with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing decorators, so no need to check
        
        # Get other decorator supplier details from entry fields
        name = self.decorator_entries["Name:"].get()
        address = self.decorator_entries["Address:"].get()
        contact_details = self.decorator_entries["Contact Details:"].get()
        decoration_theme = self.decorator_entries["Decoration Theme:"].get()
        decoration_style = self.decorator_entries["Decoration Style:"].get()

        # Create a Decorator object
        decorator = Decorator(supplier_id, name, address, contact_details, decoration_theme, decoration_style)

        # Load existing decorator supplier data or create an empty list if not found
        try:
            existing_decorators = FileHandler.load_data("decorators_data.pkl")
        except FileNotFoundError:
            existing_decorators = []

        # Add the new decorator supplier to the existing list
        existing_decorators.append(decorator)

        # Save the updated decorator supplier data
        FileHandler.save_data(existing_decorators, "decorators_data.pkl")

        messagebox.showinfo("Success", "Decorator supplier added successfully.")

    def display_decorators(self):
        # Display functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = FileHandler.load_data("decorators_data.pkl")
            display_text = ""
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    display_text += f"Supplier ID: {decorator.supplier_id}\n"
                    display_text += f"Name: {decorator.name}\n"
                    display_text += f"Address: {decorator.address}\n"
                    display_text += f"Contact Details: {decorator.contact_details}\n"
                    display_text += f"Decoration Theme: {decorator.decoration_theme}\n"
                    display_text += f"Decoration Style: {decorator.decoration_style}\n"
                    break  # Exit loop once the decorator supplier is found
            else:
                messagebox.showinfo("Error", "Decorator supplier not found.")
                return
            messagebox.showinfo("Decorator Supplier Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Decorators", "No decorator suppliers found.")

    def delete_decorator(self):
        # Delete functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = FileHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    existing_decorators.remove(decorator)
                    FileHandler.save_data(existing_decorators, "decorators_data.pkl")
                    messagebox.showinfo("Success", "Decorator supplier deleted successfully.")
                    return
            messagebox.showinfo("Error", "Decorator supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No decorator suppliers found.")

    def modify_decorator(self):
        # Modify functionality for decorator suppliers
        supplier_id = self.decorator_entries["Supplier ID:"].get()
        try:
            existing_decorators = FileHandler.load_data("decorators_data.pkl")
            for decorator in existing_decorators:
                if decorator.supplier_id == supplier_id:
                    # Update decorator supplier details
                    decorator.name = self.decorator_entries["Name:"].get()
                    decorator.address = self.decorator_entries["Address:"].get()
                    decorator.contact_details = self.decorator_entries["Contact Details:"].get()
                    decorator.decoration_theme = self.decorator_entries["Decoration Theme:"].get()
                    decorator.decoration_style = self.decorator_entries["Decoration Style:"].get()
                    FileHandler.save_data(existing_decorators, "decorators_data.pkl")
                    messagebox.showinfo("Success", "Decorator supplier details modified successfully.")
                    return
            messagebox.showinfo("Error", "Decorator supplier not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No decorator suppliers found.")

def main():
    root = tk.Tk()
    app = DecoratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
