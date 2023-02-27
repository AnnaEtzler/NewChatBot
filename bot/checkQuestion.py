import game_quiz.game
from bot import keywords
from database import repository


def check(question):
    if question in keywords.keywords_list:
        result = keywords.check_keywords_list(question)
    else:
        result = check_question(question)
    return result


def check_question(question):
    if question == "game":
        game_quiz.game.play()
        return ""

    return repository.getAnswer(question)



