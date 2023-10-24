from PyQt5.QtGui import QPixmap,QColor,QPalette,QGuiApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QFormLayout,QComboBox,QMainWindow,QMessageBox,QAction,QTableWidget,QTableWidgetItem,\
QColorDialog,QComboBox,QProgressBar,QFrame,QSlider
from PyQt5.QtWidgets import (QApplication, QWidget,
  QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout,QLineEdit)
import time as tm
import numpy as np
import scipy
from scipy import stats
import cv2


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100,500, 800)
        self.setFixedSize(500,800)
        self.setWindowTitle('Min,Max,mean,Median,Mode calculator')

        # self.com1=QComboBox(self)
        # self.com1.addItem('Python',self)
        # self.com1.addItem('Java', self)
        # self.com1.addItem('C++', self)
        # self.com1.addItem('PyQt', self)
        # self.com1.move(250,300)
        # self.com1.resize(200,20)
        # self.com1.activated.connect(self.combo)

        # self.lay = QVBoxLayout()
        # self.lay.addWidget(self.tw)
        # self.setLayout(self.lay)
        #

        mainM1=self.menuBar()
        helpM = mainM1.addMenu('Help')
        exitM = mainM1.addMenu('Exit')

        exitB  = QAction('Exit', self)
        exitM.addAction(exitB)
        exitB.triggered.connect(self.exit_)

        helpB  = QAction('Help', self)
        helpM.addAction(helpB)
        helpB.triggered.connect(self.help_)

        self.label1=QLabel(self)
        self.label1.setText("Please enter the digits and push the \"Enter\" key afterwards. Push the \"Go!\" after entering last digit.")
        self.label1.move(10,70)
        self.label1.resize(500, 100)

        self.textbox1=QLineEdit(self)
        self.textbox1.move(10,150)
        self.textbox1.resize(120, 30)

        self.pushbotton0=QPushButton('New Calculation',self)
        self.pushbotton0.move(10, 50)
        self.pushbotton0.clicked.connect(self.new_)

        self.pushbotton1=QPushButton('Enter',self)
        self.pushbotton1.move(150, 150)
        self.pushbotton1.clicked.connect(self.add_)

        self.pushbotton2=QPushButton('Go!',self)
        self.pushbotton2.move(270,150)
        self.pushbotton2.clicked.connect(self.calculate_)

        #show list of digits
        self.textbox2=QLineEdit(self)
        self.textbox2.move(10,200)
        self.textbox2.resize(480, 30)

        self.textbox3=QLineEdit(self)
        self.textbox3.move(10,250)
        self.textbox3.resize(80, 30)

        self.textbox4=QLineEdit(self)
        self.textbox4.move(110,250)
        self.textbox4.resize(80, 30)

        self.textbox5=QLineEdit(self)
        self.textbox5.move(210,250)
        self.textbox5.resize(80, 30)

        self.textbox6=QLineEdit(self)
        self.textbox6.move(310,250)
        self.textbox6.resize(80, 30)

        self.textbox7=QLineEdit(self)
        self.textbox7.move(410,250)
        self.textbox7.resize(80, 30)

        self.label1=QLabel(self)
        self.label1.move(10, 300)
        self.label1.resize(480, 480)

        # label1=QLabel('Input',self)
        # label1.move(215,23)
        # label2=QLabel('Output',self)
        # label2.move(215,43)

        self.statusBar().showMessage('Reza Mousavi')
        self.show()

    def graph_(self):
        pass





    def help_(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Please enter each digit and click the \"Next\" afterwards and click the \"Finish\" after last digit.")
        msgBox.setWindowTitle("Help")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()


    def exit_(self):
        qmb=QMessageBox.question(self,"message",'Do you really want to close?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Help )
        if qmb==QMessageBox.Yes:
            self.close()
        elif qmb==QMessageBox.No:
            pass
        elif qmb==QMessageBox.Help:
            self.help_()

    def new_(self):
        self.textbox1.setText('')
        self.textbox2.setText('')
        self.textbox3.setText('')
        self.textbox4.setText('')
        self.textbox5.setText('')
        self.textbox6.setText('')
        self.textbox7.setText('')
        plt.figure(figsize=(10,5))
        plt.savefig(r'C:\Users\Ariya Rayaneh\Desktop\white.jpg')
        pix = QPixmap(r'C:\Users\Ariya Rayaneh\Desktop\white.jpg')
        self.label1.setPixmap(pix)
        self.reset_()

    def add_(self):

        a=int(self.textbox1.text())
        con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\digits.db')
        my_cursor = con.cursor()
        my_cursor.execute(f"INSERT INTO digits(digit) VALUES('{a}') ")
        con.commit()
        self.textbox1.setText('')

    def calculate_(self):
        con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\digits.db')
        my_cursor = con.cursor()
        my_cursor.execute("SELECT * FROM digits")
        results = my_cursor.fetchall()
        print(results[0][0])
        k=[]
        for i in results:
            k.append(i[0])
        self.textbox2.setText('The list of digits is:  '+str(k))
        self.textbox3.setText('minimum:  '+str(min(sorted(k))))
        self.textbox4.setText('mean:  '+str(sum(sorted(k))/len(k)))
        self.textbox5.setText('median:  '+str(np.median(sorted(k))))
        self.textbox6.setText('mode:  ' + str(stats.mode(sorted(k))))
        self.textbox7.setText('maximum: '+str(max(sorted(k))))
        plt.figure(figsize=(12,15))
        plt.subplot(2, 2, 1)
        plt.hist(k,color='b',edgecolor='r',linewidth=2)
        plt.grid()
        plt.title('Hist Plot',fontsize=18)
        plt.xticks(fontsize=18,rotation=30)
        plt.yticks(fontsize=18)
        plt.subplot(2,2,2)
        plt.plot(k,marker='o',mec = 'r', mfc = 'r',color='b')
        plt.grid()
        plt.title('Line Plot',fontsize=18)
        plt.xticks(fontsize=18,rotation=30)
        plt.yticks(fontsize=18)
        plt.subplot(2, 2,3 )
        plt.boxplot(k)
        plt.grid()
        plt.title('Box Plot',fontsize=18)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)

        plt.savefig(r'C:\Users\Ariya Rayaneh\Desktop\graph.jpg')
        #plt.show()
        pic1=cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\graph.jpg')
        pic1=cv2.resize(pic1,(480,480))
        pic1=cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\graph1.jpg',pic1)

        pix = QPixmap(r'C:\Users\Ariya Rayaneh\Desktop\graph1.jpg')
        self.label1.setPixmap(pix)



    def reset_(self):
        print('hello')
        con = sqlite3.connect(r'C:\Users\Ariya Rayaneh\Desktop\digits.db')
        my_cursor = con.cursor()
        my_cursor.execute("DELETE FROM digits")
        con.commit()

if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())