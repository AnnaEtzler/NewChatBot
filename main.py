import sys
import time
import database
from bot import helper, checkQuestion, command_line_argument


#database.init_database.get_answer_and_questions()
#database.init_database.initDatabase()
#database.init_database.initQuestions()
#database.init_database.initAnswers()

def start():
    if len(sys.argv) < 2:
        print(helper.getData() + " Hello")
        while True:
            question = input(helper.getData() + " How can I help you?\n")
            if question.lower() == "bye":  # exit
                print(helper.getData() + " Bye")
                break
            answer = checkQuestion.check(question)  # search the answer
            if answer == "":
                continue
            print(helper.getData() + " " + answer)
            time.sleep(1)
    else:
        command_line_argument.check()


start()

