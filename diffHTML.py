# A small script that can download or import HTML files
# After importing, it generates a diff file for the two.
# Additionally, it can be run from the command line with arguments,
# So as to increase efficiency.

# Jacob Orner (jayc0b0)
# ~ 18 July, 2015

import difflib
import urllib
import sys


def main():
	if len(sys.argv) == 1:
		print '''
It looks like you ran this script without any arguments or incorrectly.
* If you'd like to use this script to download your HTML files:
	+ Run this script with the argument "dl"
	+ EX: >> python scriptName.py DLhtml
* If you'd like to use this script to generate a diff files:
	+ Save your two HTML files in the same directory as this script.
	+ Run this script with your HTML filenames as the two arguments.
	+ EX: >> python scriptName.py file1.html file2.html
		'''
		raw_input("Press any key to exit...\n>> ")
		sys.exit()
	elif len(sys.argv) == 2 and sys.argv[1] == "dl":
		URL = str(raw_input("Please enter the URL for the 1st page you wish to retrieve.\n>> "))
		print "Your URL is...\n>> " + URL
		fileName1 = raw_input("Please enter the filename you would like to save the HTML as, including the .html extension.\n>> ").lower()
		urllib.urlretrieve(URL, fileName1)
		URL = str(raw_input("Please enter the URL for the 2nd page you wish to retrieve.\n>> "))
		print "Your URL is...\n>> " + URL
		fileName2 = raw_input("Please enter the filename you would like to save the HTML as, including the .html extension.\n>> ").lower()
		urllib.urlretrieve(URL, fileName2)
		choice = str(raw_input("Would you like to compare files now? Y/N\n>> ")).lower()
		if choice == "y":
			diffHTML(fileName1, fileName2)
		else:
			raw_input("Input Error. Press any key to exit...\n>> ")
			sys.exit()
	elif len(sys.argv) == 3:
		diffHTML(sys.argv[1], sys.argv[2])
	else:
		print '''
It looks like you ran this script without any arguments or incorrectly.
* If you'd like to use this script to download your HTML files:
        + Run this script with the argument "dl"
	+ EX: >> python scriptName.py DLhtml
* If you'd like to use this script to generate a diff files:
	+ Save your two HTML files in the same directory as this script.
	+ Run this script with your HTML filenames as the two arguments.
	+ EX: >> python scriptName.py file1.html file2.html
		'''
		raw_input("Press any key to exit...\n>> ")
		sys.exit()


def diffHTML(fileName1, fileName2):
	file1 = open(fileName1, 'r')
	file2 = open(fileName2, 'r')
	diff = difflib.unified_diff(file1.readlines(), file2.readlines(), lineterm='')
	delta = '\n'.join(list(diff))
	open('diff.txt', 'w').close()
	diffFile = open('diff.txt', 'a')
	diffFile.write(delta)
	raw_input("Writing to diff.txt...\n>> ")
	raw_input("Press any key to exit...\n>> ")
	diffFile.close()
	sys.exit()


if __name__ == "__main__":
	main()

