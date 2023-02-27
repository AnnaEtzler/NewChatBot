import telebot

import telegram_bot
from bot import helper, checkQuestion
from database import repository


def check():
    parser = helper.parser_initialization()
    args = vars(parser.parse_args())
    if args["questions"]: #16 Allow service-provider to list all questions via command line arguments
        repository.getQuestions()


    elif args["ask"]: #15 Allow users to ask questions via command line arguments
        print(repository.getAnswer(args.get("ask")))


    elif args["add"]:   # 17 Allows the service-provider to add and remove questions
        question = args["question"]
        answer = args["answer"]
        repository.add(question, answer)

    elif args["remove"]:
        question = args["question"]
        repository.remove(question)

    elif args["import"]:  #14 Add support for Q&A CSV import
        filepath = args["filepath"]
        repository.importNewQuestions(filepath)

    elif args["telegram"]:  # start telegram  bot
        bot = telebot.TeleBot("5912626227:AAFZK5IDJ3gqeTsj6p4LdAMpYA5F6JNtCr8")
        @bot.message_handler()
        def get_user_text(message):
            if message.text.lower() == "bye":
                bot.send_message(message.chat.id, "bye")
                bot.stop_polling()
            else:
                answer = checkQuestion.check(message.text)
                bot.send_message(message.chat.id, answer)

        bot.infinity_polling()
    else:
        print("keine passende arguments")









