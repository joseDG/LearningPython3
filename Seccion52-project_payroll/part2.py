
class StaffMember:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Employee(StaffMember):
    def __init__(self, name, address, day_to_pay):
        super().__init__(name, address)
        self.day_to_pay = day_to_pay


class HourlyEmployee(Employee):
    def __init__(self, name, address, day_to_pay, total_working_hours, salary_per_hour):
        super().__init__(name, address, day_to_pay)
        self.total_working_hours = total_working_hours
        self.salary_per_hour = salary_per_hour

    @property
    def amount_to_pay(self):
        return self.total_working_hours * self.salary_per_hour


class SalariedEmployee(Employee):
    def __init__(self, name, address, day_to_pay, monthly_salary):
        super().__init__(name, address, day_to_pay)
        self.monthly_salary = monthly_salary

    @property
    def amount_to_pay(self):
        return self.monthly_salary


class CommissionSalariedEmployee(SalariedEmployee):
    def __init__(self, name, address, day_to_pay, monthly_salary, commission_rate, current_month_sales):
        super().__init__(name, address, day_to_pay, monthly_salary)
        self.commission_rate = commission_rate
        self.current_month_sales = current_month_sales

    @property
    def amount_to_pay(self):
        return super().amount_to_pay + self.current_month_sales * self.commission_rate


class Volunteer(StaffMember):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    @property
    def amount_to_pay(self):
        return self.current_payment











class Item:
    def __init__(self, desc, price_per_one, quantity):
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity

    @property
    def price(self):
        return self.price_per_one * self.quantity
    

class Book(Item):
    def __init__(self, desc, price_per_one, quantity, author):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity
        self.author = author
        
class Food(Item):
    def __init__(self, desc, price_per_one, quantity, expiration_date):
        super().__init__(desc, price_per_one, quantity)
        self.desc = desc
        self.price_per_one = price_per_one 
        self.quantity = quantity
        self.author = expiration_date


class Invoice:
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def amount_to_pay(self):
        return sum([item.price for item in self.items])


class Payroll:
    def __init__(self):
        self.payables = []

    def add_payable(self, payable):
        self.payables.append(payable)

    @property
    def amount_to_pay(self):
        return sum([payable.amount_to_pay for payable in self.payables])


class Company:
    def __init__(self):
        self.payroll = Payroll()

    def run(self):
        self.payroll.add_payable(Volunteer('Most', 'AddressV', 700))
        self.payroll.add_payable(HourlyEmployee('Belal', 'AddressH', 1, 10, 3))
        self.payroll.add_payable(SalariedEmployee('Ziad', 'AddressS', 2, 3000))
        self.payroll.add_payable(CommissionSalariedEmployee('Safa', 'AddressC', 6, 2500, 0.001, 5000))

        invoice = Invoice(1234)
        invoice.add_item(Book('book1', 10, 7, ''))
        invoice.add_item(Food('food1', 5, 6, ''))
        self.payroll.add_payable(invoice)

        print(self.payroll.amount_to_pay)   # 6335


if __name__ == '__main__':
    Company().run()
