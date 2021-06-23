#usr/bin/env python3
#General class for the people mentioned in the prompt
#Parent class of MAINSUBJECT

from .utilities import *
from .validator import *

class Person(object): #This class allows us to easily add and store information for an aribitrary number of people

	#Initialize Person Class and variables
	def __init__(self,name,maiden_name,initials,nicknames,birth_day,birth_year,greek_zodiac,chinese_zodiac,Birthstone):
		self.name=name
		self.maiden_name = maiden_name
		self.initials = initials
		self.nicknames = nicknames
		self.birth_day = birth_day
		self.birth_year=birth_year
		self.greek_zodiac = greek_zodiac
		self.chinese_zodiac = chinese_zodiac
		self.Birthstone = Birthstone

	#Person Class Function that requests Person's Name
	def getName(self):

		self.initials = '' #defined as empty, in case name is not generated -> this would confused the program later on

		person_name = input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()
		if len(person_name) == 0: valid = True
		else: valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_name) !=0 and not valid:
		# the 'valid' boolean keeps us from getting stuck in an infinite loop here if the user decides to enter an empty field after
		# being told their first input was invalid

			if nonzero_blankspace_reg.match(person_name): #ensures input isn't only blank space characters
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Empty Space, try again.")
				person_name = input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()


			elif not letters_and_spaces_reg.match(person_name):
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Input contains non-letter characters, try again.")
				person_name = input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()

			else: valid = True #if the name input is valid, continue

		person_name = spaceShaver(person_name) # removes spaces from end of name

		if len(person_name) != 0: #if name is entered, BEWGor sets the person's name to the entry.
			#If name is NOT entered, then  BEWGor uses the temporary value passed in construction of the Person instance.

			self.name = person_name  #set class variable to input value

			# if name is given, this block extracts the person's Initials.
			initials = ""
			for i in self.name.title(): #set first letter of each part of name to be capital
				if i.isupper(): initials += i  #if letter is capital, add to initials string

			self.initials = initials.upper() #ensure that initials are upper and add to instance variables

	#Class Function that requests Person's Maiden Name
	def getMaidenName(self):
		person_maiden_name = input("> Enter " + self.name +"'s Maiden Name - if applicable >:").title()

		# The 'valid' boolean is true if the name value is empty or meets the correct criteria
		if len(person_maiden_name) == 0: valid = True
		else: valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_maiden_name) !=0 and not valid:
		# the 'valid' boolean keeps us from getting stuck in an infinite loop here if the user decides to enter an empty field after
		# being told their first input was invalid

			if nonzero_blankspace_reg.match(person_maiden_name): #ensures input isn't only blank space characters
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Empty Space, try again.")
				person_maiden_name = input("> Enter " + self.name +"'s Maiden Name, separated by spaces - if applicable >:").title()

			elif not letters_and_spaces_reg.match(person_maiden_name): #checks to see if value contains improper characters
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Input contains non-letter characters, try again.")
				person_maiden_name = input("> Enter " + self.name + "'s Maiden Name, separated by spaces - if applicable >:").title()

			else: valid = True

		self.maiden_name = spaceShaver(person_maiden_name) #remove spaces from end of name

	# Person Class Function that requests Nicknames
	def getNicknames(self):
		print (""" For nicknames, think about common name shortenings,
 such as 'Michael' into 'Mike'
 Also enter usernames and online handles.
 """)

		nicknames =[] #list that will contain inputted nicknames, or return blank if none are given
		entered = []

		nickname = input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(nickname) != 0: #if no nicknames added, move on.

			if nonzero_blankspace_reg.match(nickname): #ensures input isn't only blank space characters
				nickname = input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")

			elif nickname in nicknames or nickname in entered: #check for double input
				print (" [-] That input has already been entered. Try again >:")
				nickname = input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")

			elif ' ' in nickname:
				nicknames.extend((spaceHandler(nickname))) #create variants of input if input contains spaces
				entered.append(nickname) #adds to 'entered' list to prevent double-adds


			else:
				nicknames.append(nickname) #adds input to list if valid
				entered.append(nickname) # adds to 'entered" list to prevent double-adds

			nickname = input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")

		nicknames=list(set(nicknames)) #remove duplicates
		self.nicknames = ' '.join(nicknames)

	#Person Class Function that requests Birth day (no year)
	def getBirthday(self):
		print(' Be Aware BEWGor uses DDMM formatting!\n Winter Solstice falls on  21/12, 22/12, or 23/12 in this format.')
		person_birth_day = input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

		valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_birth_day) !=0 and not valid:
		# the 'valid' boolean keeps us from getting stuck in an infinite loop here if the user decides to enter an empty field after
		# being told their first input was invalid

			if not four_digs_reg.match(person_birth_day): #ensures input is four digits exactly, nothing else
				print (" [-] Days must be exactly 4 digits")
				person_birth_day = input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			elif int(person_birth_day[2:4]) > 12: #checks for an invalid month
				print (" [-] Invalid month- After December, but before January - check your DDMM format")
				person_birth_day = input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			elif int(person_birth_day[0:2]) > 31: #checks for an invalid day
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				person_birth_day = input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			elif not doesDayExist(person_birth_day): #ensures day exists
				print (" [-] Invalid date. That month has fewer days. Try again.")
				valid = False
				person_birth_day = input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			else: valid = True #all criteria have been met

		self.birth_day = person_birth_day #change value to entry - including to a null value if nothing is entered

	#Person Class Function that requests birth YEAR
	def getBirthyear(self):
		person_birth_year = input("> Enter " + self.name +"'s Birth year (YYYY) >:")

		valid = False
		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_birth_year) !=0 and not valid:

			if not four_digs_reg.match(person_birth_year): #ensures input is four digits exactly, nothing else
				print (" [-] Birth years must be exactly 4 digits, try again.")
				person_birth_year = input("> Enter " + self.name +"'s Birth year (YYYY) >:")


			elif isYearFuture(person_birth_year): #ensures user does not enter a year in the future
				print (" [-] That year is in the future, try again.")
				person_birth_year = input("> Enter " + self.name +"'s Birth year (YYYY) >:")


			else: valid = True #if all criteria have been met

		self.birth_year = person_birth_year #change value to entry - including to a null value if nothing is entered

	#Person Class Function that determines Greek Zodiac Sign (Mythological/Traditional) from birthday
	def getGreekZodiac(self):

		greek_zodiac = '' #sets a null value, so if user doesn't want to include this value, BEWGor can pass an empty value


		incl_Greek_Zod = input("Would you like to include " + self.name + "'s Greek Zodiac Sign? (Y/N) >:").upper() #only determines/includes Greek Zodiac sign if user allows it

		incl_Greek_Zod = spaceShaver(incl_Greek_Zod) # cleans up input and stops false negative with "yes "

		if incl_Greek_Zod in "YES" and len(incl_Greek_Zod) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'

	# Greek Zodiac Signs:
	 #Aquarius:    20 January (01) - 18 February (02)
	 #Pisces:      19 February (02) - 20 March (03)
	 #Aries:       21 March (03) - 19 April (04)
	 #Taurus:      20 April (04) - 20 May (05)
	 #Gemini:      21 May (05) - 20 June (06)
	 #Cancer:      21 June (06) - 22 July (07)
	 #Leo:         23 July (07) - 22 August (08)
	 #Virgo:       23 August (08) - 22 September (09)
	 #Libra:       23 September (09) - 22 October (10)
	 #Scorpio:     23 October (10) - 21 November (11)
	 #Sagittarius: 22 November (11) - 21 December (12)
	 #Capricorn:   22 December (12) - 19 January (01)

			birthmonth = self.birth_day[2:4] #isolate the month from the birthday
			birth_day = int(self.birth_day[0:2]) # isolate the day from the birthday, convert to int for comparison

			# Corresponding dates for January
			if birthmonth == ('01'):
				if birth_day <= 19: greek_zodiac = 'capricorn'
				else: greek_zodiac = 'aquarius'

			# Corresponding dates for February
			elif birthmonth == ('02'):
				if birth_day <= 18: greek_zodiac = 'aquarius'
				else: greek_zodiac = 'pisces'

			# Corresponding dates for March
			elif birthmonth == ('03'):
				if birth_day <= 20: greek_zodiac = 'pisces'
				else: greek_zodiac = 'aries'

			# Corresponding dates for April
			elif birthmonth == ('04'):
				if birth_day <= 19: greek_zodiac = 'aries'
				else: greek_zodiac = 'taurus'

			# Corresponding dates for May
			elif birthmonth == ('05'):
				if birth_day <= 20: greek_zodiac = 'taurus'
				else: greek_zodiac = 'gemini'

			# Corresponding dates for June
			elif birthmonth == ('06'):
				if birth_day <= 20: greek_zodiac = 'gemini'
				else: greek_zodiac = 'cancer'

			# Corresponding dates for July
			elif birthmonth == ('07'):
				if birth_day <= 22: greek_zodiac = 'cancer'
				else: greek_zodiac = 'leo'

			# Corresponding dates for August
			elif birthmonth == ('08'):
				if birth_day <= 22: greek_zodiac = 'leo'
				else: greek_zodiac = 'virgo'

			# Corresponding dates for September
			elif birthmonth == ('09'):
				if birth_day <= 22: greek_zodiac = 'virgo'
				else: greek_zodiac = 'libra'

			# Corresponding dates for October
			elif birthmonth == ('10'):
				if birth_day <= 22: greek_zodiac = 'libra'
				else: greek_zodiac = 'scorpio'

			# Corresponding dates for November
			elif birthmonth == ('11'):
				if birth_day <= 21: greek_zodiac = 'scorpio'
				else: greek_zodiac = 'sagittarius'

			# Corresponding dates for December
			else:
				if birth_day <= 21: greek_zodiac = 'sagittarius'
				else: greek_zodiac = 'capricorn'

			print ("\n [+] Recorded " + self.name + "'s Greek Zodiac sign as '" + greek_zodiac.title() +"' \n") #alert user to inclusion of Greek Zodiac

		self.greek_zodiac = greek_zodiac #change value to entry - including to a null value if nothing is entered

	#Person Class Function that determines Birthstone (Mythological/Traditional) from birth month
	def getBirthstone(self):

		# Birthstones are an old tradition in that (in the West) may be associated with the signs of the Zodiac.
		# They are highly popular in some parts of the world, but nearly unheard of in others.
		# If your Subject is into astrology or New Age belief, this could be of great importance to them
		# It also might mean they are vulnerable to social engineering and cold reading often practiced by 'psychics'

		Birthstone = '' #sets a null value, so if user doesn't want to include this value, BEWGor can pass an empty value

		incl_Birthstone = input("Would you like to include " + self.name + "'s Birthstone (Y/N) >:").upper()  #only determines/includes Birthstone if user allows it

		incl_Birthstone = spaceShaver(incl_Birthstone) # cleans up input and stops false negative with "yes "

		if incl_Birthstone in "YES" and len(incl_Birthstone) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'#only take action if user requests it
		#if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'

			birthmonth = self.birth_day[2:4] #isolate birth month

			print ("\n Is " + self.name + " more likely to use a Birthstone from a Western or Hindu list?") #there are multiple lists of Birthstones, two are included
			stone_choice = input("> Enter 1 for Western, 2 for Hindu, or 3 to use both >:")

			#If user inputs a choice not on the list of provided choices, the process repeats until they do.
			while stone_choice !=str(1) and  stone_choice !=str(2) and stone_choice != str(3):
				print (' [-] Invalid choice, try again.')
				print (" Is " + self.name + " more likely to use a Birthstone from a Western or Hindu list?")
				stone_choice = input("> Enter 1 for Western, 2 for Hindu, or 3 to use both >:")

			if stone_choice == str(1): #if user requests a Western list
				western_dict = {'01' :'garnet', '02' :'amethyst', '03' :'aquamarine', '04' :'diamond', '05' :'emerald', '06' :'pearl', '07' :'ruby', '08' :'peridol', '09' :'sapphire', '10' :'opal', '11' :'topaz', '12' :'turquoise'}
				Birthstone = str(western_dict.get(birthmonth)).lower()

			elif stone_choice == str(2): #if user requests a Hindu list
				hindu_dict = {'01' :'serpent-stone', '02' :'chandrakanta', '03' :'siva-linga', '04' :'diamond', '05' :'emerald', '06' :'pearl', '07' :'sapphire', '08' :'ruby', '09' :'zircon', '10' :'coral', '11' :'cats-eye', '12' :'topaz'}
				Birthstone = str(hindu_dict.get(birthmonth)).lower()

			elif stone_choice == str(3): #if user requests both lists
				western_dict = {'01' :'garnet', '02' :'amethyst', '03' :'aquamarine', '04' :'diamond', '05' :'emerald', '06' :'pearl', '07' :'ruby', '08' :'peridol', '09' :'sapphire', '10' :'opal', '11' :'topaz', '12' :'turquoise'}
				hindu_dict = {'01' :'serpent-stone', '02' :'chandrakanta', '03' :'siva-linga', '04' :'diamond', '05' :'emerald', '06' :'pearl', '07' :'sapphire', '08' :'ruby', '09' :'zircon', '10' :'coral', '11' :'cats-eye', '12' :'topaz'}

				if western_dict.get(birthmonth) != hindu_dict.get(birthmonth): # include both dictionaries if stones aren't the same
					Birthstone = (str(western_dict.get(birthmonth)).lower() + " " + (str(hindu_dict.get(birthmonth)).lower()))
				else: Birthstone = str(western_dict.get(birthmonth)).lower() # if the stones are the same, use just one list

			print ("\n [+] Recorded " + self.name + "'s Birthstone as '" + Birthstone.title() +"' \n") #alert user to inclusion of Birthstone word


		self.Birthstone= Birthstone #change value to entry - including to a null value if nothing is entered

	#Person Class function that determines Chinese Zodiac Sign (Mythological) from birth year
	def getPersonChineseZodiac(self):

		# This traditional Zodiac is still quite popular in parts of Asia.
		# According to Wikipedia, it is based on an approximation of the 11.86 year oribit of the planet Jupiter
		# The form BEWGor uses is derived from the Chinese variation, which is the most popular, especially in the West
		# However, there are variations that have slight differences
		# Vietnamese, Thai, and some Turkic peoples (Like Khazars) use variants of the Chinese Zodiac
		# Check https://en.wikipedia.org/wiki/Chinese_zodiac#Chinese_zodiac_in_other_countries to see if your Subject may use a different list
		# If that is the case, you may input their terms in the "Additional Words" prompt

		self.chinese_zodiac = '' # sets a null value, so if user doesn't want to include this value, BEWGor can pass an empty value

		if len (self.birth_year) == 4: # Chinese Zodiac sign can only be determined if a birth year is given

			incl_Chinese_Zod = input("Would you like to include " + self.name + "'s Chinese Zodiac Sign? (Y/N) >:").upper() #only determines/includes Chinese Zodiac sign if user allows it

			incl_Chinese_Zod = spaceShaver(incl_Chinese_Zod) # cleans up input and stops false negative with "yes "

			if incl_Chinese_Zod in "YES" and len(incl_Chinese_Zod) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'#if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
				self.chinese_zodiac = getChineseZodiac(self.birth_year)
				print ("\n [+] Recorded " + self.name + "'s Chinese Zodiac sign as the '" + self.chinese_zodiac.title() +"'\n") #alert user to inclusion of Chinese Zodiac

	#Person Class Function that requests info about given person
	def inputInfo(self):

		#Dividers are included to clean up the input process
		#functions are called to collect information from the User
		divider()
		self.getName()
		divider()
		self.getMaidenName()
		divider()
		self.getNicknames()
		divider()
		self.getBirthday()
		divider()
		self.getBirthyear()

		# The following block ensures the entered birthday is in the present or past - if the full date is known
		valid = False # this boolean causes the while loop to run until a vaild birthdate is entered
		while len(self.birth_day) != 0 and len(self.birth_year) !=0 and not valid:

			full_birthday = self.birth_day + self.birth_year  #creates a full birth date out of birthday and birthyear

			if isItInvalidLeap(full_birthday): # if a given birth date takes place on leap day, it must be verified that date existed in the given year
				print (" [-] That day did not take place that year. Try again. \n")

				#if the given year did not have a leap day, the birthday must be verified
				self.getBirthday()
				divider()
				self.getBirthyear()
				divider()


			#If a given birth date is in the future, the User has made an error.
			# Either the inputted date is invalid, or the User as the ability to time travel and shouldn't have to bother using BEWGor.
			elif isFullDateFuture(full_birthday):
				print (" [-] You have selected a birthday in the future, that can't be right. \n")

				# Verify birthday as in the past
				self.getBirthday()
				divider()
				self.getBirthyear()


			else: valid = True


		#if valid birthday is present, acquire associated mythology - if the user wishes
		if len(self.birth_day) != 0:
			divider()
			self.getGreekZodiac()
			divider()
			self.getBirthstone()
		else:
			self.greek_zodiac = ''
			self.Birthstone = ''

		if len(self.birth_year) != 0:
			divider()
			self.getPersonChineseZodiac()
		else:
			self.chinese_zodiac = ''

	#Person Class Function that outputs important numbers
	def outputWords(self):

		word_output = [] #list that will be filled with output words

		#This condition prevents default titles used in class Construction from being used in wordlist generation
		# If the user knows a person exists, but cannot provide a specific name
		#This condition prevents BEWGor from using 'Child_Number_1' on the wordlist
		name_cond = 'Significant_Other' not in self.name and 'Child_Number_' not in self.name and 'Sibling_Number_' not in self.name and "Pet_Number_" not in self.name and "Parent_Number_" not in self.name

		#Some of the length checks, particularly the lines that include "extend" may be redundant - but they are left in for robustness
		#You know how coding is - 'That line doesn't seem to do anything, I'll delete it. Why doesn't it work anymore?'

		if len(self.name) != 0 and name_cond : word_output.extend(((self.name).lower()).split(' ')) # add Person's Name, if valid, broken up by spaces
		if len(self.initials) != 0 : word_output.append(self.initials) # add Person's initials, which have been generated automatically
		if len(self.maiden_name) != 0: word_output.append((self.maiden_name).lower()) # add Person's maiden name, assumed to not have spaces
		if len(self.nicknames) != 0: word_output.extend(((self.nicknames).lower()).split(' ')) # add person's nicknames, if present, broken up by spaces
		if len(self.greek_zodiac) != 0: word_output.append((self.greek_zodiac).lower()) # add greek zodiac sign if present
		if len(self.Birthstone) != 0: word_output.extend((self.Birthstone).lower().split(' ')) # add Birthstone(s) if present
		if len(self.chinese_zodiac) != 0:word_output.extend((self.chinese_zodiac).lower().split(' ')) # add chinese zodiac if present

		return word_output

	#Person Class Function that outputs important Days
	def outputDays(self):
		#ALPHA RELEASE - the flat 'person' class only has one important day.
		# future releases will have relationship specific days such as 'anniversary'

		day_output = []
		if len(self.birth_day) != 0: day_output.append(self.birth_day)

		return day_output

	#Person Class Function that outpus important Years
	def outputYears(self):
		#ALPHA RELEASE - the flat 'person' class only has one important year.
		# future releases will have relationship specific years

		year_output = []
		if len(self.birth_year) != 0: year_output.append(self.birth_year)

		return year_output

	#Person class function that outputs important full dates
	def outputFullDates(self):

		#ALPHA RELEASE - the flat 'person' class only has one important full date
		# future releases will have relationship specific full dates such as 'anniversary'

		full_date_output=[]

		full_birthday = self.birth_day + self.birth_year

		if len(full_birthday) == 8: full_date_output.append(full_birthday)  #if both birth_day and birth_year are present, add combination to list

		return full_date_output
