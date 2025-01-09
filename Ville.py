import datetime
birthdate = input("Anna syntymäaikasi(pp-kk-vvvv)! ")
#birthdate = "24-06-1994"
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("Your age is",age,"years.")