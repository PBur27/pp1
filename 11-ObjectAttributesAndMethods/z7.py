class Student():
    
    university = "UEK Kraków"
    id = 1000000

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = Student.id
        Student.id += 1

    def __str__(self):
        return f"{self.name} {self.surname.upper()} ({self.id})"


student1 = Student("Anna", "Maj")
student2 = Student("Jan", "Kowalski")
student3 = Student("Andrzej", "Wójcik")

print(student1)
print(student2)
print(student3)
    
