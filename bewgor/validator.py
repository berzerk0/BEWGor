#usr/bin/env python3

import re

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
