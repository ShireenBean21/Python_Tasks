from person import Person


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Customer(Person):
    def __init__(self, name, customer_id):
        super().__init__(name)
        self.customer_id = customer_id
        self.employee_served_by = None

    # serve_by_employee method takes an instance of the Employee class and sets it as the employee_served_by attribute of
    # the customer

    def rate_employee(self):
        while True:
            try:
                rating = int(input("Enter employee rating (1-5): "))
                if rating not in range(1, 6):
                    raise ValueError
                break
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 5.")
        return rating


# rate_employee method takes the customers employee rating and raises a value if input is incorrect

if __name__ == "__main__": #
    # Employee and customer data
    employees = [
        Employee("Taylor Swift", "EMP123"),
        Employee("Janet Jackson", "EMP456"),
        Employee("John Wick", "EMP789")
    ]

    customers = [
        Customer("Eddie Murphy", "1111"),
        Customer("Samuel Jackson", "2222"),
        Customer("Charlie Brown", "3333")
    ]

    # store customers to employees they were served by in a dictionary
    customer_service = {
        "1111": employees[0],
        "2222": employees[1],
        "3333": employees[2]
    }

    # Take customer id and checks if its in the dictionary then looks up which employee served them
    while True:
        customer_id = input("Enter customer ID: ")
        if customer_id in customer_service:
            customer = [c for c in customers if c.customer_id == customer_id][0]
            employee_served_by = customer_service[customer_id]
            break
        else:
            print("Invalid customer ID. Please try again.")  # message pops up if customer id not in the dictionary

    # Print customer and employee information
    print(f"Hi {customer.name} you were served by {employee_served_by.name}")

    employee_rating = customer.rate_employee()
    print(f"Thank you {customer.name} for scoring {employee_served_by.name} a {employee_rating}")
