import pickle
#Used for long term storage of data
import time
#Used for the 'wait()' function
from collections import OrderedDict
#For organized, in order, dictionaries
import pdb
#'Python Debugger: pdb.set_trace()
class color:
	BLUE = '\033[94m'
	RED = '\033[91m'
	GREEN = '\033[92m'
	DARKCYAN = '\033[36m'
	YELLOW = '\033[93m'
	PURPLE = '\033[95m'
	BOLD = '\033[1m'
	END = '\033[0m'
#Colors for use in text^
def colorThis(word, color1, color2="", resumeColor="", resumeColor2=""):
	return color1 + color2 + word + color.END + resumeColor + resumeColor2
#Used to color specific pieces of text ------ (WORD/SENTENCE, FIRSTCOLOR, SECONDOPTIONALCOLOR, COLORTHATAPPEARED BEFORE)
#!!!!!!!! WHEN USING THIS FUNCTION, if you are using the 'resumeColor', you must include a '' for the third slot (second color)
		
def superSpace(x):
        count = x
        while count > 0:
                print ""
                count = count - 1
#Used for spacing interface

def lineMake():
	print "----------------------------------------------------------------------------------------------------------"

def makeAG():
	print "========================" 
	wait(.3)
	print "=                      =" 
	wait(.3)
	for i in range(4):
		print "=" 
		wait(.3)
	print "=       ================"
	wait(.3)
	for i in range(4):
		print "=                      =" 
		wait(.3)
	print "========================"
#Draws 'G' 
def showCard(database, name, date, parlist):
	print color.GREEN + color.BOLD + date + ":" + color.END
        #Date header
	parCounter = 0
	for hole in database[name][date]:
        	if userData[name][date]["pineOaks"] == "Yes" and parCounter < 9:
                	par = color.DARKCYAN + " (Par: " + str(parlist[parCounter]) + ")" + color.END
                else:
                	par = ""
                      	#prints the pine oaks par value in a variable, or is blank

                print color.BOLD + hole + ": " + color.END + str(database[name][date][hole]) + par
                #Prints each hole in bold
                parCounter += 1
def waitingEnter():
	waitingEnter = raw_input(color.RED + "Press enter when done viewing" + color.END)
       	superSpace(50)
        #Waits for user to hit enter
def wait(x):
        time.sleep(x)
#Used to slow program down        

def pickleOut():
	outFile = open("golfingAppData.txt", "wb")
        pickle.dump(userData, outFile)
        outFile.close()
#Used to store permanent information

def pickleIn():
        inFile = open("golfingAppData.txt", "rb")
        userData = pickle.load(inFile)
        inFile.close()
        return userData
#Used to retrieve user permanent information
userData = dict(pickleIn())
#Brings in user data
pineOaksPars = [4,5,4,3,4,3,3,4,4]
emptyHoles = OrderedDict([("Hole1", 0), ("Hole2", 0), ("Hole3", 0), ("Hole4", 0), 
				("Hole5", 0), ("Hole6", 0), ("Hole7", 0), ("Hole8", 0), ("Hole9", 0), ("Total", 0)])

#Used to create score cards

superSpace(50)
#Spaces to 'open' progam
#print userData
print color.GREEN + "Welcome to the " + colorThis('Golf Tracking App.', color.BOLD, "", color.GREEN) + "\n" + \
		"Use this application to track your performance throughout the year"
#Beginning Title
superSpace(2)

mainLoop = True
while mainLoop == True:
#Program Loop

	print color.BLUE + color.BOLD + "You can either " + colorThis('save', color.DARKCYAN, color.BOLD, color.BLUE, color.BOLD) + \
		 	" a score into the database, " + colorThis('search', color.DARKCYAN, color.BOLD, color.BLUE, color.BOLD) + " for a scorecard, or " + \
		 	colorThis('delete information.', color.DARKCYAN, color.BOLD, color.BLUE) + "\nYou can also view the Help and Credits Pages" + color.END
	superSpace(1)

	menuChoice = (raw_input("Enter Your Choice: ")).lower()
	#Menu Choice

