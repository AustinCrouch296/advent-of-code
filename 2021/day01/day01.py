file = open("input.txt", "r") #read mode
line = file.readlines()

count = 0
num = int(line[0])

for i in range(2000):
    nextnum = int(line[i])
    
    if num < nextnum:
        count+= 1
    
    num = nextnum

print(count)