def scramble(word):
    for i in range(0, len(word)):
        for j in range(i, len(word)):
            if word[i] > word[j]:
                word = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
    return word

print(scramble("hello"))