# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addwarehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"}\n"
"#left_menu{\n"
"    background-color:#2596be;\n"
"}\n"
"\n"
"#main_body{\n"
"    background-color:#8e3ede;\n"
"}\n"
"button{\n"
"    border: none;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_menu = QtWidgets.QWidget(self.centralwidget)
        self.left_menu.setObjectName("left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.left_menu)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.left_menu)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(650, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setMinimumSize(QtCore.QSize(70, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.frame_10)
        self.plainTextEdit_3.setMaximumSize(QtCore.QSize(1000, 40))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.horizontalLayout_6.addWidget(self.plainTextEdit_3)
        self.verticalLayout_6.addWidget(self.frame_10, 0, QtCore.Qt.AlignLeft)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_14)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../project/assets/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.frame_14)
        self.plainTextEdit_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.horizontalLayout_10.addWidget(self.plainTextEdit_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../project/assets/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.verticalLayout_6.addWidget(self.frame_11, 0, QtCore.Qt.AlignLeft)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_12)
        self.label_7.setMinimumSize(QtCore.QSize(70, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.frame_12)
        self.plainTextEdit_5.setMaximumSize(QtCore.QSize(1000, 40))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.horizontalLayout_8.addWidget(self.plainTextEdit_5)
        self.verticalLayout_6.addWidget(self.frame_12, 0, QtCore.Qt.AlignLeft)
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_9.addWidget(self.pushButton_6)
        self.btn_back = QtWidgets.QPushButton(self.frame_13)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_9.addWidget(self.btn_back)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        self.label_3.setMinimumSize(QtCore.QSize(65, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_8)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_5.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setMinimumSize(QtCore.QSize(65, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_7)
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_4.addWidget(self.plainTextEdit_2)
        self.verticalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignTop)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_9)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_5.addWidget(self.frame_9, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.left_menu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Create Input Form"))
        self.label.setText(_translate("MainWindow", "Product"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Image"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Provider"))
        self.label_5.setText(_translate("MainWindow", "ProductID"))
        self.label_6.setText(_translate("MainWindow", "Quantity"))
        self.label_7.setText(_translate("MainWindow", "Price"))
        self.pushButton_4.setText(_translate("MainWindow", "Remove"))
        self.pushButton_5.setText(_translate("MainWindow", "Edit"))
        self.pushButton_6.setText(_translate("MainWindow", "Add"))
        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Reciever"))
        self.label_4.setText(_translate("MainWindow", "Total"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_3.setText(_translate("MainWindow", "Reset"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
