import os, random
#Choose a random file from the /derp folder
print random.choice(os.listdir(os.getcwd() + "/derp"))