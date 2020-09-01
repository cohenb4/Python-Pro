import random
from collections import Counter

listOfWords = []

with open("sowpods.txt", "r") as f:
    listOfWords = f.read().split()

word = random.choice((listOfWords)) #randomly chooses a word
wordcounter = Counter(word)

def hangman(tries):
  parts = [
  """         \n ________\n|   |    \n|   0    \n|  \|/   \n|   |    \n|  / \   \n|        \n|        \n_________\n""" #hangman with head, body, left and right arms, left and right legs
  ,"""         \n ________\n|   |    \n|   0    \n|  \|/   \n|   |    \n|    \   \n|        \n|        \n_________""" #hangman with head, body, left and right arms, and right leg
  ,"""         \n ________\n|   |    \n|   0    \n|  \|/   \n|   |    \n|        \n|        \n|        \n_________""" #hangman with head, body, left and right arms
  ,"""         \n ________\n|   |    \n|   0    \n|  \|    \n|   |    \n|        \n|        \n|        \n_________""" #hangman with head, body, and left arm
  ,"""         \n ________\n|   |    \n|   0    \n|   |    \n|   |    \n|        \n|        \n|        \n_________""" #hangman with head and body
  ,"""         \n ________\n|   |    \n|   0    \n|        \n|        \n|        \n|        \n|        \n_________""" #hangman with head
  ,"""         \n ________\n|   |    \n|       \n|        \n|        \n|        \n|        \n|        \n_________""" #hangman with nothing
  ]
  return parts[tries]

def start():
  name = input('Enter your name: ')
  print('Welcome to the game', name)

def main(): # defines play 
  guessedLetters = [] #holds guessed letters
  guessedWords = [] #holds guessed words
  correctLetters = [] #hold correct letters
  #guessed = False #makes sure you haven't guessed it already
  tries = 6 #allows for 6 tries for each body part
  playWord = "_ " * (len(word) - len(correctLetters))
  print(start()) 
  print(hangman(tries))
  print(tries, "tries left")
  while len(wordcounter) > 0 and tries > 0: #makes sure that the number of tries left is above zero and you have not already guessed the letter or word
    for a in word:
     if a in correctLetters:
      print(a, end =" ")
     else:
       print("_ ", end ="")
    print("\n")
    guess = input('Guess a letter or a word: ') #allows user to guess letter or word
    if len(guess) == 1 and guess.isalpha(): #guessed letters are alphabetic
      if guess in wordcounter: #guess is in word
        print(guess, "is in the word")
        guessedLetters.append(guess)
        correctLetters.append(guess)
        del wordcounter[guess]
        print(hangman(tries))
        print(tries, "tries left")
        playWord = "_ " * (len(word) - len(correctLetters))
      elif guess not in word: #if guess is not in the word
        print(guess, "is not in the word")
        tries -= 1 #subtract a try
        print(hangman(tries))
        guessedLetters.append(guess) #adds guess to guessed letters
        print(playWord)
        print(tries, "tries left")
        print(guessedLetters)
      elif guess not in guessedLetters:
        guessedLetters.add(guess)
        tries -= 1
        playWord = list(playWord) #turns dashes into a list   
      elif guess in guessedLetters: #if the guessed letter is already guessed
        print("Already guessed", guessedLetters)
        print(hangman(tries))
        print(playWord)
        print(tries, "tries left")
      if wordcounter == 0:
        print("Good job, you won!")
    elif guess.isalpha():
      if guess == word:
        print("Good job, you won!")
        break
      elif guess is not word: #guess is in word
        print(guess, "is not the word")
        tries -= 1 #subtract a try
        guessedWords.append(guess)
        print(hangman(tries))
        print(playWord)
        print(tries, "tries left") 
      elif guess in guessedWords: #if the guessed letter is already guessed
        print("Already guessed", guessedWords)
        print(hangman(tries))
        print(playWord)
        print(tries, "tries left")
        print(guessedWords)
    else:
      print("Not valid, try again")
  if tries == 0:
    print("Better luck next time, the word was", word)
  play2 = (input('Enter 1 to play again or 2 to quit: '))
  if play2 == '1':
    print(main())
  elif play2 == '2':
    print('Goodbye')
  elif play2 != '1' or '2':
    print('Invalid, type 1 or 2')
  print(guess) 

if __name__ == "__main__":
  main()