#Calculate the sum of all of the 'fuel' required
#To calculate fuel: Fuel = int(ModuleMass / 3) - 2
#ModuleMass is each number on the input file

#Part 2:
#Each fuel requires its own fuel as well
#Any negative fuel should be treated as 0
#If any fuel is remaining afterwards, it's fuel needs to be addded to the sum as well

totalFuel = 0;
tempFuel = 0;

filename = 'input.txt'
file = open(filename, mode='r') #Open input.txt in read mode
line = file.readlines()

for i in range(100):
	tempFuel = int(int((line[i])) / 3) - 2
	totalFuel += tempFuel
	
	while tempFuel > 0:
		tempFuel = int(tempFuel / 3) - 2
		if (tempFuel < 0):
			tempFuel = 0
		totalFuel += tempFuel

print(str(totalFuel))
file.close()