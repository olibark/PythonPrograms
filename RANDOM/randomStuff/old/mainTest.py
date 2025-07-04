

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
        return [dep for dep in lineArray if dep]  # Remove empty strings

def findCode(output):
    codeArray = []
    with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/codes.txt", "r") as codesFile:
        lines = codesFile.readlines()
        for dependency in output:
            for i in range(len(lines)):
                if lines[i].strip() == dependency:
                    if i + 1 < len(lines):  # Ensure the next line exists
                        codeArray.append(lines[i + 1].strip())
    return codeArray

fileLoc = "/Users/oliverbarkham/Documents/Python_programs/c_programs/AtomFolder/atom.c"
output = takeDependencies(fileLoc)

with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/output.txt", "w") as file:
    for i in range(len(output)):
        file.write(output[i] + "\n")

codes = findCode(output)
for i in range(len(codes)):
    if codes[i] == codes[i - 1]:
        codes[i] = ""
codes = [code for code in codes if code]  # Remove empty strings
print(codes)



