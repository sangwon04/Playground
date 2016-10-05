import random

def generateRandomNums(maxLen):
    randomList = []
    for i in range(int(maxLen)):
        randomList.append(random.randint(100000, 999999))
    return randomList

fileLength = raw_input('How many numbers? ')
randomList = generateRandomNums(fileLength)
f = open('randomNumbers', 'w')
for i in randomList:
    f.write(str(i) + '\n')
f.close()
