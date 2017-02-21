import os
from merriam_webster import api

os.environ["MERRIAM_WEBSTER_COLLEGIATE_KEY"] = 'YOUR_API_KEY'  # get an api key http://www.dictionaryapi.com/
filename = './input/SAMPLE.txt'  # file to be identified


def lookup(dictionary_class, key, query):
    dictionary = dictionary_class(key)
    try:
        defs = [(entry.word, entry.function, definition)
                for entry in dictionary.lookup(query)
                for definition, examples in entry.senses]
    except api.WordNotFoundException:
        defs = []
    dname = dictionary_class.__name__.replace('Dictionary', '').upper()
    if defs == []:
        print("{0}: No definitions found for '{1}'".format(dname, query))
    for word, pos, definition in defs:
        print("{0}, {1}".format(word, definition))
        with open(filename, "a") as myfile:
            if not "{0}, {1}".format(word, definition) in myfile:
                myfile.write("{0}, {1}".format(word, definition) + '\n')  # writes the definitions to the text file in
                #  case you can't get it from the console output


if __name__ == "__main__":
    processed = []
    with open(filename) as queries:
        for line in queries:
            if not '#' in line:  # ignores lines with a # in the so that comments can be made
                processed.append(line[:-1])  # add each line to be defined. removes last char (usually newline)
    print(processed) # shows words to be defined
    collkey = os.getenv("MERRIAM_WEBSTER_COLLEGIATE_KEY")
    for p in processed:
        lookup(api.CollegiateDictionary, collkey, p)
