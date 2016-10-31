import sys
import random
import myfuncs


class FlashCard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer


class FlashCardSet:
    def __init__(self, fileName=None):
        self.flashCards = []

        if fileName is not None:
            lines = open(fileName).readlines()

            for line in lines:
                question, answer = line.strip().split(',')
                newFlashCard = FlashCard(question, answer)
                self.addFlashCard(newFlashCard)

    def addFlashCard(self, card):
        self.flashCards.append(card)

    def removeFlashCard(self, card):
        self.flashCards.remove(card)

    def getRandomFlashCard(self):
        return random.choice(self.flashCards)

    def cardsRemaining(self):
        if self.flashCards:
            return True
        return False


class Game:
    def __init__(self):
        self.questionsAsked = 0
        self.correctlyAnswered = 0
        print("New game started")

    def runGame(self, flashCardSet):
        # keep asking questions till 'exit' is entered by user
        # or until no flash cards remain
        while flashCardSet.cardsRemaining():
            # get random question
            randomFlashCard = flashCardSet.getRandomFlashCard()
            question = randomFlashCard.getQuestion()
            answer = randomFlashCard.getAnswer()

            # get user's guess for current question
            guess = myfuncs.getUserGuess(question)
            if (guess == 'exit'):
                break

            self.questionsAsked += 1
            if (myfuncs.isSame(guess, answer)):
                self.correctlyAnswered += 1
                flashCardSet.removeFlashCard(randomFlashCard)
                print("Correct! Nice job.")
            else:
                print("Incorrect! The correct answer is " + answer)

    def getNumQuestionsAsked(self):
        return self.questionsAsked

    def getNumCorrectlyAnswered(self):
        return self.correctlyAnswered

    def printStats(self):
        print("Total attempts : ", self.questionsAsked)
        print("Correctly answered : ", self.correctlyAnswered)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No input file provided")
        flashCardSet = FlashCardSet()
    else:
        fileName = sys.argv[1]
        # if file does not exist in current directory, exit
        if not myfuncs.fileExists(fileName):
            print("Input file does not exist in current directory")
            exit()
        flashCardSet = FlashCardSet(fileName)

    newGame = Game()
    newGame.runGame(flashCardSet)
    newGame.printStats()
