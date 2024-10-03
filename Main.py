import tkinter as tk


def save_customer():
    customer_data = {
        "ID": id_entry.get(),
        "Name": name_entry.get(),
        "Address": address_entry.get(),
        "Salary": salary_entry.get()
    }
    for key, value in customer_data.items():
        print(f"{key}: {value}")


def create_labeled_entry(parent, label, row, column=0, padx=10, pady=10, sticky="e"):
    tk.Label(parent, text=f"{label}:").grid(row=row, column=column, sticky=sticky)
    entry = tk.Entry(parent)
    entry.grid(row=row, column=column + 1, padx=padx, pady=pady)
    return entry


root = tk.Tk()
root.title("Customer Management")
root.geometry("200x200")

id_entry = create_labeled_entry(root, "ID", 0)
name_entry = create_labeled_entry(root, "Name", 1)
address_entry = create_labeled_entry(root, "Address", 2)
salary_entry = create_labeled_entry(root, "Salary", 3)

save_button = tk.Button(root, text="Save", command=save_customer)
save_button.grid(row=4, column=1, pady=10)

root.mainloop()
