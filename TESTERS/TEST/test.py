fruits = ["banana" ,"apple" ,"orange" ,"pear", "grape" ,"pineapple"]

wordsearch = str(input("What would you like to search for?  "))

def search():
    for i in range (0, len(fruits)):
        if fruits[i] == wordsearch:
            return True
    return False


if search() == True:
    print("True")
else:
    print ("False")
