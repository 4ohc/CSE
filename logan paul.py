class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee (Person):
    def __init__(self, name, age):
        super(Employee, self).__init__('')
