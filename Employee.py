# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, id_number, dept, job):
        self.name = name
        self.id_number = id_number
        self.dept = dept
        self.job = job


employee_1 = Employee("Susan Meyers", " 47899", "Accounting", "Vice president")
employee_2 = Employee("Mark Jones", "39119", "IT", "Programmer")
employee_3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

def main():
    print("Name", "ID_number", "Department", " Job Title")

    print(employee_1.name, employee_1.id_number, employee_1.dept, employee_1.job)
    #print(employee_1.id_number)
    #print(employee_1.dept)
    #print(employee_1.job)

    print(employee_2.name, employee_2.id_number, employee_2.dept, employee_2.job )
    #print(employee_2.id_number)
    #print(employee_2.dept)
    #print(employee_2.job)

    print(employee_3.name, employee_3.id_number, employee_3.dept, employee_3.job )
    #print(employee_3.id_number)
    #print(employee_3.dept)
    #print(employee_3.job)

main()