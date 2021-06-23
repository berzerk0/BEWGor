#usr/bin/env python3
#Class with main-subject specific information
# Child class of PERSON

from .person import Person
from .utilities import *
from .validator import *

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

		gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
		while len(gender) != 0:


			if nonzero_blankspace_reg.match(gender): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")

			elif not location_chars_reg.match(gender): #checks to see if input contains any characters unlikely to be in this category
				print (" [-] Input contains invalid characters, try again.")
				gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")

			elif gender in gender_cands or gender in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")

			else:
				if ' ' in gender and not male_reg.match(gender) and not female_reg.match(gender):
				#if a gender contains spaces, split it up so BEWGor can join the words together with variations

					gender_cands.extend((spaceHandler(gender))) #create variants of input if input contains spaces
					entered.append(gender) #adds to 'entered' list to prevent double-adds
					gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")

				else:
					gender_cands.append(gender.lower())

					if male_reg.match(gender):
						gender_cands.append('male')
						entered.append('male')

						male_syn_choice = input('> Would you like to include 10 English synonyms for Male? (Y/N) >:').upper()
						male_syn_choice = spaceShaver(male_syn_choice)

						if male_syn_choice in "YES" and len(male_syn_choice) != 0:
							gender_cands.extend(['man','bro','dude','sir','gent','mr','mister','guy','boy','boi'])
							print ('\n [+] Synonyms for Male added \n')

					if female_reg.match(gender):
						gender_cands.append('female')
						entered.append('female')

						fem_syn_choice = input('> Would you like to include 10 English synonyms for Female? (Y/N) >:').upper()
						fem_syn_choice = spaceShaver(fem_syn_choice)

						if fem_syn_choice in "YES" and len(fem_syn_choice) != 0:
							gender_cands.extend(['woman','girl','gal','chick','lady','mrs','ms','miss','misses','grrl','gurl','madame'])

					entered.append(gender)

					gender = input("> Enter a value for " + self.name +"'s Identified Gender, or press enter to move on >:")
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

		nationality = input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(nationality) !=0:

			if nonzero_blankspace_reg.match(nationality): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				nationality = input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

			elif not location_chars_reg.match(nationality): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				nationality = input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

			elif nationality in nationality_cands or nationality in entered:
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				nationality = input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

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

					nationality = input("> Enter a value for " + self.name +"'s Country of Origin, or press enter to move on >:")

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

		natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

		#If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(natl_demonym) != 0:

			if nonzero_blankspace_reg.match(natl_demonym): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

			elif not location_chars_reg.match(natl_demonym): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

			elif natl_demonym in natl_demonym_cands or natl_demonym in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

			else: #if its likely to be valid
				if ' ' in natl_demonym: #if a natl_demonym contains spaces, split it up so BEWGor can join the words together with variations
					natl_demonym_cands.extend((spaceHandler(natl_demonym)))
					entered.append(natl_demonym) #adds to 'entered' list to prevent double-adds

					natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

				else:
					natl_demonym_cands.append(natl_demonym)
					entered.append(natl_demonym) #adds to 'entered' list to prevent double-adds

					natl_demonym = input("> Enter " + self.name +"'s National Demonyms, or press enter to move on >:")

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

		natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

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
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif int(natl_day[2:4]) > 12: #ensures DDMM format is correct
				print (" [-] Invalid Month. After December, but before January - check your DDMM format")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif int(natl_day[0:2]) > 31: #ensures no dates after the 31st are entered
				print (" [-] Invalid Day, no month has more than 31 days. Try again.")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif not doesDayExist(natl_day[0:4]): #ensures date provided exists
				print (" [-] Invalid Date. That month has fewer days. Try again.")
				valid = False
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif len(natl_day) == 8 and isItInvalidLeap(natl_day): #ensures full date is not invalid leap day
				print (" [-] That day did not exist that year. Try again.")
				valid = False
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

			elif len(natl_day) == 8 and isFullDateFuture(natl_day): #ensures full date is not in the future
				print (" [-] You have entered a date in the future, that can't be right.")
				valid = False # without this boolean, we might get stuck in a logical loop if the user enters an invalid input followed by an empty one
				natl_day = input("> Enter " + self.name +"'s National Day in DDMMYYYYY or DDMM format >:")

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

		ethnicity = input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")

		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(ethnicity) !=0:

			if nonzero_blankspace_reg.match(ethnicity): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				ethnicity = input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")

			elif not location_chars_reg.match(ethnicity): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				ethnicity = input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")

			elif ethnicity in ethnicity_cands or ethnicity in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				ethnicity = input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")

			else:
				if ' ' in ethnicity: #if a ethnicity contains spaces, split it up so BEWGor can join the words together with variations
					ethnicity_cands.extend((spaceHandler(ethnicity)))
					entered.append(ethnicity)

				else:
					ethnicity_cands.append(ethnicity)
					entered.append(ethnicity)

				ethnicity = input("> Enter an ethnonym for " + self.name + ", or simply press enter to move on >:")


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
		birthplace = input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(birthplace) !=0:

			if nonzero_blankspace_reg.match(birthplace): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				birthplace = input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

			elif not location_chars_reg.match(birthplace): #checks to see if input contains any characters that probably wouldn't be in a Country's name
				print (" [-] Input contains invalid characters, try again.")
				birthplace = input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

			elif birthplace in birthplace_cands or birthplace in entered:
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				birthplace = input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

			else:
				if ' ' in birthplace: #if a birthplace contains spaces, split it up so BEWGor can join the words together with variations

					birthplace_cands.extend((spaceHandler(birthplace)))
					entered.append(birthplace)


				else:
					birthplace_cands.append(birthplace)
					birthplace_cands=list(set(birthplace_cands))
					entered.append(birthplace)

				birthplace = input("> Enter " + self.name +"'s birthplace, or press enter to move on >:")

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
		hometown = input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

		# If the user enters a value, it must meet criteria
		# until all criteria is met, or a Null value is entered, BEWGor will keep asking
		while len(hometown) != 0:

			if nonzero_blankspace_reg.match(hometown): #ensures input isn't only blank space characters
				print (" [-] Empty Space, try again.")
				hometown = input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

			elif not location_chars_reg.match(hometown): #checks to see if input contains any characters that probably wouldn't be in a location's name
				print (" [-] Input contains invalid characters, try again.")
				hometown = input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

			elif hometown in hometown_cands or hometown in entered: #check for double input
				print (" [-] That input has already been added to the list.\n  Some inputs are added automatically, try again.")
				hometown = input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

			else:
				if ' ' in hometown: #if a hometown contains spaces, split it up so BEWGor can join the words together with variations
					hometown_cands.extend((spaceHandler(hometown)))
					entered.append(hometown)

				else:
					hometown_cands.append(hometown)
					entered.append(hometown)

			hometown = input("> Enter " + self.name +"'s hometown, or press enter to move on >:")

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