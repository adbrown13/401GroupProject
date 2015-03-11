import os, random
#Choose a random file from the /derp folder

numOfTestFiles = 40
numOfRepeatedFiles = int(numOfTestFiles * 0.1)
numOfUniqueFiles = numOfTestFiles - numOfRepeatedFiles

def chooseRandomFile():
    chosenFiles = []
    availableFiles = os.listdir( os.getcwd() + "/video" )

    for i in range(1,numOfUniqueFiles):
        randomfile = random.choice( list(set(availableFiles)-set(chosenFiles)) )
        chosenFiles.append(randomfile)

    repeatedFiles = []
    repeatedFiles.append(chosenFiles[0])

    for i in range(1,numOfUniqueFiles+1):
        randomFile = random.choice( list(set(chosenFiles)-set(repeatedFiles)) )
        repeatedFiles.append(randomFile)

    for i in range(1,numOfUniqueFiles+1):
        chosenFiles.insert(random.randint(1, numOfUniqueFiles-2+i), repeatedFiles[i])

    chosenFiles.append(repeatedFiles[0])

    return chosenFiles

