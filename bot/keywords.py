from bot import helper

'''I chose 5 keywords: Semester-Bachelor-Kontakt-Sprache-Kosten and stored them in a list. Then, I created 2 lists for each keyword: the
first list contains the questions and the second contains the answers. So in total there are 10 lists:5 question lists and 5 answer lists.'''

semester_fragen_list = ['1-Wann beginnt das Wintersemester 22/23?', '2-Wann endet das Wintersemester 22/23 ?',
                        '3-Wann finden die Klausuren des Wintersemesters 22/23 statt?',
                        '4-Wie viel ist der Semesterbietrag?',
                        '5-Wann beginnt das Sommersemester 2023 ? ']

semester_antworten_list = ['1-Wintersemester 22/23 fängt am 1.10.2022 an.', '2-Wintersemester 22/23 endet am 1.02.2023',
                           '3-Die Klausuren im Wintersemester 22/23 fangen am 1.01.2023 an',
                           '4-Der Semesterbeitrag ist 200 Euros',
                           '5-Sommersemester 2023 fängt am 1.04.2023 an']

bachelor_fragen_list = ['1-Welche Bachelorstudiengänge bieten wir an?',
                        '2-Wie kann ich mich für einen Bachelorstudiengang einschreiben?',
                        '3-An wen kann ich mich für Anfragen zu Bachelorstudiengängen wenden?',
                        '4-Welche Karrieremöglichkeiten gibt es für Bachelor-Absolventen?']

bachelor_antworten_list = [
    '1-Wir bieten Bachelorstudiengämge in Wirtschaft, Informatik,Recht und Ingenieurwissenschaften.',
    '2-Sie könnten uns Ihre Bewerbung  entweder per Email: applications@uni1.de oder per Post: 12345 Clausthal schicken.',
    '3-Wenden Sie sich an diese E-Mail für Bachelor-Anfragen: bachelorinq@uni1.de',
    '4-Sie könnten sich unsere Alumni Website unter Students<Alumni anschauen ']

kontakt_fragen_list = ['1-Welche E-Mail kann ich für allgemeine Anfragen kontaktieren?',
                       '2-Welche E-Mail kann ich für Bachelor-Anfragen kontaktieren?',
                       '3-Welche E-Mail kann ich für Master-Anfragen kontaktieren?',
                       '4-Wie kann ich die Zulassungsstelle kontaktieren?',
                       '5-Wie kann ich das Büro "Austauschstudenten" kontaktieren?']

kontakt_antworten_list = ['1-Allgemeine Anfrage email: General@uni1.de',
                          '2-Bachelor Anfrage email:bachelorinq@uni1.de',
                          '3-Master Anfrage email: masterinq@uni1.de',
                          '4-Telefonnummer der Zulassungsstelle:1234667',
                          '5-Telefonnummer des Büros für Austauschstudenten:34632455']

sprache_fragen_list = ['1-Muss ich meine Kenntnisse der deutschen Sprache nachweisen?',
                       '2-Welche Sprachezertifikate sind zulässig?',
                       '3-Gibt es einen Sprachkurs?',
                       '4-Wie viel kostet ein Sprachkurs?']

sprache_antworten_list = ['1-Ja, Sie sollten mindestens ein B2 Zertifikat haben.',
                          '2-DSH,Telc C1,Goethe C2',
                          '3-Es gibt einen Sprachkurs, der am 1.1.2023 anfängt.',
                          '4-Ein Sprachkurs kostet 1000 Euro']

kosten_fragen_list = ['1-Wie viel kostet das Studentenwohnheim?',
                      '2-Wie viel kosten die Lebenshaltungskosten monatlich?',
                      '3-Wie viel kostet ein Semester?',
                      '4-Gibt es eine Unterstützung bei den Kosten?']

kosten_antworten_list = [
    '1-Im Durchschnitt kostet ein Studentenwohnheim, das aus einem Privatzimmer, einer Gemeinschaftsküche und einem Bad besteht, 300 Euro pro Monat.',
    '2-Im Durchschnitt :500 Euro',
    '3-Ein Semester kostet 200 Euros',
    '4-Ja, wir bieten Studiendarlehen an.']

keywords_list = ['Semester', 'Bachelor', 'Kontakt', 'Sprache', 'Kosten']

fragen_list = [semester_fragen_list, bachelor_fragen_list, kontakt_fragen_list, sprache_fragen_list, kosten_fragen_list]

antworten_list = [semester_antworten_list, bachelor_antworten_list, kontakt_antworten_list, sprache_antworten_list,
                  kosten_antworten_list]


def check_keywords_list(question):
    index = keywords_list.index(question)
    print('\n')
    for i in fragen_list[index]:
        print(i)  # prints the question list of the corresponding keyword
    print(helper.getData() + 'Wählen Sie eine Frage aus (Geben Sie eine Nummer): ')  # allows the user to input an integer which is the number of the question
    nummer = int(input(helper.getData() + " "))
    antwort_index = nummer - 1  # I reduced the the variable i by 1 because the index of the answer is 1 less than the number of the question

    return helper.getData() + " " + antworten_list[index][antwort_index]
