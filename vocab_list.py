#Name: vocap_list.py
#Author: Douglas Bender
#Last update: 10 July, 2022
#Description: Produces a list of words found in a chunk of text
#           sorted by their frequency of occurence, with the number
#           of times each word appeared next to it.


def wordCounter(text, topWordsCount):
    wordCount = 1
    words = {}

    lowtext = text.lower()
    
    numWords = lowtext.count(" ")

    for x in range(numWords + 1):
        spaceIndex = lowtext.find(" ")

        #print(spaceIndex)

        wordToAdd = lowtext[:spaceIndex]
        #print(wordToAdd)
        
        if wordToAdd not in words:
            words[wordToAdd] = 1
        else:
            words[wordToAdd] += 1

        lowtext = lowtext[spaceIndex + 1:]

    #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sortedList = sorted(words.items(), key=lambda x: x[1], reverse=True)
    
    for x in range(0, topWordsCount):
        print("#", x + 1, " ", sortedList[x])

    export = input("Would you like to export this list to a csv file? (Y/N) ")
    export = export.lower()

    if export == "y":
        #ping export microservice
        print("File being generated now...")
    else:
        print("Thank you for using the word-list generator. Happy studying!")



sampleText = "Als Gregor als Samsa eines Morgens aus unruhigen Träumen erwachte, fand er sich in seinem Bett zu einem ungeheueren Ungeziefer verwandelt. Er lag auf seinem panzerartig harten Rücken und sah, wenn er den Kopf ein wenig hob, seinen gewölbten, braunen, von bogenförmigen Versteifungen geteilten Bauch, auf dessen Höhe sich die Bettdecke, zum gänzlichen Niedergleiten bereit, kaum noch erhalten konnte. Seine vielen, im Vergleich zu seinem sonstigen Umfang kläglich dünnen Beine flimmerten ihm hilflos vor den Augen."


userText = input("\nWelcome to the word counter! Please enter the text you'd like analyzed, and we'll output an ordered list of the most frequently occuring words in that input: ")
topWordsCount = input("How many of the top words would you like to know? ")
wordCounter(userText, int(topWordsCount))