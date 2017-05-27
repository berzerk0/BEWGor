# BEWGor - Bull's Eye Wordlist Generator
## *Pick your knows!*

#### Does your password rely on predictable patterns of accessible info? 

__Inspired by and based on [Mebus' CUPP](https://github.com/Mebus/cupp)__

ALPHA RELEASE COMING BEFORE THE END OF MAY 2017

## Under Construction, no code YET - working out the kinks.

![Pick Your Knows!](https://raw.githubusercontent.com/berzerk0/BEWGor/master/bewgor_nose.png)

## ALPHA RELEASE IS ‘FLAT’
  This means all associates are treated equally, and BEWGor only queries basic information about them

## How do I use BEWGor?

Clone it or download the zip file.
Run it with Python 2 - __NOT Python 3__

    python BEWGor.py #runs normally

    python BEWGor.py -help #presents a help screen that admittedly doesn’t say much

    python BEWGor.py -input #also runs normally


## What does BEWGor do?

At its core, BEWGor is designed help with ensuring password security.
It is a Python script that prompts the user for biographical data about a person (called the Subject),
which is then used to create likely passwords for that Subject.


All information is manually inputted and stored locally. 
No information is sent to any other location, or pulled from the web.

*If you want to improve your password security, run BEWGor on __yourself__!*

To see an example, check out the 
[Sample-Output File - 1.6 Million Lines](https://raw.githubusercontent.com/berzerk0/BEWGor/master/Sample_Output.txt)


## What are “likely” passwords for a given subject?

When it comes to generating passwords, humanity, on average, has not demonstrated too much creativity. 
The most common password is *123456* and the 2nd most common is “*password*. 
My first project, __[Probable-Wordlists](https://github.com/berzerk0/Probable-Wordlists)__ explores this in depth. 
It contains billions of the world’s most common passwords - in order of how common they are. 


If a person doesn’t use a single-word password straight out of a dictionary, they are likely to use words from their personal lives. These words are easy to remember and not screamingly obvious to others - and for many, those are good enough reasons to use them as passwords…

__Does your password sound like the answer to a security question?__

Passwords often include information like:
 * Mother’s Maiden Name
 * Name of a Childhood Pet
 * Birthdays of the password holder or a loved one
 * The password holder’s nationality

Due to Social Media use and the strength of modern day Open-Source Intelligence (OSINT), this information is *NOT HARD TO COME BY.*
 Therefore, making it it your password is *NOT SECURE.*

 __BEWGor asks for information about a person, and those they associate with, and generates potential passwords based on that data.__


Did your subject have a dog named Spot?
Was your subject born in 1980?

BEWGor will come up with many variations of these two pieces of information:

*spot1980, 1980spot, SPOT80, 80Spot and more.*

## BEWGor is based on CUPP, How Are They Different?

BEWGor takes the simplest features of CUPP and does a very deep dive.
It prompts the user for a lot more specific information, but not have all of CUPP's capabilities.

#### What Does BEWGor Do That CUPP Doesn’t?
 * Vastly Increased Information Detail on Main Subject
 * Includes Support for an arbitrary number of family members and pets
 * By using permutations to generate possible passwords, BEWGor can generate huge numbers of passwords
 * Create Upper/Lower/Reverse variations of inputted values
 * Save raw inputted values to a *Literals* file before variations are generated
 * Set upper and lower limits on output line length 
 * Check that an inputted Birthday is valid (not in the future, a false leap day, June 32nd, etc.)
 

#### What Does CUPP Do That BEWGor Doesn’t?
 * Allow the User to download Wordlists from within CUPP
 * Create ‘l33t’ variations of given lines
 * Allow the user to add special characters at the end of words without entering them specifically
 * Limit the number of outputs to the most likely formats, such as *Name+birthyear*

#### BEWGor has answers to (most of) these functionalities
 1. I’ve got you covered on wordlists - check out my other project [Probable-Wordlists](https://github.com/berzerk0/Probable-Wordlists)
 2. ’l33t’ variations might be included in a future release, but for now, using a program like [HashCat](https://hashcat.net/hashcat/) will allow you to create 133t-style and other variations of a BEWGOr wordlist as-needed
 3. HashCat can do this as well with the ‘rule’ function
 4. BEWGor is not subtle, it will generate ALL the combinations - including plenty of unlikely ones. 

This may be slimmed down in the future, but why not err on the side of having all the possibilities?


## Areas With Room For Improvement
 * Heavy Handed! Big files, intensive (produces a lot of unlikely variations)
 * Doesn’t handle non-ASCII well
 * Doesn’t handle names that include spaces well, such as *von Braun*
 * Biased towards monogamous behavior. Doesn’t ask about past significant others, or multiple current significant others
 * Treats Pets the same way it treats Children, Siblings and Significant others
 * Doesn’t include user-defined associates (mentor, protogé, any relationship I didn’t think of yet.)
 * Has mixed feelings about the word ‘of’


### What information does BEWGor collect?

*In Alpha release, associates are limited to:*

 *1 Significant other, and an arbitrary number of Children, Parents, Siblings and Pets.*

##### All Subjects
 * Full Name
 * Maiden Name
 * Nicknames/Usernames
 * Birthday (day and month)
 * Birth Year
 * From this information, it can generate initials, Greek and Chinese Zodiac Signs and Birthstone (Western and Hindu Style)


##### Main Subject:
 * Everything in All Subjects
 * Gender Identity
 * Nationality
 * National Demonym (Such as Briton, or British)
 * National Day 
 * Ethnicity
 * Birthplace
 * Hometown

##### Additional:
 * Full Dates (input the day they founded their company, anniversary, etc.)
 * Days
 * Years
 * Words
 * Numbers
 * Range of Years (if you don’t know subject’s exact age)

## Future Developments

##### Future versions will query far more detail about the main subject, such as
 * National Motto, Monarch’s Name
 * Local Demonym (Londoner, Parisian, Texan)
 * Addresses, Phone Numbers, contact information
 * Career
 * Academic History
 * Favorite things
 * Clubs and other associations
 * and more...

#### Relationship-specific prompts/classes like:
 * S/O - Meeting place, anniversary, wedding location...
 * Pets - breed, age, multiple  pets…

 
#### Ability to Save the Inputted Values - known as ‘literals’ to a Special File
This file can be edited outside of the script but can be fed into BEWGor directly, no prompting.



## Want to Contribute?
 See the Contributing.md file for guidelines


## Disclaimer and License
 * BEWGor is for LAWFUL, ETHICAL AND EDUCATIONAL PURPOSES ONLY.
 * The files contained in this repository are released "as is" without warranty, support, or guarantee of effectiveness. 
 * _However, I am open to hearing about any issues found within these files and will be actively maintaining this repository for the foreseeable future. If you find anything noteworthy, let me know and I'll see what I can do about it._



 [![BEWGor uses the GNU GPL v3](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)


BEWGor uses the GNU GPL v3 License. 
Terms can be found in the license file

or by clicking the GNU GPL v3 button above this line. 



