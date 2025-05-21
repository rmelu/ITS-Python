class Course:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def get_groups(self):
        return self.groups

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                if group.add_student(student):
                    student.set_group(group.get_name()) # Associa lo studente al gruppo
                    return True
        return False

# Esempio di utilizzo (per testare la Parte 3 - MI ASSICURO di avere già istanze di Group e Student):
if __name__ == "__main__":
    # Esempio di come POTREI creare istanze di Group e Student
    class Person:
        def __init__(self, cf, name, surname, age):
            self.cf = cf
            self.name = name
            self.surname = surname
            self.age = age

    class Student(Person):
        def __init__(self, cf, name, surname, age):
            super().__init__(cf, name, surname, age)
            self.group = None

        def set_group(self, group):
            self.group = group

    class Group:
        def __init__(self, name, limit):
            self.name = name
            self.limit = limit
            self.students = []
            self.lecturers = []

        def get_name(self):
            return self.name

        def get_limit(self):
            return self.limit

        def get_students(self):
            return self.students

        def get_lecturers(self):
            return self.lecturers

        def add_student(self, student):
            if len(self.students) < self.limit:
                self.students.append(student)
                return True
            return False

        def add_lecturer(self, lecturer):
            if len(self.lecturers) < 1:
                self.lecturers.append(lecturer)
                return True
            return False

    # Test della classe Course
    corso_informatica = Course("Corso di Informatica")

    gruppo1 = Group("Gruppo Alfa", 2)
    gruppo2 = Group("Gruppo Beta", 3)

    corso_informatica.add_group(gruppo1)
    corso_informatica.add_group(gruppo2)

    studente_a = Student("SA1", "Anna", "Verdi", 20)
    studente_b = Student("SB2", "Bruno", "Rossi", 21)
    studente_c = Student("SC3", "Carla", "Neri", 19)
    studente_d = Student("SD4", "Dario", "Bianchi", 22)
    studente_e = Student("SE5", "Elena", "Gialli", 20)

    corso_informatica.register(studente_a)
    corso_informatica.register(studente_b)
    corso_informatica.register(studente_c)
    corso_informatica.register(studente_d)
    corso_informatica.register(studente_e)

    print(f"Gruppi nel corso: {[gruppo.get_name() for gruppo in corso_informatica.get_groups()]}")
    print(f"Studenti nel Gruppo Alfa: {[s.name for s in gruppo1.get_students()]}")
    print(f"Studenti nel Gruppo Beta: {[s.name for s in gruppo2.get_students()]}")
    print(f"Gruppo di Anna: {studente_a.group}")
    print(f"Gruppo di Carla: {studente_c.group}")
    print(f"Registrazione di Elena riuscita: {studente_e.group is not None}")