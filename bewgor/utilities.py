#!/usr/bin/env python3

from math import factorial #used to calculate permutation length
from datetime import datetime
import time


from .validator import *

#Calculates number of permutations
def nPr(n, r):
	#Implements the mathematical formula for permutations
	if n-r > 0:
		return factorial(n)/factorial(n-r)
	else: return 1
	# nPr = (n!)/(n-r)!

#Creates all possible permutations of a given list
#limits output creating length boundaries
# Write these outputs to a filename passed along
def bounded_permutations(iterable, min_length, max_length, outfile, r=None):
	# NOTE: outfile_name variable isn't used in this function, so replacin outfile_name by outfile

	#This function is a modified version of the function from the Itertools library
	#Check the itertools documentation for standard comments
	#Comments included here are specific to BEWGor's modifications


	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	if r > n: return
	indices = list(range(n))
	cycles = list(range(n, n-r, -1))

	#Measures the string length of the created permutation - and only passes it along if it fits within boundaries
	if min_length <= len(str(''.join((tuple(pool[i] for i in indices[:r]))))) <= max_length:
		#writes permutation to file if it meets criteria
		outfile.writelines((str(''.join(tuple(pool[i] for i in indices[:r])))) + '\n')

	while n:
		for i in reversed(range(r)):
			cycles[i] -= 1
			if cycles[i] == 0:
				indices[i:] = indices[i+1:] + indices[i:i+1]
				cycles[i] = n - i
			else:
				j = cycles[i]
				indices[i], indices[-j] = indices[-j], indices[i]

				#Measures the string length of the created permutation - and only passes it along if it fits within boundaries
				if min_length <= len(str(''.join((tuple(pool[i] for i in indices[:r]))))) <= max_length:
					#writes permutation to file if it meets criteria
					outfile.writelines((str(''.join(tuple(pool[i] for i in indices[:r])))) + '\n')
				break
		else: return


#prints a fixed-width divider made of '---'
def divider():
	print('---------------------------------------------------------------')

# Pause, press enter to coninue
def hold_up():
	#This variable is never used, it is just a pause placeholder
	#It does not persist after unpausing
	holdup = input('Press enter to continue...')

def isYearFuture(year):
	date_format = "%Y" #sets 'YYYY" format
	now = time.strftime(date_format) #current year in YYYY

	# create datetime objects from the strings
	year_val = datetime.strptime(year, date_format) # generate value for given year
	now_val = datetime.strptime(now, date_format) # generate value for present year

	if now_val < year_val: #if given year is in the future
		return True #year is in the future
	else:
		return False #year is in past or present

# Function that checks if a date 'DDMMYYYY' is in the future
def isFullDateFuture(event_date):
	#This function is only equipped to handle strings of exactly 8 digits.
	#It assumes your

	date_format = "%d%m%Y" #sets 'DDMMYYYY" format
	now_date = time.strftime(date_format) #current date in DDMMYYYY

	# create datetime objects from the strings
	event_val = datetime.strptime(event_date, date_format) # generate value for given date
	now_val = datetime.strptime(now_date, date_format) # generate value for present date

	if now_val < event_val: #if given date is in the future
		return True #event is in the future
	else:
		return False #event is in past or present

#Function to check if day 'DDMM' exists
def doesDayExist(day):

	#if a passed string of 4 digits is on the list of nonexistent days,
	#this function returns false.
	#If a date is created that claims to be on the 32nd+ day of a month
	# This is caught elsewhere, before this function is called

	unreal_days = ['3002','3102','3104','3106','3109','3111']
	# 30 and 31 Feb
	# 31 April
	# 31 June
	# 31 September
	# 31 November
	#These days do not exist, and should not be allowed

	if day in unreal_days: return False # if one of the non-existant days
	else: return True

#Function to check if given day is valid leap day
def isItInvalidLeap(full_date):

	# This will return false for any day that isn't 29 Feb, or 29 Feb of a leap year
	# It will only return true for 29 Feb for a Non-Leap year

	if full_date[0:4] == '2902': # if 29 February

		if  (int(full_date[4:8]) - 2016) % 4 == 0: # checks to see if given year has Leap Day
			# 2016 was a leap year, and any year that is separate from 2016 by a multple of 4
			# is also a leap year

			return False #if not a leap year

		else: return True #if a date is 29 Feb of a non-leap year

	else: return False #if not 29 Feb

