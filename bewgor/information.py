#usr/bin/env python3

#ALPHA NOTE
#This function that sets up the creation of 'flat' Person class instances for each associate
# (all types of associates have the same prompts)
# will be replaced with individual relationship classes
# (Significant other, children, siblings, pets, etc)
# in future releases

import re

from .main_subject import MainSubject
from .utilities import *
from .validator import *

def getAssociates():

	associates = [] #list that will contain inputted associates, or return blank if none are given


	#Create Significant Other Instances (just one for now)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	SO_choice = input("Does the Main Subject have a Significant Other you have information on? (Y/N) >:").upper()

	SO_choice = spaceShaver(SO_choice) #cleans up answer - stops false negative with "yes "

	if SO_choice in "YES" and len(SO_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'associates.append('Signifcant_Other')
		associates.append('Significant_Other')

	divider()


	#Get number of children instances that will be created
	#(Son and daughter, not 'children' in the context of Python classes)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's children do you have information on? \nEnter '0' if there are none.")
	children_choice = input("> Enter the number here >:")

	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(children_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's children do you have information on? \nEnter '0' if there are none.")
		children_choice = input("> Enter the number here >:")

	if (children_choice) != str(0):
		for i in range(1,int(children_choice)+1):
			associates.append('Child_Number_'+str(i))

	divider()

	#Get number of Parent instances that will be created
	#(Son and daughter, not 'children' in the context of Python classes)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's parents do you have information on?")
	parents_choice = input("> Enter the number here >:")

	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(parents_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's parents do you have information on?")
		parents_choice = input("> Enter the number here >:")

	if (parents_choice) != str(0):
		for i in range(1,int(parents_choice)+1):
			associates.append('Parent_Number_'+str(i))

	divider()

	#Get number of Sibling instances that will be created
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's siblings do you have information on? \nEnter '0' if there are none.")
	siblings_choice = input("> Enter the number here >:")

	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(siblings_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's siblings do you have information on? \nEnter '0' if there are none.")
		siblings_choice = input("> Enter the number here >:")

	if (siblings_choice) != str(0):
		for i in range(1,int(siblings_choice)+1):
			associates.append('Sibling_Number_'+str(i))

	divider()

	# Get number of pet instances that will be created
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's pets do you have information on? \nEnter '0' if there are none.")
	pets_choice = input("> Enter the number here >:")

	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(pets_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's pets do you have information on?\nEnter '0' if there are none.")
		pets_choice = input("> Enter the number here >:")

	if (pets_choice) != str(0):
		for i in range(1,int(pets_choice)+1):
			associates.append('Pet_Number_'+str(i))

	return associates

# Function that creates "Phone Spellings" of a group of words
# NOT INCLUDING PHONESPELLING IN ALPHA RELEASE, IT NEEDS REFINING
def getPhoneSpelling(words):

	all_letters = re.compile('^[a-zA-Z]+$') #ensure only perform spelling on words that are all letters - no numbers or punctuation

	phonespellings = []

	two_group = ['a','b','c']
	three_group = ['d','e','f']
	four_group = ['g','h','i']
	five_group = ['j','k', 'l']
	six_group = ['m','n','o']
	seven_group = ['p','q','r','s']
	eight_group = ['t','u','v']
	nine_group = ['w','x','y','z']

	for word in words:
		if all_letters.match(word) and len(word) <= 8:
		#only create phonespellings of words that aren't too long
		#8 aeems like a good enough max length since it is minimum WPA length


			spelling = ""

			for charac in word:
				if charac.lower() in two_group:      spelling += "2"
				elif charac.lower() in three_group:  spelling += "3"
				elif charac.lower() in four_group:   spelling += "4"
				elif charac.lower() in five_group:   spelling += "5"
				elif charac.lower() in six_group:    spelling += "6"
				elif charac.lower() in seven_group:  spelling += "7"
				elif charac.lower() in eight_group:  spelling += "8"
				elif charac.lower() in nine_group:   spelling += "9"

				phonespellings.append(spelling)

	return phonespellings

#Function to aquire additional full dates
def getMoreFullDates():
	print ("""--- Get More Full Dates (DDMMYYYY)---

 Want to add any other specific full dates? Simply press enter if not.

 The prompts after this will request specific days (DDMM) and years
 If you wish to add a date from a year with less than 4 digits,
 or wish to specify an era (AD, BC, CE, BCE)
 do so later in the 'Add Additional Specific Words' prompt.
 """)


	fulldates = [] # list that will contain full dates, or return blank if none are given

	fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(fulldate) !=0:

		if nonzero_blankspace_reg.match(fulldate): #rejects inputs of just empty space characters
			print (" [-] Empty Space, try again.")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif not eight_digs_reg.match(fulldate): #reject inputs that aren't 8 digits exactly
			print (" [-] Invalid Characters, try again.")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif int(fulldate[2:4]) > 12: #rejects bad month input
			print (" [-] Invalid Month. After December, before January - check your DDMMYYYY format")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif int(fulldate[0:2]) > 31: #rejects bad day input
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif not doesDayExist(fulldate[0:4]): #rejects dates that do not exist
			print (" [-] Invalid date. That month has fewer days. Try again.")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")


		elif isItInvalidLeap(fulldate): #rejects invalid leap days
			print (" [-] That day did not take place that year. Try again >:")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif fulldate in fulldates: #rejects inputs that have already been entered
			print (" [-] That date has already been entered. Try again >:")
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		else:
			fulldates.append(fulldate) #add the date to the list
			fulldate = input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

	fulldates = list(set(fulldates)) # ensures there are no duplicates
	return fulldates

#Function to request additional specific Days (day and month, no year)
def getMoreDays():

	print("""--- Get Additional Specific Days ---

 Want to add any other specific Days? Simply press enter if not.
 This prompt does not consider year, just day and month
 """)
	add_spec_days = [] #list that will be populated with additional days


	#Adding days in the future is allowed here.

	add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_spec_day) != 0:

		if nonzero_blankspace_reg.match(add_spec_day):  # ensures input isn't only blank space characters
			print (' [-] Empty space, try again.')
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		elif not four_digs_reg.match(add_spec_day): # ensures input is limited to 4 digits exactly
			print (' [-] Days must be 4 Digits, try again.')
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		elif int(add_spec_day[2:4]) > 12: #checks for an invalid month
			print (" [-] Invalid month- After December, but before January - check your DDMM format")
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		elif int(add_spec_day[0:2]) > 31: #checks for an invalid day
			print (" [-] Invalid Day, no month has more than 31 days. Try again.")
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		elif not doesDayExist(add_spec_day): #ensures day exists
			print (" [-] Invalid date. That month has fewer days. Try again.")
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		elif add_spec_day in add_spec_days: # check for double input
			print (' [-] That input has already been added to the list. Try again')
			add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

		else:
			add_spec_days.append(add_spec_day) #if the day is valid, add it to list

		add_spec_day = input("> Enter an additional day here, or simply press enter to move on >:")

	add_spec_days = list(set(add_spec_days))	#removes duplicates, just in case
	return add_spec_days

#Function to request additional specific years
def getMoreYears():

	print("""--- Get Additional Specific Years---

 Want to add any other specific years? Simply press enter if not.
 Adding years that are in the future is permitted.

 Only 4 Digit years are allowed.
 Years with fewer digits can be added in "Add Additional Numbers'

 Era (AD, CE, BC, BCE) is not allowed -
 Years with Era must be added in "Add Addtional Words"
 """)
	add_spec_years = [] #list that will be populated with additional years


	#Adding years in the future is allowed here.

	add_spec_year = input("> Enter an additional year here, or simply press enter to move on >:")

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_spec_year) != 0:

		if nonzero_blankspace_reg.match(add_spec_year):  # ensures input isn't only blank space characters
			print (' [-] Empty space, try again.')
			add_spec_year = input("> Enter an additional year here, or simply press enter to move on >:")

		elif not four_digs_reg.match(add_spec_year): # ensures input is limited to 4 digits exactly
			print (' [-] Invalid entry, try again.')
			add_spec_year = input("> Enter an additional year here, or simply press enter to move on >:")


		elif add_spec_year in add_spec_years: # check for double input
			print (' [-] That input has already been added to the list. Some inputs are added automatically, try again')
			add_spec_year = input("> Enter an additional year here, or simply press enter to move on >:")

		else:
			add_spec_years.append(add_spec_year) #if the year is valid, add it to list

		add_spec_year = input("> Enter an additional year here, or simply press enter to move on >:")

	add_spec_years = list(set(add_spec_years))	#removes duplicates, just in case
	return add_spec_years

#Function gets range of years - useful if a main_subject's exact age is not known
def getYearRange():
	print ("""---Range of Years---

 This can be useful if you don't know someone's exact age.
 Note that wordlists are calculated through permutation (nPr),
 Meaning generated wordlists will grow exponentially.
 You might not want to add TOO big a range.
 A range of 5 is recommended
 The next prompt will ask for specific years.
 Years in the future are allowed...
 but it's unlikely someone was born in the future.

 Both start and end years are included.
 Starting year must be *BEFORE* ending year.
	""")

	starting_year = input("> Enter START year in YYYY format, or press enter to move on >:")
	if len(starting_year) ==0: return '' #if no range entered, return null and move on

	valid = False

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(starting_year) !=0 and not valid:

		if nonzero_blankspace_reg.match(starting_year): #rejects inputs of empty space characters
			print (" [-] Empty Space, try again.")
			starting_year = input("> Enter START year in YYYY format, or press enter to move on >:")

		elif not four_digs_reg.match(starting_year): #rejects inputs that do not fit the format
			valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
			print (" [-] Invalid format, try again.")
			starting_year = input("> Enter START year in YYYY format, or press enter to move on >:")

		else: valid = True # if all criteria have been met

	if len(starting_year) ==0: return '' #if no START year entered, move on


	ending_year = input("> Enter END year in YYYY format >:")

	valid = False

	# If the user enters a value, it must meet criteria
	# until all criteria is met, BEWGor will keep asking
	while not valid:

		if nonzero_blankspace_reg.match(ending_year): #rejects inputs of empty space characters
			print (" [-] Empty Space, try again.")
			ending_year = input("> Enter END year in YYYY format >:")

		elif not four_digs_reg.match(ending_year): #rejects inputs that do not fit the format
			valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
			print (" [-] Invalid format, try again.")
			ending_year = input("> Enter END year in YYYY format >:")

		elif ending_year == starting_year: # ensures years are not equal
			print (" [-] Starting and Ending Year cannot be equal. Try again.")
			ending_year = input("> Enter END year in YYYY format >:")

		elif int(ending_year) < int(starting_year): # ensures starting year precedes ending year
			print (" [-] Ending year must be after Starting year. Try again.")
			ending_year = input("> Enter END year in YYYY format >:")

		elif len(ending_year) ==0: # ensures ending year is populated
			print (' [-] Ending year cannot be a null value. Try again')
			ending_year = input("> Enter END year in YYYY format >:")

		elif int(ending_year) - int(starting_year) > 10:
			print (" [-] Using " + ending_year + " as an ending year would result in a range of " + str(int(ending_year) - int(starting_year)) +" years.")
			long_range_choice = input('Do you want to use '+ ending_year + ' as your end year? (Y/N) >:').upper()
			long_range_choice = spaceShaver(long_range_choice) # cleans up input and stops false negative with "yes "

			if long_range_choice not in "YES" and len(long_range_choice) != 0:
				ending_year = input("> Enter END year in YYYY format >:")
			else: valid = True

		else: valid = True

	year_range = []
	for year in range(int(starting_year), int(ending_year)+1):
		year_range.append(str(year))

	return year_range

#Function to request additional misc. words
def getMoreWords():
	print ("""--- Get Additional Words ---

 Want to add any other additional words?
 This is the time to add any information you
 might have that was not asked about previously.
 If you wish to add numbers in HEXIDECIMAL, you must do so here.

 If you are guessing the password for a given domain or purpose,
 consider entering its name here.

 Inputs containing spaces will have variations generated
 that do NOT include spaces.
	""")

	add_words = [] #list that will contain inputted words, or return blank if none are given


	add_word = input("> Enter an additional word here, or simply press enter to move on >:")

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_word) != 0:

		if nonzero_blankspace_reg.match(add_word):  #rejects inputs of just empty space characters
			print (' [-] Empty space, try again.')
			add_word = input("> Enter an additional word here, or simply press enter to move on >:")

		elif add_word in add_words: #rejects inputs that have already been entered
			print (' [-] That input has already been added to the list. \n Some inputs are added automatically. Try again.')
			add_word = input("> Enter an additional word here, or simply press enter to move on >:")

		else:

			if ' ' in add_word: add_words.append(spaceHandler(spaceShaver(add_word)))
			# creates a variants of a string containing spaces
			#but removes trailing spaces

			else:add_words.append(spaceShaver(add_word)) #removes trailing spaces


		add_word = input("> Enter an additional word here, or simply press enter to move on >:")

	add_words = list(set(add_words)) #removes duplicates
	return add_words

#Function to request additional numbers
def getMoreNumbers():
	print ("""--- Get Additional Numbers ---

 Want to add any other specific numbers? Simply press enter if not.
 many people will add simple numbers like '123' to their passwords.
 Others add numbers they find amusing, such as '69' or '420'
 Only digits (0-9) will be accepted
 """)

	add_nums = [] #list that will be populated with additional numbers

	add_num = input("> Enter an additional number, or simply press enter to move on >:")

	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_num) != 0:

		if nonzero_blankspace_reg.match(add_num): #rejects inputs of just empty space characters
			print (' [-] Empty space, try again.')
			add_num = input("> Enter an additional number, or simply press enter to move on >:")

		elif not at_least_one_dig_reg.match(add_num): #rejects inputs that are not only numbers
			print (" [-] Invalid characters, try again.")
			add_num = input("> Enter an additional number, or simply press enter to move on >:")

		elif add_num in add_nums: #rejects inputs that have already been entered
			print (' [-] That input has already been added to the list. Try again.')
			add_num = input("> Enter an additional number, or simply press enter to move on >:")

		else:
			add_nums.append(add_num) #adds number to list if valid

		add_num = input("> Enter an additional number, or simply press enter to move on >:")

	add_nums = list(set(add_nums)) #removes duplicates, just in case
	return add_nums

#Function to Generate possible full birthdates based on a birth_day and a range of years
def getBirthdayRange(birth_day,year_range):
	print (' --- Possible Birthdays --- \n \n')

	#print ("If you did not know " + main_subject.name + "'s birth year, BEWGor")
	print ("If you did not know targets' birth year, BEWGor")
	print (""" could not have generated a full birthdate for your Person.
			Based on the year range you just created and the Person's birthday,
			BEWGor can generate potential full birthdates.
			Birthdays detected as in the future will not be added.
			""")	

	guess_bday_choice = input('> Would you like to do this? (Y/N) >:').upper() # #only determines possible full dates if user allows it

	guess_bday_choice = spaceShaver(guess_bday_choice) # cleans up input and stops false negative with "yes "

	poss_bdays = [] #list to store possible birthdays

	if guess_bday_choice in "YES" and len(guess_bday_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'

		# This block iterates through the list of years, and adds valid birthdays to the list
		# It rejects birthdays that are in the future, or take place on non-existant leap days
		for i in year_range:
			if not isFullDateFuture(birth_day + i) and not isItInvalidLeap(birth_day + i):# ensures dates being added are valid
				poss_bdays.append(birth_day + i) #adds day to list

		#alert user to inclusion of possible birthdays
		#print ("\n [+] Generated and included a full date of '" + (main_subject.birth_day) + "' for years " \
		#	+ poss_bdays[0][4:8] + " through " + poss_bdays[-1][4:8] + ". \n")
		print ("\n [+] Generated and included a full date of '(CHECK)(main_subject.birth_day)' for years " \
			+ poss_bdays[0][4:8] + " through " + poss_bdays[-1][4:8] + ". \n")

	return poss_bdays

#Function to Generate possible Chinese Zodiac Signs based on a range of years
def getChineseZodiacRange(year_range):

	add_CN_zod = [] # list that will hold generated Chinese Zodiac Signs

	print (""" --- Possible Chinese Zodiac Signs ---

 If you did not know the Main Subject's birth year, BEWGor
 could not have determined the Chinese Zodiac Sign for that year.
 Signs can be determined from the list of years you just created.
 Additional prompts may appear to clear up possible translations.
 """)

	more_CN_zod_choice = input('> Would you like to do this? (Y/N) >:').upper() # #only determines/includes these Chinese Zodiac signs if user allows it

	more_CN_zod_choice = spaceShaver(more_CN_zod_choice) # cleans up input and stops false negative with "yes "

	if more_CN_zod_choice in "YES" and len(more_CN_zod_choice) != 0: # if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'

		# This block does NOT reject future years, since the Zodiac signs are periodic.
		# At most, 12 signs (with a few possilbe variants) will be added to the list
		for year in year_range:
			add_CN_zod.append(getChineseZodiac(year)) #gets Chinese Zodiac sign for all the years in the range

	#alert user to inclusion of potential Chinese Zodiac Signs
	print ("\n [+] Determined and included Chinese Zodiac Signs for years "+ year_range[0] + " through " + year_range[-1] + ". \n")
	return add_CN_zod

#Function to strip optional zeroes of dates
#e.g 02/02/2017 -> 2/2/2017
def createNoLeadingZeroDays(daylist):

	no_leading_zero_days = [] #empty list to be filled with days purged of zeroes

	if len(daylist) > 0: #only perform zero purge if there are any days to purge

		#Removes zeroes from days to match potentially different formats
		#I.E if you entered 2 March as "02/03" it will return "23"
		# If you entered 20/03 it will return 203

		for day in daylist: #for all days in list

			if '0' in day[0] or '0' in day[2]: #if leading zeroes present

				nlz_day = day[0:2] #isolate day
				nlz_mon = day[2:4] #isolate month

				if nlz_day[0] == '0': nlz_day = nlz_day[1] # Remove leading zero from day
				if nlz_mon[0] == '0': nlz_mon =nlz_mon[1] # Remove leading zero from month

				no_leading_zero = nlz_day+nlz_mon #combine strings purged of leading zeroes
				no_leading_zero_days.append(no_leading_zero) #add

	return no_leading_zero_days
