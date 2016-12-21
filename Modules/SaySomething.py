import subprocess

from Modules.Joke import getRandomJoke


def say_something(text):

    command = "say " + text
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if __name__ == "__main__":
    joke = getRandomJoke()
    say_something(joke)
