from __future__ import annotations
import abc

# --- 1. Classe Astratta Persona ---
class Person(abc.ABC):
    """
    Classe base astratta per persone all'interno del sistema universitario.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abc.abstractmethod
    def get_role(self) -> str:
        """
        Metodo astratto per restituire il ruolo della persona (es. 'Studente', 'Professore').
        Da implementare nelle sottoclassi.
        """
        pass

    def __str__(self) -> str:
        """
        Restituisce una rappresentazione in stringa della persona.
        """
        return f"{self.get_role()}: {self.name}, Età: {self.age}"

# --- 2. Sottoclassi Studente e Professore ---
class Student(Person):
    """
    Rappresenta uno studente nel sistema universitario.
    """
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses: list[Course] = []  # Lista di istanze di Course

    def get_role(self) -> str:
        return "Studente"

    def enroll(self, course: Course):
        """
        Iscrive lo studente a un corso.
        """
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  # Aggiunge lo studente al corso
            print(f"{self.name} iscritto a '{course.name}'.")
        else:
            print(f"{self.name} è già iscritto a '{course.name}'.")

    def __str__(self) -> str:
        enrolled_courses = ", ".join([c.name for c in self.courses]) if self.courses else "Nessuno"
        return f"{super().__str__()}, ID: {self.student_id}, Corsi: [{enrolled_courses}]"

class Professor(Person):
    """
    Rappresenta un professore nel sistema universitario.
    """
    def __init__(self, name: str, age: int, professor_id: str):
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department: Department | None = None  # Istanza di Department
        self.courses: list[Course] = []  # Lista di istanze di Course

    def get_role(self) -> str:
        return "Professore"

    def assign_to_course(self, course: Course):
        """
        Assegna il professore a un corso.
        """
        if course not in self.courses:
            self.courses.append(course)
            course.set_professor(self)  # Imposta il professore per il corso
            print(f"Prof. {self.name} assegnato a '{course.name}'.")
        else:
            print(f"Prof. {self.name} è già assegnato a '{course.name}'.")

    def set_department(self, department: Department):
        """
        Assegna il professore a un dipartimento.
        """
        if self.department is None or self.department != department:
            if self.department: # Rimuovi dal vecchio dipartimento se assegnato
                self.department.remove_professor(self)
            self.department = department
            department.add_professor(self) # Aggiungi il professore al dipartimento
            print(f"Prof. {self.name} assegnato al Dipartimento di {department.name}.")
        else:
            print(f"Prof. {self.name} è già assegnato al Dipartimento di {department.name}.")

    def __str__(self) -> str:
        dept_name = self.department.name if self.department else "Non assegnato"
        taught_courses = ", ".join([c.name for c in self.courses]) if self.courses else "Nessuno"
        return f"{super().__str__()}, ID: {self.professor_id}, Dipartimento: {dept_name}, Insegna: [{taught_courses}]"

# --- 3. Classe Course ---
class Course:
    """
    Rappresenta un corso accademico.
    """
    def __init__(self, course_name: str, course_code: str):
        self.name = course_name
        self.code = course_code
        self.students: list[Student] = []  # Lista di istanze di Student
        self.professor: Professor | None = None  # Istanza di Professor

    def add_student(self, student: Student):
        """
        Aggiunge uno studente al corso.
        """
        if student not in self.students:
            self.students.append(student)
            # Nota: L'iscrizione dello studente (student.enroll) dovrebbe già gestire l'aggiunta qui.
            # Questo metodo è più per uso interno del corso.
            print(f"Studente '{student.name}' aggiunto al corso '{self.name}'.")
        else:
            print(f"Studente '{student.name}' è già nel corso '{self.name}'.")

    def set_professor(self, professor: Professor):
        """
        Imposta il professore per il corso.
        """
        if self.professor is None or self.professor != professor:
            if self.professor: # Rimuovi il corso dal vecchio professore se assegnato
                self.professor.courses.remove(self)
            self.professor = professor
            if self not in professor.courses: # Assicurati che il corso sia nella lista del professore
                professor.courses.append(self)
            print(f"Prof. {professor.name} assegnato come docente per '{self.name}'.")
        else:
            print(f"Prof. {professor.name} è già il docente di '{self.name}'.")

    def __str__(self) -> str:
        professor_name = self.professor.name if self.professor else "Non assegnato"
        student_names = ", ".join([s.name for s in self.students]) if self.students else "Nessuno"
        return (f"Corso: {self.name} ({self.code})\n"
                f"  Docente: {professor_name}\n"
                f"  Iscritti: [{student_names}]")

# --- 4. Classe Department ---
class Department:
    """
    Rappresenta un dipartimento universitario.
    """
    def __init__(self, name: str):
        self.name = name
        self.courses: list[Course] = []  # Lista di istanze di Course
        self.professors: list[Professor] = []  # Lista di istanze di Professor

    def add_course(self, course: Course):
        """
        Aggiunge un corso al dipartimento.
        """
        if course not in self.courses:
            self.courses.append(course)
            print(f"Corso '{course.name}' aggiunto al Dipartimento di {self.name}.")
        else:
            print(f"Corso '{course.name}' è già nel Dipartimento di {self.name}.")

    def add_professor(self, professor: Professor):
        """
        Aggiunge un professore al dipartimento.
        """
        if professor not in self.professors:
            self.professors.append(professor)
            # Nota: L'assegnazione del dipartimento al professore dovrebbe gestire l'aggiunta qui.
            # Questo metodo è più per uso interno del dipartimento.
            print(f"Prof. {professor.name} aggiunto al Dipartimento di {self.name}.")
        else:
            print(f"Prof. {professor.name} è già nel Dipartimento di {self.name}.")

    def remove_professor(self, professor: Professor):
        """
        Rimuove un professore dal dipartimento.
        """
        if professor in self.professors:
            self.professors.remove(professor)
            if professor.department == self:
                professor.department = None # Disassocia il dipartimento dal professore
            print(f"Prof. {professor.name} rimosso dal Dipartimento di {self.name}.")
        else:
            print(f"Prof. {professor.name} non trovato nel Dipartimento di {self.name}.")

    def __str__(self) -> str:
        course_names = ", ".join([c.name for c in self.courses]) if self.courses else "Nessuno"
        professor_names = ", ".join([p.name for p in self.professors]) if self.professors else "Nessuno"
        return (f"Dipartimento: {self.name}\n"
                f"  Corsi offerti: [{course_names}]\n"
                f"  Professori: [{professor_names}]")

# --- 5. Classe University ---
class University:
    """
    Rappresenta l'università nel suo complesso, gestendo dipartimenti e studenti.
    """
    def __init__(self, name: str):
        self.name = name
        self.departments: list[Department] = []  # Lista di istanze di Department
        self.students: list[Student] = []  # Lista di istanze di Student

    def add_department(self, department: Department):
        """
        Aggiunge un dipartimento all'università.
        """
        if department not in self.departments:
            self.departments.append(department)
            print(f"Dipartimento '{department.name}' aggiunto a {self.name}.")
        else:
            print(f"Dipartimento '{department.name}' è già presente in {self.name}.")

    def add_student(self, student: Student):
        """
        Aggiunge uno studente all'università.
        """
        if student not in self.students:
            self.students.append(student)
            print(f"Studente '{student.name}' aggiunto a {self.name}.")
        else:
            print(f"Studente '{student.name}' è già presente in {self.name}.")

    def __str__(self) -> str:
        department_names = "\n  ".join([str(d) for d in self.departments]) if self.departments else "  Nessun dipartimento."
        student_names = "\n  ".join([str(s) for s in self.students]) if self.students else "  Nessuno studente."
        return (f"=== Università: {self.name} ===\n"
                f"--- Dipartimenti ---\n{department_names}\n"
                f"--- Studenti Iscritti all'Università ---\n{student_names}")
                
if __name__ == "__main__":
    print("### Inizializzazione dell'Università ###")
    my_university = University("Università degli Studi di Pythonville")
    print(my_university)

    print("\n### Creazione di Dipartimenti ###")
    dept_cs = Department("Informatica")
    dept_lit = Department("Letteratura")
    dept_eng = Department("Ingegneria")

    my_university.add_department(dept_cs)
    my_university.add_department(dept_lit)
    my_university.add_department(dept_eng)

    print("\n### Creazione di Corsi ###")
    course_ds = Course("Strutture Dati", "CS101")
    course_alg = Course("Algoritmi", "CS102")
    course_ml = Course("Machine Learning", "CS301")
    course_med_lit = Course("Letteratura Medievale", "LIT201")
    course_rom_lit = Course("Letteratura Romantica", "LIT202")
    course_thermo = Course("Termodinamica", "ENG201")

    dept_cs.add_course(course_ds)
    dept_cs.add_course(course_alg)
    dept_cs.add_course(course_ml)
    dept_lit.add_course(course_med_lit)
    dept_lit.add_course(course_rom_lit)
    dept_eng.add_course(course_thermo)

    print("\n### Creazione di Professori ###")
    prof_rossi = Professor("Prof. Rossi", 45, "P001")
    prof_bianchi = Professor("Prof. Bianchi", 50, "P002")
    prof_verdi = Professor("Prof. Verdi", 38, "P003")

    prof_rossi.set_department(dept_cs)
    prof_bianchi.set_department(dept_lit)
    prof_verdi.set_department(dept_eng)

    print("\n### Creazione di Studenti ###")
    student_mario = Student("Mario Rossi", 20, "S001")
    student_luisa = Student("Luisa Neri", 21, "S002")
    student_giulia = Student("Giulia Verdi", 19, "S003")
    student_paolo = Student("Paolo Gialli", 22, "S004")

    my_university.add_student(student_mario)
    my_university.add_student(student_luisa)
    my_university.add_student(student_giulia)
    my_university.add_student(student_paolo)

    print("\n### Assegnazione Professori ai Corsi ###")
    prof_rossi.assign_to_course(course_ds)
    prof_rossi.assign_to_course(course_alg)
    prof_bianchi.assign_to_course(course_med_lit)
    prof_verdi.assign_to_course(course_thermo)
    # Prova ad assegnare lo stesso professore allo stesso corso (non dovrebbe ripetersi)
    prof_rossi.assign_to_course(course_ds)

    print("\n### Iscrizione Studenti ai Corsi ###")
    student_mario.enroll(course_ds)
    student_mario.enroll(course_alg)
    student_luisa.enroll(course_ds)
    student_luisa.enroll(course_ml)
    student_giulia.enroll(course_med_lit)
    student_paolo.enroll(course_thermo)
    student_paolo.enroll(course_alg) # Paolo si iscrive a un corso del Dipartimento di Informatica

    # Prova a iscrivere lo stesso studente allo stesso corso (non dovrebbe ripetersi)
    student_mario.enroll(course_ds)

    print("\n--- STATO ATTUALE DELL'UNIVERSITÀ ---")
    print(my_university)

    print("\n### Dettagli specifici di Corsi ###")
    print(course_ds)
    print(course_ml)
    print(course_med_lit)

    print("\n### Dettagli specifici di Professori ###")
    print(prof_rossi)
    print(prof_bianchi)

    print("\n### Dettagli specifici di Studenti ###")
    print(student_mario)
    print(student_luisa)
    print(student_giulia)
    print(student_paolo)

    print("\n### Prova di riassegnazione professore ###")
    prof_rossi.set_department(dept_eng) # Rossi cambia dipartimento
    prof_rossi.assign_to_course(course_thermo) # Rossi ora insegna Termodinamica

    print("\n--- STATO FINALE AGGIORNATO ---")
    print(my_university)
    print(prof_rossi) # Verifica che i corsi di Rossi siano aggiornati
    print(course_thermo) # Verifica che il professore del corso sia cambiato
    print(course_ds) # Verifica che il professore sia stato rimosso (se non assegnato ad altri)