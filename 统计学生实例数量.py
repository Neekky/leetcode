class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1 #定义成Student.count后，它的数值可以不断累加

bart = Student('Bart')
bar = Student('Bar')
two=Student('two')
print(Student.count)

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1 #改成self.count后，它的数值不能累加

bart = Student('Bart')
bart = Student('Bart')
bart = Student('Bart')
print(bart.count)
