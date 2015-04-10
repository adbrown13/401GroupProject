import os, random
#Choose a random file from the /derp folder



def chooseRandomFile():
    chosenFiles = []
    availableFiles = os.listdir( os.getcwd() + "/video" )
    numOfTestFiles = len(availableFiles)
    numOfRepeatedFiles = int( (numOfTestFiles*0.1) )
    numOfUniqueFiles = numOfTestFiles - numOfRepeatedFiles

    for i in range(0, numOfTestFiles):
        availableFiles[i] = "video/" + availableFiles[i]

    for i in range(0, numOfTestFiles):
        randomfile = random.choice( list(set(availableFiles)-set(chosenFiles)) )
        chosenFiles.append(randomfile)

    repeatedFiles = []
    repeatedFiles.append(chosenFiles[0])

    for i in range(1,numOfRepeatedFiles+1):
        randomFile = random.choice( list(set(chosenFiles)-set(repeatedFiles)) )
        repeatedFiles.append(randomFile)

    for i in range(1,numOfRepeatedFiles+1):
        chosenFiles.insert(random.randint(1, numOfUniqueFiles-2+i), repeatedFiles[i])

    chosenFiles.append(repeatedFiles[0])

    return chosenFiles

