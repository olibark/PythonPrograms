import random
import string



def random_char_generator(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_chars = ''.join(random.choice(characters) for _ in range(length))
    return random_chars
array = []
length_of_password = int(input("How long would you like the password to be? "))
input = input("Would you like to have your password contain both numbers and characters? (num, char, both) ")
if input == ("num"):
    for i in range (length_of_password):
        num = random.randint(0, 9)
        array.append(num)
    for i in range (length_of_password):
        print (array[i])
elif input == ("char"):
    for i in range (length_of_password):
        random_string = random_char_generator(1)
        array.append(random_string)
        print (array[i], sep= ' ')
elif input == ("both"):
    for i in range (length_of_password):
        if random.choice([True, False]):
            array.append(random.randint(0, 9))
        else:
            array.append(random_char_generator(1))
elif input == ("all"):
    for i in range (length_of_password):
        if random.choice([True, False]):
            array.append(random.randint(0, 9))
        else:
            file = open("expanded_phrases_words.txt","r")
            for line in file:
                line = line.strip()
                line = line.split()
            for i in range (length_of_password):
                    array.append(line)




print("Your password: ", end='')
print(*array, sep='')










