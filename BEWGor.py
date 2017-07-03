#usr/bin/python
#
#                                    .`
#                                     /
#                                    :.
#                                   `o
#                                   +.
#                                  .s
#                                  y.
#                                 ++
#                                -h`
#                               `d-
#                               h+
#                              ss
#                             sh`
#                            sh`
#                          `yh`
#                         .hy`
#                        /mo`
#                      .sd:
#                    `/dy.
#                   :hd:
#                 -ym+`
#               -yms.
#             .smy-
#           `omh-                                  ``````
#          /md/                                      ```.-:-.
#        .yNo`                                             .-/:`
#       /md-                                                  -+/
#      oNy`                                                     /s`
#     sMs`                                                       :y`
#    +My                                                          y+
#   -Nm`                                                          :d
#   yM+                                                           /d
#  `NM`                                                           d+
#  `MM                                                           od`
#   mM.                                                        `sd.
#   sMs                               ````````               `/ds`
#   `dM/                        ``-+shhmmmmmdhyso/-```````.:ohy-
#    .mN+`                  `./shmmddhysssyyys/:/ohmdhyyyhhs/`
#     `yNh:`            `./sdmy+-oyyy/.```-oyyy-  `yyy..`
#       -yNds/.````.-/oydNmdh:  .yyy: `yh/  syyo   oyy.
#         ./sdmmmmmmmhs+-`+yy:  .yyy/`+ds: `syyo   oyy.
#              ````       -yyo   /yyshy.`.:syys.  .yys
#                          +yy+   :ymhyyyyyyy+`  .syy-
#                           +yyo..ho.:/+++/-`   :yyy-
#                            -syym+`        `./syy+`
#                             -dyyyyso+//++oyyys/.
#                          `+hm: `-/+ossssso/:.
#                          :sd+`
#                            .
#   ____    ______  __          __   _____
#   |  _ \  |  ____| \ \        / /  / ____|
#   | |_) | | |__     \ \  /\  / /  | |  __    ___    _ __
#   |  _ <  |  __|     \ \/  \/ /   | | |_ |  / _ \  | '__|
#   | |_) | | |____     \  /\  /    | |__| | | (_) | | |
#   |____/  |______|     \/  \/      \_____|  \___/  |_|
#
#
#    ___          _   _   _          ___
#   | _ )  _  _  | | | | ( )  ___   | __|  _  _   ___
#   | _ \ | || | | | | | |/  (_-<   | _|  | || | / -_)
#   |___/  \_,_| |_| |_|     /__/   |___|  \_, | \___|
#   __      __                 _   _   _   |__/ _
#   \ \    / /  ___   _ _   __| | | | (_)  ___ | |_
#    \ \/\/ /  / _ \ | '_| / _` | | | | | (_-< |  _|
#     \_/\_/   \___/ |_|   \__,_| |_| |_| /__/  \__|
#    / __|  ___   _ _    ___   _ _   __ _  | |_   ___   _ _
#   | (_ | / -_) | ' \  / -_) | '_| / _` | |  _| / _ \ | '_|
#    \___| \___| |_||_| \___| |_|   \__,_|  \__| \___/ |_|
#
#
#
# 	Bull's Eye Wordlist Generator
#	BEWGor (pronounced Booger)
#
#  Inspired by and based on
#  CUPP 3.1.0-alpha
#  Common User Passnumbers Profiler
#  Located at *** https://github.com/Mebus/cupp ***
#
#  [Author]
#
#  berzerk0 @ GitHub with Major Thanks to...
#
#  Muris Kurgas aka j0rgan
#  j0rgan [at] remote-exploit [dot] org
#  http://www.remote-exploit.org
#  http://www.azuzi.me
#
#  ADDITIONAL THANKS TO:
#
#  Willem Rebergen
#  Michael Omari
#  Kenth Kvein and Marcus Nordli
#  Ramon Luis Ayala Rodriguez
#  Lee McCormick
#  Amelia and the rest of the Jax Crew
#  Dominic 'TB' Peroso
#  and Nick McGurk
#
#
# [DISCLAIMER]
#
# Any and all actions taken with this software are for LAWFUL, ETHICAL AND EDUCATIONAL PURPOSES ONLY.
# By using this software, you agree to not hold either berzerk0, GitHub or Muris Kurgas
# responsible for your actions.
# By using this you agree to these terms and are completely culpable for your own behavior.
#
#
# [LICENSE]
# This software is licensed under the GNU General Public License Version 3
# 
# The Full Text of this license can be found at *** https://www.gnu.org/licenses/gpl-3.0.en.html ***
# A summarized, bullet point list of the license is presented below

# PERMISSIONS
#    Commercial use
#    Modification
#    Distribution
#    Patent use
#    Private use

# CONDITIONS

#    License and copyright notice
#    State changes
#    Disclose source
#    Same license

# LIMITATIONS

#    Liability
#    Warranty


#------------------------Beginning of Actual Code------------------------#


#-----------Class, Function and Regex Definitions----------#

#import necessary libraries
import re, sys, time #re for regular expression use, sys for argument passing, time for determining when an event occured
from datetime import datetime # datetime in order to determine when an event occurred
from math import factorial #used to calculate permutation length


#----------Regular expressions to be used later to check for valid inputs---------#
four_digs_reg = re.compile("^[0-9]{4}$") #exactly 4 digits, no spaces
eight_digs_reg = re.compile("^[0-9]{8}$") #exactly 8 digits, no spaces
at_least_one_dig_reg = re.compile("^[0-9]+$") #at least one number, nothing else
nonzero_blankspace_reg = re.compile("^\s+$") #all empty spaces
letters_and_spaces_reg = re.compile('^[a-zA-Z  \-]+$') #ensures a line only contains letters and spaces, supports hyphens (for names)
location_chars_reg = re.compile('[a-zA-Z\'\. ]') #matches only characters I predict would be found in a location's name
male_reg = re.compile('\s*[Mm][Aa][Ll][Ee]\s*') #matches all variations of the word 'male'
female_reg = re.compile('\s*[Ff][Ee][Mm][Aa][Ll][Ee]\s*') #matches all variations of the word 'female'
ends_in_space_reg = re.compile('\s+$') #matches strings with a space at the end - used to trim off this sapce
space_of_space_reg = re.compile('\s+[Oo]f\s+') #matches strings containing ' of ' or ' Of ' - a unique TitleCase rule
filename_reg = re.compile('^[a-zA-Z0-9\-_]+$') #forces  a friendly filename



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
def bounded_permutations(iterable, min_length, max_length, outfile_name, r=None):
	
	#This function is a modified version of the function from the Itertools library
	#Check the itertools documentation for standard comments
	#Comments included here are specific to BEWGor's modifications
	
	
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	if r > n: return
	indices = range(n)
	cycles = range(n, n-r, -1)
	
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

#shows the BEWGor logo in ASCII art
def showNose():
	print ("""
                          .`                      
                          :                       
                         -.                       
                        `+                        
                        +.                        
                       -+                         
                      `s                          
                     `s.                          
                     s:                           
                   `s/                            
                  `s/                             
                 -y:                              
               `+y.                               
              :y+`                                
            -ss.                                  
          -ss-                                    
        .sy:                         ```          
      `+h/`                          ```.-.`      
     -hs.                                 .-:`    
    :d/                                     `/-   
   /m:                                        o-  
  .m+                                         .s  
  sd                                          .y  
  ds                                          s:  
  dy                                        `oo   
  +m.                   ``.::::-.``       `/s:    
   yd.              `-+shddhhhhhsooso+//+oo:`     
    +do.`      ``:oyyo:yys-..-oys` -hy-.`         
     .+hyo+++osyyohh. -yy-`yh .yy: `yy            
        `-:::-.   +y/ `syoy:.-oys` -ys            
                  `sy: `yyyyyys/` -yy.            
                   `oy+y- `..`  .+yo.             
                    `ssyyo+//+osy+-               
                  `sd+  .-://:-.                  
                   `-              """)
	
#prints a fixed-width divider made of '---'
def divider():
	print('---------------------------------------------------------------')

