from ProcessRequest import process_requests
import time
import random
from SaySomething import say_something

class ComProcessor:

    def process_command(self, command, input1=None, input2=None, input3=None, input4=None):

        """
        this function takes a command and several inputs and processed it.

        available commands:
        - What time is it? -> returns date/time
        - Get url content. -> returns html content of an url
        - Give me a random number. -> returns random number
        """

        self.command = command

        commands = {"time" : "What time is it?",
                    "request" : "Get url content.",
                    "random" : "Give me a random number."
                    }

    #time-command:
        if command == commands["time"]:
            localtime = time.strftime("The actual time is: %H oclock and %M minutes")
            say_something(str(localtime))
            return localtime

    #html reauest command:
        if command == commands["request"]:
            html = process_requests(input1, input2, input3, input4)
            return html

        if command == commands["random"]:
            number = random.randrange(input1, input2)
            say_something(str(number))
            return number


if __name__ == "__main__":
    new_processor = ComProcessor()
    number = new_processor.process_command("Give me a random number.", 1, 100)
    print(number)
    new_processor.process_command("What time is it?")