# Generates Chinese Zodiac sign for a given year
# This function is not integrated into a class because it can
# also be used on a list of arbitrary years
def getChineseZodiac(birth_year):

	birthyear =int(birth_year) #converts from string so modulo can be used

		#The Chinese Zodiac has 12 Signs, and therefore repeats every 12 years.
		#If a given year is separated by one of the landmark years given below by a multiple of 12, the signs for those two years are equal
		# 2017 and 2002 are both years of the rooster. 2017 and 1897 are both years of the rooster


	if ((birthyear - 2008) % 12) == 0: chinese_zodiac = "rat"
	elif ((birthyear - 2009) % 12) == 0: chinese_zodiac = "ox"
	elif ((birthyear - 2010) % 12) == 0: chinese_zodiac = "tiger"
	elif ((birthyear - 2011) % 12) == 0: chinese_zodiac = "rabbit"
	elif ((birthyear - 2012) % 12) == 0: chinese_zodiac = "dragon"
	elif ((birthyear - 2013) % 12) == 0: chinese_zodiac = "snake"
	elif ((birthyear - 2014) % 12) == 0: chinese_zodiac = "horse"
	elif ((birthyear - 2015) % 12) == 0: chinese_zodiac = "goat"
	elif ((birthyear - 2016) % 12) == 0: chinese_zodiac = "monkey"
	elif ((birthyear - 2017) % 12) == 0: chinese_zodiac = "rooster"
	elif ((birthyear - 2018) % 12) == 0: chinese_zodiac = "dog"
	else: chinese_zodiac = "pig"

	# Some signs can have multiple names, so BEWGor will prompt the user for their choice

	# Years of the Rat may also be called Years of the Mouse, as there may be no easy distinction between the two in Chinese
	if chinese_zodiac == "rat":
		print ("\n The Chinese Zodiac sign for the year " + birth_year +" is the '" + chinese_zodiac.title() +"'")
		print (" This sign is usually called the Rat, but occaisionally it is called the Mouse.")
		print (' Which would you like to use? 1 - Rat, 2 - Mouse, 3 - Both') # user chooses which value
		zodiac_choice = input("> Enter the number of your choice here >:")

		#If user inputs a choice not on the list of provided choices, the process repeats until they do.
		while zodiac_choice !=str(1) and  zodiac_choice !=str(2) and zodiac_choice !=str(3): #Checks for valid choice
			print (" [-] Invalid choice, try again.")
			print (" This sign is usually called the Rat, but occaisionally it is called the Mouse.")
			print (' Which would you like to use? 1 - Rat, 2 - Mouse, 3 - Both') #user chooses which value

			if zodiac_choice == str(1):chinese_zodiac = "rat"
			if zodiac_choice == str(2):chinese_zodiac = "mouse"
			if zodiac_choice == str(3):chinese_zodiac = "mouse rat"

	# Years of the Goat may also be called Years of the Sheep or Ram - there is less distinction between these animals in Chinese
	elif chinese_zodiac == "goat":
		print ("\n The Chinese Zodiac sign for the year " + birth_year +" is the '" + chinese_zodiac.title() +"'")
		print (" This sign is often called the Ram or Sheep as well as the Goat.")
		print (" Which would you like to use? 1 - Goat, 2 - Ram, 3 - Sheep, 4 - All Three") #user chooses which value

		zodiac_choice = input("> Enter the number of your choice here >:")

		#If user inputs a choice not on the list of provided choices, the process repeats until they do.
		while zodiac_choice !=str(1) and  zodiac_choice !=str(2) and zodiac_choice !=str(3) and zodiac_choice != str(4): #Checks for valid choice
			print (" [-] Invalid choice, try again.")
			print (" This sign is often called the Ram or Sheep as well as the Goat.")
			print (" Which would you like to use? 1 - Goat, 2 - Ram, 3 - Sheep, 4 - All Three") #user chooses which value
			zodiac_choice = input("> Enter the number of your choice here >:")

			if zodiac_choice == str(1): chinese_zodiac = "goat"
			if zodiac_choice == str(2): chinese_zodiac = "ram"
			if zodiac_choice == str(3): chinese_zodiac = "sheep"
			if zodiac_choice == str(4): chinese_zodiac = "goat ram sheep"

	# Years of the Pig may be called years of the Boar, but this translation is rare
	elif chinese_zodiac == "pig":
		print ("\n The Chinese Zodiac sign for the year " + birth_year +" is the '" + chinese_zodiac.title() +"'")
		print (" This sign is usually called the Pig, but rarely it is called the Boar.") #user chooses which value
		print (' Which would you like to use? 1 - Pig, 2 - Boar, 3 - Both ') #user chooses which value
		zodiac_choice = input("> Enter the number of your choice here >:")

		#If user inputs a choice not on the list of provided choices, the process repeats until they do.
		while zodiac_choice !=str(1) and  zodiac_choice !=str(2) and zodiac_choice !=str(3): #Checks for valid choice
			print (" [-] Invalid choice, try again.")
			print (" This sign is usually called the Pig, but rarely it is called the Boar.")
			print (' Which would you like to use? 1 - Pig, 2 - Boar, 3 - Both ') #user chooses which value
			zodiac_choice = input("> Enter the number of your choice here >:")

			if zodiac_choice == str(1):chinese_zodiac = "pig"
			if zodiac_choice == str(2):chinese_zodiac = "boar"
			if zodiac_choice == str(3):chinese_zodiac = "pig boar"

	return chinese_zodiac