# Pause, press enter to coninue
def hold_up():
	#This variable is never used, it is just a pause placeholder
	#It does not persist after unpausing
	holdup = raw_input('Press enter to continue...')

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
		zodiac_choice = raw_input("> Enter the number of your choice here >:")

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

		zodiac_choice = raw_input("> Enter the number of your choice here >:")

		#If user inputs a choice not on the list of provided choices, the process repeats until they do.
		while zodiac_choice !=str(1) and  zodiac_choice !=str(2) and zodiac_choice !=str(3) and zodiac_choice != str(4): #Checks for valid choice
			print (" [-] Invalid choice, try again.")
			print (" This sign is often called the Ram or Sheep as well as the Goat.")
			print (" Which would you like to use? 1 - Goat, 2 - Ram, 3 - Sheep, 4 - All Three") #user chooses which value
			zodiac_choice = raw_input("> Enter the number of your choice here >:") 

			if zodiac_choice == str(1): chinese_zodiac = "goat"
			if zodiac_choice == str(2): chinese_zodiac = "ram"
			if zodiac_choice == str(3): chinese_zodiac = "sheep"
			if zodiac_choice == str(4): chinese_zodiac = "goat ram sheep"

	# Years of the Pig may be called years of the Boar, but this translation is rare
	elif chinese_zodiac == "pig":
		print ("\n The Chinese Zodiac sign for the year " + birth_year +" is the '" + chinese_zodiac.title() +"'")
		print (" This sign is usually called the Pig, but rarely it is called the Boar.") #user chooses which value
		print (' Which would you like to use? 1 - Pig, 2 - Boar, 3 - Both ') #user chooses which value
		zodiac_choice = raw_input("> Enter the number of your choice here >:")

		#If user inputs a choice not on the list of provided choices, the process repeats until they do.
		while zodiac_choice !=str(1) and  zodiac_choice !=str(2) and zodiac_choice !=str(3): #Checks for valid choice
			print (" [-] Invalid choice, try again.")
			print (" This sign is usually called the Pig, but rarely it is called the Boar.")
			print (' Which would you like to use? 1 - Pig, 2 - Boar, 3 - Both ') #user chooses which value
			zodiac_choice = raw_input("> Enter the number of your choice here >:")

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
	
	term_write_choice = raw_input('> Would you like to do this? (Y/N) >:').upper() #prompts user for choice
	term_write_choice = spaceShaver(term_write_choice)
	
	if term_write_choice in "YES" and len(term_write_choice) != 0:
		
		print(' If you do not enter a filename, the default will be "BEWGor_Terms.txt')
		outfile_name = raw_input('> Enter a filename, without the ".txt" extension >:')
		
		# If the inputted filename is non-zero in length, but contains unfriendly characters
		# Sometimes filenames containing characters like spaces () " ' {} can cause problems
		# The regex forces the filename to exculde these characters
		
		while len(outfile_name) !=0 and not filename_reg.match(outfile_name):
			print(' [-] Invalid filename, try again.')
			outfile_name = raw_input("> Enter a filename, without the .txt extension >:")
				
			
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

#General class for the people mentioned in the prompt
#Parent class of MAINSUBJECT
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
	
		person_name = raw_input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()
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
				person_name = raw_input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()


			elif not letters_and_spaces_reg.match(person_name):
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Input contains non-letter characters, try again.")
				person_name = raw_input("> Enter " + self.name + "'s Full Name, separated by spaces - or as much as you have >:").title()

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
		person_maiden_name = raw_input("> Enter " + self.name +"'s Maiden Name - if applicable >:").title()

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
				person_maiden_name = raw_input("> Enter " + self.name +"'s Maiden Name, separated by spaces - if applicable >:").title()

			elif not letters_and_spaces_reg.match(person_maiden_name): #checks to see if value contains improper characters
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				print (" [-] Input contains non-letter characters, try again.")
				person_maiden_name = raw_input("> Enter " + self.name + "'s Maiden Name, separated by spaces - if applicable >:").title()
		
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
		
		nickname = raw_input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")
		
		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(nickname) != 0: #if no nicknames added, move on.
		
			if nonzero_blankspace_reg.match(nickname): #ensures input isn't only blank space characters
				nickname = raw_input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")
		
			elif nickname in nicknames or nickname in entered: #check for double input
				print (" [-] That input has already been entered. Try again >:")
				nickname = raw_input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")
				
			elif ' ' in nickname: 
				nicknames.extend((spaceHandler(nickname))) #create variants of input if input contains spaces
				entered.append(nickname) #adds to 'entered' list to prevent double-adds
					
				
			else:
				nicknames.append(nickname) #adds input to list if valid
				entered.append(nickname) # adds to 'entered" list to prevent double-adds
				
			nickname = raw_input("> Enter one of " + self.name + "'s Nicknames or usernames, or simply press enter to move on >:")
		
		nicknames=list(set(nicknames)) #remove duplicates
		self.nicknames = ' '.join(nicknames)

	#Person Class Function that requests Birth day (no year)
	def getBirthday(self):
		print(' Be Aware BEWGor uses DDMM formatting!\n Winter Solstice falls on  21/12, 22/12, or 23/12 in this format.')
		person_birth_day = raw_input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")
		
		valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_birth_day) !=0 and not valid:
		# the 'valid' boolean keeps us from getting stuck in an infinite loop here if the user decides to enter an empty field after
		# being told their first input was invalid

			if not four_digs_reg.match(person_birth_day): #ensures input is four digits exactly, nothing else
				print (" [-] Days must be exactly 4 digits")
				person_birth_day = raw_input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			elif int(person_birth_day[2:4]) > 12: #checks for an invalid month
				print (" [-] Invalid month- After December, but before January - check your DDMM format")
				person_birth_day = raw_input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")

			elif int(person_birth_day[0:2]) > 31: #checks for an invalid day
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				person_birth_day = raw_input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")
				
			elif not doesDayExist(person_birth_day): #ensures day exists
				print (" [-] Invalid date. That month has fewer days. Try again.")
				valid = False
				person_birth_day = raw_input("> Enter " + self.name +"'s Birthday (without year, DDMM) >:")
				
			else: valid = True #all criteria have been met

		self.birth_day = person_birth_day #change value to entry - including to a null value if nothing is entered

	#Person Class Function that requests birth YEAR
	def getBirthyear(self):
		person_birth_year = raw_input("> Enter " + self.name +"'s Birth year (YYYY) >:")
		
		valid = False
		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(person_birth_year) !=0 and not valid: 
		
			if not four_digs_reg.match(person_birth_year): #ensures input is four digits exactly, nothing else
				print (" [-] Birth years must be exactly 4 digits, try again.")
				person_birth_year = raw_input("> Enter " + self.name +"'s Birth year (YYYY) >:")
				
				
			elif isYearFuture(person_birth_year): #ensures user does not enter a year in the future
				print (" [-] That year is in the future, try again.")
				person_birth_year = raw_input("> Enter " + self.name +"'s Birth year (YYYY) >:")
				
				
			else: valid = True #if all criteria have been met

		self.birth_year = person_birth_year #change value to entry - including to a null value if nothing is entered

	#Person Class Function that determines Greek Zodiac Sign (Mythological/Traditional) from birthday
	def getGreekZodiac(self):
		
		greek_zodiac = '' #sets a null value, so if user doesn't want to include this value, BEWGor can pass an empty value
		
		
		incl_Greek_Zod = raw_input("Would you like to include " + self.name + "'s Greek Zodiac Sign? (Y/N) >:").upper() #only determines/includes Greek Zodiac sign if user allows it
		
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
		
		incl_Birthstone = raw_input("Would you like to include " + self.name + "'s Birthstone (Y/N) >:").upper()  #only determines/includes Birthstone if user allows it
		
		incl_Birthstone = spaceShaver(incl_Birthstone) # cleans up input and stops false negative with "yes "
		
		if incl_Birthstone in "YES" and len(incl_Birthstone) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'#only take action if user requests it
		#if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
			
			birthmonth = self.birth_day[2:4] #isolate birth month
			
			print ("\n Is " + self.name + " more likely to use a Birthstone from a Western or Hindu list?") #there are multiple lists of Birthstones, two are included
			stone_choice = raw_input("> Enter 1 for Western, 2 for Hindu, or 3 to use both >:")
			
			#If user inputs a choice not on the list of provided choices, the process repeats until they do.
			while stone_choice !=str(1) and  stone_choice !=str(2) and stone_choice != str(3):
				print (' [-] Invalid choice, try again.')
				print (" Is " + self.name + " more likely to use a Birthstone from a Western or Hindu list?")
				stone_choice = raw_input("> Enter 1 for Western, 2 for Hindu, or 3 to use both >:")

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
			
			incl_Chinese_Zod = raw_input("Would you like to include " + self.name + "'s Chinese Zodiac Sign? (Y/N) >:").upper() #only determines/includes Chinese Zodiac sign if user allows it
			
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

