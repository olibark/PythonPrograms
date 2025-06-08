class coder:
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
            return lineArray

    def findCode():
        with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/output.txt", "r") as dep_file:
            dependencies = dep_file.read().splitlines()
        with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/codes.txt", "r") as code_file:
            codes = code_file.read().splitlines()

        for dep in dependencies:
            if dep in codes:
                index = codes.index(dep)
        return codes

    #fileLocation = input("File: ")
    fileLocation = "/Users/oliverbarkham/Documents/Python_programs/c_programs/AtomFolder/atom.c"
    output = takeDependencies(fileLocation)
    """for i in range(len(output)):
        print(output[i])"""

    with open("/Users/oliverbarkham/Documents/Python_programs/TOOL/output.txt", "w") as file:
        for i in range(len(output)):
            file.write(output[i] + "\n")

codes = coder.findCode()
#print(codes)
for i in range(0, len(codes)):
    #print(codes[i])
    print(codes[i])