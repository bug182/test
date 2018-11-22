from datetime import datetime
import time
import os
current_date = datetime.now()
years = []
years_alive = []
year_s = input('Give a year farther than your birth year: ')
def cls():
	os.system('cls')

def add_years(s_year):
	print('Just fetching every year from '+ year_s + ' to the current year')
	start_year = int(year_s)
	for year in range(start_year, current_date.year + 1):
		time.sleep(.15)
		years.append(year)
		print(year)
	print('Done!')
	time.sleep(3)
	cls()

add_years(year_s)

'''
birth = input('What year were you born? ')
print('So you were born in ' + birth + ', dope!')

def calculate(birth_y):
	i = -1
	for from_birth in range(birth_y, current_date.year +1):
		i +=1
		years_alive.append(from_birth)
	return i
	
	
num_of_years = calculate(int(birth))
print('You have been alive for ' + str(num_of_years) + ' years!')
print('The years you have been alive are the following: ' + str(years_alive))
'''