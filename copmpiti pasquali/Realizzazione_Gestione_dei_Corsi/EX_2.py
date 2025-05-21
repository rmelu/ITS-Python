class Person:
    def __init__(self, name: str, surname: str, age: int, cf: str):
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        self.cf: str = cf

class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group: str | None = None

    def set_group(self, group: str):
        self.group = group
        return self.group
    
    def get_group(self) -> str | None:
        return self.group
    
class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name: str, limit:int):
        self. name: str = name
        self.limit: str = limit
        self.students: list[str] = []
        self.lecturers: list[str] = []

    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> str:
        return self.limit
    
    def get_students(self) -> list[str]:
        return self.students
    
    def get_lecturers(self) -> list[str]:
        return self.lecturers
    
    def add_student(self, student_id: str):
        if len(self.students) < self.limit and student_id not in self.students:
            self.students.append(student_id)
            return True
        return False
    
    def add_lecturer(self, lecturer: str):
        if lecturer not in self.lecturers:
            self.lecturers.append(lecturer)
            return True
        return False
    
if __name__ == "__main__":
    gruppo_a = Group("Gruppo A", 25)
    student = Student("CF123", "Mario", "Rossi", 30)
    student.set_group("Gruppo A")
    print(f"Gruppo dello studente: {student.get_group()}")


person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)
lecturer1 = Lecturer(cf="CF789", name="Dr. Emily", surname="Brown", age=45)

# Test della classe Person
print("Test della classe Person:")
print(f"CF: {person1.cf}, Atteso: CF123")
print(f"Nome: {person1.name}, Atteso: John")
print(f"Cognome: {person1.surname}, Atteso: Doe")
print(f"Età: {person1.age}, Atteso: 30")

# Test della classe Student
print("\nTest della classe Student:")
print(f"CF: {student1.cf}, Atteso: CF456")
print(f"Nome: {student1.name}, Atteso: Jane")
print(f"Cognome: {student1.surname}, Atteso: Smith")
print(f"Età: {student1.age}, Atteso: 20")
print(f"Gruppo iniziale: {student1.group}, Atteso: None")

# Test metodo set_group della classe Student
group1 = Group(name="Group A", limit=10)
student1.set_group(group1)
print("\nDopo set_group di student1:")
print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")

# Test della classe Lecturer
print("\nTest della classe Lecturer:")
print(f"CF: {lecturer1.cf}, Atteso: CF789")
print(f"Nome: {lecturer1.name}, Atteso: Dr. Emily")
print(f"Cognome: {lecturer1.surname}, Atteso: Brown")
print(f"Età: {lecturer1.age}, Atteso: 45")

# Creazione di un gruppo e aggiunta di studenti e docenti
group2 = Group(name="Group B", limit=2)
group2.add_student(student1)
group2.add_lecturer(lecturer1)

print("\nDopo aggiunta di student1 e lecturer1 a group2:")
print(f"Studenti in group2: {[student.cf for student in group2.get_students()]}, Atteso: [CF456]")
print(f"Docenti in group2: {[lecturer.cf for lecturer in group2.lecturers]}, Atteso: [CF789]")