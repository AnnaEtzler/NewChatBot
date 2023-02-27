import argparse
import datetime
import sys


def getData():
    data = datetime.datetime.today().strftime("%H:%M:%S")
    return data


def parser_initialization():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ask", help="Wird benutzt um eine Frage direkt zu stellen")
    parser.add_argument("--questions", action="store_true", help="Liste aller bekannten Fragen")
    parser.add_argument("--add", action="store_true", help="Wird benutzt um eine Frage hinzuzufügen")
    parser.add_argument("--remove", action="store_true", help="Wird benutzt um eine Frage zu entfernen")
    parser.add_argument("--question", required="--add" in sys.argv or "--remove" in sys.argv, help="Text der Frage")
    parser.add_argument("--answer", required="--add" in sys.argv, help="Text der Antwort")
    parser.add_argument("--import", action="store_true", help="Importieren von externen Dateien")
   # parser.add_argument("--filetype", required="--import" in sys.argv, help="Dateityp")
    parser.add_argument("--filepath", required="--import" in sys.argv, help="Pfad der Datei")
    parser.add_argument("--telegram", action='store_true', help="Wird telegram bot aktiviert ")

    return parser

def initGame():
    game = {"In welcher Einheit wird der elektrische Widerstand gemessen?": ["Ohm", "Volt", "Ampere", "Watt"],
            "Welche ist die korrekte Schreibweise?": ["nemlich", "nämlich", "nähmlich", "nehmlich"],
            "Wie lautet der Satz des Pythagoras?": ["a²-b²=c²", "a²+b²=c²", "a²*b²=c²", "Was ist Pythagoras?"],
            "Was ist die Hauptstadt von Deutschland?": ["Köln", "München", "Berlin", "Hamburg"],
            "Wie viele Bundesländer hat Deutschland?": ["17", "Deutschland hat keine Bundesländer",
                                                        "Malle ist nur einmal im Jahr!!!", "16"],
            "Was bedeutet die Abkürzung IT": ["Internationaler Tierschutz", "Informationstechnik", "Italien",
                                              "Intime Teamarbeit"],
            "Was ist der höchste Berg Deutschlands?": ["Zugspitze", "Brocken", "Großer Berg", "Fichtelberg"],
            "Welches ist das höchste Amt in Deutschland?": ["König von Deutschland", "Imperator", "Bundespräsident",
                                                            "DT-Studenten"],
            "Was macht ein DT-Student am liebsten?": ["Mathe-Vorlesung", "WInf-Vorlesung", "Schlafen", "Plotten"],
            "Wie lautet das chemische Symbol für Wasserstoff?": ["O", "WS", "WA", "H"]
            }

    return game