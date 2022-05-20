
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
        self.hours = 0

    def add_days_worked(self):
        self.days_worked += 1
    
    def print_days_worked(self, name):
        print(str(self.name) + "has worked " + str(self.days_worked) + " days")

    def add_sick_leaves(self):
        self.sick_leaves += 1
    
    def print_sick_leaves(self, name):
        print(str(self.name) + "has " + str(self.sick_leaves) + " sick days")

    def add_time_worked(self, hours):
        self.hour += hours

    def print_time_worked(self, name):
        print(str(name) + " has worked " + str(self.hours) + " hours")


class Pay(Work):

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        super().__init__(name, age, sex, phone_number, zip, employee_contractor)
        self.salary = 0
        self.rate = 0
        self.final_pay = 0

    def print_salary(self):
        print("Salary : ", self.salary)
    
    def set_starting_salary(self, amount):
        self.salary = amount

    def print_rate(self):
        print("Hourly rate : ", self.rate)
 
    def set_rate_per_hour(self, rate):
        self.rate = rate

    def final_pay(self, employee_contractor):
        final_pay = 0
        if (str(self.employee_contractor) == "employee"):
            print("Final Pay : " + str(self.salary))
        elif (str(self.employee_contractor == "contractor")):
            print("Final Pay : " + str(int(self.time_worked) * int(self.rate)))

    def salary_raise(self, name, percent_raise):
        print(str(self.name) + "'s salary has been raise by " + str(percent_raise) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary + (self.salary * percent_raise)))
        self.salary += int(percent_raise) * int(self.salary)
        
    def salary_cut(self, name, percent_cut):
        print(str(self.name) + "'s salary has been cut by " + str(percent_cut) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary - (self.salary * percent_cut)))
        self.salary -= int(percent_cut) * int(self.salary) 
    
    def rate_raise(self, name, amount_raise):
        print(str(self.name) + "'s hourly rate has been raise by " + str(amount_raise) + \
            "% from $" + str(self.rate) + " to $" + str(self.salary + amount_raise))
        self.salary += int(amount_raise) 

    def rate_cut(self, name, amount_cut):
        print(str(self.name) + "'s hourly rate has been cut by " + str(amount_cut) + \
            "% from $" + str(self.rate) + " to $" + str(self.salary + amount_cut))
        self.salary -= int(amount_cut) 


dict = {}
names = []
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
            elif name in dict:
                print("This name is already registered")
            else:
                names.append(name)
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

        dict[name] = [name, age, sex, phone_number, zip, employee_contractor]
        again = input("Add another employee? (y/n) ")
        if (str(again).lower() == 'n'):
            break


def remove_employee():
    while True:
        emp_name = input("Which employee would you like to remove? \n" + \
            str(names) + "\n: ")
        if (str(emp_name).lower() == 'q'):
            quit()
        elif (emp_name not in names):
            print("This is not a valid employee name")
        else:
            validate = input("Are you sure? (y/n) ")
            if (str(validate).lower() == 'y'):
                del dict[emp_name]
                names.remove(str(emp_name))
                print(str(emp_name) + " has been removed")
                break




while True:
    emp_name = input("\nWhich employee would you like to know about? \n" + str(names) + "\n: ")
    if (str(emp_name).lower() == 'q'):
        quit()
    elif (emp_name not in names):
        print("This is not a valid employee name")
    else:
        break

which_info = input("What would you like to know about " + str(emp_name) + "?" + \
    "\nGeneral Info \nPrivate Info \nTime Worked \nStarting Salary \nPay rate" + \
        "\n: "
    )



