# LUOKAT JA OLIOT
# ===============

# OLION MALLIT ELI LUOKAT
# ========================

# KIRJASTOJEN JA MODUULIT
# =======================

import datetime


class Student():
    """A class for student objects."""

    # Konstruktori-metodi eli oliomuodostin
    def __init__(self, name: str, group: str, dateOfBirth: str):
        """Constructor for the Student object

        Args:
            name (str): The name of the student
            group (str): His or her class
            dateOfBirth (str): Date of birth in iso format 
        """
        # Luokan kentät joista tulee objektin ominaisuudet
        self.name = name
        self.group = group
        self.birthday = dateOfBirth

    def studentOf(self) -> None:
        """Prints students name and class on the console
        """
        memberInGrroup = f"{self.name} opiskelee luokalla {self.group}."
        print(memberInGrroup)

    def calculateAge(self) -> int:
        """Calculates student's current age in fuul years

        Returns:
            int: age in years
        """
        birthDay = datetime.datetime.fromisoformat(self.birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days/ 365
        return round(ageInYears)

student = Student("Jonne", "Auto23A", "2008-05-21")
    
print(student.name, "on syntynyt", student.birthday, "ja kuuluu ryhmään", student.group)

student2 = Student("Tuittu", "Tivi20oa", "1990-03-09")
student2.studentOf()
print("ikä on", student2.calculateAge())










