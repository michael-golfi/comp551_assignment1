import csv

def getAgeGroup(age):
	if (age>11 and age<15):
		return 1
	if (age>=15 and age<20):
		return 2
	if (age>=20 and age<25):
		return 3
	if (age>=25 and age<30):
		return 4
	if (age>=30 and age<35):
		return 5
	if (age>=35 and age<40):
		return 6
	if (age>=40 and age<45):
		return 7
	if (age>=45 and age<50):
		return 8
	if (age>=50 and age<55):
		return 9
	if (age>=55 and age<60):
		return 10
	if (age>=60 and age<65):
		return 11
	if (age>=65 and age<70):
		return 12
	if (age>=70 and age<75):
		return 13
	if (age>=75 and age<79):
		return 14 

def checkDivision(age, gender):
	age_group = ''
	age_group = str(getAgeGroup(int(age)))
	if (gender == 'M'):
		return ('M: ' + age_group)
	else:
		return ('F: ' + age_group)
# make sure to change the full path
with open('/Users/ralphbousamra/Desktop/Project1_data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	spamreader.__next__()
	for row in spamreader:
		if(len(row) > 8):
			print (row[0] + ": " + checkDivision(row[len(row)-6], row[len(row)-5]))
		else:
			print (row[0] + ": " + checkDivision(row[2], row[3]))
