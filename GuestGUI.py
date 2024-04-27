import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from ClientandGuestManagement.Guest import Guest

class GuestGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guest Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for guest details
        self.setup_guest_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_guest_widgets(self):
        # Set up labels and entry fields for guest details
        guest_labels = ["Guest ID:", "Name:", "Address:", "Contact Details:"]
        self.guest_entries = {}
        for i, label_text in enumerate(guest_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.guest_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        guest_button_texts = ["Add Guest", "Display Guests", "Delete Guest", "Modify Guest"]
        guest_button_commands = [self.add_guest, self.display_guests, self.delete_guest, self.modify_guest]
        for i, text in enumerate(guest_button_texts):
            button = tk.Button(self.master, text=text, command=guest_button_commands[i])
            button.grid(row=6 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_guest(self):
        guest_id = self.guest_entries["Guest ID:"].get()
        # Check if a guest with the same ID already exists
        try:
            existing_guests = FileHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    messagebox.showerror("Error", "A guest with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing guests, so no need to check
        
        # Get other guest details from entry fields
        name = self.guest_entries["Name:"].get()
        address = self.guest_entries["Address:"].get()
        contact_details = self.guest_entries["Contact Details:"].get()

        # Create a Guest object
        guest = Guest(guest_id, name, address, contact_details)

        # Load existing guest data or create an empty list if not found
        try:
            existing_guests = FileHandler.load_data("guests_data.pkl")
        except FileNotFoundError:
            existing_guests = []

        # Add the new guest to the existing list
        existing_guests.append(guest)

        # Save the updated guest data
        FileHandler.save_data(existing_guests, "guests_data.pkl")

        messagebox.showinfo("Success", "Guest added successfully.")

    def display_guests(self):
        # Display functionality for guests
        guest_id = self.guest_entries["Guest ID:"].get()
        try:
            existing_guests = FileHandler.load_data("guests_data.pkl")
            display_text = ""
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    display_text += f"Guest ID: {guest.guest_id}\n"
                    display_text += f"Name: {guest.name}\n"
                    display_text += f"Address: {guest.address}\n"
                    display_text += f"Contact Details: {guest.contact_details}\n"
                    break  # Exit loop once the guest is found
            else:
                messagebox.showinfo("Error", "Guest not found.")
                return
            messagebox.showinfo("Guest Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Guests", "No guests found.")

    def delete_guest(self):
        # Delete functionality for guests
        guest_id = self.guest_entries["Guest ID:"].get()
        try:
            existing_guests = FileHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    existing_guests.remove(guest)
                    FileHandler.save_data(existing_guests, "guests_data.pkl")
                    messagebox.showinfo("Success", "Guest deleted successfully.")
                    return
            messagebox.showinfo("Error", "Guest not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No guests found.")

    def modify_guest(self):
        # Modify functionality for guests
        guest_id = self.guest_entries["Guest ID:"].get()
        try:
            existing_guests = FileHandler.load_data("guests_data.pkl")
            for guest in existing_guests:
                if guest.guest_id == guest_id:
                    # Update guest details
                    guest.name = self.guest_entries["Name:"].get()
                    guest.address = self.guest_entries["Address:"].get()
                    guest.contact_details = self.guest_entries["Contact Details:"].get()
                    FileHandler.save_data(existing_guests, "guests_data.pkl")
                    messagebox.showinfo("Success", "Guest details modified successfully.")
                    return
            messagebox.showinfo("Error", "Guest not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No guests found.")

def main():
    root = tk.Tk()
    app = GuestGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
