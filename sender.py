import requests
from model.question import Question


class Sender:
    def __init__(self, question: Question, telegram_bot_url):
        self._question = question
        self._telegram_bot_url = telegram_bot_url

    def send_quiz(self):
        requests.post(self._telegram_bot_url, json=self._question)

    def run(self):
        self.send_quiz()
