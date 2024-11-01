#Xordle
import pygame, sys
from pygame.locals import QUIT
from random import *
from random import randint
width = 550
height = 700
x = 100
y = 100
pygame.init()

#Defines the RGB values for colours to use later on
grey = (91, 99, 99)
orange = (255, 178, 44)
green = (88, 255, 59)
blank = (220,220,220)

#2D Array to set the colour values of each box in the grid
colours = [
  [blank,blank,blank,blank,blank],
  [blank,blank,blank,blank,blank],
  [blank,blank,blank,blank,blank],
  [blank,blank,blank,blank,blank],
  [blank,blank,blank,blank,blank],
  [blank,blank,blank,blank,blank]
  ]
guessedLetters = [['','','','',''],
                  ['','','','',''],
                  ['','','','',''],
                  ['','','','',''],
                  ['','','','',''],
                  ['','','','','']]

# A 2D array of the X and Y coords of each box just in case needs to be referenced and can be useful for debugging
# positions = [
#   [100,200],[175,100],[250,100],[325,100],[400,100]],
#   [100,],[175,100],[250,100],[325,100],[400,100]],
#   [100,100],[175,100],[250,100],[325,100],[400,100]],
#   [100,100],[175,100],[250,100],[325,100],[400,100]],
#   [100,100],[175,100],[250,100],[325,100],[400,100]],
#   [100,100],[175,100],[250,100],[325,100],[400,100]],
#   ]


#Partly sets up PyGame and declares a font that can be later referenced and used
font = pygame.font.SysFont('Courier', 20, bold=True, italic=False)
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('YORDLE!')

f = open('dictionary.txt','r')

guessed = []
lives = 6

words = []

correct = []

def select_word():
  with open("dictionary.txt","r") as dictionary:
    line = dictionary.readline().strip()
    words.append(line)
    while line:
      line = dictionary.readline().strip()
      Upcase = line.upper()
      words.append(Upcase)
  word = str(words[randint(0,len(words))])
  word = word.upper()
  return word


def dash(words):
  dashes = ["_" for i in words]
  print(*dashes)
  return dashes

window.fill((100,100,100))


def writeLetter(char,x,y,win):
  text = font.render(char,True,(255,255,255))
  win.blit(text,(x,y))

def printWord(win):
  x,y = 120,115

  for i in range(len(guessedLetters)):
    for j in range(len(guessedLetters[i])):
      writeLetter(guessedLetters[i][j],x+i*75,y+j*75,win)

def addLetters(word,guessCount):
  i = guessCount-1
  for j in range(len(word)):
    guessedLetters[j][i] = word[j]


