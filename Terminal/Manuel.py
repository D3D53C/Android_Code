# coding=utf-8
import Basic.servo as Servo


# noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
class ManuelC:
    def __init__(self, Style, Array_Glieder, Klaue):

        self.style = Style

        self.K1_Open = Klaue[0]
        self.K1_Close = Klaue[1]

        self.F1S    = Array_Glieder[0]
        self.K1     = Array_Glieder[0]
        self.F2S    = Array_Glieder[1]
        self.F3S    = Array_Glieder[2]
        self.F4S    = Array_Glieder[3]
        self.F5S    = Array_Glieder[4]
        self.H1S    = Array_Glieder[5]
        self.E1S    = Array_Glieder[6]
        self.E2S    = Array_Glieder[7]

    def Kontrolle(self):
        x = 0
        Auswahlstring = "Manuele Kontrollle \n" \
                        "Daumen 1,Zeigefinger 2,Mittelfinger 3, Ringfinger 4, KFinger 5 \n" \
                        "Handgelenk 6, EllenbogenH 7, EllenbogenV 8\n"\
                        "Falls Klaue ausgewählt is: 9 \n\n"

        KlaueString = "Zum schliessen 1 Drücken\n"\
                      "Zum öffnen 2 druecken\n\n"
        while (x <= 1):
            Auswahl = int(input(Auswahlstring))
            if Auswahl == 1:
                Degree = int(input("Degree ?\n"))
                self.Daumen(Degree)
            elif Auswahl == 2:
                Degree = int(input("Degree ?\n"))
                self.Zeigefinger(Degree)
            elif Auswahl == 3:
                Degree = int(input("Degree ?\n"))
                self.Mittelfinger(Degree)
            elif Auswahl == 4:
                Degree = int(input("Degree ?\n"))
                self.Ringfinger(Degree)
            elif Auswahl == 5:
                Degree = int(input("Degree ?\n"))
                self.KleinerFinger(Degree)
            elif Auswahl == 6:
                Degree = int(input("Degree ?\n"))
                self.Handgelenk(Degree)
            elif Auswahl == 7:
                Degree = int(input("Degree ?\n"))
                self.EllenbogenH(Degree)
            elif Auswahl == 8:
                Degree = int(input("Degree ?\n"))
                self.EllenbogenV(Degree)
            elif Auswahl == 9:
                Offen_Geschlossen = int(input(KlaueString))
                self.Klaue(Offen_Geschlossen)

    # noinspection PyCallByClass
    def KleinerFinger(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Ringfinger(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Mittelfinger(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Zeigefinger(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Daumen(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def EllenbogenH(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def EllenbogenV(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    # noinspection PyCallByClass
    def Handgelenk(self, Degree):
        # noinspection PyCallByClass
        self.Finger.change_position(Degree)

    def Klaue(self, Offengeschlossen):
        if Offengeschlossen == 1:
            self.K1.change_position(self.K1_Close)
        elif Offengeschlossen == 2:
            self.K1.change_position(self.K1_Open)
        elif Offengeschlossen <=0:
            print ("Error")
        elif Offengeschlossen >= 3:
            print ("Error")