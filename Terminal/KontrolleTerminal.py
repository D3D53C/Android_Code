# coding=utf-8
from .Action import ActrionC as Action
from .Manuel import ManuelC as Manuel
from Basic.LED import LED as LED
from Basic.servo import Servo as Servo


# noinspection PyCallByClass
class StartC(object):
                
    def __init__(self):

        self.Style = 1;
        Array_Glieder = [0, 1, 2, 3, 4, 5, 6, 7]
        Klaue = [0, 1]

        Klaue[0] = 180
        Klaue[1] = 0

        Array_Glieder[0] = Servo(29, 50, 500, 2500, 180)  # Kralle + Finger1
        Array_Glieder[1] = Servo(31, 50, 500, 2500, 180)  # Finger2
        Array_Glieder[2] = Servo(33, 50, 500, 2500, 180)  # Finger3
        Array_Glieder[3] = Servo(35, 50, 500, 2500, 180)  # Finger4
        Array_Glieder[4] = Servo(37, 50, 500, 2500, 180)  # Finger5
        Array_Glieder[5] = Servo(40, 50, 500, 2500, 180)  # Handgelenk
        Array_Glieder[6] = Servo(36, 50, 500, 2500, 180)  # Ellenbogen 1
        Array_Glieder[7] = Servo(38, 50, 500, 2500, 180)  # Ellenbogen 2

        self.Action = Action(self.Style, Array_Glieder, Klaue)
        self.Manuel = Manuel(self.Style, Array_Glieder, Klaue)
        
        
        self.StyleString =   "\nStyle Auswahl\n" \
                         "[1] Style mit Fingern\n" \
                         "[2] Style mit Klaue\n"\
                         "Ihre Eingabe :"
                
        self.Eingabebestaetigung = "Eingabe Bestätigt \n"\
                               "\n\n"
    # noinspection PyCallByClass
    def Change_Style(self):
                self.Style = int(input(self.StyleString))
                print(self.Eingabebestaetigung)
        
        
    def Starten(self):
        print("\n\n\n")
        Auswahlstring = "Ihnen stehen folgende Actionen zurverfügung:\n\n" \
                        "[1]    Action1 (Finger auf und zu)\n" \
                        "[2]    Action2 (Bewegt Elenbogen hoch Handgelenk nach vorne und alle Finger auf und zu)\n" \
                        "[3]    Action3 (Greifen)\n" \
                        "[4]    Manuel  (Laesst sie die Gelenke einzeld bewegen)\n" \
                        "[5]    LED Morsecode\n" \
                        "[6]    Style Ändern\n" \
                        "Die Zahl in der Eckigen Klammer ist für die Eingabe: "
        while (True):
            Auswahl = int(input(Auswahlstring))

            if (Auswahl == 1):
                print("\n\n\n")
                Action.Action1(self)
                break
            elif (Auswahl == 2):
                print("\n\n\n")
                Action.Action2()
                break
            elif (Auswahl == 3):
                print("\n\n\n")
                Action.Action3()
                break
            elif (Auswahl == 4):
                print("\n\n\n")
                Manuel.Kontrolle()
            elif (Auswahl == 5):
                print("\n\n\n")
                x = 0
                LED.Start(self)
                while (x <= 1):
                    Buchstabe = int(input("Bitte einen Buchtaben auswählen 1-26 = A-Z Ä=27 Ü=28 Ö=29"))
                    # noinspection PyCallByClass
                    LED.LED.Alphabet(Buchstabe)
                    Ende = int(input("Noch ein Buchstabe ? [Y=1/N=0]"))
                    if (Ende == 1):
                        break
                    elif (Ende == 0):
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
    
