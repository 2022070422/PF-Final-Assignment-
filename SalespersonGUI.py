import tkinter as tk
from tkinter import messagebox
from DataStorage.FileHandler import FileHandler
from EmployeeManagement.Employee import Employee
from EmployeeManagement.Salesperson import Salesperson

class SalespersonGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Salesperson Management System")
        self.master.geometry("500x600")  # Set window dimensions
        
        # Set up labels and entry fields for salesperson details
        self.setup_salesperson_widgets()
        
        # Set up buttons for various actions
        self.setup_buttons()

    def setup_salesperson_widgets(self):
        # Set up labels and entry fields for salesperson details
        salesperson_labels = ["Name:", "Employee ID:", "Department:", "Job Title:", "Basic Salary:", "Age:", "Date of Birth:", "Passport Details:", "Sales Targets:"]
        self.salesperson_entries = {}
        for i, label_text in enumerate(salesperson_labels):
            label = tk.Label(self.master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)  # Add padding
            entry = tk.Entry(self.master)
            entry.grid(row=i, column=1, padx=10, pady=5)  # Add padding
            self.salesperson_entries[label_text] = entry

    def setup_buttons(self):
        # Set up buttons for various actions
        salesperson_button_texts = ["Add Salesperson", "Display Salespersons", "Delete Salesperson", "Modify Salesperson"]
        salesperson_button_commands = [self.add_salesperson, self.display_salespersons, self.delete_salesperson, self.modify_salesperson]
        for i, text in enumerate(salesperson_button_texts):
            button = tk.Button(self.master, text=text, command=salesperson_button_commands[i])
            button.grid(row=9 + i, column=0, columnspan=2, padx=10, pady=5, sticky="ew")  # Add padding and make buttons fill entire width

    def add_salesperson(self):
        employee_id = self.salesperson_entries["Employee ID:"].get()
        # Check if a salesperson with the same ID already exists
        try:
            existing_salespersons = FileHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    messagebox.showerror("Error", "A salesperson with the same ID already exists.")
                    return
        except FileNotFoundError:
            pass  # No existing salespersons, so no need to check
        
        # Get other salesperson details from entry fields
        name = self.salesperson_entries["Name:"].get()
        department = self.salesperson_entries["Department:"].get()
        job_title = self.salesperson_entries["Job Title:"].get()
        basic_salary = float(self.salesperson_entries["Basic Salary:"].get())
        age = int(self.salesperson_entries["Age:"].get())
        dob = self.salesperson_entries["Date of Birth:"].get()
        passport_details = self.salesperson_entries["Passport Details:"].get()
        sales_targets = float(self.salesperson_entries["Sales Targets:"].get())

        # Create a Salesperson object
        salesperson = Salesperson(name, employee_id, department, job_title, basic_salary, age, dob, passport_details, sales_targets)

        # Load existing salesperson data or create an empty list if not found
        try:
            existing_salespersons = FileHandler.load_data("salespersons_data.pkl")
        except FileNotFoundError:
            existing_salespersons = []

        # Add the new salesperson to the existing list
        existing_salespersons.append(salesperson)

        # Save the updated salesperson data
        FileHandler.save_data(existing_salespersons, "salespersons_data.pkl")

        messagebox.showinfo("Success", "Salesperson added successfully.")

    def display_salespersons(self):
        # Display functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = FileHandler.load_data("salespersons_data.pkl")
            display_text = ""
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    display_text += f"Name: {salesperson.name}\n"
                    display_text += f"Employee ID: {salesperson.employee_id}\n"
                    display_text += f"Department: {salesperson.department}\n"
                    display_text += f"Job Title: {salesperson.job_title}\n"
                    display_text += f"Basic Salary: {salesperson.basic_salary}\n"
                    display_text += f"Age: {salesperson.age}\n"
                    display_text += f"Date of Birth: {salesperson.dob}\n"
                    display_text += f"Passport Details: {salesperson.passport_details}\n"
                    display_text += f"Sales Targets: {salesperson.sales_targets}\n"
                    break  # Exit loop once the salesperson is found
            else:
                messagebox.showinfo("Error", "Salesperson not found.")
                return
            messagebox.showinfo("Salesperson Details", display_text)
        except FileNotFoundError:
            messagebox.showinfo("No Salespersons", "No salespersons found.")

    def delete_salesperson(self):
        # Delete functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = FileHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    existing_salespersons.remove(salesperson)
                    FileHandler.save_data(existing_salespersons, "salespersons_data.pkl")
                    messagebox.showinfo("Success", "Salesperson deleted successfully.")
                    return
            messagebox.showinfo("Error", "Salesperson not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No salespersons found.")

    def modify_salesperson(self):
        # Modify functionality for salespersons
        employee_id = self.salesperson_entries["Employee ID:"].get()
        try:
            existing_salespersons = FileHandler.load_data("salespersons_data.pkl")
            for salesperson in existing_salespersons:
                if salesperson.employee_id == employee_id:
                    # Update salesperson details
                    salesperson.name = self.salesperson_entries["Name:"].get()
                    salesperson.department = self.salesperson_entries["Department:"].get()
                    salesperson.job_title = self.salesperson_entries["Job Title:"].get()
                    salesperson.basic_salary = float(self.salesperson_entries["Basic Salary:"].get())
                    salesperson.age = int(self.salesperson_entries["Age:"].get())
                    salesperson.dob = self.salesperson_entries["Date of Birth:"].get()
                    salesperson.passport_details = self.salesperson_entries["Passport Details:"].get()
                    salesperson.sales_targets = float(self.salesperson_entries["Sales Targets:"].get())
                    FileHandler.save_data(existing_salespersons, "salespersons_data.pkl")
                    messagebox.showinfo("Success", "Salesperson details modified successfully.")
                    return
            messagebox.showinfo("Error", "Salesperson not found.")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No salespersons found.")

def main():
    root = tk.Tk()
    app = SalespersonGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
