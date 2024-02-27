from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np

import AddInvoive, InvoiceManagement, Statistical, Consumer, Discount, Employee, Home, Login, Product, Addwarehouse, Supplier, Warehouse
import sys

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def invoiceManagement():
        global ui
        ui = InvoiceManagement.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.AddButton.clicked.connect(addInvoice)
        ui.SearchButton_2.clicked.connect(home)
        MainWindow.show()

def addInvoice():
        global ui
        ui = AddInvoive.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.BackButton.clicked.connect(invoiceManagement)
        MainWindow.show()

def statistical():
        global ui
        ui = Statistical.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.CB_ThongKe.currentIndexChanged.connect(change)
        ui.BackButton.clicked.connect(home)
        MainWindow.show()

def change():
        if(ui.CB_ThongKe.currentIndex()==(0)):
            ui.stackedWidget.setCurrentWidget(ui.DTNV)
        if(ui.CB_ThongKe.currentIndex()==(1)):
            ui.stackedWidget.setCurrentWidget(ui.SPBC)
        if(ui.CB_ThongKe.currentIndex()==(2)):
            ui.stackedWidget.setCurrentWidget(ui.DTCT)
            ui.CB_ThongKe.setCurrentIndex(0)

            categories = ['A', 'B', 'C', 'D']
            data1 = np.array([30, 20, 25, 15])
            plt.subplot(1, 2, 1)
            plt.bar(categories, data1, color='skyblue')
            plt.title('Biểu Đồ 1')
            plt.show()

def consumer():
       global ui
       ui = Consumer.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton.clicked.connect(home)
       MainWindow.show()

def discount():
       global ui
       ui = Discount.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton_2.clicked.connect(home)
       MainWindow.show()

def employee():
       global ui
       ui = Employee.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_back.clicked.connect(home)
       MainWindow.show()

def login():
       global ui
       ui = Login.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton.clicked.connect(home)
       MainWindow.show()

def product():
       global ui
       ui = Product.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton_5.clicked.connect(home)
       MainWindow.show()

def warehouse():
       global ui
       ui = Warehouse.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_back.clicked.connect(home)
       ui.btn_nhacungcap.clicked.connect(supplier)
       ui.btn_add.clicked.connect(addwarehouse)
       MainWindow.show()

def addwarehouse():
       global ui
       ui = Addwarehouse.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_back.clicked.connect(warehouse)
       MainWindow.show()

def supplier():
       global ui
       ui = Supplier.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_back.clicked.connect(home)
       ui.btn_kho.clicked.connect(warehouse)
       MainWindow.show()

def home():
       global ui
       ui = Home.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_Cashier.clicked.connect(invoiceManagement)
       ui.btn_Employ.clicked.connect(employee)
       ui.btn_Products.clicked.connect(product)
       ui.btn_Discount.clicked.connect(discount)
       ui.btn_Consum.clicked.connect(consumer)
       ui.btn_Static.clicked.connect(statistical)
       ui.btn_Inven.clicked.connect(warehouse)
       ui.btn_Logout.clicked.connect(login)
       MainWindow.show()

login()
sys.exit(app.exec())
