from PyQt5.QtWidgets import QApplication


from random import choice, shuffle
from time import sleep

app = QApplication([])
from m2 import*
from m3 import*

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
       self.question = question
       self.answer = answer
       self.wrong_answer1 = wrong_answer1
       self.wrong_answer2 = wrong_answer2
       self.wrong_answer3 = wrong_answer3
q1 = Question("Привіт як твій настрій?", "шикарно", "добре", "погано", "супер погано")
q2 = Question("В каком году приисходят приключения 4 сезона джо джо?", "1999", "1930", "1956", "1978")
q3 = Question("Какой главний герой 4 сезона джо джо?", "жоски", "джотаро", "акуясу", "койчи")
q4 = Question("В какой сезон джо джо появился джорно джовано?", "5", "1", "3", "7")
q5 = Question("Кто бив владельцам хермит пюрпул?", "джозеф", "джотаро", "жоски", "допио")
q6 = Question("Кто бив владельцам кинг кримсона?", "боос", "наранчо", "фугу", "бучилати")
q7 = Question("Как дио контролиравав своих приспешников?", "паразит", "гипноз", "вампирская кровь", "яд")
q8 = Question("Какой стенд у дио?", "зе ворлд", "кинг кримсон", "аеросмит", "стар платинум")
q9 = Question("Какой стенд був у мисти?", "сикс пістолс", "кинг кримсон", "ге", "вайт албум")
q10 = Question("Как еволіцінували стенди в джо джо?", "реквием стрела", "випить кровь джозефа", "менянея вида владельца", "сила")
window.show()
app.exec_()
