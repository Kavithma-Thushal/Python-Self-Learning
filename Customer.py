import tkinter as tk
import mysql.connector
from mysql.connector import Error


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='demo'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


def save_customer():
    customer_data = {
        "ID": id_entry.get(),
        "Name": name_entry.get(),
        "Address": address_entry.get(),
        "Salary": salary_entry.get()
    }

    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        query = """INSERT INTO customers (id, name, address, salary) VALUES (%s, %s, %s, %s)"""
        try:
            cursor.execute(query, (
                customer_data["ID"], customer_data["Name"], customer_data["Address"], customer_data["Salary"]))
            connection.commit()
            print("Customer saved successfully!")
        except Error as e:
            print(f"Failed to insert data into MySQL table: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Connection to database failed!")


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
