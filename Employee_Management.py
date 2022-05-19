
class Employee:

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone_number = phone_number
        self.zip = zip
        self.employee_contractor = employee_contractor

    def print_general_info(self):
        print("General Info : ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Sex : ", self.sex)
    
    def print_personal_info(self):
        print("Personal Info: ")
        print("Phone Number : ", self.phone_number)
        print("Zip : ", self.zip)
        if (self.employee_contractor.lower() == "employee"):
            print("Job Title : employee")
        elif (self.employee_contractor.lower() == "contractor"):
            print("Job Title : contractor")


class Work(Employee): 

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        super().__init__(name, age, sex, phone_number, zip, employee_contractor)
        self.days_worked = 0
        self.sick_leaves = 0
        self.hours = {}
    
    def add_days_worked(self, name):
        self.days_worked += 1
        print(str(self.name) + "has worked " + str(self.days_worked) + " days")

    def add_sick_leaves(self, name):
        self.sick_leaves += 1
        print(str(self.name) + "has " + str(self.sick_leaves) + " sick days")

    def time_worked(self, name):
        pass


class Salary(Work):

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        super().__init__(name, age, sex, phone_number, zip, employee_contractor)
        self.salary = 0

    def print_salary(self):
            print("Salary : ", self.salary)
    
    def starting_salary(self, amount):
        self.salary = amount

    def rate_per_hour(self):
        pass

    def salary_raise(self, name, percent_raise):
        self.percent_raise = percent_raise
        print(str(self.name) + "'s salary has been raise by " + str(self.percent_raise) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary + (self.salary * self.percent_raise)))
        self.salary = self.salary + (self.salary * self.percent_raise)
        
    def salary_cut(self, name, percent_cut):
        self.percent_cut = percent_cut
        print(str(self.name) + "'s salary has been cut by " + str(self.percent_cut) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary - (self.salary * self.percent_cut)))
        self.salary = self.salary - (self.salary * self.percent_cut)
    

names = {}
name = ""
age = 0
sex = 'm'
phone_number = 0
zip = 0
employee_contractor = "employee"

def add_employee():
    while True:
        print("Please provide the following information about the employee : ")

        while True:
            name = input("Employee name : ")
            if (str(name).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (type(name) != str):
                print("Please inut a valid name")
            elif name in names:
                print("This name is already registered")
            else:
                names[name] = True
                break

        while True:
            age = input("Employee age : ")
            if (str(age).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (age.isdigit()):
                break
            else:
                print("Please input a valid age")

        while True:
            sex = input("Employee sex (m/f/i) : ")
            if (str(sex).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (type(sex) != str or (str(sex).lower() != 'm' and \
                str(sex).lower() != 'f' and str(sex).lower() != 'i')):
                print("Please input a valid sex")
            else:
                break

        while True:
            phone_number = input("Employee phone number : ")
            if (str(phone_number).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (phone_number.isdigit()):
                break
            else:
                print("Please input a valid phone number")
        
        while True:
            zip = input("Employee zip code : ")
            if (str(zip).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (zip.isdigit()):
                break
            else:
                print("Please input a valid zip code")
            
        while True:
            employee_contractor = input("Employee job status (employee/contractor) : ")
            if (str(employee_contractor).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (str(employee_contractor).lower == "employee" or \
                str(employee_contractor == "contractor")):
                break
            else:
                print("Please input a valid job status")

        names[name] = [name, age, sex, phone_number, zip, employee_contractor]
        again = input("Add another employee? (y/n) ")
        if (str(again).lower() == 'n'):
            break


def remove_employee():
    pass

add_employee()
emp_name = input("\nWhich employee would you like to know about? \n" + str(names) + "\n: ")
which_info = input("What would you like to know about " + str(emp_name) + "?" + \
    "\nGeneral Info \nPrivate Info \nTime Worked \nStarting Salary \nPay rate" + \
        "\n: "
    )





