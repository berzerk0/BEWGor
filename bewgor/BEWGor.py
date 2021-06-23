#usr/bin/env python3
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


#import necessary libraries
import argparse
import re, sys, time #re for regular expression use, sys for argument passing, time for determining when an event occured
from datetime import datetime # datetime in order to determine when an event occurred


from .main_subject import MainSubject
from .person import Person
from .banners import (
	showTheName,
	showMiniName,
	showNose
)

# I am a little lazy to write all function and variable names
from .utilities import *
from .information import *
from .validator import *

def parse_args():
	parser = argparse.ArgumentParser(
			description = """
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
                """,
	formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('-i', '--interactive',
						action='store_true',
						help='Prompts user for information on a Person to generate potential passwords')
	parser.add_argument('-q', '--quiet',
						action='store_true',
						help='Run quietly')

	return parser

def main():
	parser = parse_args()
	args = parser.parse_args()

	if not args.interactive:
			print(parser.print_help())
			exit(1)

	if not args.quiet:
			showNose() #Show the Main Logo and Puns.
	showTheName() #Show the ASCII Title

	#These lists will be populated with inputs
	important_years = []
	important_days = []
	important_full_dates = []
	important_numbers = []
	important_days = []
	important_words = []

	pause = input('Press enter to begin...')

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
 
	associates_choice = input("Do you have information on any of " + main_subject.name + "'s family or associates? (Y/N) >:").upper()
	
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
	reverse_word_choice = input('> Would you like to do this? (Y/N) >:').upper()

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
	reverse_number_choice = input('> Would you like to do this? (Y/N) >:').upper()

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
	
	perm_length = input('\n> Enter the maximum permutation length >:')
	while not certain:
	
		while not at_least_one_dig_reg.match(str(perm_length)): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			perm_length = input('> Enter the maximum permutation length >:')

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
		big_num_choice = input('Are you sure you want to use this permutation length? (Y/N) >:').upper()
	
		big_num_choice = spaceHandler(big_num_choice) # cleans up input and stops false negative with "yes "
	
		#ensures user knows what they are getting into
		if big_num_choice in "YES" and len(big_num_choice) != 0: certain = True 
		else: perm_length = input('> Enter the maximum permutation length >:')
		
	
	divider()
	
	# This section provides a lower length boundary on lines added to the file
	print("""    ---- MINIMUM Line Length ----
 BEWGor will create all permutations of the items inputted.
 This can be unweildy, and you might not want to keep them all.
 The default --MINIMUM-- line length is 1
 You may set a minimumline length below:
 """)
	min_line_length = input('> Enter the minimum line length >:')
	
	if len(min_line_length) != 0:
		
		while not at_least_one_dig_reg.match(min_line_length): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			min_line_length = input('> Enter the minimum line length >:')
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
	max_line_length = input('> Enter the maximum line length >:')
	if len(max_line_length) != 0:
		while not at_least_one_dig_reg.match(max_line_length): #check that the input is valid
			print (" [-] Invalid input. Try again.")
			max_line_length = input('> Enter the maximum line length >:')
		max_line_length = int(max_line_length)
	else: max_line_length = 20
	
	
	divider()
	print("\n------Output Wordlist File Name----- \n")
	print(""" This action will OVERWRITE any identically named
 file in your current directory.
 If a name is not provided, the default name is 'BEWGor_Wordlist.txt'
 
 The filename can only include letters, numbers, dashes and underscores.
 """)
	outfile_name = input("> Enter the output file name, without the .txt extension >:")
	
	while len(outfile_name) !=0 and not filename_reg.match(outfile_name): #Yes, the '.' belongs in the regex but... next relase.
			print(' [-] Invalid filename, try again.')
			outfile_name = input("> Enter the output file name, without the .txt extension >:")
			
	if len(outfile_name) ==0 :
		outfile_name = "BEWGor_Wordlist"
		
	print ('\nReady to generate '+str(perms)+' lines and write the lines of appropriate \nlength to '+outfile_name+'.txt!')
	pause = input('\n     Press ENTER to let the BEWGor fly...')

	outfile = open(outfile_name+'.txt','w+') #open file
	outfile.truncate() #clear file

	print ("\n Computing permutations and writing lines.\n This can take a while...")
	for i in range(1, perm_length+1):
			bounded_permutations(info, min_line_length, max_line_length,outfile, i)
			
	outfile.close() #close file
	
	divider()
	print ("\n"+outfile_name+".txt has been written. \n")
	
	divider()
	showMiniName()
	print('\nThank you for using BEWGor!')
	exit()
