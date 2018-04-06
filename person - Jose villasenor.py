class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee (Person):
    def __init__(self, name, money_made, age):
        super(Employee, self).__init__(name, age)
        self.name = name
        self.money_made = money_made

    def go_home(self):
        print("%s leaves work" % self.name)


class Programmer(Employee):
    def __init__(self, job_name, name, money_made, age):
        super(Programmer, self).__init__(name, money_made, age)
        self.job_name = job_name

    def type(self):
        print("%s goes to work for 7 hours" % self.name)

    def job_earnings(self):
        print("their job is %s" % self.job_name)
        print("they went home and made %s " % self.money_made)


test = Programmer("programing", "jake", '$44', 24)
test.go_home()
test.work()
test.job_earnings()