#Class with main-subject specific information
# Child class of PERSON
class MainSubject(Person):

	def __init__(self,name,maiden_name,initials,nicknames,birth_day,birth_year,greek_zodiac,chinese_zodiac,Birthstone,gender,nationality,natl_demonym,natl_day,ethnicity,birthplace,hometown):
		
		#Create Main Subject Variables
		self.name = name
		self.gender = gender
		self.nationality = nationality
		self.natl_demonym = natl_demonym
		self.natl_day = natl_day
		self.ethnicity = ethnicity
		self.birthplace = birthplace
		self.hometown = hometown
		
		#ALPHA NOTE: to be included after alpha release
		# self.local_demonym
		# education
		# career
		# Favorite things
		# and more
	
	#Requests main subjects gender identity
	def getGender(self):
		
		print ("---" + self.name +"'s Gender Identity, in all relevant forms---")
		print (""" 
     MALE and FEMALE are the most commonly identified genders.
 BEWGor can include (English) synonyms for these two choices if 
 they are entered. You may wish to inlcude synonyms in the
 Subject's native language. For example, a Spanish speaker might
 include "chico" in their password. A German speaker may include "Frau"
    Transgendered or transsexual people may identify as male,
 female, trans, queer or something else. Some people do not identify with
 the concept of a binary Male/Female gender system.
    Note that sexuality is different than gender identity,
 and that there will not be a prompt requesting information
 about sexuality specifically. If you have information you
 wish to include about your subject's sexuality do so in the
 "ADDITIONAL WORDS" prompt at the end of the profiling process.
 
    Use 'male' or 'female' to bring up a prompt to include synonyms.
 """)
 
		gender_cands =[] #list that will contain inputted genders, or return blank if none are given
		entered = []
		
		gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
		while len(gender) != 0:
			
			
			if nonzero_blankspace_reg.match(gender): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
				
			elif not location_chars_reg.match(gender): #checks to see if input contains any characters unlikely to be in this category
				print (" [-] Input contains invalid characters, try again.")
				gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
				
			elif gender in gender_cands or gender in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
				
			else:
				if ' ' in gender and not male_reg.match(gender) and not female_reg.match(gender):
				#if a gender contains spaces, split it up so BEWGor can join the words together with variations
					
					gender_cands.extend((spaceHandler(gender))) #create variants of input if input contains spaces
					entered.append(gender) #adds to 'entered' list to prevent double-adds	
					gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
					
				else:
					gender_cands.append(gender.lower()) 
					
					if male_reg.match(gender):
						gender_cands.append('male')
						entered.append('male')
						
						male_syn_choice = raw_input('> Would you like to include 10 English synonyms for Male? (Y/N) >:').upper()
						male_syn_choice = spaceShaver(male_syn_choice)	
						
						if male_syn_choice in "YES" and len(male_syn_choice) != 0:
							gender_cands.extend(['man','bro','dude','sir','gent','mr','mister','guy','boy','boi'])
							print ('\n [+] Synonyms for Male added \n')
					
					if female_reg.match(gender):
						gender_cands.append('female')
						entered.append('female')
						
						fem_syn_choice = raw_input('> Would you like to include 10 English synonyms for Female? (Y/N) >:').upper()
						fem_syn_choice = spaceShaver(fem_syn_choice)	

						if fem_syn_choice in "YES" and len(fem_syn_choice) != 0:
							gender_cands.extend(['woman','girl','gal','chick','lady','mrs','ms','miss','misses','grrl','gurl','madame'])
					
					entered.append(gender)
					
					gender = raw_input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
					print ('\n [+] Synonyms for Female added \n')
					
		gender_cands=list(set(gender_cands))  #removes duplicates from list	
		self.gender = ' '.join(gender_cands)  #change value to entry - including to a null value if nothing is entered

	#Requests Main Subject's Country of Origin
	def getNationality(self):
	
		print ("---" + self.name +"'s Country of Origin, in all relevant alternate forms---")
		print("""
 For example, an English speaker might refer to 'Germany',
 while a German speaker calls it 'Deutschland.'
 Countries also may have abbreviated forms, such as 'USA', 'U.S.A" or "The US"
 Include Spaces and apostrophes as necessary.
 
 Capitalization will be handled automatically.
 """)
 
		nationality_cands =[]  #list that will contain inputted Countries, or return blank if none are given
		entered = []
		
		nationality = raw_input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")
		
		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(nationality) !=0:
		
			if nonzero_blankspace_reg.match(nationality): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				nationality = raw_input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

			elif not location_chars_reg.match(nationality): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				nationality = raw_input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")
			
			elif nationality in nationality_cands or nationality in entered:
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				nationality = raw_input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")
				
			else:
				#If a country's full name is given, such as "Federal Republic of Germany"
				#BEWGor must handle the spaces given by coming up with variants like 'Federal-Republic' 'Federal_Republic' and 'FederalRepublic'
				
				#If a country's name contains the word 'of', BEWGor must generate variations where of is and is not capitalized
				#Later, when variations of important words are created, all capital, all lowercase and '
				#Title Case (where the first letter of every word is capitalized, and the rest aren't)
				#BEWGor does not generate a variation where the nation is in Title Case, except for the word 'of'
				#Therefore that must be handled with spaceHandler
				
					if ' ' in nationality: #if a nationality contains spaces, split it up so BEWGor can join the words together with variations
						
						nationality_cands.extend((spaceHandler(nationality)))
						
						# This was included so capitlization would be preserved
						# Without it, entries like "The US" may come end up as "The Us"
						nationality_cands.extend(nationality.split(' '))
						
						entered.append(nationality)	
					
					else:
						
						nationality_cands.append(nationality)
						entered.append(nationality)
					
					nationality = raw_input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")
					
		nationality_cands=list(set(nationality_cands)) #removes duplicates
		self.nationality = ' '.join(nationality_cands) #change value to entries - including to a null value if nothing is entered

	#Requests Main Subject's National Demonyms
	def getNatlDemonyms(self):
		print ("---Adjectives or Nouns to Describe a Person From " + self.name + "'s Country---")
		print ("""
 These are known as National Demonyms.
 A person from Germany is both 'German' and can be called 'a German.'
 Consider demonyms in that country's native language as well, which
 may have gender. Not just "Cuban" but "Cubano" or "Cubana." You may
 want to inlcude nicknames for the demonym as well - such as "Aussie"
 or "Ozzy" for an Australian.
 Capitalization will be handled automatically.
 """)
		natl_demonym_cands =[] #list that will contain inputted nicknames, or return blank if none are given
		entered = []
		
		natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")
		
		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(natl_demonym) != 0:
			
			if nonzero_blankspace_reg.match(natl_demonym): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

			elif not location_chars_reg.match(natl_demonym): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")
			
			elif natl_demonym in natl_demonym_cands or natl_demonym in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")
				
			else: #if its likely to be valid
				if ' ' in natl_demonym: #if a natl_demonym contains spaces, split it up so BEWGor can join the words together with variations
					natl_demonym_cands.extend((spaceHandler(natl_demonym)))
					entered.append(natl_demonym) #adds to 'entered' list to prevent double-adds
					
					natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")
					
				else:
					natl_demonym_cands.append(natl_demonym)
					entered.append(natl_demonym) #adds to 'entered' list to prevent double-adds
					
					natl_demonym = raw_input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")
		
		natl_demonym_cands = list(set(natl_demonym_cands)) # removes duplicates from candidate nationalties			
		self.natl_demonym = ' '.join(natl_demonym_cands) # #change value to entries - including to a null value if nothing is entered
	
	#Requests Main Subject's National Day
	def getNationalDay(self):
		
		print ("---" +self.name +"'s National Day---")
		print ("""
 These are often the date the nation got independence, won a battle,
 or the day the nation celebrates a religious or royal figure.
 In the US, the national day is 4 July 1776, the day the country declared
 independence. In Oman, the day is 18 November to celebrate the
 Sultan's Birthday. In Ethiopia, the day is 28 May, to celebrate the defeat
 of a ruling party seen as corrupt.
 """)
		
		natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

		# The 'valid' boolean is true if the birthday value is empty or meets the correct criteria
		if len(natl_day) == 0: valid = True
		else: valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
		
		
		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking	
		while len(natl_day) !=0 and not valid:
		# the 'valid' boolean keeps us from getting stuck in an infinite loop here if the user decides to enter an empty field after
		# being told their first input was invalid

			if not four_digs_reg.match(natl_day) and not eight_digs_reg.match(natl_day): #ensures input is four or eight digits exactly
				print (" [-] Invalid Input, date must be 4 or 8 Digits exactly.")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")
			
			elif int(natl_day[2:4]) > 12: #ensures DDMM format is correct
				print (" [-] Invalid Month. After December, but before January - check your DDMM format")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif int(natl_day[0:2]) > 31: #ensures no dates after the 31st are entered
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")
				
			elif not doesDayExist(natl_day[0:4]): #ensures date provided exists
				print (" [-] Invalid Date. That month has fewer days. Try again.")
				valid = False
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")
				
			elif len(natl_day) == 8 and isItInvalidLeap(natl_day): #ensures full date is not invalid leap day
				print (" [-] That day did not exist that year. Try again.")
				valid = False
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif len(natl_day) == 8 and isFullDateFuture(natl_day): #ensures full date is not in the future
				print (" [-] You have entered a date in the future, that can't be right.")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = raw_input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			else: valid = True # if all criteria have been met

		self.natl_day = natl_day #change value to entry - including to a null value if nothing is entered

	#Requests Main Subject's Ethnonyms
	def getEthnicity(self):
	
		print ("---" + self.name +"'s Ethnonyms, in all relevant alternate forms---")
		print("""
 For example, there is a large number of ethnic Chinese living in Malaysia.
 These people are ethnically Chinese, but their nationality is Malaysian.
 The ethnonym in this case would be 'Chinese' or 'Malaysian-Chinese.'
 An ethnic group can exist independent of geography, consider
 the Jewish or Romani Peoples.
    In some countires, such as the US, it is common for people to consider their
 racial identity as a part of or the whole of their ethnic identity
 - and vice versa. For example, it is common practice in the US for
 some younger people of East Asian descent to include the nickname abbreviation
 "AZN" in their usernames and passwords. 
    Nicknames for ethnicities are often unfriendly, but some groups
 co-opt these offensive terms to take the sting out of them.
 You may want to consider adding these to the list.
    Even if a person's family has been living in one nation for generations,
 they may consider their ethnic identity to be the same as their ancestors.
   Enter nouns and adjectives here, such as "Gael" AND "Gaelic"
   In many cases, nationality and ethnicity are the same.
 If that is so, simply move on.
 
 Capitalization will be handled automatically.
 """)
 
		ethnicity_cands =[] #list that will contain inputted ethnonyms, or return blank if none are given
		entered = []
		
		ethnicity = raw_input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")
		
		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(ethnicity) !=0:
			
			if nonzero_blankspace_reg.match(ethnicity): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				ethnicity = raw_input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")

			elif not location_chars_reg.match(ethnicity): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				ethnicity = raw_input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")
			
			elif ethnicity in ethnicity_cands or ethnicity in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				ethnicity = raw_input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")
				
			else:
				if ' ' in ethnicity: #if a ethnicity contains spaces, split it up so BEWGor can join the words together with variations
					ethnicity_cands.extend((spaceHandler(ethnicity)))
					entered.append(ethnicity)	
					
				else:
					ethnicity_cands.append(ethnicity)
					entered.append(ethnicity)
					
				ethnicity = raw_input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")
		
		
		ethnicity_cands = list(set(ethnicity_cands)) # removes duplicates from entered values
		self.ethnicity = ' '.join(ethnicity_cands)  # change value to entries - including to a null value if nothing is entered

	#Requests Main Subject's Birthplace
	def getBirthplace(self):
		
		birthplace_cands =[] #list that will contain inputted birthplaces, or return blank if none are given
		entered = []
		
		print ("---" + self.name + "'s Birthplace---")
		print ("""
 Consider the name of cities, neighborhoods and more.
 Consider nicknames for these places, such as 'Chi-Town' for 'Chicago'
 or 'The Heights' for a neighborhood like 'Washington Heights'
 """)
		birthplace = raw_input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")
		
		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(birthplace) !=0:
				
			if nonzero_blankspace_reg.match(birthplace): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				birthplace = raw_input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

			elif not location_chars_reg.match(birthplace): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				birthplace = raw_input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")
			
			elif birthplace in birthplace_cands or birthplace in entered:
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				birthplace = raw_input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")
				
			else:
				if ' ' in birthplace: #if a birthplace contains spaces, split it up so BEWGor can join the words together with variations
					
					birthplace_cands.extend((spaceHandler(birthplace)))
					entered.append(birthplace)	
					
					
				else:
					birthplace_cands.append(birthplace)
					birthplace_cands=list(set(birthplace_cands))
					entered.append(birthplace)
					
				birthplace = raw_input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")
		
		birthplace_cands = list(set(birthplace_cands)) # removes duplicates from birthplace candidates
		self.birthplace = ' '.join(birthplace_cands)  # change value to entries - including to a null value if nothing is entered
	
	#Requests Main Subject's Hometown
	def getHometown(self):
		
		hometown_cands =[] #list that will contain inputted hometowns, or return blank if none are given
		entered = []
		
		print ("---The Town " + self.name + " Calls 'Home'---")
		print ("""
 This might be different than the city they actually live.
 And often overlaps with birthplace.
 Again, consider nicknames for the location.
 
 If this answer overlaps with birthplace, simply move on.
 """)
		hometown = raw_input("> Enter " + self.name +"'s hometown, or press enter to move on >:")
		
		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(hometown) != 0:
		
			if nonzero_blankspace_reg.match(hometown): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				hometown = raw_input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

			elif not location_chars_reg.match(hometown): #checks to see if input contains any characters that probably wouldn't be in a location's name
				print (" [-] Input contains invalid characters, try again.") 
				hometown = raw_input("> Enter " + self.name +"'s hometown, or press enter to move on >:")
			
			elif hometown in hometown_cands or hometown in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				hometown = raw_input("> Enter " + self.name +"'s hometown, or press enter to move on >:")
				
			else:
				if ' ' in hometown: #if a hometown contains spaces, split it up so BEWGor can join the words together with variations
					hometown_cands.extend((spaceHandler(hometown)))
					entered.append(hometown)	
					
				else:
					hometown_cands.append(hometown)
					entered.append(hometown)
					
			hometown = raw_input("> Enter " + self.name +"'s hometown, or press enter to move on >:")
			
		hometown_cands=list(set(hometown_cands)) #removes duplicates from candidte hometowns			
		self.hometown = ' '.join(hometown_cands) # change value to entries - including to a null value if nothing is entered

	#Requests all of the Main Subject's Info
	def main_sub_inputInfo(self):
		divider()
		self.getName()
		if self.name == "The Person": self.name = "The Main Subject" #if main subject's name is not entered, refer to them as "The Main Subject"
		
		divider()
		self.getMaidenName()
		divider()
		self.getNicknames()
		divider()
		self.getBirthday()
		divider()
		self.getBirthyear()
		divider()
		
		# The following block ensures the entered birthday is in the present or past - if the full date is known
		valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
		while len(self.birth_day) != 0 and len(self.birth_year) !=0 and not valid:

			full_birthday = self.birth_day + self.birth_year

			if isItInvalidLeap(full_birthday): #ensures full date is not invalid leap day
				print (" [-] That day did not take place that year. Try again >:")
				
				divider()
				self.getBirthday()
				divider()
				self.getBirthyear()
				
			elif isFullDateFuture(full_birthday): #ensures full date is not in the future
				print (" [-] You have selected a birthday in the future, that can't be right. \n")

				divider()
				self.getBirthday()
				divider()
				self.getBirthyear()
				
			else: valid = True
		

		#if valid birthday is present, acquire associated mythology
		if len(self.birth_day) != 0:
			self.getGreekZodiac()
			divider()
			self.getBirthstone()
		
		else:
			self.greek_zodiac = ''
			self.Birthstone = ''
			
		if len(self.birth_year) != 0:
			divider()
			self.getPersonChineseZodiac()
		else: self.chinese_zodiac = ''
		
		
		#Get the Main-Subject Specific Data
		
		self.getGender()
		divider()
		self.getNationality()
		divider()
		self.getNatlDemonyms()
		divider()
		self.getNationalDay()
		divider()
		self.getEthnicity()
		divider()
		self.getBirthplace()
		divider()
		self.getHometown()
		
	#Outputs all of the Main Subject's Collected Words
	def main_sub_outputWords(self):

		word_output = []
		
		#only add the subject's name to the list if something has been entered, not 'The Main Subject'
		if len(self.name) != 0 and self.name != "The Main Subject": word_output.extend(((self.name).lower()).split(' ')) # add name to list, split up at spaces
		if len(self.initials) !=0 : word_output.append(self.initials)
		if len(self.maiden_name) != 0: word_output.append((self.maiden_name).lower())
		if len(self.nicknames) != 0: word_output.extend(((self.nicknames).lower()).split(' '))
		if len(self.greek_zodiac) != 0: word_output.append((self.greek_zodiac).lower())
		if len(self.Birthstone) != 0: word_output.extend(((self.Birthstone).lower()).split(' '))
		if len(self.chinese_zodiac) != 0:word_output.extend(((self.chinese_zodiac).lower()).split(' '))
		if len(self.gender) != 0:word_output.extend(((self.gender).lower()).split(' '))
		if len(self.nationality) != 0:word_output.extend((self.nationality).split(' '))
		if len(self.birthplace) != 0:word_output.extend((self.birthplace).split(' '))
		if len(self.ethnicity) != 0:word_output.extend(((self.ethnicity).lower()).split(' '))
		if len(self.hometown) != 0:word_output.extend(((self.hometown).lower()).split(' '))
		
		word_output = list(set(word_output))
		return word_output

	#Outputs all of the Main Subjects Collected Days
	def main_sub_outputDays(self):
		day_output = []

		if len(self.birth_day) != 0: day_output.append(self.birth_day)
		
		#if day and month of national day are available, include that
		if len (self.natl_day) != 0: day_output.append(self.natl_day[0:4])

		return day_output

	#Outputs all of the Main Subjects Collected Years
	def main_sub_outputYears(self):
		year_output = []

		if len(self.birth_year) != 0: year_output.append(self.birth_year)
		
		#if year of national day is available, include that
		if len(self.natl_day) == 8 : year_output.append(self.natl_day[4:8])

		return year_output

	#Outputs all of the Main Subjects Collected Full Dates
	def main_sub_outputFullDates(self):
		full_date_output=[]

		full_birthday = self.birth_day + self.birth_year

		#if the full birthdate is available, day month and year, include that
		if len(full_birthday) == 8: full_date_output.append(full_birthday)
		
		#if the full national day is available, include that
		if len(self.natl_day) == 8 : full_date_output.append(self.natl_day) 

		return full_date_output


