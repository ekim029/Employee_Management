
class Employee:

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone_number = phone_number
        self.zip = zip
        self.employee_contractor = employee_contractor

    def get_name(self):
        return self.name
    
    def set_name(self, names):
        self.name = names

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_zip(self, zip):
        self.zip = zip

    def get_employee_contractor(self):
        return self.employee_contractor

    def set_employee_contractor(self, ec):
        self.employee_contractor = ec

    def print_general_info(self):
        print("\nGeneral Info : ")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Sex :", self.sex)
        if (self.employee_contractor.lower() == "employee"):
            print("Job Title : employee")
        elif (self.employee_contractor.lower() == "contractor"):
            print("Job Title : contractor")
    
    def print_personal_info(self):
        print("\nPersonal Info: ")
        print("Phone Number : ", self.phone_number)
        print("Zip : ", self.zip)


class Work(Employee): 

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        super().__init__(name, age, sex, phone_number, zip, employee_contractor)
        self.days_worked = 0
        self.sick_leaves = 0
        self.hours = 0

    def add_days_worked(self, days):
        self.days_worked += int(days)
    
    def print_days_worked(self):
        print(str(self.name) + " has worked " + str(self.days_worked) + " days")

    def add_sick_leaves(self, days):
        self.sick_leaves += int(days)
    
    def print_sick_leaves(self):
        print(str(self.name) + " has " + str(self.sick_leaves) + " sick days")

    def add_time_worked(self, hour):
        self.hours += hour

    def print_time_worked(self):
        print(str(self.name) + " has worked " + str(self.hours) + " hours")


class Pay(Work):

    def __init__(self, name, age, sex, phone_number, zip, employee_contractor):
        super().__init__(name, age, sex, phone_number, zip, employee_contractor)
        self.salary = 0
        self.rate = 0
        self.final_pay = 0

    def print_salary(self):
        print("Salary : $" + str(self.salary))
    
    def set_salary(self, amount):
        self.salary = amount

    def print_rate(self):
        print("Hourly rate : $" + str(self.rate))
 
    def set_rate_per_hour(self, rate):
        self.rate = rate

    def print_final_pay(self):
        if (str(self.employee_contractor).lower() == "employee"):
            print("Final Pay : $" + str(self.salary))
        elif (str(self.employee_contractor).lower() == "contractor"):
            print("Final Pay : $" + str(self.hours * self.rate))

    def salary_raise(self, percent_raise):
        print(str(self.name) + "'s salary has been raise by " + str(percent_raise) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary + (self.salary * percent_raise)))
        self.salary += percent_raise * int(self.salary)
        
    def salary_cut(self, percent_cut):
        print(str(self.name) + "'s salary has been cut by " + str(percent_cut) + \
            "% from $" + str(self.salary) + " to $" + str(self.salary - (self.salary * percent_cut)))
        self.salary -= percent_cut * int(self.salary) 
    
    def rate_raise(self, amount_raise):
        print(str(self.name) + "'s hourly rate has been raise by $" + str(amount_raise) + \
            ", from $" + str(self.rate) + " to $" + str(self.salary + amount_raise))
        self.rate += int(amount_raise) 

    def rate_cut(self, amount_cut):
        print(str(self.name) + "'s hourly rate has been cut by $" + str(amount_cut) + \
            ", from $" + str(self.rate) + " to $" + str(self.salary - amount_cut))
        self.rate -= int(amount_cut) 


dict, names = {}, []
name, sex, employee_contractor = "", "", ""
age, phone_number, zip = 0, 0, 0


def add_employee():
    while True:
        print("Please provide the following information about the employee : ")

        while True:
            name = input("Employee name : ")
            if (str(name).lower() == 'q'):
                print("Quitting Program")
                quit()
            elif (not name.isalpha()):
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
            elif (str(employee_contractor).lower() == "employee" or \
                str(employee_contractor).lower() == "contractor"):
                break
            else:
                print("Please input a valid job status")

        dict[name] = [name, age, sex, phone_number, zip, employee_contractor]
        break_var = False
        while True:
            again = input("Add another employee? (y/n) ")
            if (str(again).lower() == 'q'):
                quit()
            elif (str(again).lower() != 'n' and str(again).lower() != 'y'):
                print("Please input a valid option (y/n) : ")
            elif (str(again).lower() == 'n'):
                break_var = True
                break
            else:
                break
        
        if (break_var):
            break


def remove_employee():
    while True:
        emp_name = input("Which employee would you like to remove? \n" + \
            str(names) + "\n: ")
        if (str(emp_name).lower() == 'q'):
            print("Quitting Program")
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

def is_number(input):
    return float(input) or int(input)