#Menu_Save -v
	if menuChoice == "save":
		superSpace(50)
		name = (raw_input("Enter name for entry: ")).title()
		if name not in userData:
			userData[name] = {}
		#Checks if user name already exists, and if not, creates a dictionary

		print "Did you golf at Pine Oaks? Yes or No. "
		pineOaksCheck = raw_input("-> ").lower()
		#Checks to see if the outing was Pine Oaks. Used later for par comparison
		superSpace(50)
		print "Okay, Enter the date that you golfed in DD/MM/YYYY format."
		date = raw_input("-> ")

		#WITHIN THIS IF/ELSE STATEMENT -v
		if pineOaksCheck == 'yes' or pineOaksCheck == 'y':
			userData[name][date] = OrderedDict(emptyHoles)
			userData[name][date]["pineOaks"] = "Yes"
        	else:
            
			userData[name][date] = OrderedDict(emptyHoles)
			userData[name][date]["pineOaks"] = "No"
		#Creates key for the inputed date, for the user
		
		#NOPAR IS GIVEN A VALUE WHEN NOT ASSIGNED -^

		superSpace(50)
		print "Now enter the stroke values for each hole:"
		superSpace(1)	
		for hole in userData[name][date]:
			value = 0
			#Iterates through the dictionary, adding values as it goes
			if hole != "Total" and hole != "pineOaks": #Skips over the non-hole keys
				value = int((raw_input(hole + ": ")))
					
				#Stroke Value
				userData[name][date][hole] = value
				userData[name][date]["Total"] += value
		superSpace(50)
		print color.BOLD + "Here is your score card..." + color.END
		wait(1.3)
		
		showCard(userData, name, date, pineOaksPars)
		waitingEnter()

		print colorThis('Thank You ', color.RED) + "for submitting a score card!\nFeel free to enter another one, or simply type 'quit'" 
		superSpace(1)
				#Adds stroke value to running total
		pickleOut()
