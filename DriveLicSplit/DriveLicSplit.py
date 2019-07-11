# Developed with Python 3.7.4
# using Atom as an IDE

data = [ "Johanna" , "" , "Rye" , "13-Dec-1981" , "F" ]
# data = [ "Johanna" , "" , "Ryegsdfhdjd" , "13-Dec-1981" , "F" ]

monthsDict = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
}

license = ""
fname   = data[0]
mname   = data[1]
surname = data[2]
dob     = data[3]
sex     = data[4]

licenseFname    = ""
licenseMname    = ""
licenseSurname  = ""
licenseDecade   = ""
licenseYear     = ""
licenseMonth    = ""
licenseDay      = ""

day     = dob.split("-")[0]
month   = dob.split("-")[1]
year    = dob.split("-")[2]

print(monthsDict[month])
print("Was born the ", day, " of ", month, " of ", year)

print("Surname length: ", len(surname))
print(len(surname) < 5)

# 1-5 The first five characters of the surname
# (padded with 9s if less than 5 characters)
if len(surname) < 5:
    licenseSurname = surname.ljust(5,"9")
else:
    licenseSurname = surname[:5]

license += licenseSurname.upper()
print("licenseSurname ", licenseSurname)

# The decade digit from the year of birth (e.g. for 1987 it would be 8)
licenseDecade = year[2]
license += licenseDecade
print("licenseDecade is ", licenseDecade)

# 7–8 : The month of birth in digits
# (7th character incremented by 5 if driver is female)
if(sex == "F"):
    newVal = int(monthsDict[month][0]) + 5
    newVal = str(newVal)
    oldVal = monthsDict[month][0]
    print("oldVal: ", oldVal)
    print("newVal: ", newVal)
    licenseMonth = monthsDict[month].replace(oldVal, newVal)
else:
    licenseMonth = monthsDict[month]

license += licenseMonth
print("licenseMonth is ", licenseMonth)

# 9–10 : The date within the month of birth
licenseDay = day
license += licenseDay
print("licenseDay ", licenseDay)

# 11 : The last digit from the year of birth
licenseYear = year[3]
license += licenseYear
print("licenseYear ", licenseYear)

# 12–13 : The first initial from the first name and middle name,
# padded with a 9 if no middle name
licenseFname = fname[0]
license += licenseFname

if(mname == ""):
    licenseMname = "9"
else:
    licenseMname = mname[0]

license += licenseMname

print("licenseMname ", licenseMname)
print("\n")
print("License is ", license)
