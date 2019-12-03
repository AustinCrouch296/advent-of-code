#Part 1:
#Recreate an Intcode program that uses these conditions:
#Starting at index 0, split the code into brackets of 4
#The first value is your "opcode" which tells you which operation to do
#Code 1: Add second value and third value and place it at the index given by fourth value
#Code 2: Multiply second value and third value and place it at index given by fourth value
#Code 99: Exit program, Any other code: Invalid
#Using these rules figure out the value of index[0] when code 99 is run, when index[1]=12 and index[2]=2

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

#Before activating, change these two numbers in the input:
intAt[1] = 12
intAt[2] = 2

#Runs opcode program until error or code 99:
#If code 99, print the final index of 0 for result
x = 0
while (1 == 1):
	opcode = intAt[x]
	
	if (opcode == 1):
		intAt[intAt[x+3]] = intAt[intAt[x+1]] + intAt[intAt[x+2]]
	elif (opcode == 2):
		intAt[intAt[x+3]] = intAt[intAt[x+1]] * intAt[intAt[x+2]]
	elif (opcode == 99):
		print("intAt[0] = " + str(intAt[0]))
		exit()
	else:
		print("Error, Invalid Opcode. Opcode was " + str(opcode))
		
	x += 4