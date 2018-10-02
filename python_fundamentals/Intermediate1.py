#1 randInt() returns a random integer between 0 to 100
import random
def randInt():
    ran = round(random.random()*100)
    return ran

#2 randInt(max=50) returns a random integer between 0 to 50
import random
def randInt(max):
    ran = round(random.random() * max)
    return ran

#3 randInt(min=50) returns a random integer between 50 to 100
import random
def randInt(min):
    ran = round((random.random() * (100-min))+min)
    return ran

#4 randInt(min=50, max=500) returns a random integer between 50 and 500
import random
def randInt(min,max):
    ran = round((random.random() * (max-min))+min)
    return ran