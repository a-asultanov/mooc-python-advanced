# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    count = len(employee.subordinates)

    if len(employee.subordinates) == 0:
        return 0
    
    if len(employee.subordinates) > 0:
        for i in range(len(employee.subordinates)):
            count += count_subordinates(employee.subordinates[i])
          
    return count