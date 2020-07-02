#define a simple function with def key word
def printHello():
    print("hello!!!!!")
# call the function
printHello()

#=====================================
#Functions that take in and use parameter
def printName(name):
    print("hello "+name+"!!!!")
#call the function
printName("max")

#=====================================
# The prine use of the function is to run the same code for different values
listOne=[1,2,3,4,5,6,7]
listTwo=[11,12,13,134]
def listInformation(sampleList):
    print("the values within the list are.....")
    for value in sampleList:
        print(value)
    print("The length of this list is..."+str(len(sampleList)))
#call the function
listInformation(listOne)
listInformation(listTwo)