#Menu_Search -v	
	elif menuChoice == "search":
	#Allows user to search through available score cards
		superSpace(50)
		searchLoop = True
		while searchLoop == True:
		#Search menu loop
			
			if len(userData) == 0:
				print "Oops, it looks like there is no data to search!\n" + \
					"Returning to search menu..."
				wait(2)
				superSpace(50)
				break
				#No user data, Returns to main menu
			print color.BOLD + "You can search by " + colorThis('name', color.RED, "", color.BOLD) +  ", or " + \
			 		colorThis('date.', color.RED) + "\nEnter whichever you would like. "

			searchChoice = (raw_input("->")).lower()
			#Users choice of Name or Date
		
			if searchChoice == "name" or searchChoice == 'n': #Menu_Search
				superSpace(50)
				print "Okay, enter the name you are looking for."
				nameSearch = (raw_input("->")).title()
				#User inputed name to search for	
				superSpace(50)
				#Checks to decide when all names have cycled
				
				if nameSearch in userData:
				#Name is found
					print "You can view score cards by " + colorThis('date', color.RED) + "(d), see " + \
							colorThis('all dates golfed', color.RED) + "(a), or " + colorThis('view averages', color.RED) + "(vg)"

					
					nameChoice = raw_input("->").lower()
					superSpace(50)
					#User chooses what to do with account

					if nameChoice == "date" or nameChoice == 'd':
						#User chooses to see a specific card
						print "Dates:"
						for date in userData[nameSearch]:
							print colorThis(date, color.PURPLE)
                        	#Prints all dates

						date = raw_input("Please enter a date: ")		
						if date in userData[nameSearch]:
						#Makes sure user enters a valid date
							superSpace(50)
							showCard(userData,nameSearch, date, pineOaksPars)
						else:
							print "Please enter a correct date"
					
					elif nameChoice == "all" or nameChoice == 'a':
						#User chooses to see all dates golfed
						print "You golfed on:"
						for date in userData[nameSearch]:
							print colorThis(date, color.PURPLE)
							#Prints all dates

					elif nameChoice == "average" or nameChoice == 'vg':
					#Users chooses to see averages
						superSpace(50)
						print "You can view " + colorThis('hole by hole', color.RED) + "averages on Pine Oaks cards (h), or " + \
								colorThis('total averages', color.RED) + ". (t)"

						averageChoice = raw_input("->").lower()
						
						countParHole = emptyHoles
						#Dictionary used to store each individual hole total
						dateCount = 0
						#Used to keep track of the number of dates added to the total

						if averageChoice == "hole" or averageChoice == 'h': 
						#User chooses to view hole averages on the Pine Oaks Course

							for date in userData[nameSearch]:
							#Iterates through the dictionary for nameSearch
								
								if userData[nameSearch][date]["pineOaks"] == "Yes": #Dates when the user played at pine oaks
									dateCount += 1
									for hole in userData[nameSearch][date]: #Iterates through all of the holes
										
										if hole != "pineOaks": #All holes except "pineOaks", including "total"
											countParHole[hole] += userData[nameSearch][date][hole] #Adds hole value to specific total

							if dateCount > 0: #Only if there were dates found
								superSpace(50)
								print color.BOLD + "Here are the hole averages:" + color.END
								
								for hole in countParHole: #Individually prints out hole values
									countParHole[hole] = int(countParHole[hole])/dateCount # Makes the value an average instead of just a total
									print color.BOLD + hole + ": " + color.END + str(countParHole[hole])

							else: #No dates were found
								print color.BOLD + "No data to average, sorry." + color.END

						elif averageChoice == "total" or averageChoice == 't':
							superSpace(50)
							print "You can view your " + colorThis('Pine Oaks total', color.RED) +  "average (po), or your " + \
									colorThis('overall total'. color.RED) + "average. (o)"

							totalChoice = raw_input("->")
							totalCount = 0 #Running total
							superSpace(50)

							if totalChoice == "pine oaks" or totalChoice == 'po': #User chooses to see Pine Oaks specific average

								for date in userData[nameSearch]: 
									if userData[nameSearch][date]["pineOaks"] == "Yes": #Finds all cards with Pine Oaks
										totalCount += userData[nameSearch][date]["Total"] #Adds totals to the running count
										dateCount += 1

								totalCount = totalCount / dateCount #Averages out the total
 								superSpace(50)
								print color.BOLD + "Your average on the Pine Oaks Golf Course is " + str(totalCount) + "." + color.END
							
							elif totalChoice == "overall" or totalChoice == 'o': #User chooses to see overall averages, regardless of course par
								for date in userData[nameSearch]: 
										totalCount += userData[nameSearch][date]["Total"]
										dateCount += 1

								totalCount = totalCount / dateCount #Averages out the total
 								superSpace(50)
								print color.BOLD + "Your overall average is " + str(totalCount) + "." + color.END 


					waitingEnter()
					#Waits for user to hit enter
 
				else: #if is_name_in(nameSearch):
				#User enters a name that does not exist
					print "That name does not have any scorecards logged.\n" + \
						"Returning to search menu..."
					wait(1)
					#Returns to search menu
					superSpace(50)
				
			elif searchChoice == "date" or searchChoice == 'd': #Menu_Search
				superSpace(50)
				print "Okay, enter the date you are looking for."
                                dateSearch = raw_input('->')
				#User inputed date to search for
				namesFound = []
				forCounter = 0
				for names in userData:
                                        #Iterates through available names, to then find dates
					for date in userData[names]:		
						if dateSearch == date:
							namesFound.append(names)	
						
				if len(namesFound) != 0: #Checks to make sure names have been found
					superSpace(50)
					print "There are " + str(len(namesFound)) + " names on this date:"
					
					for name in namesFound:
						print color.RED + name + color.END
						#prints all names found
					superSpace(1)
					print "Are you looking to view a " + colorThis('specific card', color.RED) + \
							",or see " + colorThis('who won', color.RED) + " that day? (if there is more than one person)"

					print color.BOLD + "Type the name, or 'win'" + color.END
					viewSelect = (raw_input("->")).title()
					#User chooses name
					superSpace(50)

					if viewSelect == "Win" or viewSelect == 'W': #User selects to view the winner for the day
						winningNameValue = 0 #Winning score
						winningName = "" #Winning name
						
						for name in namesFound:
							if winningNameValue < userData[name][dateSearch]["Total"]: #If the value is less than, then this name is higher
								winningNameValue = userData[name][dateSearch]["Total"] #Sets value to name
								winningName = name
						print color.BOLD + "The winner for the day is: " + color.GREEN + winningName + \
								" (" + color.BLUE + str(winningNameValue) + color.GREEN + ") " + color.END
						waitingEnter()
					
					elif viewSelect in namesFound:
					#Makes sure user entered correct name
						print "Okay, here is the score card..."
						wait(1)
						showCard(userData, viewSelect, dateSearch, pineOaksPars)
						waitingEnter()
					else:	
					#User did not enter correct name
						print "That name did not match any listed, returning to search menu...."
						wait(1.3)
						superSpace(50)
				else:#No names in 'namesFound'
                                        print "That date does not have any scorecards logged.\n" + \
                                                "Returning to search menu..."
                                        wait(1)
                                        #User inputs wrong date, Returns to search menu
                                        superSpace(50)
			
			elif searchChoice == 'quit' or searchChoice == 'q': #Menu_Search
				superSpace(50)
				searchLoop = False
				#Allows user to quit out of search menu	
