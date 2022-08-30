class Student:

    def __init__(self, id, first_name, middle_name, last_name, dob, course, period):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = dob
        self.course = course
        self.period = period

    # incapsulation(setters and getters)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_middle_name(self):
        return self.middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_dob(self, dob):
        self.dob = dob

    def get_dob(self):
        return self.dob

    def set_course(self, course):
        self.course = course

    def get_course(self):
        return self.course

    def set_period(self, period):
        self.period = period

    def get_period(self):
        return self.period
