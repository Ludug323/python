def removeVowel(word):
    for Str in 'aeiou':
        word = word.replace(Str,'')
    return word
print(removeVowel("animal"))