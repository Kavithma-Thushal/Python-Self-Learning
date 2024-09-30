import tkinter as tk


def save_customer():
    id_data = id_entry.get()
    name_data = name_entry.get()
    address_data = address_entry.get()
    salary_data = salary_entry.get()

    # Printing data to the console
    print(f"ID: {id_data}")
    print(f"Name: {name_data}")
    print(f"Address: {address_data}")
    print(f"Salary: {salary_data}")


# Create the main window
root = tk.Tk()
root.title("Customer Management")
root.geometry("200x200")

# Create and place labels and entry widgets for each field
tk.Label(root, text="ID:").grid(row=0, column=0, sticky="e")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Address:").grid(row=2, column=0, sticky="e")
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Salary:").grid(row=3, column=0, sticky="e")
salary_entry = tk.Entry(root)
salary_entry.grid(row=3, column=1, padx=10, pady=10)

# Create and place the save button
save_button = tk.Button(root, text="Save", command=save_customer)
save_button.grid(row=4, column=1, pady=10)

# Start the event loop
root.mainloop()
