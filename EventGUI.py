import tkinter as tk
from tkinter import messagebox
from EventManagement.Event import Event
from DataStorage.FileHandler import FileHandler

class EventGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for event details
        self.setup_event_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_event_widgets(self):
        
        # Set up labels and entry fields for event details
        event_labels = ["Event ID:", "Type:", "Theme:", "Date:", "Time:", "Duration:", "Venue:", "Client ID:", "Guest List:", "Suppliers:"]
        self.event_entries = {}
        for i, label_text in enumerate(event_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.event_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        event_button_texts = ["Add Event", "Display Events", "Delete Event", "Modify Event"]
        event_button_commands = [self.add_event, self.display_events, self.delete_event, self.modify_event]
        for i, text in enumerate(event_button_texts):
            button = tk.Button(self.master, text=text, command=event_button_commands[i])
            button.grid(row=10 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_event(self):
        event_id = self.event_entries["Event ID:"].get()
        # Check if an event with the same ID already exists
        try:
            existing_events = FileHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                    messagebox.showerror("Error", "An event with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing events, so no need to check
        
        # Get other event details from entry fields
        type = self.event_entries["Type:"].get()
        theme = self.event_entries["Theme:"].get()
        date = self.event_entries["Date:"].get()
        time = self.event_entries["Time:"].get()
        duration = self.event_entries["Duration:"].get()
        venue = self.event_entries["Venue:"].get()
        client_id = self.event_entries["Client ID:"].get()
        guest_list = self.event_entries["Guest List:"].get()
        suppliers = self.event_entries["Suppliers:"].get()

        # Create an Event object
        event = Event(event_id, type, theme, date, time, duration, venue, client_id, guest_list, suppliers)

        # Load existing event data or create an empty list if not found
        try:
            existing_events = FileHandler.load_data("events_data.pkl")
        except FileNotFoundError:
            existing_events = []

        # Add the new event to the existing list
        existing_events.append(event)

        # Save the updated event data
        FileHandler.save_data(existing_events, "events_data.pkl")

        messagebox.showinfo("Success", "Event added successfully.")

    def display_events(self):
    # Display functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = FileHandler.load_data("events_data.pkl")
            display_text = ""
            for event in existing_events:
                if event.event_id == event_id:
                    display_text += f"Event ID: {event.event_id}\n"
                    display_text += f"Type: {event.type}\n"
                    display_text += f"Theme: {event.theme}\n"
                    display_text += f"Date: {event.date}\n"
                    display_text += f"Time: {event.time}\n"
                    display_text += f"Duration: {event.duration}\n"
                    display_text += f"Venue: {event.venue}\n"
                    display_text += f"Client ID: {event.client_id}\n"
                    display_text += f"Guest List: {', '.join(event.guest_list)}\n"
                    display_text += f"Suppliers: {', '.join(event.suppliers)}\n"
                    break  # Exit loop once the event is found
            else:
                messagebox.showinfo("Error", "Event not found.")
                return
            messagebox.showinfo("Event Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Events", "No events found.")



    def delete_event(self):
    # Delete functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = FileHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                    existing_events.remove(event)
                    FileHandler.save_data(existing_events, "events_data.pkl")
                    messagebox.showinfo("Success", "Event deleted successfully.")
                    return
            messagebox.showinfo("Error", "Event not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No events found.")


    def modify_event(self):
    # Modify functionality for events
        event_id = self.event_entries["Event ID:"].get()
        try:
            existing_events = FileHandler.load_data("events_data.pkl")
            for event in existing_events:
                if event.event_id == event_id:
                # Update event details
                    event.type = self.event_entries["Type:"].get()
                    event.theme = self.event_entries["Theme:"].get()
                    event.date = self.event_entries["Date:"].get()
                    event.time = self.event_entries["Time:"].get()
                    event.duration = self.event_entries["Duration:"].get()
                    event.venue = self.event_entries["Venue:"].get()
                    event.client_id = self.event_entries["Client ID:"].get()
                    event.guest_list = self.event_entries["Guest List:"].get().split(",")  # Convert to list
                    event.suppliers = self.event_entries["Suppliers:"].get().split(",")  # Convert to list
                    FileHandler.save_data(existing_events, "events_data.pkl")
                    messagebox.showinfo("Success", "Event details modified successfully.")
                    return
            messagebox.showinfo("Error", "Event not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No events found.")



def main():
    root = tk.Tk()
    app = EventGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
