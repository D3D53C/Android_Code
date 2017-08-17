# coding=utf-8
from .Action import ActrionC as Action
from .Manuel import ManuelC as Manuel
from Basic.LED import LED_C as LED
from Basic.servo import Servo as Servo
import sys


# noinspection PyCallByClass
class StartC(object):
    def __init__(self):

        self.Style = 1
        Array_Glieder = [0, 1, 2, 3, 4, 5, 6, 7]
        self.Pin_Array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        Klaue = [0, 1]

        Klaue[0] = 180
        Klaue[1] = 0
        self.Pin_Array[0] = 29
        self.Pin_Array[1] = 32
        self.Pin_Array[2] = 33
        self.Pin_Array[3] = 35
        self.Pin_Array[4] = 37
        self.Pin_Array[5] = 40
        self.Pin_Array[6] = 36
        self.Pin_Array[7] = 38
        self.Pin_Array[8] = 7


        Array_Glieder[0] = Servo(self.Pin_Array[0], 50, 500, 2500, 180)  # Kralle + Finger1
        Array_Glieder[1] = Servo(self.Pin_Array[1], 50, 500, 2500, 180)  # Finger2
        Array_Glieder[2] = Servo(self.Pin_Array[2], 50, 500, 2500, 180)  # Finger3
        Array_Glieder[3] = Servo(self.Pin_Array[3], 50, 500, 2500, 180)  # Finger4
        Array_Glieder[4] = Servo(self.Pin_Array[4], 50, 500, 2500, 180)  # Finger5
        Array_Glieder[5] = Servo(self.Pin_Array[5], 50, 500, 2500, 180)  # Handgelenk
        Array_Glieder[6] = Servo(self.Pin_Array[6], 50, 500, 2500, 180)  # Ellenbogen 1
        Array_Glieder[7] = Servo(self.Pin_Array[7], 50, 500, 2500, 180)  # Ellenbogen 2

        self.Action = Action(self.Style, Array_Glieder, Klaue)
        self.Manuel = Manuel(self.Style, Array_Glieder, Klaue)
        self.LED = LED(self.Pin_Array[8])

        self.StyleString =          "\nStyle Auswahl\n" \
                                    "[1] Style mit Fingern\n" \
                                    "[2] Style mit Klaue\n" \
                                    "Ihre Eingabe :"
        self.Eingabebestaetigung =  "Eingabe Bestätigt \n" \
                                    "\n\n"
        self.SettingsString =       "\n *********Settings*********\n " \
                                    "[0] Daumen         => Pin:" + self.Pin_Array[0] + "\n"\
                                    "[1] Zeigefinger    => Pin:" + self.Pin_Array[1] + "\n"\
                                    "[2] Mittelfinger   => Pin:" + self.Pin_Array[2] + "\n"\
                                    "[3] Ringfinger     => Pin:" + self.Pin_Array[3] + "\n"\
                                    "[4] Kleinerfinger  => Pin:" + self.Pin_Array[4] + "\n"\
                                    "[5] Handgelenk     => Pin:" + self.Pin_Array[5] + "\n"\
                                    "[6] Ellenbogen H.  => Pin:" + self.Pin_Array[6] + "\n"\
                                    "[7] Ellenbogen V.  => Pin:" + self.Pin_Array[7] + "\n"\
                                    "[8] LED            => Pin:" + self.Pin_Array[8] + "\n"\
                                    "[9] Style          =>     " , self.Style        , "\n"\
                                    "Wollen sie etwas Ändern? (Y = 1|N = 0): "



    def Settings(self):
        Entscheidung = int(input(self.SettingsString))
        if (Entscheidung == 1):
            WasEntscheidung = int(input("Die Zahl in den Eckigen klammern eingeben dessen Pin sie Ändern wollen: "))
            if WasEntscheidung == 9:
                self.Style = int(input(self.StyleString))
                print(self.Eingabebestaetigung)
            else:
                self.Pin_Array[WasEntscheidung] = int(input("Neuer Pin eingeben: "))
                print(self.Eingabebestaetigung)
        elif (Entscheidung == 0):
            pass
        else:
            print("ERROR 406")

    def Starten(self):
        print("\n\n\n")
        Auswahlstring = "Ihnen stehen folgende Aktionen zurverfügung:\n\n" \
                        "[0]    Um das Programm zu beenden\n" \
                        "[1]    Action1 (Finger auf und zu)\n" \
                        "[2]    Action2 (Bewegt Elenbogen hoch Handgelenk nach vorne und alle Finger auf und zu)\n" \
                        "[3]    Action3 (Greifen)\n" \
                        "[4]    Manuel  (Laesst sie die Gelenke einzeld bewegen)\n" \
                        "[5]    LED Morsecode\n" \
                        "[6]    Einstellungen\n" \
                        "Die Zahl in der Eckigen Klammer ist für die Eingabe: "
        while (True):
            Auswahl = int(input(Auswahlstring))

            if (Auswahl == 1):
                print("\n\n\n")
                self.Action.Action1()
                break
            elif (Auswahl == 0):
                print("\n\n\n")
                sys.exit("Vielen dank für die benutzung dieser Software")
            elif (Auswahl == 2):
                print("\n\n\n")
                self.Action.Action2()
                break
            elif (Auswahl == 3):
                print("\n\n\n")
                self.Action.Action3()
                break
            elif (Auswahl == 4):
                print("\n\n\n")
                self.Manuel.Kontrolle()
            elif (Auswahl == 5):
                print("\n\n\n")
                x = 0
                while (x <= 1):
                    Buchstabe = int(input("Bitte einen Buchtaben auswählen 1-26 = A-Z Ä=27 Ü=28 Ö=29:  "))
                    # noinspection PyCallByClass
                    self.LED.Alphabet(Buchstabe)
                    Ende = int(input("Noch ein Buchstabe ? [Y=1/N=0] --> "))
                    if (Ende == 0):
                        print("\n\n")
                        break
                    elif (Ende == 1):
                        x = 1
                    else:
                        print("Error 405")
            elif (Auswahl == 6):
                print("\n\n\n")
                self.Change_Style()
                """
            else:
                print("ERROR")
                break
               """
