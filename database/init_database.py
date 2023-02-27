import sqlite3 as sq

def initDatabase():
    c = sq.connect('questions_answers.db')
    c.close()


def initQuestions():
    questions = [("1", "Welche Bachelor-Studiengaenge werden an der Ostfalia angeboten?"),
                 ("2", "Welche Masterstudiengaenge werden an der Ostfalia angeboten?"),
                 ("3", "Was sind die Voraussetzungen fuer ein Bachelor-Studium?"),
                 ("4", "Was sind die Voraussetzungen fuer ein Masterstudium?"),
                 ("5", "Wie kann ich Ostfalia kontaktieren?"),
                 ("6", "Werden Stipendien angeboten?"),
                 ("7", "Gibt es Studiengebuehren?"),
                 ("8", "Gibt es eine Frist fuer die Bewerbung?"),
                 ("9", "Gibt es Angebote fuer ein Studentenwohnheim?"),
                 ("10", "Kann ich von einer anderen Universitaet wechseln?")]

    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS questions(
                   id INT,
                   question TEXT);
                """)
        conn.commit()
        cur.executemany("INSERT INTO questions VALUES(?, ?);", questions)
        conn.commit()

def initAnswers():
    answers = [
        ("1", "Die Ostfalia bietet Bachelor-Studiengaenge in den Bereichen Wirtschaft, Ingenieurwesen und Informatik an."),
        ("1", "Die Ostfalia bietet eine breite Palette von Bachelor-Studiengaengen an, darunter Ingenieurwissenschaften, Wirtschaftswissenschaften und Informatik." ),
        ("1", "Die Ostfalia bietet die folgenden Bachelor-Studiengaenge an  Wirtschaftswissenschaften, Ingenieurwesen und Informatik."),
        ("1", "Die Informationen konnen Sie auf dem Webseite bekommen https://www.ostfalia.de/cms/de/ "),

        ("2","Die Ostfalia bietet Masterstudiengaenge in den Bereichen Wirtschaft, Ingenieurwesen und Informatik an." ),
        ("2", "Die Ostfalia bietet ein breites Spektrum an Masterstudiengaengen in den Bereichen Ingenieurwesen, Wirtschaft und Informatik an."),
        ("2", "Die Ostfalia bietet folgende Masterstudiengaenge an  Wirtschaftswissenschaften, Ingenieurwissenschaften und Informatik."),
        ("2", "Die Informationen konnen Sie auf dem Webseite bekommen https://www.ostfalia.de/cms/de/ "),

        ("3", 'Um fuer einen Studiengang einzuschreiben, sind ein Abiturzeugnis und ein Nachweis zur deutschen Sprachkenntnisse erforderlich.'),
        ("3", 'Fuer die Aufnahme eines Bachelorstudiums an der Ostfalia sind folgende Zeugnisse erforderlich  ein Abiturzeugnis und ein Nachweis ueber deutsche Sprachkenntnisse.'),
        ("3", 'Schulabschluss und ein Nachweis ueber deutsche Sprachkenntnisse muessen vorgelegt werden, um in einen Bachelor-Studiengang eingeschrieben zu werden.'),


        ("4", 'Um in einen Masterstudiengang eingeschrieben zu werden, sind ein Bachelor-Zeugnis und ein Nachweis deutscher Sprachkenntnisse erforderlich. '),
        ("4", 'Fuer die Aufnahme eines Masterstudiums an der Ostfalia sind folgende Nachweise erforderlich  ein Bachelor-Zeugnis und ein Nachweis ueber deutsche Sprachkenntnisse.'),
        ("4", 'Fuer die Bewerbung zu einem Master-Studiengang muessen Sie ein Bachelor-Zeugnis und einen Deutsch-Sprachnachweis vorlegen.'),
        ("4", 'Fuer die Immatrikulation in einen Masterstudiengang muessen ein Bachelor-Zeugnis und ein Nachweis ueber Deutschkenntnisse vorgelegt werden.'),


        ("5", 'Sie koennen die Ostfalia per E-Mail erreichen  beratung@ostfalia, oder per Telefon  12345678.'),
        ("5", 'Ostfalia E-Mail ist beratung@ostfalia und Telefonnummer ist 987654321'),
        ("5", 'Ja, bitte kontaktieren Sie diese email  stipendium@ostfalia.'),
        ("5", ' Die Kontaktdaten der Ostfalia lauten E-Mail  beratung@ostfalia, und Telefon 1234567.'),


        ("6", 'Ja, wir bieten unter bestimmten Bedingungen Stipendien an.'),
        ("6", ' Fuer weitere Informationen wenden Sie sich bitte an die folgende E-Mail-Adresse  stipendium@ostfalia.'),


        ("7", ' Ja, ein Semester kostet insgesamt 200 Euro.'),
        ("7", 'Ein Semester kostet 200 Euro. '),
        ("7", 'Es gibt einen Semesterbeitrag von 200 Euro'),
        ("7", 'Ja, das Semester an der Ostfalia kostet 200 Euro inklusive der Ostfalia Card Gebuehren.'),


        ("8", 'Ja, die Bewerbungsfrist fuer das Wintersemester ist immer am 15.07, und die Bewerbungsfrist fuer das Sommersemester ist am 15.01.'),
        ("8", 'Ja, der 15.07. ist der Bewerbungstermin fuer das Wintersemester, der 15.01. fuer das Sommersemester. '),
        ("8", ' Ja, Sie koennen sich fuer das Wintersemester bis zum 15.07 und fuer das Sommersemester bis zum 15.01 bewerben.'),
        ("8", 'Die Informationen konnen Sie auf dem Webseite bekommen https://www.ostfalia.de/cms/de/ '),

        ("9", 'Ja, wir bieten eine breite Palette von Zimmern fuer Studenten. Bitte kontaktieren Sie diese E-Mail fuer Anfragen  wohnheim@ostfalia. '),
        ("9", 'Ja, es gibt ein Studentenwohnheim. Bitte kontaktieren Sie diese E-Mail  wohnheim@ostfalia.'),
        ("9", 'Ja, wir bieten Studentenwohnheime zu guenstigen Preisen an. Bitte kontaktieren Sie diese Email fuer weitere Informationen  wohnheim@ostfalia.'),
        ("9", 'Ja, bitte kontaktieren Sie diese E-Mail fuer weitere Informationen/Anfragen  wohnheim@ostfalia.'),

        ("10", 'Ja, wir akzeptieren Quereinsteiger, allerdings erst nach Pruefung der abgeschlossenen Kurse an der anderen Universitaet.'),
        ("10", ' Ja, Sie koennen Ihr Studium an der Ostfalia fortsetzen, aber zuerst muessen wir die Kurse bewerten, die Sie an der anderen Universitaet abgeschlossen haben.'),
        ("10", ' Ja, das koennen Sie unter bestimmten Bedingungen. '),
        ("10", 'Ja, die Informationen konnen Sie auf dem Webseite bekommen https://www.ostfalia.de/cms/de/')]

    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS answers(
                   id INT,
                   answer TEXT);
                """)
        cur.executemany("INSERT INTO answers VALUES(?, ?);", answers)
        conn.commit()






def get_answer_and_questions():
    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions")
        list_of_q = cur.fetchall()

        print(list_of_q)
        print("------------------------------------------------------------")


    with sq.connect("questions_answers.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM answers")
        list_of_answers = cur.fetchall()
        print(list_of_answers)
