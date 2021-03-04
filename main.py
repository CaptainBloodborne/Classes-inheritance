# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    pass


class Teacher:
    pass


class Student:
    pass


if __name__ == "__main__":
    # check if this code is working
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    for person in persons:
        print(person.show())
