#Victoria Elliott
#2022

import string
import turtle
from turtle import Screen

data = open("words.txt", "r")
words = data.read().splitlines()

#Asks user if they want to play again
def retry():
    playAgain = input("Play again? (type yes or no): ")
    if playAgain == "yes":
        hangMan()
    elif playAgain == "no":
        print("Thanks for playing!")
#Lets the user pick the word length from 2-22, 24, 28 and 29
def usersWordLength(words):
    wordLengths =[]
    for word in words:
        length = len(word)
        if length not in wordLengths:
            wordLengths.append(length) 
    wordLengths.sort() #puts the word list in order 
    print("Choose from the list of word lengths:", wordLengths) #prints a list of the word lengths found in words.txt
    while True:
        length = int(input("\nFrom the list above, choose a word length: "))
        if length in wordLengths:
            return length
        else:
            print("Invalid input, try again!")    
#Lets the user choose the number of guesses they have
def usersNumOfGuesses():
    while True:
        guesses = int(input("How many guesses would you like? Please choose from 1-19: "))
        if guesses > 0 and guesses < 20:
            return guesses            
        else:
            print("Invalid input, try again!")
#Hyphenates the secretWord
def hyphenateWords(length):
    hyphen = ""
    for _ in range(0,length):
        hyphen += " - "
    return hyphen
# Saves a list of all words that are the length of the users requested word length
def listOfWordsWithUsersRequestedLength(lines,length):
    words = []
    for word in lines:
        if len(word) == length:
            words.append(word)
    return words
#Letters that the user guessed
def letterGuess(lettersGuessed):
    alphabet = list(string.ascii_lowercase)  
    done = False
    while not done:
        letter = str(input("Guess a letter: " )).lower()
        for letters in alphabet:
            if letter not in alphabet:
                print("Invalid input, try again\n")
            if letter in lettersGuessed:
                while letter in lettersGuessed:
                    print(letter + " was already guessed, try again\n")
                    letter = str(input("Guess a letter: " )).lower()
            else:
                return letter
        done = True
    return letter 
#secretWord, this function reveals whether the user guessed a letter in the word
def word(words,guessedLetters):
    word = ""
    for letter in words:
        if letter in guessedLetters:
            word += letter
        else: 
            word += " - "
    return word
# Generates a lists of remaining words that the user can guess
def getWordsRemaining(guess, wordsRemaining, numOfGuesses, wordLength):   
    dictLetters = dictGenerator(wordsRemaining, guess)
    hyphendatedLetters = hyphenateWords(wordLength)
    if numOfGuesses == 0 and hyphendatedLetters in dictLetters:
        newListOfWords = hyphenateWords(wordLength)
    else:
        newListOfWords = wordsWithHighestCount(dictLetters)
    words = generateListOfWords(wordsRemaining, guess, newListOfWords)
    return words
def dictGenerator(wordsRemaining, guess):
    wordFamilies = {}
    for word in wordsRemaining:
        words = ""
        for letter in word:
            if(letter == guess):
                words += guess
            else:
                words += "-"
                
        if words not in wordFamilies:
            wordFamilies[words] = 1
        else:
            wordFamilies[words] = wordFamilies[words] + 1
    return wordFamilies
def generateListOfWords(wordsRemaining, guess, groupOfWords):
    words = []
    for word in wordsRemaining:
        wordList = ""
        for letter in word:
            if(letter == guess):
                wordList += guess
            else:
                wordList += "-"
                
        if(wordList == groupOfWords):
            words.append(word)
    return words
def wordsWithHighestCount(wordGroup):
    groupOfWords = ""
    maxCount = 0
    for index in wordGroup:
        if wordGroup[index] > maxCount:
            maxCount = wordGroup[index]
            groupOfWords = index
    return groupOfWords

#OfficialHangManGame
def hangMan():
    playAgain = "yes"
    while playAgain == "yes": 
        gameOver = False
        wordLength = usersWordLength(words)
        numOfGuesses = usersNumOfGuesses()
        wordsRemaining = listOfWordsWithUsersRequestedLength(words, wordLength)
        secretWord = hyphenateWords(wordLength)
        guessedLetters = []
        while not gameOver:
            print("\nCurrent word: ", secretWord)
            print("\nRemaining Guesses: ", numOfGuesses)
            guess = letterGuess(guessedLetters)
            guessedLetters.append(guess)
            print("Letters Guessed: ", guessedLetters)
            wordsRemaining = getWordsRemaining(guess, wordsRemaining, numOfGuesses, wordLength)
            secretWord = word(wordsRemaining[0], guessedLetters)
            if guess in secretWord:
                numOfGuesses = numOfGuesses
            else:
                numOfGuesses -= 1
            if "-" not in secretWord:
                gameOver = True
                print("Congrats you guessed the word! The word was:", secretWord)
            if numOfGuesses == 0 and gameOver == False:
                gameOver = True
                print("Hung! The word was: ", wordsRemaining[0])
                HMC = turtle.Turtle()
                BL = turtle.Turtle()
                lost = turtle.Turtle()
                lost.hideturtle()
                def hangManFunc():
                    wn = Screen()
                    rootwindow = wn.getcanvas().winfo_toplevel()
                    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
                    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
                    BL.width(5)
                    HMC.width(5)
            
                    BL.hideturtle()
                    HMC.penup() 
                    HMC.goto(-120, 70)
                    HMC.pendown()
                    HMC.hideturtle()
                    HMC.rt(90)
                    HMC.fd(180)
                    HMC.bk(125)
                    HMC.lt(135)
                    HMC.fd(80)
                    HMC.lt(135)
                    HMC.fd(58)
                    HMC.rt(180)
                    HMC.fd(180)
                    HMC.rt(90)
                    HMC.fd(40)

                    HMC.penup()
                    HMC.rt(90)
                    HMC.fd(20)
                    HMC.lt(90)
                    HMC.fd(20)
                    HMC.pendown()

                    HMC.circle(20)

                    HMC.penup()
                    HMC.lt(90)
                    HMC.fd(20)
                    HMC.rt(90)
                    HMC.fd(20)
                    HMC.pendown()
                    HMC.fd(40)
                    HMC.lt(40)
                    HMC.fd(40)
                    HMC.bk(40)
                    HMC.rt(80)
                    HMC.fd(40)

                    BL.penup()
                    BL.goto(-115,-110)
                    BL.pendown()
                    BL.bk(75)
                    BL.fd(150)

                hangManFunc()
                lost.penup()
                lost.goto(-155,100)
                lost.write("Game Over!", font=("Verdana", 30, "bold"))
                turtle.Screen().bgcolor("red")
                turtle.done()   
        gameOver = True     
        playAgain = "no"
        break
hangMan()
retry()