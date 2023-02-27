import progress
from bot import helper


def getAnswers(answers):
    counter = 0
    for i in answers:
        counter += 1
        print(f"{counter}) {i}")

def play():
    game = helper.initGame()
    questions = game.keys()
    flag = True
    punkte = 0
    counter = 1
    while flag:
        for q in questions:
            message =f"{counter}.{q}"
            print(message)
            answers = game.get(q)
            getAnswers(answers)
            answer = input("you antwort: ")
            if answer == "exit":
                return

            while answer not in ["1", "2", "3", "4"]:
                print("Answer must be 1 or 2 or 3 or 4")
                answer = input("you antwort: ")

            check = checkAntwort(q, answer, game)
            if check is True:
                punkte += 1
            Progress.showProgress(punkte)
            print(f"{punkte} from 10")
            counter = counter + 1
            if counter == 11:
                print("End of game")
                flag = False

def checkAntwort(question, answer, game):
    rightAnswers = {
        "In welcher Einheit wird der elektrische Widerstand gemessen?": "1",
        "Welche ist die korrekte Schreibweise?": "2",
        "Wie lautet der Satz des Pythagoras?": "2",
        "Was ist die Hauptstadt von Deutschland?": "3",
        "Wie viele Bundesländer hat Deutschland?": "4",
        "Was bedeutet die Abkürzung IT": "2",
        "Was ist der höchste Berg Deutschlands?": "1",
        "Welches ist das höchste Amt in Deutschland?": "3",
        "Was macht ein DT-Student am liebsten?": "4",
        "Wie lautet das chemische Symbol für Wasserstoff?": "4"
    }
    result = rightAnswers.get(question)

    if answer == result:
        return True
    return False
'''

    def play(self):
        Punktestand = 0
        while len(self.questions) > 0:
            i = randint(0, len(self.questions) - 1)
            ausgabe(str(self.questions[i]))
            options, correct_answer = self.answers[i]
            for j in range(len(options)):
                ausgabe(str(j + 1) + ":" + options[j])
            guess = input(datetime.now().strftime(
                "%H:%M:%S") + " " + "Rainer: " + "Bitte wähle eine Antwortmöglichkeit aus (1,2,3,4): ")
            if guess == "stop":
                ausgabe(f"Du hast aktuell {Punktestand} von möglichen 10 Punkten")
                time.sleep(2)
                os.system("cls")
                break
            if guess.isnumeric():
                if guess == correct_answer:
                    Punktestand += 1
                    ausgabe("Korrekt!")
                else:
                    ausgabe("Falsch. Die richtige Antworte wäre: " + correct_answer)

                # self.questions.remove(self.questions[i])
                del self.questions[i]
                del self.answers[i]
            else:
                ausgabe("Fehler! Bitte nutze nur 1,2,3 oder 4")
                continue
        ausgabe("Du hast" + " " + str(Punktestand) + " " + "von möglichen" + " " + "10" + " " + "Punkten erreicht")

'''



