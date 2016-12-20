from ProcessRequest import process_requests
import time

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
                    "request": "Get url content."}

    #time-command:
        if command == commands["time"]:
            localtime = time.strftime("%d.%m.%Y - actual time: %H:%M:%S")
            return localtime

    #html reauest command:
        if command == commands["request"]:
            html = process_requests(input1, input2, input3, input4)
            return html


if __name__ == "__main__":
    new_processor = ComProcessor()
    html_text = new_processor.process_command("Get url content.", "https://www.webpagetest.org/", "text")
    print(html_text)