#ALPHA NOTE
#This function that sets up the creation of 'flat' Person class instances for each associate
# (all types of associates have the same prompts)
# will be replaced with individual relationship classes
# (Significant other, children, siblings, pets, etc)
# in future releases
def getAssociates():
	
	associates = [] #list that will contain inputted associates, or return blank if none are given
	
	
	#Create Significant Other Instances (just one for now)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	SO_choice = raw_input("Does the Main Subject have a Significant Other you have information on? (Y/N) >:").upper()
	
	SO_choice = spaceShaver(SO_choice) #cleans up answer - stops false negative with "yes "
	
	if SO_choice in "YES" and len(SO_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'associates.append('Signifcant_Other')
		associates.append('Significant_Other')
	
	divider()
		
	
	#Get number of children instances that will be created
	#(Son and daughter, not 'children' in the context of Python classes)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's children do you have information on? \nEnter '0' if there are none.")
	children_choice = raw_input("> Enter the number here >:")
	
	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(children_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's children do you have information on? \nEnter '0' if there are none.")
		children_choice = raw_input("> Enter the number here >:")
		
	if (children_choice) != str(0):
		for i in range(1,int(children_choice)+1):
			associates.append('Child_Number_'+str(i))
	
	divider()
	
	#Get number of Parent instances that will be created
	#(Son and daughter, not 'children' in the context of Python classes)
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's parents do you have information on?")
	parents_choice = raw_input("> Enter the number here >:")
	
	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(parents_choice):
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's parents do you have information on?")
		parents_choice = raw_input("> Enter the number here >:")
		
	if (parents_choice) != str(0):
		for i in range(1,int(parents_choice)+1):
			associates.append('Parent_Number_'+str(i))
	
	divider()
	
	#Get number of Sibling instances that will be created
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's siblings do you have information on? \nEnter '0' if there are none.")
	siblings_choice = raw_input("> Enter the number here >:")
	
	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(siblings_choice): 
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's siblings do you have information on? \nEnter '0' if there are none.")
		siblings_choice = raw_input("> Enter the number here >:")
		
	if (siblings_choice) != str(0):
		for i in range(1,int(siblings_choice)+1):
			associates.append('Sibling_Number_'+str(i))
	
	divider()		
	
	# Get number of pet instances that will be created
	# IN ALPHA THESE ARE SIMPLY THE 'PERSON' CLASS
	print ("How many of the Main Subject's pets do you have information on? \nEnter '0' if there are none.")
	pets_choice = raw_input("> Enter the number here >:")
	
	# If user inputs a choice not on the list of provided choices, the process repeats until they do.
	while not at_least_one_dig_reg.match(pets_choice): 
		print (" [-] Invalid choice, try again.")
		print ("How many of the Main Subject's pets do you have information on?\nEnter '0' if there are none.")
		pets_choice = raw_input("> Enter the number here >:")
		
	if (pets_choice) != str(0):
		for i in range(1,int(pets_choice)+1):
			associates.append('Pet_Number_'+str(i))
	
	return associates	
		
# Function to show the big ASCII Art
def showTheName():
#Now with puns!
	print ( """

  ___          _   _   _          ___
 | _ )  _  _  | | | | ( )  ___   | __|  _  _   ___
 | _ \ | || | | | | | |/  (_-<   | _|  | || | / -_)
 |___/  \_,_| |_| |_|     /__/   |___|  \_, | \___|
 __      __                 _   _   _   |__/ _
 \ \    / /  ___   _ _   __| | | | (_)  ___ | |_
  \ \/\/ /  / _ \ | '_| / _` | | | | | (_-< |  _|
   \_/\_/   \___/ |_|   \__,_| |_| |_| /__/  \__|
  / __|  ___   _ _    ___   _ _   __ _  | |_   ___   _ _
 | (_ | / -_) | ' \  / -_) | '_| / _` | |  _| / _ \ | '_|
  \___| \___| |_||_| \___| |_|   \__,_|  \__| \___/ |_|
 also knowns as BEWGor
 Pronounced "Booger"
 "Pick your Knows!"
 

 by berzerk0 @ Github
 Version 0.0.1 - 'FLAT' ALPHA RELEASE
	""")

#Function to show the mini ASCII Art
def showMiniName():
	print ("""
  ___ _____      _____
 | _ ) __\ \    / / __|___ _ _
 | _ \ _| \ \/\/ / (_ / _ \ '_|
 |___/___| \_/\_/ \___\___/_| """ )

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
	
	fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(fulldate) !=0:
		
		if nonzero_blankspace_reg.match(fulldate): #rejects inputs of just empty space characters
			print (" [-] Empty Space, try again.")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")

		elif not eight_digs_reg.match(fulldate): #reject inputs that aren't 8 digits exactly
			print (" [-] Invalid Characters, try again.")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
		
		elif int(fulldate[2:4]) > 12: #rejects bad month input
			print (" [-] Invalid Month. After December, before January - check your DDMMYYYY format")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
			
		elif int(fulldate[0:2]) > 31: #rejects bad day input
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
		
		elif not doesDayExist(fulldate[0:4]): #rejects dates that do not exist 
			print (" [-] Invalid date. That month has fewer days. Try again.")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
			
		
		elif isItInvalidLeap(fulldate): #rejects invalid leap days
			print (" [-] That day did not take place that year. Try again >:")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
			
		elif fulldate in fulldates: #rejects inputs that have already been entered
			print (" [-] That date has already been entered. Try again >:")
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
		
		else:
			fulldates.append(fulldate) #add the date to the list
			fulldate = raw_input("> Enter a full date in DDMMYYYY format, or press enter to move on >:")
			
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
	
	add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:")
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_spec_day) != 0:
		
		if nonzero_blankspace_reg.match(add_spec_day):  # ensures input isn't only blank space characters
			print (' [-] Empty space, try again.')
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:")
		
		elif not four_digs_reg.match(add_spec_day): # ensures input is limited to 4 digits exactly
			print (' [-] Days must be 4 Digits, try again.')
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:")
	
		elif int(add_spec_day[2:4]) > 12: #checks for an invalid month
			print (" [-] Invalid month- After December, but before January - check your DDMM format")
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:") 	

		elif int(add_spec_day[0:2]) > 31: #checks for an invalid day
			print (" [-] Invalid Day, no month has more than 31 days. Try again.")
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:") 	
				
		elif not doesDayExist(add_spec_day): #ensures day exists
			print (" [-] Invalid date. That month has fewer days. Try again.")
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:") 	
			
		elif add_spec_day in add_spec_days: # check for double input
			print (' [-] That input has already been added to the list. Try again')
			add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:")
		
		else:
			add_spec_days.append(add_spec_day) #if the day is valid, add it to list
		
		add_spec_day = raw_input("> Enter an additional day here, or simply press enter to move on >:")
		
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
	
	add_spec_year = raw_input("> Enter an additional year here, or simply press enter to move on >:")
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_spec_year) != 0:
		
		if nonzero_blankspace_reg.match(add_spec_year):  # ensures input isn't only blank space characters
			print (' [-] Empty space, try again.')
			add_spec_year = raw_input("> Enter an additional year here, or simply press enter to move on >:")
		
		elif not four_digs_reg.match(add_spec_year): # ensures input is limited to 4 digits exactly
			print (' [-] Invalid entry, try again.')
			add_spec_year = raw_input("> Enter an additional year here, or simply press enter to move on >:")
			
		
		elif add_spec_year in add_spec_years: # check for double input
			print (' [-] That input has already been added to the list. Some inputs are added automatically, try again')
			add_spec_year = raw_input("> Enter an additional year here, or simply press enter to move on >:")
		
		else:
			add_spec_years.append(add_spec_year) #if the year is valid, add it to list
		
		add_spec_year = raw_input("> Enter an additional year here, or simply press enter to move on >:")
		
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
	
	starting_year = raw_input("> Enter START year in YYYY format, or press enter to move on >:")
	if len(starting_year) ==0: return '' #if no range entered, return null and move on
	
	valid = False
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(starting_year) !=0 and not valid:

		if nonzero_blankspace_reg.match(starting_year): #rejects inputs of empty space characters
			print (" [-] Empty Space, try again.")
			starting_year = raw_input("> Enter START year in YYYY format, or press enter to move on >:")

		elif not four_digs_reg.match(starting_year): #rejects inputs that do not fit the format
			valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
			print (" [-] Invalid format, try again.")
			starting_year = raw_input("> Enter START year in YYYY format, or press enter to move on >:")

		else: valid = True # if all criteria have been met
		
	if len(starting_year) ==0: return '' #if no START year entered, move on
	
	
	ending_year = raw_input("> Enter END year in YYYY format >:")
	
	valid = False
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, BEWGor will keep asking
	while not valid:

		if nonzero_blankspace_reg.match(ending_year): #rejects inputs of empty space characters
			print (" [-] Empty Space, try again.")
			ending_year = raw_input("> Enter END year in YYYY format >:")

		elif not four_digs_reg.match(ending_year): #rejects inputs that do not fit the format
			valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
			print (" [-] Invalid format, try again.")
			ending_year = raw_input("> Enter END year in YYYY format >:")

		elif ending_year == starting_year: # ensures years are not equal
			print (" [-] Starting and Ending Year cannot be equal. Try again.")
			ending_year = raw_input("> Enter END year in YYYY format >:")
			
		elif int(ending_year) < int(starting_year): # ensures starting year precedes ending year
			print (" [-] Ending year must be after Starting year. Try again.")
			ending_year = raw_input("> Enter END year in YYYY format >:")

		elif len(ending_year) ==0: # ensures ending year is populated
			print (' [-] Ending year cannot be a null value. Try again')
			ending_year = raw_input("> Enter END year in YYYY format >:")
		
		elif int(ending_year) - int(starting_year) > 10:
			print (" [-] Using " + ending_year + " as an ending year would result in a range of " + str(int(ending_year) - int(starting_year)) +" years.")
			long_range_choice = raw_input('Do you want to use '+ ending_year + ' as your end year? (Y/N) >:').upper()
			long_range_choice = spaceShaver(long_range_choice) # cleans up input and stops false negative with "yes "
			
			if long_range_choice not in "YES" and len(long_range_choice) != 0:
				ending_year = raw_input("> Enter END year in YYYY format >:")
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
	
	
	add_word = raw_input("> Enter an additional word here, or simply press enter to move on >:")
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking	
	while len(add_word) != 0:
		
		if nonzero_blankspace_reg.match(add_word):  #rejects inputs of just empty space characters
			print (' [-] Empty space, try again.')
			add_word = raw_input("> Enter an additional word here, or simply press enter to move on >:")
		
		elif add_word in add_words: #rejects inputs that have already been entered
			print (' [-] That input has already been added to the list. \n Some inputs are added automatically. Try again.')
			add_word = raw_input("> Enter an additional word here, or simply press enter to move on >:")
		
		else:
		
			if ' ' in add_word: add_words.append(spaceHandler(spaceShaver(add_word)))
			# creates a variants of a string containing spaces
			#but removes trailing spaces
			
			else:add_words.append(spaceShaver(add_word)) #removes trailing spaces
		
		
		add_word = raw_input("> Enter an additional word here, or simply press enter to move on >:")
		
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
	
	add_num = raw_input("> Enter an additional number, or simply press enter to move on >:")
	
	# If the user enters a value, it must meet criteria
	# until all criteria is met, or a Null value is entered, BEWGor will keep asking
	while len(add_num) != 0:
		
		if nonzero_blankspace_reg.match(add_num): #rejects inputs of just empty space characters
			print (' [-] Empty space, try again.')
			add_num = raw_input("> Enter an additional number, or simply press enter to move on >:")
		
		elif not at_least_one_dig_reg.match(add_num): #rejects inputs that are not only numbers
			print (" [-] Invalid characters, try again.")
			add_num = raw_input("> Enter an additional number, or simply press enter to move on >:")
			
		elif add_num in add_nums: #rejects inputs that have already been entered
			print (' [-] That input has already been added to the list. Try again.')
			add_num = raw_input("> Enter an additional number, or simply press enter to move on >:")
		
		else:
			add_nums.append(add_num) #adds number to list if valid
		
		add_num = raw_input("> Enter an additional number, or simply press enter to move on >:")
		
	add_nums = list(set(add_nums)) #removes duplicates, just in case
	return add_nums

