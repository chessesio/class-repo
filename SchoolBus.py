#There's a school bus that contains up to 1 driver and 10 students
#The school bus can drive only if there are 10 students and 1 driver

class Student:

    def __init__(self):
        pass


class Driver:
    
    def __init__(self):
        pass


class SchoolBus:

    driver_counter = 0
    student_counter = 0

    def __init__(self):
        self.bus = []

    def add_driver(self,driver):
        if len(self.bus) <= 10:
            self.bus.append(driver)
            SchoolBus.driver_counter += 1

    def add_student(self,student):
        if len(self.bus) <= 10:
            self.bus.append(student)
            SchoolBus.student_counter += 1

    def drive(self):
        driver_count = 0
        student_count = 0
        for person in self.bus:
            if isinstance(person, Driver):
                driver_count += 1

            elif isinstance(person, Student):
                student_count += 1

        if driver_count == 1 and student_count == 10:
            print("Let's go!")

        else:
            print("I can only drive if there's 1 driver and 10 students")
            print("There is/are {} driver(s)".format(driver_count))
            print("There is/are {} student(s)".format(student_count))

    def get_passengers(self):
        print("There is/are {} driver(s) in the bus".format(SchoolBus.driver_counter))
        print("There is/are {} student(s) in the bus".format(SchoolBus.student_counter))


    def loop(self):
        a = 3
        go = SchoolBus()
        while a != 1:

            
            choice = input("What do you want to do?\n1 Add driver\n2 Add student\n3 to view passengers\n4 to drive bus\n5 Exit\n")

            if choice == "1":
                go.add_driver(Driver())
                
            elif choice == "2":
                go.add_student(Student())

            elif choice == "3":
                go.get_passengers()

            elif choice == "4":
                go.drive()

            elif choice == "5":
                a = 1

            else:
                print("Invalid choice!")

board = SchoolBus()
board.loop()