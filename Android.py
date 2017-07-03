#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Android.py:	Is the Code for a School Project"""

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "0.5"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "In Progress"

from Terminal.KontrolleTerminal import StartC as Terminal
Terminal1 = Terminal()

"""
F1S = Finger 1 Signal Daumen                            29
F2S = Finger 2 Signal Zeigefinger                       31
F3S = Finger 3 Signal Mittelfinger                      33
F4S = Finger 4 Signal Ringfinger                        35
F5S = Finger 5 Signal Kleinerfinger                     37

H1S = Handgelenk 1 Signal Handgelenk                    40

E1S = Ellenbogen 1 Signal Ellenbogen Horizontale        36
E2S = Ellenbogen 2 Signal Ellenbogen Vertikal           38

LEDPin                                                  7
"""


def main():
    welcomestring = "       ***Robot-Hand-Controller***\n" \
                    "          by Marc Steinebrunner\n\n"

    print(welcomestring)
    Var = int(input("Wollen sie das Programm im Terminal Modus[1] starten oder im Blynk modus[2]: "))
    while True:
        if Var == 1:
            Terminal1.Starten()
            break
        elif Var == 2:
            print("Not available")
            break
        else:
            print("Error")

if __name__ == '__main__':
    main()
