from random import randint
import sys
import io
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>758</width>
    <height>676</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="circle_btn">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>20</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>жмакни</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>758</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        disin = io.StringIO(template)
        uic.loadUi(disin, self)
        self.setFixedSize(750, 750)
        self.flag = False
        self.circle_btn.clicked.connect(self.check)


    def check(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            prop = [randint(0, 255), randint(0, 255), randint(0, 255)]
            self.qp.setBrush(QColor(*prop))
            size = int(randint(10, 300))
            self.qp.drawEllipse(int(randint(10, 650)), int(randint(10, 700)), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
