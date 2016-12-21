# -*- coding: utf-8-*-
import random
import re


WORDS = ["JOKE", "KNOCK KNOCK"]


def getRandomJoke(filename="data/jokes.txt"):

    with open(filename, 'r') as myfile:
        data = myfile.read()

    jokes = data.split(";")
    r = random.randrange(0, len(jokes))
    joke = jokes[r]
    return joke


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by telling a joke.
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    joke = getRandomJoke()

    mic.say("Knock knock")

    def firstLine(text):
        mic.say(joke[0])

        def punchLine(text):
            mic.say(joke[1])

        punchLine(mic.activeListen())

    firstLine(mic.activeListen())


def isValid(text):
    """
        Returns True if the input is related to jokes/humor.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bjoke\b', text, re.IGNORECASE))

if __name__ == "__main__":
    joke = getRandomJoke()
    print(joke)