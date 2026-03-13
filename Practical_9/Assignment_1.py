# Lab Assignment-1
# Shivam Dipte

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    # Manager inherits Employee, can be extended later
    pass


def main():
    managers = []

    for i in range(10):
        print(f"\n Enter details for Manager {i+1}")
        m = Manager()
        m.get_input()
        managers.append(m)

    print("\n Manager Information ")
    for i, m in enumerate(managers, start=1):
        print(f"\nManager {i}:")
        m.print_info()


if __name__ == "__main__":
    main()







#  Or =========================================================================

# Lab Assignment-1
# Shivam Dipte

class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


def main():
    managers = []

    for i in range(10):
        print(f"\nEnter details for Manager {i+1}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        address = input("Enter address: ")

        m = Manager(name, age, salary, address)
        managers.append(m)

    print("\nManager Information")
    for i, m in enumerate(managers, start=1):
        print(f"\nManager {i}:")
        m.print_info()


if __name__ == "__main__":
    main()
