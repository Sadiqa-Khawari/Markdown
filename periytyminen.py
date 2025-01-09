# PERIYTYMINEN INHERITANCE
# ========================

# KIRJASTOT JA MODUULIT
# ======================
import oliot
from oliot import Student
import datetime



class Person():
    """Commonn class for all persons in Raseko"""

    def __init__(self, etunimi: str, sukunimi: str):

        """Creates a Person object
            Args:
            etunimi (str): A first name 
            sukunimi (str): A last age 
        """
        self.etunimi = etunimi
        self.sukunimi = sukunimi
    @staticmethod
    def calculateAge(birthday) -> float:
        """Calculates student's current age in fuul years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)

    @classmethod
    def calculateAge2(cls, birthday):
        """Calculates student's current age in fuul years

        Returns:
            float: age in years
        """
        birthDay = datetime.datetime.fromisoformat(birthday)
        age = datetime.datetime.now() - birthDay
        ageInYears = age.days / 365
        return round(ageInYears)
        
# ALILUOKKA ELI LAPSILUOKKA (SUB / CHILD CLASS)
#----------------------------------------------
class RasekoStudent(Person):
    """The student class, inherits from Person class"""
    def __init__(self, etunimi: str, sukunimi: str, opiskelijanumero: str):
        """Creates a student object

        Args:
            etunimi (str): Opiskelijan etunimi 
            sukunimi (str): Opiskelijan sukunimi
            opiskelijanumero (str): Opiskelijanumero
        """
        super().__init__(etunimi, sukunimi) # Määritellään tapahtuvaksi yliluokan mukaan.
        self.opiskelijanumero = opiskelijanumero # Ei määritelty yliluokassa

class RasekoTeacher(Person):
    """Creates a teacher inheriting the Person class

    Args:
        Person (class): Name of the super class
    """
    def __init__(self, etunimi: str, sukunimi: str, luokat: list[str]):
        """Constructor metod for teacher objects

        Args:
            etunimi (str): Teacher's given name
            sukunimi (str): Teacher's surname
            luokat (list[str]): List of student groups
        """
        super().__init__(etunimi, sukunimi)
        self.luokat = luokat
    
if __name__ == "__main__":
    rasekoStudent = RasekoStudent("Jonne", "Janttari", "456543")
    print(rasekoStudent.sukunimi)

    luokat = ["TiVi23A", "TiVi23B", "TiVi20oa"]
    rasekoTeacher = RasekoTeacher("Markku", "Kynsijärvi", luokat)
    print(f"{rasekoTeacher.etunimi} opettaa ryhmiä {rasekoTeacher.luokat}")

    # Luodaan moduulista oliot.py Student-olio
    student = Student("Tuittu Kiukkunen", "Auto22B", "2007-10-23")
    print(f"{student.name} on {student.calculateAge()} vuotta vanha.")

    ika = Person.calculateAge('2008-03-22')
    print(ika)

    ika2 = Person.calculateAge2('1978-12-10')
    print(ika2)
        