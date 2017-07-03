
from Basic.servo import Servo as Servo
import time
import sys


# noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
class ActrionC():
    
    style = 1
    
    def __init__(self, Style, Array_Glieder, Klaue):
        self.style = Style
        self.K1Open = Klaue[0]
        self.K1Closed = Klaue[1]

        self.F1S = Array_Glieder[0]
        self.K1 = Array_Glieder[0]
        self.F2S = Array_Glieder[1]
        self.F3S = Array_Glieder[2]
        self.F4S = Array_Glieder[3]
        self.F5S = Array_Glieder[4]
        self.H1S = Array_Glieder[5]
        self.E1S = Array_Glieder[6]
        self.E2S = Array_Glieder[7]

    def Action1(self):  # Finger einzelnd ein und Ausklappen

        if self.style == 1:
            self.F2S.change_position(0)
            time.sleep(2)
            self.F2S.change_position(180)
            time.sleep(0.5)
            self.F3S.change_position(0)
            time.sleep(2)
            self.F3S.change_position(180)
            time.sleep(0.5)
            self.F4S.change_position(0)
            time.sleep(2)
            self.F4S.change_position(180)
            time.sleep(0.5)
            self.F5S.change_position(0)
            time.sleep(0.5)
            self.F5S.change_position(180)
        elif self.style == 2:
            self.K1.change_position(self.K1Open)
            time.sleep(0.5)
            self.K1.change_position(self.K1Closed)

    # noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
    def Action2(self):  # Bewegt Ellenbogen hoch, dreht Handgelenk, Schließt und öffnet alle Finger

        if self.style == 1:

            self.E1S.change_position(90)
            self.H1S.change_position(0)
            time.sleep(2)
            self.H1S.change_position(90)
            self.F5S.change_position(0)
            self.F4S.change_position(0)
            self.F3S.change_position(0)
            self.F2S.change_position(0)
            time.sleep(2)
            self.F1S.change_position(0)
            time.sleep(5)
            self.F1S.change_position(180)
            time.sleep(2)
            self.F5S.change_position(180)
            self.F4S.change_position(180)
            self.F3S.change_position(180)
            self.F2S.change_position(180)

        elif self.style == 2:
            self.E1S.change_position(90)
            self.H1S.change_position(0)
            time.sleep(2)
            self.H1S.change_position(90)
            self.K1.change_position(self.K1Open)
            time.sleep(0.5)
            self.K1.change_position(self.K1Closed)
            time.sleep(4)
            self.K1.change_position(self.K1Open)
            time.sleep(0.5)
            self.K1.change_position(self.K1Closed)

    # noinspection PyCallByClass,PyCallByClass,PyCallByClass,PyCallByClass
    def Action3(self):  #

        if self.style == 1:

            self.E1S.change_position(180)
            time.sleep(1)
            self.E2S.change_position(0)
            time.sleep(4)
            self.F5S.change_position(0)
            self.F4S.change_position(0)
            self.F3S.change_position(0)
            self.F2S.change_position(0)
            time.sleep(2)
            self.F1S.change_position(0)
            time.sleep(2)
            self.E1S.change_position(90)
            self.E2S.change_position(90)
            time.sleep(2)
            self.H1S.change_position(180)
            time.sleep(2)
            self.F1S.change_position(180)
            time.sleep(2)
            self.F5S.change_position(180)
            self.F4S.change_position(180)
            self.F3S.change_position(180)
            self.F2S.change_position(180)

        elif self.style == 2:
            self.E1S.change_position(180)
            time.sleep(1)
            self.E2S.change_position(0)
            time.sleep(4)
            self.K1.change_position(self.K1Open)
            self.E1S.change_position(90)
            self.E2S.change_position(90)
            time.sleep(2)
            self.H1S.change_position(180)
            time.sleep(2)
            self.K1.change_position(self.K1Closed)
            """
            Erweitungen vorgesehen
            """
