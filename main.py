import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QMessageBox, QTableWidgetItem, QListWidgetItem
from Main_Window import MainWidget1
from login1 import LoginWidget
from file import FileWidget
from file_register import FileRegisterWidget
from calendar1 import CalendarWidget
from trial import TrialWidget
from register1 import RegisterWidget
from pymongo import MongoClient
from datetime import datetime
import hashlib
import res

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        
    def initUi(self):
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self)
        self.vlayout.addWidget(self.stacked_widget)
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["AVAC"]
        self.collection = self.db["users"]
        self.collection_durusmalar= self.db["durusmalar"]
        
        
        self.login_widget = QWidget()
        self.file_widget = QWidget()
        self.file_register_widget = QWidget()
        self.calendar_widget = QWidget()
        self.trial_widget = QWidget()
        self.register_widget = QWidget()
        self.main_widget = QWidget()
        
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.file_widget)
        self.stacked_widget.addWidget(self.file_register_widget)
        self.stacked_widget.addWidget(self.calendar_widget)
        self.stacked_widget.addWidget(self.trial_widget)
        self.stacked_widget.setCurrentWidget(self.login_widget)
        self.setLayout(self.vlayout)
        
        # set none whatever needs to be set none
        self.login_object = None
        self.register_object = None
        self.main_object = None
        self.file_object = None
        self.file_register_object = None
        self.calendar_object = None
        self.meltem_object = None
        self.trial_object = None
        self.login_page()


    def login_page(self):
        self.login_object = LoginWidget()
        self.login_object.setupUi(self.login_widget)
        self.login_object.start_btn.clicked.connect(self.login)
        self.register_page()
        self.login_object.kayit_giris.mousePressEvent = lambda event: self.stacked_widget.setCurrentWidget(self.register_widget)
        
        
    def register_page(self):
        self.register_object = RegisterWidget()
        self.register_object.setupUi(self.register_widget)
        self.register_object.Reg_pushButton.clicked.connect(self.register)

        
    def main_page(self):
        self.main_object = MainWidget1()
        self.main_object.setupUi(self.main_widget)
        self.main_object.horizontalLayout.removeWidget(self.main_object.icon_only_widget)
        self.main_object.stackedWidget.setCurrentWidget(self.main_object.entry_page)
        self.main_object.kayitEkle.clicked.connect(self.dosyaEkle)
        self.main_object.file_button.clicked.connect(self.file_page_load)
        self.file_page()
        self.main_object.file_register_button.clicked.connect(lambda: self.main_object.stackedWidget.setCurrentWidget(self.main_object.file_register_page))
        self.file_register_page()
        self.main_object.calendar_button.clicked.connect(self.calendar_page_load)
        self.calendar_page()
        self.main_object.trial_button.clicked.connect(self.trial_page_load)
        self.trial_page()

    def calendar_page_load(self):
        self.main_object.stackedWidget.setCurrentWidget(self.main_object.calender_page)
        durusmalar = self.collection_durusmalar.find({})
        self.main_object.tableWidget.clearContents()
        self.main_object.tableWidget.setRowCount(0)
        for item in durusmalar:
            self.main_object.tableWidget.insertRow(0)
            self.main_object.tableWidget.setItem(0, 0, QTableWidgetItem(item["ad_soyad"]))
            self.main_object.tableWidget.setItem(0, 1, QTableWidgetItem(item["dosya_adı"]))
            self.main_object.tableWidget.setItem(0, 2, QTableWidgetItem(item["aciklama"]))

    def file_page_load(self):
        self.main_object.stackedWidget.setCurrentWidget(self.main_object.file_page)    
        durusmalar = self.collection_durusmalar.find({})
        self.main_object.list_2.clearContents()
        self.main_object.list_2.setRowCount(0)
        for item in durusmalar:
            self.main_object.list_2.insertRow(0)
            self.main_object.list_2.setItem(0, 0, QTableWidgetItem(item["ad_soyad"]))
            self.main_object.list_2.setItem(0, 1, QTableWidgetItem(item["dosya_turu"]))
            self.main_object.list_2.setItem(0, 2, QTableWidgetItem(item["dosya_adı"]))
            self.main_object.list_2.setItem(0, 3, QTableWidgetItem(item["dava_ucreti"]))
            self.main_object.list_2.setItem(0, 4, QTableWidgetItem(item["durusma_zamanı"]))
            self.main_object.list_2.setItem(0, 5, QTableWidgetItem(item["aciklama"]))  

    def trial_page_load(self):
        self.main_object.stackedWidget.setCurrentWidget(self.main_object.trial_page)
        durusmalar = self.collection_durusmalar.find({})
        self.main_object.future_trial.clear()
        self.main_object.past_trial.clear()

        for item in durusmalar:
            tarih = item["durusma_zamanı"]
            formatted_tarih = datetime.strptime(tarih, "%a %b %d %H:%M:%S %Y")

            now = datetime.now()
            if formatted_tarih > now:
                self.main_object.future_trial.addItem(QListWidgetItem(f'{item["durusma_zamanı"]} {item["dosya_adı"]}'))
            else:
                self.main_object.past_trial.addItem(QListWidgetItem(f'{item["durusma_zamanı"]} {item["dosya_adı"]}'))


    def dosyaEkle(self):
        ad_soyad = self.main_object.line_adSoyad.text().strip()
        dosya_adı = self.main_object.line_dosyaname.text().strip()
        dosya_turu = self.main_object.line_dsyTr.text().strip()
        dava_ucreti = self.main_object.line_alnckUcrt.text().strip()
        durusma_zamanı = self.main_object.dateTimeEdit
        durusma_zamanı.setDisplayFormat("dd/MM/yyyy - hh:mm:ss")
        durusma_zamanı_string = durusma_zamanı.dateTime().toString()
        print(durusma_zamanı, durusma_zamanı_string)
        dava_ucreti = self.main_object.line_alnckUcrt.text().strip()
        aciklama = self.main_object.text_Aciklama.toPlainText()  

        self.collection_durusmalar.insert_one({"ad_soyad": ad_soyad, "dosya_adı": dosya_adı, "dosya_turu": dosya_turu,"dava_ucreti": dava_ucreti, "durusma_zamanı": durusma_zamanı_string,"aciklama": aciklama})


    def file_page(self):
        self.file_object = FileWidget()
        self.file_object.setupUi(self.file_widget)
        
    def file_register_page(self):
        self.file_register_object = FileRegisterWidget()
        self.file_register_object.setupUi(self.file_register_widget)
    
    def calendar_page(self):
        self.calendar_object = CalendarWidget()
        self.calendar_object.setupUi(self.calendar_widget)
    
    def trial_page(self):
        self.trial_object = TrialWidget()
        self.trial_object.setupUi(self.trial_widget)

    def login(self):
        self.username = self.login_object.usernameLE.text().strip()
        password = self.login_object.passwordLE.text().strip()
        hashed_password = hashlib.md5(password.encode()).hexdigest()  
        self.user_data = self.collection.find_one({"username": self.username})      
        if self.collection.find_one({"username": self.username, "password": hashed_password}):
            self.main_page()
            self.stacked_widget.setCurrentWidget(self.main_widget)    

    def register(self):
        self.username = self.register_object.usernameLE.text().strip()
        password = self.register_object.passWordLE_2.text().strip()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        office_name = self.register_object.officenameLE.text().strip()
        office_no = self.register_object.officeNO.text().strip()
        if self.collection.find_one({"username": self.username}):
            QMessageBox.warning(self, "Warning", "Username is already taken")
        else:
            self.collection.insert_one({"username": self.username, "password": hashed_password, "office_name": office_name, "office_no": office_no})
            self.main_page()
            self.stacked_widget.setCurrentWidget(self.main_widget)
          
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
