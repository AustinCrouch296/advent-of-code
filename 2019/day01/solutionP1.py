#Calculate the sum of all of the 'fuel' required
#To calculate fuel: Fuel = int(ModuleMass / 3) - 2
#ModuleMass is each number on the input file

totalFuel = 0;

filename = 'input.txt'
file = open(filename, mode='r') #Open input.txt in read mode
line = file.readlines()

for i in range(100):
	totalFuel += int(int((line[i])) / 3) - 2
	print('Line ' + str(i+1) + ' = ' + str(int(line[i])))

print(str(totalFuel))
file.close()