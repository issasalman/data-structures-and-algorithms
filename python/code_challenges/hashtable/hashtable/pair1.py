from hashtable import HashTable

def unique_characters(string):
    """
    a function called repeated word that finds the first word to occur more than once in a string
    """
    if not string:
        return "not a string"

    hashed_word = HashTable()
    string = string.replace('.','')
    string = string.replace(' ','')

    string = string.replace(',','')


    splited_words = string.lower()
    for string in splited_words:
        if hashed_word.contains(string):
          return False
        else:
            hashed_word.add(string,string)
    return True

print(unique_characters("Donald the duck"))

