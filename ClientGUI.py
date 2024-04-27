import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from EventManagement.Event import Event
from ClientandGuestManagement.Client import Client

class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Client Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for client details
        self.setup_client_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_client_widgets(self):
        # Set up labels and entry fields for client details
        client_labels = ["Client ID:", "Name:", "Address:", "Contact Details:", "Budget:"]
        self.client_entries = {}
        for i, label_text in enumerate(client_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.client_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        client_button_texts = ["Add Client", "Display Clients", "Delete Client", "Modify Client"]
        client_button_commands = [self.add_client, self.display_clients, self.delete_client, self.modify_client]
        for i, text in enumerate(client_button_texts):
            button = tk.Button(self.master, text=text, command=client_button_commands[i])
            button.grid(row=10 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_client(self):
        client_id = self.client_entries["Client ID:"].get()
        # Check if a client with the same ID already exists
        try:
            existing_clients = FileHandler.load_data("clients_data.pkl")
            for client in existing_clients:
                if client.client_id == client_id:
                    messagebox.showerror("Error", "A client with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing clients, so no need to check
        
        # Get other client details from entry fields
        name = self.client_entries["Name:"].get()
        address = self.client_entries["Address:"].get()
        contact_details = self.client_entries["Contact Details:"].get()
        budget = float(self.client_entries["Budget:"].get())

        # Create a Client object
        client = Client(client_id, name, address, contact_details, budget)

        # Load existing client data or create an empty list if not found
        try:
            existing_clients = FileHandler.load_data("clients_data.pkl")
        except FileNotFoundError:
            existing_clients = []

        # Add the new client to the existing list
        existing_clients.append(client)

        # Save the updated client data
        FileHandler.save_data(existing_clients, "clients_data.pkl")

        messagebox.showinfo("Success", "Client added successfully.")

    def display_clients(self):
        # Display functionality for clients
        client_id = self.client_entries["Client ID:"].get()
        try:
            existing_clients = FileHandler.load_data("clients_data.pkl")
            display_text = ""
            for client in existing_clients:
                if client.client_id == client_id:
                    display_text += f"Client ID: {client.client_id}\n"
                    display_text += f"Name: {client.name}\n"
                    display_text += f"Address: {client.address}\n"
                    display_text += f"Contact Details: {client.contact_details}\n"
                    display_text += f"Budget: {client.budget}\n"
                    break  # Exit loop once the client is found
            else:
                messagebox.showinfo("Error", "Client not found.")
                return
            messagebox.showinfo("Client Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Clients", "No clients found.")

    def delete_client(self):
        # Delete functionality for clients
        client_id = self.client_entries["Client ID:"].get()
        try:
            existing_clients = FileHandler.load_data("clients_data.pkl")
            for client in existing_clients:
                if client.client_id == client_id:
                    existing_clients.remove(client)
                    FileHandler.save_data(existing_clients, "clients_data.pkl")
                    messagebox.showinfo("Success", "Client deleted successfully.")
                    return
            messagebox.showinfo("Error", "Client not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No clients found.")

    def modify_client(self):
        # Modify functionality for clients
        client_id = self.client_entries["Client ID:"].get()
        try:
            existing_clients = FileHandler.load_data("clients_data.pkl")
            for client in existing_clients:
                if client.client_id == client_id:
                    # Update client details
                    client.name = self.client_entries["Name:"].get()
                    client.address = self.client_entries["Address:"].get()
                    client.contact_details = self.client_entries["Contact Details:"].get()
                    client.budget = float(self.client_entries["Budget:"].get())
                    FileHandler.save_data(existing_clients, "clients_data.pkl")
                    messagebox.showinfo("Success", "Client details modified successfully.")
                    return
            messagebox.showinfo("Error", "Client not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No clients found.")

def main():
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
