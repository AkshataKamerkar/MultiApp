import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTrackerApp:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        self.master.title("Expense Tracker")

        # Variables to store user input
        self.amount_var = tk.DoubleVar()
        self.description_var = tk.StringVar()
        self.category_var = tk.StringVar(value="Select Category")

        # List to store entered expenses
        self.expenses = []

        # Set the visual style using the "xpnative" theme
        style = ttk.Style()
        style.theme_use("xpnative")

        # GUI Elements
        # Labels and Entry widgets for amount, description, and category
        self.amount_label = ttk.Label(master, text="Amount:")
        self.amount_entry = ttk.Entry(master, textvariable=self.amount_var)

        self.description_label = ttk.Label(master, text="Description:")
        self.description_entry = ttk.Entry(master, textvariable=self.description_var)

        self.category_label = ttk.Label(master, text="Category:")
        self.category_menu = ttk.Combobox(master, textvariable=self.category_var,
                                          values=["Food", "Transportation", "Entertainment"])

        # Buttons for adding expenses and viewing summaries
        self.add_button = ttk.Button(master, text="Add Expense", command=self.add_expense)
        self.summary_button = ttk.Button(master, text="View Summary", command=self.view_summary)

        # Layout
        # Grid layout for organizing widgets
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.category_menu.grid(row=2, column=1, padx=10, pady=10)

        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.summary_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Set initial window size
        self.master.geometry("400x250")

    def add_expense(self):
        # Function to handle adding expenses
        amount = self.amount_var.get()
        description = self.description_var.get()
        category = self.category_var.get()

        # Validate user input
        if amount <= 0 or not description or category == "Select Category":
            messagebox.showerror("Error", "Please enter valid data.")
        else:
            # Add the expense to the list
            expense = {"Amount": amount, "Description": description, "Category": category}
            self.expenses.append(expense)
            messagebox.showinfo("Success", "Expense added successfully!")

    def view_summary(self):
        # Function to handle viewing expense summaries
        if not self.expenses:
            messagebox.showinfo("Summary", "No expenses to display.")
        else:
            # Display a summary of monthly expenses
            summary = "Monthly Expenses:\n"
            for expense in self.expenses:
                summary += f"{expense['Description']} - ${expense['Amount']}\n"
            messagebox.showinfo("Summary", summary)

def main():
    # Main function to create and run the application
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
