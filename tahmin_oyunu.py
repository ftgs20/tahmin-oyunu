# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 00:04:32 2019

@author: fatih tosun
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *

import sys
import random
import time



class Pencere(QWidget):
    def __init__ (self):
        super().__init__()
        self.setUI()
        self.tahmin=0
        self.kücük_sayi=0
        self.büyük_sayi=100
        self.sayac=0
        
    
    def setUI(self):
        self.setWindowTitle("Sayı Tahmin Programı")
        self.soru_ekrani=QLabel()
        self.cevap_ekrani=QLineEdit()
        self.mesaj=QLabel()
        self.button=QPushButton("BAŞLA")
        self.button1=QPushButton()
        self.cikalim=QPushButton("Çıkış")
        
        self.media=QMediaPlayer()
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/Gong.mp3")))
        self.media1=QMediaPlayer()
        self.media1.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/PING.mp3")))
        self.media2=QMediaPlayer()
        self.media2.setMedia(QMediaContent(QUrl.fromLocalFile("C:/Users/fatih/Desktop/Yeni klasör/Yeni klasör/alkis1.wav")))

        self.media.setVolume(50)
        self.media1.setVolume(50)
        self.media2.setVolume(50)
        
        self.soru_ekrani.setFont(QFont("Comic Sans MS",25))
        self.cevap_ekrani.setFont(QFont("Comic Sans MS",25))
        self.mesaj.setFont(QFont("Comic Sans MS",25))
        self.button.setFont(QFont("Comic Sans MS",25))
        self.button1.setFont(QFont("Comic Sans MS",25))
        self.cikalim.setFont(QFont("Comic Sans MS",25))

        #setFont(QFont("Comic Sans MS",25))    
        
        self.button1.setText("Tahmin Et")        
        self.soru_ekrani.setText("Tahmin Et oyununa hoşgeldin.\nBaşlamak için BAŞLA'ya bas.")
        
        v_box=QVBoxLayout()
        v_box.addWidget(self.soru_ekrani)
        v_box.addWidget(self.button)
        v_box.addWidget(self.cevap_ekrani)
        v_box.addWidget(self.button1)
        v_box.addWidget(self.mesaj)
        v_box.addWidget(self.cikalim)
        
        
        
        
        
        
        self.button.clicked.connect(self.sayi_getir)
        self.cevap_ekrani.returnPressed.connect(self.tahmin_et)
        self.cikalim.clicked.connect(self.cikis)
        self.button1.clicked.connect(self.tahmin_et)
        
        self.setLayout(v_box)
        self.button1.close()              
        
        self.show() 
        
    def sayi_getir(self):
         self.tahmin=random.randint(0,100)
         self.button1.show()
         self.button.close()
         self.media.play()
         self.sayac=0
         self.kücük_sayi=0
         self.büyük_sayi=100
         self.soru_ekrani.setText("{} ile {} sayıları arasında bir sayı giriniz.".format(self.kücük_sayi,self.büyük_sayi))
         
         
         
    def cikis(self):
        sys.exit()
        
    def tahmin_et(self):
        print(self.cevap_ekrani.text())
        print(self.tahmin)
            
        self.soru_ekrani.setText("{} ile {} sayıları arasında bir sayı giriniz.".format(self.kücük_sayi,self.büyük_sayi))
           
        if self.tahmin==int(self.cevap_ekrani.text()):
            self.mesaj.setText("{} tahminde doğru bildiniz. TEBRİKLER...".format(self.sayac))
            self.soru_ekrani.setText("Tekrar Oynamak için BAŞLA'ya basınız")
            self.media2.play()
            self.button1.close()
            self.button.show()
                
                
        elif self.tahmin < int(self.cevap_ekrani.text()):
            self.büyük_sayi=int(self.cevap_ekrani.text())
            self.cevap_ekrani.clear()
            self.media1.play()
            self.sayac +=1
            self.soru_ekrani.setText("{} ile {} sayıları arasında bir sayı giriniz.".format(self.kücük_sayi,self.büyük_sayi))
            
                
            
        elif self.tahmin>int(self.cevap_ekrani.text()):
            self.kücük_sayi=int(self.cevap_ekrani.text())
            self.cevap_ekrani.clear()
            self.media1.play()
            self.sayac +=1
            self.soru_ekrani.setText("{} ile {} sayıları arasında bir sayı giriniz.".format(self.kücük_sayi,self.büyük_sayi))
            
      
        
if __name__ ==  "__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())