#Menu_Delete -v
	elif menuChoice == "delete" or menuChoice == 'd':
		superSpace(50)
		print "Okay would you like to " + colorThis('delete an account', color.RED) + "(a)," + \
				colorThis(' a specific date', color.RED) + " (d), or " + colorThis('everything?', color.RED) + "(e)"
		deleteChoice = raw_input("->")
		superSpace(50)	
		
		if deleteChoice == "account" or deleteChoice == 'a': #Menu_Delete 
			#User chooses to delete a specific account
			print "What is the account name?"
                	deleteName = raw_input("->").title()
			#User inputed name
			superSpace(50)

			print "Okay, type Yes to confirm this."
			if  deleteName in userData and raw_input("Delete?: ").lower() == "yes":
			#Makes sure one last time
				del userData[deleteName]
				pickleOut()
				print color.RED + "Okay, it is deleted" + color.END
				wait(1.3)
				superSpace(50)
			else:
				superSpace(50)
				print "Information is not correct, returning to main menu..."
				wait(1.6)
				superSpace(50)
				#User did not type in 'yes'

		elif deleteChoice == "date" or deleteChoice == 'd': #Menu_Delete
			#User chooses to delete a specific date
			superSpace(50)
                        print "Okay, enter the date you are looking for."
			dateSearch = raw_input("->")
                        #User inputed date to search for
                        namesFound = []
                        forCounter = 0
                        
			for names in userData:
                                #Iterates through available names, to then find dates
                               	for date in userData[names]:
                                        if dateSearch == date:
                                               	namesFound.append(names)
 
                        if len(namesFound) != 0: #Checks to make sure names were found
                        	print "There are " + str(len(namesFound)) + " names on this date:"
                                for name in namesFound:
                               		print color.RED + name + color.END
					#prints all names found

                                print "Which one are you looking for? (or all)"
                                nameSelect = (raw_input("->")).title()
				#User chooses name
				superSpace(50)
                               	
				if nameSelect == "All" or nameSelect == 'A':
					#Deletes all names on date
					print "Okay, type Yes to confirm this."
                        		if raw_input("Delete?: ").lower() == "yes":
                                	#Makes sure one last time
						for name in namesFound:
							del userData[name][dateSearch]
							pickleOut()
						print color.RED + "Okay, they are deleted" + color.END
                                 		wait(1.3)
                                 		superSpace(50)
							#Iterates through names and deletes one by one
                        		else:
                               	 	#User did not type 'yes'	
						print "Returning to main menu"
                                		wait(1)
						superSpace(50)
					
				elif nameSelect in namesFound:
				#User enters one of the names listed, and this checks to make sure it was listed
					print "Okay, type Yes to confirm this."
                                       	if raw_input("Delete?: ").lower() == "yes":
                                        	del userData[nameSelect][dateSearch]
						pickleOut()
						print color.RED + "Okay, it is deleted" + color.END
                                                wait(1.3)                  
						superSpace(50)

			else:#No names in namesFound
                                print "That date does not have any scorecards logged."
                                #User inputs wrong date, Returns to search menu
			
			print "Returning to main menu"
                        wait(1)
                       	superSpace(50)

		elif deleteChoice == "everything" or deleteChoice == 'e':
			#User chooses to delete all data
			superSpace(50)
			
			print "Are you absolutely sure you want to do this?"
			if raw_input("Delete?: ").lower() == "yes":
				userData = {}
				pickleOut()
				print color.RED + "Okay, everything is deleted" + color.END
                        	wait(1.3)               

			else:
				print "Returning to main menu"
                                wait(1)
				#User does not type 'yes'
                        superSpace(50)
#Menu_Help -v
	elif menuChoice == "help" or menuChoice == 'h':
		superSpace(50)
		lineMake()
		print color.BOLD + color.GREEN + "Welcome to the Help Page!" + color.END
		print color.BLUE + "Here is a list of tips and pointers for using the app:" + color.END
		superSpace(1)
		print "->When at any menu that " + \
			color.BOLD + "does not contain options with the same first letter" + color.END + \
			" then you can use the first letter to choose the menu choice."
		print "->You can quit out of all menus by entering 'q' or 'quit'"
		print "->You can ask for all of the names that have score cards (and how many cards) by entering 'sa'" + \
			" or 'show all'"
		print "->If you want to edit a date, you can always enter a new date using that same date. It will overwrite."
		print "->When prompted to type 'yes' to confirm a deletion, entering anything else will return to the menu."
		print "->If you type 'c' or 'credits' at the main menu, it will bring you to the credits page."
		lineMake()
		waitingEnter()
		superSpace(50)
#Menu_Credits -v
	elif menuChoice == "credits" or menuChoice == 'c':
		superSpace(50)
		lineMake()
		lineMake()
		makeAG() 
		
		print color.BOLD + color.RED +  "This application was written by Andrew Smith on May 13, 2015" + color.END
		wait(3)
		print "Returning to menu"
		wait(1.5)
		superSpace(50)
#Menu_Quit -v
        elif menuChoice == "quit" or menuChoice == 'q':
                        superSpace(50)
                        mainLoop = False
                        #Allows user to quit out of main menu

#Menu_ShowALL -v
	elif menuChoice == "showall" or menuChoice == "sa":
		superSpace(50)
		print color.GREEN + "All names logged, with score cards logged:" + color.END
		for name in userData:
			print colorThis(name, color.BOLD) + ": " + colorThis(str(len(userData[name])), color.RED)
		superSpace(1)

