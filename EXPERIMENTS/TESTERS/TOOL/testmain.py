import json
import os

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

def updateSettingsJson(compile_and_run_command):
    settings_path = "/Users/oliverbarkham/Library/Application Support/Code/User/settings.json"
    
    # Read the existing settings.json file
    if os.path.exists(settings_path):
        with open(settings_path, "r") as settings_file:
            settings_data = json.load(settings_file)
    else:
        settings_data = {}

    # Ensure "code-runner.executorMap" exists
    if "code-runner.executorMap" not in settings_data:
        settings_data["code-runner.executorMap"] = {}

    # Update the "c" entry with the new compile and run command
    settings_data["code-runner.executorMap"]["c"] = compile_and_run_command

    # Write the updated settings back to the file
    with open(settings_path, "w") as settings_file:
        json.dump(settings_data, settings_file, indent=4)
    print(f"Updated settings.json with the new compile and run command.")

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

# Generate the compile and run command
build_dir = "/Users/oliverbarkham/Documents/Python_programs/c_programs/AtomFolder/build"
output_binary = f"{build_dir}/atom"
compile_command = f"mkdir -p {build_dir} && gcc {fileLoc} -o {output_binary}"

for code in codes:
    if code == "sdl2":
        compile_command += " -lSDL2 -lSDL2_image -lSDL2_ttf"
    if code == "curl/curl.h":
        compile_command += " -lcurl"
    if code == "jansson.h":
        compile_command += " -ljansson"
    # Add more mappings here if needed for other dependencies

# Append the run command
compile_and_run_command = f"{compile_command} && {output_binary}"

# Update the settings.json file
updateSettingsJson(compile_and_run_command)

print("Compile and run command:")
print(compile_and_run_command)