import sqlite3 as sq
import random

def add(question, answer): # 17
    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        count = cur.execute("SELECT count(*) FROM questions;").fetchone()
        countNew = count[0] + 1
        print(countNew, question, answer)
        cur.execute(f"INSERT INTO questions (id, question) VALUES ({countNew}, '{question}');")
        cur.execute(f"INSERT INTO answers (id, answer) VALUES ({countNew}, '{answer}');")
        conn.commit()
        print(getQuestions())


def remove(question): # 17 DELETE FROM
    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM questions WHERE question='{question}'")
        print(cur.fetchone())
        print("deleted")


def getQuestions():
    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions")
        list_of_q = cur.fetchall()
        print(list_of_q)

def getAnswer(question):
    id = searchId(question)
    if id == 0:
        return "Question is not recognized"
    with sq.connect("questions_answers.db") as conn:
        curr = conn.cursor()
        curr.execute(f"SELECT * FROM answers WHERE id={id}")
        list_of_answers = curr.fetchall()
        random_answer = random.randint(0, len(list_of_answers)-1)
        result = list_of_answers[random_answer][1]
    return result


def importNewQuestions(filepath):
    info = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for l in lines:
            info.append(l.split("#"))
    questions = []
    answers = []
    for i in info:
        question = (i[0].split(";"))
        questions.append(question)
        answer = (question[0], i[1].split(";"))
        answers.append(answer)
    answersResult = []
    for a in answers:
        for k in a[1]:
            res = (a[0], k)
            answersResult.append(res)
    with sq.connect("questions_answers.db") as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO answers VALUES(?, ?);", answersResult)
        cur.executemany("INSERT INTO questions VALUES(?, ?);", questions)
        con.commit()
    print("ok")

def searchId(question):
    with sq.connect("questions_answers.db") as con:
        id = 0
        cur = con.cursor()
        cur.execute("SELECT * FROM questions;")
        all_results = cur.fetchall()
        for i in all_results:
            if question in i:
                id = i[0]
        return id