#Function that takes a string that contains spaces and creates variations
# also handles TitleCase variants of phrases containing the world 'of'
def spaceHandler(phrase):

	if ' ' in phrase: #if a phrase contains spaces, split it up so BEWGor can join the words together with variations

		phrase = phrase.title() #make first letter of every word capital, including "Of"
		#This changes the user's input, but later on in the script, varitaions will be created, such as all upper or lowercase

		in_phrases = [phrase] #put the phrase on to a list that will be expanded and iterated over if a phrase contains 'Of'

		out_phrases = [] #list that will hold generated variations

		#This block addresses possibile capitalization of the word 'of'
		# In TitleCase, 'of' does not conventially have a capital 'O'
		# However, this is not always done consistently.
		# BEWGor creates variations where of is and isn't in TitleCase
		if len(space_of_space_reg.findall(phrase)) > 0: in_phrases.append(phrase.replace(' Of ', ' of ')) #if ' Of ' in string, created variations

		for item in in_phrases: # for all variations

			space_breakup = item.split(' ') #breakup by space

			#Rejoin by other phrases
			out_phrases.append('_'.join(space_breakup)) #creates variation joined by underscores - 'Some_Words'
			out_phrases.append('-'.join(space_breakup)) #creates variation joined by dashes - 'Some-Words'
			out_phrases.append(''.join(space_breakup)) #creates variation joined directly - 'SomeWords'
			out_phrases.extend(space_breakup) #adds indivudual words to the list indepedently, 'Some' and 'Words'

		return list(set(out_phrases)) #returns all variations and words extracted, after removing duplicates
	else: return phrase #if phrase did not have a space, return phrase as is

#Function that takes spaces off the end of a string
def spaceShaver(phrase):

	while len(ends_in_space_reg.findall(phrase)) > 0: #if the name ends in spaces...
				phrase = phrase[0:-1] #keep removing characters from the string until it doesn't end in a space

	return phrase


# This feature will be expanded upon after Initial release
# The plan is to generate a specially formatted file that can be
# created to and then fed into this program directly instead of going prompt by prompt
# ALPHA RELEASE FUNCTION - outputs all entered values to a file.
def outputTerms(term_list):

	print("""\n ---------- Output 'Terms' to a File --------

 All values have been entered, BEWGor can save them directly to a txt file.""")

	term_write_choice = input('> Would you like to do this? (Y/N) >:').upper() #prompts user for choice
	term_write_choice = spaceShaver(term_write_choice)

	if term_write_choice in "YES" and len(term_write_choice) != 0:

		print(' If you do not enter a filename, the default will be "BEWGor_Terms.txt')
		outfile_name = input('> Enter a filename, without the ".txt" extension >:')

		# If the inputted filename is non-zero in length, but contains unfriendly characters
		# Sometimes filenames containing characters like spaces () " ' {} can cause problems
		# The regex forces the filename to exculde these characters

		while len(outfile_name) !=0 and not filename_reg.match(outfile_name):
			print(' [-] Invalid filename, try again.')
			outfile_name = input("> Enter a filename, without the .txt extension >:")


		if len(outfile_name) ==0 : outfile_name = 'BEWGor_Terms'

		outfile = open(outfile_name+'.txt','w+') #opens file to be written
		outfile.truncate() # ensures file is empty

		term_list.sort(key=len) # sort by length
		term_list = list(set(term_list)) #removes duplicates

		for item in term_list: #write every line to file
			outfile.writelines(item + '\n') #write to file

		divider()

		#announces that the Terms file has been written and its length
		print('\n ' + str(len(term_list)) + ' terms written to ' + outfile_name + '.txt')
