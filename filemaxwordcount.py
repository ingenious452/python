import sys


def wordFrequency(file):
    # input the file name
    fileName = file
    if len(fileName) < 1:
        fileName = 'clown.txt'
    # checking the existense of the file-----------
    try:
        fhandle = open(file, 'r')
    except:
        print('File Does not exist in you current directory')
        # error is to let the program continue even though there is nothin in fhandle after except the program will continue to run
        sys.exit()

    # word dictonary---
    wordDict = dict()
    # reading the file lines
    for line in fhandle:
        # stripping the lines of the whitespace in the right side
        line = line.rstrip()
    # splitting the word in the file making list
        words = line.split()
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1

    fhandle.close()
    # ------------------- end of for loop -----------
    # displayin the max frequent word dictonary-------
    wrdFreq = None
    wrd = None

    for key, value in wordDict.items():
        if wrdFreq == None or wrdFreq < value:
            wrdFreq = value
            wrd = key

    return (wrd, wrdFreq)
