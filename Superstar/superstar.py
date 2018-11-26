import random
from sys import argv


#  ____                            _             
# / ___| _   _ _ __   ___ _ __ ___| |_ __ _ _ __ 
# \___ \| | | | '_ \ / _ | '__/ __| __/ _` | '__|
#  ___) | |_| | |_) |  __| |  \__ | || (_| | |   
# |____/ \__,_| .__/ \___|_|  |___/\__\__,_|_|   
#             |_|                                


def folgt_niemandem(superstar, namen_liste, schon_ueberprueft):
    superstar_name = namen_liste[superstar]
    for person in namen_liste:
        if person != superstar_name and person != namen_liste[schon_ueberprueft]:
            if folgt(person, superstar_name):
                return False
    return True


def naechster(index, laenge):
    index += 1
    if index == laenge:
        index = 0
    return index


def folgt(gefolgter, folgender):
    print("Folgt Mitglied %s Mitglied %s?" % (folgender, gefolgter))
    global abfragen
    abfragen += 1
    file.seek(marker)  # Die Datei soll wieder nach der ersten Zeile anfangen zu lesen
    for line in file.readlines():
        if gefolgter in line and folgender in line:
            line = line.split()
            if folgender == line[0]:
                return True
    return False


def suche(namen_liste):
    superstar = random.randint(0, int(len(namen_liste) - 1))
    naechste_person = naechster(superstar, len(namen_liste))
    schon_ueberprueft = superstar
    nicht_superstar = []
    while len(nicht_superstar) < len(namen_liste):
        if folgt(namen_liste[superstar],
                 namen_liste[naechste_person]):  # Wird der superstar von der naechsten_person gefolgt?
            if naechste_person not in nicht_superstar:
                nicht_superstar.append(naechste_person)  # Die naechste_person kann nicht der Superstar sein
            naechste_person = naechster(naechste_person, len(namen_liste))
        else:
            nicht_superstar.append(superstar)  # Der potentielle superstar ist doch nicht der Superstar
            superstar, naechste_person, schon_ueberprueft = naechste_person, naechster(naechste_person, len(
                namen_liste)), superstar  # Der neue Superstar folgt nicht dem alten Superstar -> superstar in schon_uberprueft abgespeichert
        if naechste_person == superstar:
            if folgt_niemandem(superstar, namen_liste,
                               schon_ueberprueft):  # ueberpruefen ob der Superstar niemand folgt
                return namen_liste[superstar]
            else:
                return "niemand"
    return "niemand"


if __name__ == '__main__':

    file_name = argv[1]

    # Die Datei oeffnen
    file = open(file_name, "r")

    # Die Kosten der Suche
    abfragen = 0
    # Die erste Zeile mit allen Namen einlesen und in einem Array speichern
    namen = file.readline().split()

    if len(namen) != len(set(namen)):
        print("Fehler, Namen kommen oeffters vor!")
    # Ende der ersten Zeile der Datei
    marker = file.tell()

    if len(namen) > 1:
        # Das Resultat ausgeben
        print("Der Superstar ist: %s" % suche(namen))

        # Die Kosten der Suche ausgeben
        print('Die Abfragen kosten: %d€' % abfragen)
    else:
        print("fehlerhafte Datei!")
    # Die Datei schließen
    file.close()
