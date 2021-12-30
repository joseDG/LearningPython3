

class Employee:
    def __init__(self, name):
        self.name = name


    def print(self):
        print(self.name)


def hack():
    print('Hey!')

if __name__ == '__main__':
    emp = Employee('Mostafa')
    emp.print() # Mostafa

    emp.print = hack
    emp.print() # Hey!
