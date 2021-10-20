# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def show(self):
        return ', '.join(
            [f"{key}: {value}" for key, value in  self.__dict__.items()]
                         )


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.Salary = salary


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.Grades = grades


if __name__ == "__main__":
    # check if this code is working
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    for person in persons:
        print(person.show())
