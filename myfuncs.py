import os


def getUserGuess(question):
    return input(question + '? ').lower()


def isSame(guess, answer):
    if (guess == answer.lower()):
        return True
    return False


def fileExists(fileName):
    if (os.path.isfile('./' + fileName)):
        return True
    return False