#Function to Generate possible full birthdates based on a birth_day and a range of years
def getBirthdayRange(birth_day,year_range):
	print (' --- Possible Birthdays --- \n \n')
		   
	print ("If you did not know " + main_subject.name + "'s birth year, BEWGor")
	print (""" could not have generated a full birthdate for your Person.
 Based on the year range you just created and the Person's birthday,
 BEWGor can generate potential full birthdates.
 Birthdays detected as in the future will not be added.
 """)
	
	guess_bday_choice = raw_input('> Would you like to do this? (Y/N) >:').upper() # #only determines possible full dates if user allows it
	
	guess_bday_choice = spaceShaver(guess_bday_choice) # cleans up input and stops false negative with "yes "
		
	poss_bdays = [] #list to store possible birthdays	
							
	if guess_bday_choice in "YES" and len(guess_bday_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
		
		# This block iterates through the list of years, and adds valid birthdays to the list
		# It rejects birthdays that are in the future, or take place on non-existant leap days
		for i in year_range:
			if not isFullDateFuture(birth_day + i) and not isItInvalidLeap(birth_day + i):# ensures dates being added are valid
				poss_bdays.append(birth_day + i) #adds day to list
		
		#alert user to inclusion of possible birthdays			
		print ("\n [+] Generated and included a full date of '" + (main_subject.birth_day) + "' for years " + poss_bdays[0][4:8] + " through " + poss_bdays[-1][4:8] + ". \n")
			
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
	
	more_CN_zod_choice = raw_input('> Would you like to do this? (Y/N) >:').upper() # #only determines/includes these Chinese Zodiac signs if user allows it
		
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

#------------------Show Help Information----------------------#
if len(sys.argv) >= 2 and sys.argv[1] == '-help': # shows help info if user inputs '-help' as an argument

	showNose() #show Nose ASCII Art
	showTheName()  #show Name ASCII Art

	print (" \n [ Options ] \n \n")
	print ("	-help	Display this help screen")
	print ("	-input	Prompts user for information on a Person to generate potential passwords" )
	print ("    <no arugment > is treated the same as -input") #if the user does not provide an argument, prompts will appear
	
	#ALPHA NOTE: these functions may be included in future releases
	#print ("	-import	Generates variations and permutations from text file" )
	#print ("   -input-min  Prompts user to input the minimum amount of)
	exit()

#------------------Run Script----------------------#
elif len(sys.argv) < 2 or sys.argv[1] == '-input': # runs script if user inputs '-input' or nothing as an argument
#Future versions may support reading from a file 

	showNose() #Show the Main Logo and Puns.
	showTheName() #Show the ASCII Title

	#These lists will be populated with inputs
	important_years = []
	important_days = []
	important_full_dates = []
	important_numbers = []
	important_days = []
	important_words = []
	
	pause = raw_input('Press enter to begin...')

	showMiniName() #Shows small ASCII logo

	# Prints Introduction
	print( """
 You will be asked a series of questions about your Subject.
 Your answers will be used to generate a wordlist.
 The lists are generated using all permutations of inputted numbers and words.

 If you are unable or uninterested in providing input for a specific prompt...
 
      ***ANY PROMPT CAN BE LEFT BLANK BY PRESSING ENTER***

 If you do not know how to answer a prompt, more research may be needed.
 Use  --- http://wwww.osintframework.com/ --- to find many useful tools.
 
	           ***PAY ATTENTION***
	
   Many prompts include specific details about input - read carefully.
   Failing to do so will result in a poor quality wordlist!

 Let's begin!
 """)
	
	hold_up() # "Press Enter to Contrinue"

#------------------Get Main Subject Information----------------------#

	divider()
	print("\n------------------Section A: Main Subject Information----------------------\n")
	
	# Constructs Main Subject Instance
	main_subject = MainSubject('The Main Subject','','','','','','','','','','','','','','','') 

	#Request the info for the Main Subject
	main_subject.main_sub_inputInfo()

	important_words.extend(main_subject.main_sub_outputWords()) # Add Main Subject's names, nicknames to important words
	important_days.extend(main_subject.main_sub_outputDays())  # Add  Main Subject's known days to important days
	important_years.extend(main_subject.main_sub_outputYears()) # Add Main Subject's known years to important years
	important_full_dates.extend(main_subject.main_sub_outputFullDates()) # Add Main Subject's known full dates to important full dates
	
	
#------------------Get Info About Associates ----------------------#
	divider()
	print("\n------------------Section B: Information Subject's Associates------------------\n")
	divider()
	
	print (""" If you have information on any of the Main Subject's family members
 or pets, BEWGor will prompt for information.
 Currently, it will specifically ask about,
 Significant Others (Spouses, Romantic Partners) Parents,
 Children, Siblings and Pets.
 """)
 
	associates_choice = raw_input("Do you have information on any of " + main_subject.name + "'s family or associates? (Y/N) >:").upper()
	
	associates_choice = spaceShaver(associates_choice)
	
	if associates_choice in "YES" and len(associates_choice) != 0: #if User answers "YES" - the program will begin the process of adding assocites
	#if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
		
		associates = getAssociates() # Gets list of known associates
	
		#iterate through list of associates and ask appropriate questions
		for associate in associates:
			
			exec(associate + " = Person('" + associate + "','','','','','','','','')") # creates Person instance for a given associate
			exec(associate +".inputInfo()") # requests basic information about given associate
			
			exec("important_words.extend("  + associate + ".outputWords())") # Add names, nicknames to important words for a given associate
			exec("important_days.extend(" + associate + ".outputDays())")  # Add known days to important days for a given associate
			exec("important_years.extend(" + associate + ".outputYears())") # Add known years to important years for a given associate
			exec("important_full_dates.extend(" + associate + ".outputFullDates())") # Add known full dates to important full dates for a given associate
	
	else: print ("\n [+] No information about Family or Associates added. Moving on.") #if the User did not answer yes, no associates will be added
	
	
	
#------------------Get Additional Information Unassociated with Specific Person----------------------#

	divider()
	print("\n------------------Section C: Addtional Information---------------------\n")
	divider()
		
	year_range = getYearRange()  # Generates range of years
	if len(year_range) != 0: #if range generated, add years to list
		important_years.extend(year_range)
	
	# If a range of years is given, prompt to add additional information now determinable
	if len(year_range) > 0:
		
		# If the Main Subject's Birth Day was given, but not necessarily their birth YEAR
		# BEWGor can create a list of potential birthdays given a list of years
		
		if len(main_subject.birth_day) == 4: 
			divider()
			important_full_dates.append(getBirthdayRange(main_subject.birth_day,year_range))
			
		divider()
		
		# If a range of years is given, BEWGor may generate Chinese Zodiac Signs
		important_words.extend(getChineseZodiacRange(year_range)) #from this range of years, we can generate Chinese Zodiac signs
			
	divider()
	#Request additional full dates by calling function
	important_full_dates = getMoreFullDates() 
	
	divider()
	important_years.extend(getMoreYears()) #get additional years by calling function

	divider()
	important_numbers.extend(getMoreNumbers()) #get additional random numbers by calling function
	
	divider()
	
	important_words.extend(getMoreWords()) #get additional words by calling function
	
	important_words = list(set(important_words)) #Remove Duplicate words
	
	# Iterates over all important words and checks for entries that contain only blankspace
	# These were prevented from being added at any point so far, but this ensures it
	
	for item in important_words: 
		if nonzero_blankspace_reg.match(item): important_words.remove(item)
	
	
	if len(important_words + important_years + important_full_dates + important_numbers + important_days) != 0:
		# Output entries to a file for future use, if user requestes
		divider()
		outputTerms(list(set(important_words + important_years + important_full_dates + important_numbers + important_days)))
	else:
		print ('\n')
		divider()
		showMiniName()
		print('\nBEWGor can only work if you answer at least one of the prompts!')
		print('You did not enter in any information! \n\nBEWGor will now exit\n\n')
		divider()
		exit()


# ------ ALPHA RELEASE NOTE -----
# NOT INCLUDING PHONESPELLING IN ALPHA RELEASE, IT NEEDS REFINING
#One last thing before we process the numbers - phonespelling
# Now that we have important numbers, it is common for people to spell out some of these numbers in their favorite numbers
# For example, 'Mike' can be spelled on a phone by pressing 6453
# This is only done for words less than 8 characters long.

	#important_numbers.extend(getPhoneSpelling(important_words))
	
	
	#ALPHA NOTE: In future releases, there may be a prompt here that creates a combination
	#of subject's initials - as requested in https://github.com/Mebus/cupp/issues/10
	# I deemed it more important to get the Alpha release up and running before including this,
	# but it is on the list
	
#------------------Process the Words, Create Variants----------------------#

	divider()
	print("\n-------All Information Collected, Beginning Processing-------\n")
	divider()


	# Create ALLCAPS, all lowercase and TitleCase Variations of important Words
	# these are done separately, so variations of variations are not created
	addendum_important_words = [(important_words[i]).title() for i in range(len(important_words))]
	addendum_important_words.extend([important_words[i].upper() for i in range(len(important_words))])
	addendum_important_words.extend([important_words[i].lower() for i in range(len(important_words))])
	important_words.extend(addendum_important_words)
	
	#Create Reversals of important words - optional but recommended for accuracy
	print("\n Do you wish to create reversals of all words (not numbers) mentioned so far?")
	print (" This will double the quantity of words to be permuted from " + str(len(important_words)) + " to " + str(2 *len(important_words)) + '.')
	print (" This will DRASTICALLY affect the number of possibilities generated. \n")
	reverse_word_choice = raw_input('> Would you like to do this? (Y/N) >:').upper()

	reverse_word_choice = spaceShaver(reverse_word_choice) # cleans up input and stops false negative with "yes "

	#If user wishes, create reversal of words
	if reverse_word_choice in "YES" and len(reverse_word_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
		
		important_words.extend([(important_words[i])[::-1] for i in range(len(important_words))]) #creates reversals of all variations and originals
		
	print (' [+] Word Reversals Created')
	
	important_words.sort(key = len) # sorts by length
	important_words = list(set(important_words)) # removes duplicate words


#------------------Process the Numbers, Extract Alternative Forms----------------------#

	#Extracts individual days and years out of full dates
	for i in range(len(important_full_dates)):
		important_days.append((important_full_dates[i])[0:4])
		important_years.append((important_full_dates[i])[4:8])
		
		
	#This script's default format is DDMMYYYY for dates, but we also want to support MMDDYYYY
	#This gets dates in DDMM and MMDD format
	other_format_days = []
	for i in range(len(important_days)): other_format_days.append((important_days[i])[2:4] + (important_days[i])[0:2])
	important_days.extend(other_format_days)

	#We've prompted for days that had to be 4 digits long
	#A person might not enter in 2 February as 02/02, but 2/2
	#This function generates variations without the optional zero
	important_days.extend(createNoLeadingZeroDays(important_days))

	#Sort and remove duplicates from important_days
	important_days = list(set(important_days))


	#Make a list of the transformation of YYYY years into 2 digits
	# I.E 2017 - > 17
	twodig_years = []
	for i in range(len(important_years)): twodig_years.append((important_years[i])[2:4])
	important_years.extend(twodig_years)
	
	# Since alternate forms such as DDMM into MMDD, 03/03 into 3/3, and 2017 into 17
	# BEWGor must ensure full dates have been created from all variations
	# In future releases, this may also be done in reverse order, year + day
	# But for now, we will let the permutations take care of that
	for day in important_days: 
		for year in important_years:
			important_full_dates.append(day + year)
		
	# In future releases, this may also be done in reverse order, year + day

	#Now both years and days have been processed, let's combine them
	# It is safer to do this one by one in case we have empty values
	important_numbers.extend(list(set(important_days))) # adds important days with the duplicates removed
	important_numbers.extend(list(set(important_years))) # adds important days with the duplicates removed
	important_numbers.extend(list(set(important_full_dates))) # adds important days with the duplicates removed
	
	important_numbers.sort(key=len) # sorts by length 
	important_numbers = list(set(important_numbers)) #removes duplicates
	
	divider()
	
	#Requests to create reverse versions of all numbers given so far - optional but improves wordlist quality
	#A person might know enough not to include an obvious number like their birth year, but want to keep
	#things easy to remember - in this instance they may simply reverse the number
	print("\n Do you wish to create reversals of all numbers (years, days, etc.) mentioned so far?")
	print(" Note these are not reversals in the style of '01012017' becoming '20170101,'")
	print(" But literal reversals. '01012017' becomes '71021010' ")
	print (" This will double the quantity of numbers to be permuted from " + str(len(important_numbers)) + " to " + str(2 *len(important_numbers)) +'.')
	print (" This will DRASTICALLY affect the number of possibilities generated. \n")
	reverse_number_choice = raw_input('> Would you like to do this? (Y/N) >:').upper()

	reverse_number_choice = spaceShaver(reverse_number_choice) # cleans up input and stops false negative with "yes "

	#If user wishes, create reversal of numbers
	if reverse_word_choice in "YES" and len(reverse_word_choice) != 0: #if user enters 'yesno,' they think they are slick and BEWGor will treat their input as a 'yes'
		
		important_numbers.extend([(important_numbers[i])[::-1] for i in range(len(important_numbers))]) #Get reversals of all the numbers, if requested
	#Get reversals of all the numbers, if requested
	
		print (' Number Reversals Created')
	

	#Sort and remove duplicates from important_numbers again, now that we have made changes
	important_numbers = list(set(important_numbers))

	#Put the words and the numbers on the same list, ready to create permutations 
	info =important_words
	info.extend(important_numbers)
	info.sort(key=len)

	#This block calculates the lengths of permutations in lengths 1-5
	perm_lens = [0] * 6 #creates a list of 6 zeros
	for i in range(1,6):
          perm_lens[i] = nPr(len(info),i) + perm_lens[i-1]
		  # Calculates the number of permutations at the given permutation length,
		  # And adds the number of permutations from the lengths before it
		  # This is done because we do not just create permutations for a GIVEN length
		  # But for the given length and lengths under it
		  # I.E - if the given length is 3, we calculate permutations for lengths of
		  # 1, 2 AND 3. Not JUST 3.

	divider()
	print (''' ---- Maximum Number of Items per Line/Permutation Length ----
		   
 What is the maximum number of items per entry you would like?
 For example, if you have a name of Sinbad Sailor and the birth year 1001,
 A maximum item length of one would produce variations of "Sinbad" "Sailor" and "1001"
 But not "SinbadSailor" or "Sinbad1001"
    3 is the default number, which would produce all permutations of
 "Sinbad" "Sailor" and "1001" permuted with one another, as well as
 the single items, and just 2 permuted items.
    The increasing this number will **QUICKLY** and **DRASTICALLY**
 change the size of your wordlist. Maximum number of items per entry is
 equal to 5, but it is **STRONGLY** advised you do not exceed 3.
 
 The computer with 8GB of RAM this program was first tested on often could not handle a length of 4.
 Optimizaiton of this process is in progress.
		  ''')
	print ("Permutation length of 1 will produce " + str(perm_lens[1]) + " lines.")
	print ("Permutation length of 2 will produce " + str(perm_lens[2]) + " lines.")
	print ("Permutation length of 3 will produce " + str(perm_lens[3]) + " lines.")
	print ("Permutation length of 4 will produce " + str(perm_lens[4]) + " lines.")
	print ("Permutation length of 5 will produce " + str(perm_lens[5]) + " lines.")

	certain = False
	# This boolean halts advancement of BEWGor until the user fully 
	# understands how many lines will be generated
	
	perm_length = raw_input('\n> Enter the maximum permutation length >:')
	while not certain:
	
		while not at_least_one_dig_reg.match(str(perm_length)): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			perm_length = raw_input('> Enter the maximum permutation length >:')

		perm_length = int(perm_length)
		
		if  perm_length > 5:
			print (" [-] Exceeded maxiumum permuation length, setting length to 5. ")
			perm_length = 5
			hold_up()
		
		elif len(str(perm_length)) ==0 or (perm_length) < 1:
			print (" [-] Empty or invalid entry, setting max number of items to 3")
			perm_length = 3
			hold_up()
	
		perms = perm_lens[perm_length]
	
		#Puts a long string of numbers into perspective
		print('A permutation length of ' + str(perm_length) +' will have to parse ' + str(round(perms/1000000000.00,2)) + ' billion (' + str(round(perms/1000000.00,2)) + ' million) lines.')
		big_num_choice = raw_input('Are you sure you want to use this permutation length? (Y/N) >:').upper()
	
		big_num_choice = spaceHandler(big_num_choice) # cleans up input and stops false negative with "yes "
	
		#ensures user knows what they are getting into
		if big_num_choice in "YES" and len(big_num_choice) != 0: certain = True 
		else: perm_length = raw_input('> Enter the maximum permutation length >:')
		
	
	divider()
	
	# This section provides a lower length boundary on lines added to the file
	print("""    ---- MINIMUM Line Length ----
 BEWGor will create all permutations of the items inputted.
 This can be unweildy, and you might not want to keep them all.
 The default --MINIMUM-- line length is 1
 You may set a minimumline length below:
 """)
	min_line_length = raw_input('> Enter the minimum line length >:')
	
	if len(min_line_length) != 0:
		
		while not at_least_one_dig_reg.match(min_line_length): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			min_line_length = raw_input('> Enter the minimum line length >:')
		min_line_length = int(min_line_length)
	else: min_line_length = 1
	
	divider()
	
	#This section proivdes an upper length limit on lines added to the file
	print("""    ---- MAXIMUM Line Length ----
 BEWGor will create all permutations of the items inputted.
 This can be unweildy, and you might not want to keep them all.
 The default ++MAXIMUM++ line length is 20.
 
 If you have input long words or have a permutation length of 4 or 5,
 It is recommended you increase this value.
 
 You may set a maximum line length below:
 """)
	max_line_length = raw_input('> Enter the maximum line length >:')
	if len(max_line_length) != 0:
		while not at_least_one_dig_reg.match(max_line_length): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			max_line_length = raw_input('> Enter the maximum line length >:')
		max_line_length = int(max_line_length)
	else: max_line_length = 20
	
	
	divider()
	print("\n------Output Wordlist File Name----- \n")
	print(""" This action will OVERWRITE any identically named
 file in your current directory.
 If a name is not provided, the default name is 'BEWGor_Wordlist.txt'
 
 The filename can only include letters, numbers, dashes and underscores.
 """)
	outfile_name = raw_input("> Enter the output file name, without the .txt extension >:")
	
	while len(outfile_name) !=0 and not filename_reg.match(outfile_name): #Yes, the '.' belongs in the regex but... next relase.
			print(' [-] Invalid filename, try again.')
			outfile_name = raw_input("> Enter the output file name, without the .txt extension >:")
			
	if len(outfile_name) ==0 :
		outfile_name = "BEWGor_Wordlist"
		
	print ('\nReady to generate '+str(perms)+' lines and write the lines of appropriate \nlength to '+outfile_name+'.txt!')
	pause = raw_input('\n     Press ENTER to let the BEWGor fly...')

	outfile = open(outfile_name+'.txt','w+') #open file
	outfile.truncate() #clear file

	print ("\n Computing permutations and writing lines.\n This can take a while...")
	for i in range(1, perm_length+1):
			bounded_permutations(info, min_line_length, max_line_length,outfile_name, i)
			
	outfile.close() #close file
	
	divider()
	print ("\n"+outfile_name+".txt has been written. \n")
	
	divider()
	showMiniName()
	print('\nThank you for using BEWGor!')
	exit()
