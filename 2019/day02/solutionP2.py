#Part 1:
#Recreate an Intcode program that uses these conditions:
#Starting at index 0, split the code into brackets of 4
#The first value is your "opcode" which tells you which operation to do
#Code 1: Add second value and third value and place it at the index given by fourth value
#Code 2: Multiply second value and third value and place it at index given by fourth value
#Code 99: Exit program, Any other code: Invalid
#Using these rules figure out the value of index[0] when code 99 is run, when index[1]=12 and index[2]=2

#Part 2:
#index[1] is now considered the 'noun', and index[2] the 'verb'
#Using the numbers in input.txt, find a noun & verb combination that gives you "index[0] = 19690720" when code 99 is run

#Reads data from input.txt:
filename = 'input.txt'
file = open(filename, mode='r') #
line = file.readline()

#Splits data into an array of strings, removing commas:
line = line.split(",")

#Converts array of strings into an array of integers:
intAt = [''] * len(line)
for i in range(len(line)):
	intAt[i] = int(line[i])

#Initalizing variables:
x = 0
noun = 0
verb = 0
parameter = [0, 0, 0]

#Code loops until all possible noun/verb combinations are run or an invalid opcode is entered.
while (1 == 1):
	opcode = intAt[x]
	intAt[1] = noun
	intAt[2] = verb
	
	if (opcode == 1):
		parameter = [intAt[x+1], intAt[x+2], intAt[x+3]]
		intAt[parameter[2]] = intAt[parameter[0]] + intAt[parameter[1]]
		x += 4
	elif (opcode == 2):
		parameter = ([intAt[x+1], intAt[x+2], intAt[x+3]])
		intAt[parameter[2]] = intAt[parameter[0]] * intAt[parameter[1]]
		x += 4
	elif (opcode == 99):
		#If the index[0] is correct, end the program and give the successful numbers:
		if (intAt[0] == 19690720):
			print("noun = " + str(noun) + ", verb = " + str(verb))
			exit()
		#Else, display a failed message, increase the noun counter/verb counter if noun 0-99 have already occurred
		#And reset x to 0 and the input.txt results back to normal
		else:
			print("[" + str(noun) + "][" + str(verb) + "] failed.")
			
			noun += 1
			
			#Backup exit if all noun 0-99 and verb 0-99 combinations are unsuccessful:
			if (noun == 100 and verb == 99):
				exit()
				
			if (noun == 100):
				noun = 0
				verb += 1
				
			for i in range(len(line)):
				intAt[i] = int(line[i])
			x = 0
	else:
		print("Error, Invalid Opcode. Opcode was " + str(opcode))
		exit()