# PYTEST-TESTAUSFUNKTIOT
# ======================

# MODUULIEN JA KIRJASTOJEN LASTAUKSET
# -----------------------------------

# Käyttöjärjestelmän virheilmoitusten testaus vaatii pytest:n lataamisen
import pytest # Jos testaa virheilmoituksia, voi jättää pois

# Ladataa testattavat moduuli
import periytyminen

# Luodaan testiolioita eri luokista testejä varten

person = periytyminen.Person("Assi", "Kalma")

student = periytyminen.RasekoStudent("Jonne", "Janttari", 45678)

teacher = periytyminen.RasekoTeacher("Mikko", "Viljanen", ["TiVi20oa", "TiVi20ka", "TiVi22"])


# TESTAUSFUNKTIOT ELI YKSIKÖTESTIT
# --------------------------------

def test_person_properties():
    assert person.givenName == "Assi"
    assert person.surName == "Kalma"

def test_person_age3():
    assert round(person.calculteAge3("2008-12-11")) == 16

def test_student_properties():
    assert student.studentNumber == 45678