def get_info(emp_name):
    name, age, sex, phone_number, zip, employee_contractor = dict[emp_name]
    user = Pay(name, age, sex, phone_number, zip, employee_contractor)
    
    while True:
        if (str(employee_contractor).lower() == "employee"):
            which_info = input("\nWhat would you like to know about " + str(user.get_name()) + "?" + \
            "\nGeneral Info (a) \nPrivate Info (b) \nNumber of Days Worked (c) \nNumber of Sick Days (d) \
                \nHours Worked (e) \nFinal Pay Amount (f) \nSalary (g) \nBack (Back) \nQuit (Q) \n: "
            )
        else:
            which_info = input("\nWhat would you like to know about " + str(user.get_name()) + "?" + \
            "\nGeneral Info (a) \nPrivate Info (b) \nNumber of Days Worked (c) \nNumber of Sick Days (d) \
                \nHours Worked (e) \nFinal Pay Amount (f) \nRate per Hour (g) \nBack (Back) \nQuit (Q) \n: "
            )
        if (str(which_info).lower() == 'q'):
            print("Quitting Program")
            quit()
        elif (str(which_info).lower() == "back"):
            break
        elif (str(which_info).lower() not in "abcdefg"):
            print("Please input a valid option")
        elif (str(which_info).lower() == 'a'):
            user.print_general_info()
        elif (str(which_info).lower() == 'b'):
            user.print_personal_info()
        elif (str(which_info).lower() == 'c'):
            user.print_days_worked()
        elif (str(which_info).lower() == 'd'):
            user.print_sick_leaves()
        elif (str(which_info).lower() == 'e'):
            user.print_time_worked()
        elif (str(which_info).lower() == 'f'):
            user.print_final_pay()
        elif (str(which_info).lower() == 'g' and \
            str(employee_contractor).lower() == "employee"):
            user.print_salary()
        else:
            user.print_rate()


