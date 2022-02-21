
class miembro_equipo:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Empleado(miembro_equipo):
    def __init__(self, name, address, day_to_pay):
        super().__init__(name, address)
        self.day_to_pay = day_to_pay


class Empleado_hora(Empleado):
    def __init__(self, name, address, day_to_pay, total_working_hours, salary_per_hour):
        super().__init__(name, address, day_to_pay)
        self.total_working_hours = total_working_hours
        self.salary_per_hour = salary_per_hour

    @property
    def amount_to_pay(self):
        return self.total_working_hours * self.salary_per_hour


class Empleado_salariado(Empleado):
    def __init__(self, name, address, day_to_pay, monthly_salary):
        super().__init__(name, address, day_to_pay)
        self.monthly_salary = monthly_salary

    @property
    def amount_to_pay(self):
        return self.monthly_salary


class Comision_Salariar_Empleado(Empleado_salariado):
    def __init__(self, name, address, day_to_pay, monthly_salary, commission_rate, current_month_sales):
        super().__init__(name, address, day_to_pay, monthly_salary)
        self.commission_rate = commission_rate
        self.current_month_sales = current_month_sales

    @property
    def amount_to_pay(self):
        return super().amount_to_pay + self.current_month_sales * self.commission_rate


class Volunteer(miembro_equipo):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    @property
    def amount_to_pay(self):
        return self.current_payment

