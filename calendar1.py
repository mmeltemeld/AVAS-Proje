# Form implementation generated from reading ui file 'calender.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class CalendarWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 763)
        Form.setStyleSheet("background-color: rgba(57, 57, 57);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setMinimumSize(QtCore.QSize(981, 741))
        self.widget.setStyleSheet("background-color: rgba(112, 112, 112);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(959, 719))
        self.widget_2.setObjectName("widget_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.widget_2)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 250, 421, 361))
        self.calendarWidget.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(430, 250, 521, 361))
        self.tableWidget.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.giris = QtWidgets.QLabel(parent=self.widget_2)
        self.giris.setGeometry(QtCore.QRect(0, 0, 1071, 181))
        self.giris.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"")
        self.giris.setText("")
        self.giris.setObjectName("giris")
        self.return_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.return_2.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.return_2.setStyleSheet("image: url(:/image/return.png);\n"
"background-color: rgb(230,230,230);")
        self.return_2.setText("")
        self.return_2.setObjectName("return_2")
        self.ana_Amblem = QtWidgets.QLabel(parent=self.widget_2)
        self.ana_Amblem.setGeometry(QtCore.QRect(430, 10, 161, 91))
        self.ana_Amblem.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"image: url(:/image/amblem.png);")
        self.ana_Amblem.setText("")
        self.ana_Amblem.setObjectName("ana_Amblem")
        self.baslik = QtWidgets.QLabel(parent=self.widget_2)
        self.baslik.setGeometry(QtCore.QRect(330, 110, 371, 51))
        self.baslik.setStyleSheet("QLabel{\n"
"background-color: rgb(255, 214, 97);\n"
"border-radius:15px;\n"
"border:0px solid black;\n"
"font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"")
        self.baslik.setObjectName("baslik")
        self.sayfa_amblem = QtWidgets.QLabel(parent=self.widget_2)
        self.sayfa_amblem.setGeometry(QtCore.QRect(130, 50, 111, 81))
        self.sayfa_amblem.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"image: url(:/image/trial.png);")
        self.sayfa_amblem.setText("")
        self.sayfa_amblem.setObjectName("sayfa_amblem")
        self.verticalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Müvekkil Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Dosya Adı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Açıklama Notu"))
        self.baslik.setText(_translate("Form", "<html><head/><body><p align=\"center\">AVAS AJANDA</p></body></html>"))