def edit_info(emp_name):
    name, age, sex, phone_number, zip, employee_contractor = dict[emp_name]
    user = Pay(name, age, sex, phone_number, zip, employee_contractor)

    while True:
        if (str(user.get_employee_contractor()).lower() == "employee"):
            which_info = input("\nWhat would you like to edit about " + str(user.get_name()) + "? \
                \nEdit Name (a) \nEdit Age (b) \nEdit Phone Number (c) \nEdit Zip Code (d) \
                    \nEdit Job Title (e) \nEdit Days Worked (f) \nEdit Sick-Leave Days (g) \
                    \nEdit Hour Worked (h) \nEdit Salary (i) \nGive Salary Raise (j) \
                    \nGive Salary Cut (k) \nBack (Back) \nQuit (Q) \n: "
            )
        else:
            which_info = input("\nWhat would you like to edit about " + str(user.get_name()) + "?  \
                \nEdit Name (a) \nEdit Age (b) \nEdit Phone Number (c) \nEdit Zip Code (d) \
                    \nEdit Job Title (e) \nEdit Days Worked (f) \nEdit Sick-Leave Days (g) \
                    \nEdit Hour Worked (h) \nEdit Rate per Hour (i) \nGive Rate Raise (j) \
                    \nGive Rate Cut (k) \nBack (Back) \nQuit (Q) \n: "
            )

        if (str(which_info).lower() == 'q'):
            print("Quitting Program")
            quit()
        elif (str(which_info).lower() == "back"):
            break
        elif (str(which_info).lower() not in "abcdefghijk"):
            print("Please input a valid option")
        elif(str(which_info).lower() == 'a'):
            while True:
                new_name = input(str(user.get_name()) + "'s new name: ")
                if (type(new_name) != str):
                    print("Please input a valid name")
                elif (str(new_name).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif new_name in dict:
                    print("This name is already registered")
                else:
                    for i in range(len(names)):
                        if (names[i] == user.get_name()):
                            names[i] = new_name  

                    dict[new_name] = dict[user.get_name()]
                    dict[new_name][0] = new_name
                    del dict[user.get_name()]

                    user.set_name(new_name)
                    break
        elif (str(which_info).lower() == 'b'):
            while True:
                new_age = input(str(user.get_name()) + "'s new age: ")
                if (str(new_age).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not new_age.isdigit()):
                    print("Please input a valid age")
                else:
                    user.set_age(new_age)
                    dict[user.get_name()][1] = new_age
                    break
        elif(str(which_info).lower() == 'c'):
            while True:
                new_phone_number = input(str(user.get_name()) + "'s new phone number: ")
                if (str(new_phone_number).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not new_phone_number.isdigit()):
                    print("Please input a valid phone number")
                else:
                    user.set_phone_number(new_phone_number)
                    dict[user.get_name()][3] = new_phone_number
                    break
        elif (str(which_info).lower() == 'd'):
            while True:
                new_zip = input(str(user.get_name()) + "'s new zip code: ")
                if (str(new_zip).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not new_zip.isdigit()):
                    print("Please input a valid zip code")
                else:
                    user.set_zip(new_zip)
                    dict[user.get_name()][4] = new_zip
                    break
        elif (str(which_info).lower() == 'e'):
            while True:
                new_job_title = input(str(user.get_name()) + "'s new job title (employee/contractor): ")
                if (str(new_job_title).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (str(new_job_title).lower() != "employee" and \
                    str(new_job_title).lower() != "contractor"):
                    print("Please input a valid job title")
                else:
                    user.set_employee_contractor(new_job_title)
                    dict[user.get_name()][-1] = new_job_title
                    break
        elif (str(which_info).lower() == 'f'):
            while True:
                new_days_worked = input("Add number of work-days for " + str(user.get_name()) + ": ")
                if (str(new_days_worked).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not new_days_worked.isdigit()):
                    print("Please input a valid number")
                else:
                    user.add_days_worked(new_days_worked)
                    break
        elif (str(which_info).lower() == 'g'):
            while True:
                new_sick_days = input("Add number of sick-leave days for " + str(user.get_name()) + ": ")
                if (str(new_sick_days).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not new_sick_days.isdigit()):
                    print("Please input a valid number")
                else:
                    user.add_sick_leaves(new_sick_days)
                    break
        elif (str(which_info).lower() == 'h'):
            while True:
                new_time_worked = input("Add number of hours worked for " + str(user.get_name()) + ": ")
                if (str(new_time_worked).lower() == 'q'):
                    print("Quitting Program")
                    quit()
                elif (not is_number(new_time_worked)):
                    print("Please input a valid number")
                else:
                    if (float(new_time_worked)):
                        user.add_time_worked(float(new_time_worked))
                    else:
                        user.add_time_worked(int(new_time_worked))
                    break
        elif (str(which_info).lower() == 'i'): 
            while True:
                if (str(user.employee_contractor).lower() == "employee"):
                    new_salary = input("Set " + str(user.get_name()) + "'s salary: ")
                    if (str(new_salary).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(new_salary)):
                        print("Please input a valid number")
                    else:
                        user.set_salary(new_salary)
                        break
                else:
                    new_rate = input("Set " + str(user.get_name()) + "'s rate per hour: ")
                    if (str(new_rate).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(new_rate)):
                        print("Please input a valid number")
                    else:
                        user.set_rate_per_hour(new_rate)
                        break
        elif (str(which_info).lower() == 'j'): 
            while True:
                if (str(user.employee_contractor).lower() == "employee"):
                    salary_raise = input("Give " + str(user.get_name()) + " a salary raise by %: ")
                    if (str(salary_raise).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(salary_raise)):
                        print("Please input a valid number")
                    else:
                        if (float(salary_raise)):
                            user.salary_raise(float(salary_raise))
                        else:
                            user.salary_raise(int(salary_raise))
                        break
                else:
                    rate_raise = input("Give " + str(user.get_name()) + " a rate raise by $: ")
                    if (str(rate_raise).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(rate_raise)):
                        print("Please input a valid number")
                    else:
                        if (float(rate_raise)):
                            user.rate_raise(float(rate_raise))
                        else:
                            user.rate_raise(int(rate_raise))
                        break
        
        elif (str(which_info).lower() == 'k'): 
            while True:
                if (str(user.employee_contractor).lower() == "employee"):
                    salary_cut = input("Give " + str(user.get_name()) + " a salary cut by %: ")
                    if (str(salary_cut).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(salary_cut)):
                        print("Please input a valid number")
                    else:
                        if (float(salary_cut)):
                            user.salary_cut(float(salary_cut))
                        else:
                            user.salary_cut(int(salary_cut))
                        break
                else:
                    rate_cut = input("Give " + str(user.get_name()) + " a rate cut by $: ")
                    if (str(rate_cut).lower() == 'q'):
                        print("Quitting Program")
                        quit()
                    elif (not is_number(rate_cut)):
                        print("Please input a valid number")
                    else:
                        if (float(rate_cut)):
                            user.rate_cut(float(rate_cut))
                        else:
                            user.rate_cut(int(rate_cut))
                        break


while True:
    print("\nWhat would you like to do?")
    user = input("Get Info About Employee (Get) \nEdit Info About Employee (Edit) \
        \nAdd Employee (Add) \nRemove Employee (Remove) \nBack (Back) \nQuit (Q) \n: ")
    if (str(user).lower() == 'q'):
        quit()
    elif (str(user).lower() == "back"):
        quit()
    elif (str(user).lower() == "get"):
        if (names == []):
            print("There are no employees to get")
        else: 
            while True:
                emp_name = input("\nWhich employee would you like to get information about? \n" + str(names) + \
                    "\nBack (Back) \nQuit (Q) \n: ")
                if (str(emp_name).lower() == 'q'):
                    quit()
                elif (str(emp_name).lower() == "back"):
                    break 
                elif (emp_name not in names):
                    print("This is not a valid employee name")
                else:
                    get_info(emp_name)
    elif (str(user).lower() == "edit"):
        if (names == []):
            print("There are no employees to edit")
        else:
            while True:
                emp_name = input("\nWhose information would you like to edit? \n" + str(names) + \
                    "\nBack (Back) \nQuit (Q) \n: ")
                if (str(emp_name).lower() == 'q'):
                    quit()
                elif (str(emp_name).lower() == "back"):
                    break
                elif (emp_name not in names):
                    print("This is not a valid employee name")
                else:
                    edit_info(emp_name)
    elif (str(user).lower() == "add"):
        add_employee()
    elif (str(user).lower() == "remove"):
        if names == []: 
            print("There are no employees to remove")
        else:
            remove_employee()
    else:
        print("Please input a valid command")

