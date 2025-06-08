

#shows the needed dependencies for the c program that is at fileLocation



def takeDependencies(fileLocation):
    lineArray = []
    with open(fileLocation, 'r') as file:
        for line in file:
            if line.startswith("#include"):
                lineArray.append(line)
        for i in range(len(lineArray)):
            lineArray[i] = lineArray[i].replace("#include", "")
            lineArray[i] = lineArray[i].replace("<", "")
            lineArray[i] = lineArray[i].replace(">", "")
            lineArray[i] = lineArray[i].replace("\n", "")
            lineArray[i] = lineArray[i].replace(" ", "")
        for i in range(len(lineArray)):
            if lineArray[i].startswith("stdio.h"):
                lineArray[i] = ""
        return lineArray
        
def findCode(output):
    codeArray = []
    with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/codes.txt", "r") as codesFile:
        for line in codesFile:
            if line in output:
                codeArray.append(line)
    return codeArray

fileLoc = "/Users/oliverbarkham/Documents/Python_programs/c_programs/AtomFolder/atom.c"
output = takeDependencies(fileLoc)

with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/output.txt", "w") as file:
        for i in range(len(output)):
            file.write(output[i] + "\n")
print(findCode(output))


