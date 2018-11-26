import math

# Auszahlung berechen
from sys import argv

#  __     __    _ _     _                  _                
#  \ \   / ___ | |   __| | __ _ _ __   ___| |__   ___ _ __  
#   \ \ / / _ \| |  / _` |/ _` | '_ \ / _ | '_ \ / _ | '_ \ 
#    \ V | (_) | | | (_| | (_| | | | |  __| |_) |  __| | | |
#     \_/ \___/|_|_ \__,_|\__,_|_| |_|\___|_.__/ \___|_| |_|


def auszahlung(guesses):
    return sum(min(abs(number - guess) for guess in guesses) for number in glueckszahlen)


def zahlen_berechnen():
    letztes_ergebnis = 0
    intervall_len = int(math.ceil(len(glueckszahlen) / 10))  # Runde die Nummer
    while intervall_len < len(glueckszahlen):  # Endlosschleife vermeiden
        ergebnis = []
        while len(ergebnis) < 10:  # 10 Zahlen generieren
            start = len(ergebnis) * intervall_len
            ende = len(ergebnis) * intervall_len + intervall_len
            segment = glueckszahlen[start:ende]  # Eine Segment aus der der Liste herausnehmen
            if len(segment) == 0:  # Wenn keine Nummern im Segment die ganze Liste benutzen
                segment = glueckszahlen

            ergebnis.append(
                min([nummer for nummer in segment],
                    key=lambda nummer: sum(
                        min(abs(glueckszahl - zahl) for zahl in ergebnis + [nummer]) for glueckszahl in
                        segment)))  # Die Nummer mit der kleinsten Auszahlung ermitteln, dabei durch alle gluckszahlen iterieren

        if letztes_ergebnis and auszahlung(ergebnis) > auszahlung(
                letztes_ergebnis):  # Die letzte Zahlenreihe zurueckgeben falls die neue eine groessere Auszahlung bedeutet
            return letztes_ergebnis
        letztes_ergebnis = ergebnis
        intervall_len += 1


if __name__ == '__main__':

    datei_name = argv[1]
    glueckszahlen = sorted([int(line) for line in open(datei_name, "r").readlines() if
                            1 <= int(line) <= 1000])  # Lese alle Zahlen zwischen 1 und 1000 ein

    if len(set(glueckszahlen)) <= 10:  # Es muessen mehr als 10 verschiedene Zahlen in der Liste enthalten sein
        ausgabe = sorted(list(set(glueckszahlen)) + [0] * (
                10 - len(set(glueckszahlen))))  # Die Ausgabe auf 10 Zahlen mit 0 auffuellen und sortieren
    else:
        ausgabe = sorted(zahlen_berechnen())  # Zahlen im Ergebnis sortieren

    # Ergebnis ausgeben
    print("AL's Zahlen %r\nEinnahmen: %d€ - Ausgaben: %d€ = Gewinn: %d€" % (
        ausgabe, len(glueckszahlen) * 25, auszahlung(ausgabe), len(glueckszahlen) * 25 - auszahlung(ausgabe)))