def main(win):
  #fontTitle = pygame.font.SysFont('', 1500, bold=True, italic=False)


  text = font.render("YORDLE", True, (255, 255, 255))
  boxtext = text.get_rect()
  boxtext.center = (275, 75)

  guessCount = 0
  game = True
  global lives
  while game == True:
    win.fill((10,10,10))
    word = select_word()
    guessCount += 1


    while guessCount <= 6:


      win.blit(text, boxtext)
      #Row 1
      Box1a = pygame.draw.rect(win, (colours[0][0]), (x,y,50,50))
      Box1b = pygame.draw.rect(win, (colours[0][1]), (x+75,y,50,50))
      Box1c = pygame.draw.rect(win, (colours[0][2]), (x+150,y,50,50))
      Box1d = pygame.draw.rect(win, (colours[0][3]), (x+225,y,50,50))
      Box1e = pygame.draw.rect(win, (colours[0][4]), (x+300,y,50,50))

      #Row 2
      Box2a = pygame.draw.rect(win, (colours[1][0]), (x,y+75,50,50))
      Box2b = pygame.draw.rect(win, (colours[1][1]), (x+75,y+75,50,50))
      Box2c = pygame.draw.rect(win, (colours[1][2]), (x+150,y+75,50,50))
      Box2d = pygame.draw.rect(win, (colours[1][3]), (x+225,y+75,50,50))
      Box2e = pygame.draw.rect(win, (colours[1][4]), (x+300,y+75,50,50))

      #Row 3
      Box3a = pygame.draw.rect(win, (colours[2][0]), (x,y+150,50,50))
      Box3b = pygame.draw.rect(win, (colours[2][1]), (x+75,y+150,50,50))
      Box3c = pygame.draw.rect(win, (colours[2][2]), (x+150,y+150,50,50))
      Box3d = pygame.draw.rect(win, (colours[2][3]), (x+225,y+150,50,50))
      Box3e = pygame.draw.rect(win, (colours[2][4]), (x+300,y+150,50,50))
      #Row 4
      Box4a = pygame.draw.rect(win, (colours[3][0]), (x,y+225,50,50))
      Box4b = pygame.draw.rect(win, (colours[3][1]), (x+75,y+225,50,50))
      Box4c = pygame.draw.rect(win, (colours[3][2]), (x+150,y+225,50,50))
      Box4d = pygame.draw.rect(win, (colours[3][3]), (x+225,y+225,50,50))
      Box4e = pygame.draw.rect(win, (colours[3][4]), (x+300,y+225,50,50))
      #Row 5
      Box5a = pygame.draw.rect(win, (colours[4][0]), (x,y+300,50,50))
      Box5b = pygame.draw.rect(win, (colours[4][1]), (x+75,y+300,50,50))
      Box5c = pygame.draw.rect(win, (colours[4][2]), (x+150,y+300,50,50))
      Box5d = pygame.draw.rect(win, (colours[4][3]), (x+225,y+300,50,50))
      Box5e = pygame.draw.rect(win, (colours[4][4]), (x+300,y+300,50,50))
      #Row 6
      Box6a = pygame.draw.rect(win, (colours[5][0]), (x,y+375,50,50))
      Box6b = pygame.draw.rect(win, (colours[5][1]), (x+75,y+375,50,50))
      Box6c = pygame.draw.rect(win, (colours[5][2]), (x+150,y+375,50,50))
      Box6d = pygame.draw.rect(win, (colours[5][3]), (x+225,y+375,50,50))
      Box6e = pygame.draw.rect(win, (colours[5][4]), (x+300,y+375,50,50))

      printWord(win)
      pygame.display.update()
      guess = input("Please enter a 5-letter word to guess: ")


      guess = guess.upper()
      while len(guess) != 5:
        guess = input("!!Enter a 5-letter word!!: ")
        guess = guess.upper()
      while guess.isalpha() != True:
        guess = input("Enter a word, no symbols or numbers!!: ")
        guess = guess.upper()
      while guess not in words:
        guess = input("Not in word list try again: ")
        guess = guess.upper()


      addLetters(guess,guessCount)
      game = True

      for i in range(len(word)):
        if guess[i] == word[i]:
          #Change letter to green
          colours[guessCount - 1][i] = green
        elif guess[i] in word:
          #Change letter to orange to signify its in the word somewhere else
          colours[guessCount - 1][i] = orange
        else:
          #All letters go grey
          colours[guessCount - 1][i] = grey
      if word ==  guess:
        print("Congrats you guessed the word")
        print("The word was", word)
        game = False
        break


      guessCount += 1


      pygame.display.update()

  pygame.display.update()
      #Row 1
  Box1a = pygame.draw.rect(win, (colours[0][0]), (x,y,50,50))
  Box1b = pygame.draw.rect(win, (colours[0][1]), (x+75,y,50,50))
  Box1c = pygame.draw.rect(win, (colours[0][2]), (x+150,y,50,50))
  Box1d = pygame.draw.rect(win, (colours[0][3]), (x+225,y,50,50))
  Box1e = pygame.draw.rect(win, (colours[0][4]), (x+300,y,50,50))

      #Row 2
  Box2a = pygame.draw.rect(win, (colours[1][0]), (x,y+75,50,50))
  Box2b = pygame.draw.rect(win, (colours[1][1]), (x+75,y+75,50,50))
  Box2c = pygame.draw.rect(win, (colours[1][2]), (x+150,y+75,50,50))
  Box2d = pygame.draw.rect(win, (colours[1][3]), (x+225,y+75,50,50))
  Box2e = pygame.draw.rect(win, (colours[1][4]), (x+300,y+75,50,50))

      #Row 3
  Box3a = pygame.draw.rect(win, (colours[2][0]), (x,y+150,50,50))
  Box3b = pygame.draw.rect(win, (colours[2][1]), (x+75,y+150,50,50))
  Box3c = pygame.draw.rect(win, (colours[2][2]), (x+150,y+150,50,50))
  Box3d = pygame.draw.rect(win, (colours[2][3]), (x+225,y+150,50,50))
  Box3e = pygame.draw.rect(win, (colours[2][4]), (x+300,y+150,50,50))
      #Row 4
  Box4a = pygame.draw.rect(win, (colours[3][0]), (x,y+225,50,50))
  Box4b = pygame.draw.rect(win, (colours[3][1]), (x+75,y+225,50,50))
  Box4c = pygame.draw.rect(win, (colours[3][2]), (x+150,y+225,50,50))
  Box4d = pygame.draw.rect(win, (colours[3][3]), (x+225,y+225,50,50))
  Box4e = pygame.draw.rect(win, (colours[3][4]), (x+300,y+225,50,50))
  #Row 5
  Box5a = pygame.draw.rect(win, (colours[4][0]), (x,y+300,50,50))
  Box5b = pygame.draw.rect(win, (colours[4][1]), (x+75,y+300,50,50))
  Box5c = pygame.draw.rect(win, (colours[4][2]), (x+150,y+300,50,50))
  Box5d = pygame.draw.rect(win, (colours[4][3]), (x+225,y+300,50,50))
  Box5e = pygame.draw.rect(win, (colours[4][4]), (x+300,y+300,50,50))
  #Row 6
  Box6a = pygame.draw.rect(win, (colours[5][0]), (x,y+375,50,50))
  Box6b = pygame.draw.rect(win, (colours[5][1]), (x+75,y+375,50,50))
  Box6c = pygame.draw.rect(win, (colours[5][2]), (x+150,y+375,50,50))
  Box6d = pygame.draw.rect(win, (colours[5][3]), (x+225,y+375,50,50))
  Box6e = pygame.draw.rect(win, (colours[5][4]), (x+300,y+375,50,50))

  printWord(win)
  pygame.display.update()


main(window)
