# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(590, 120, 141, 22))
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 5), QtCore.QTime(10, 5, 0)))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 160, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 250, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 72, 16))
        self.label_5.setObjectName("label_5")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(350, 120, 141, 22))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 5), QtCore.QTime(10, 5, 0)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 10, 401, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 961, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 180, 461, 381))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 190, 81, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 190, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 120, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(260, 150, 72, 15))
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(350, 150, 131, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 40, 581, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 570, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 570, 131, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 121, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 40, 121, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(10, 320, 65, 16))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 340, 65, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 360, 65, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 380, 65, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 400, 65, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 420, 65, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 440, 65, 16))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 460, 65, 16))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(10, 480, 65, 16))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(10, 500, 65, 16))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 520, 65, 16))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(10, 540, 65, 16))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(10, 560, 65, 16))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(10, 580, 65, 16))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(80, 320, 65, 16))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(80, 340, 65, 16))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setGeometry(QtCore.QRect(80, 360, 65, 16))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setGeometry(QtCore.QRect(80, 380, 65, 16))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setGeometry(QtCore.QRect(80, 400, 65, 16))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_20.setGeometry(QtCore.QRect(80, 420, 65, 16))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_21.setGeometry(QtCore.QRect(80, 440, 65, 16))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_22.setGeometry(QtCore.QRect(80, 460, 65, 16))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_24 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_24.setGeometry(QtCore.QRect(80, 500, 65, 16))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_25.setGeometry(QtCore.QRect(80, 520, 65, 16))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_26.setGeometry(QtCore.QRect(80, 540, 65, 16))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_27.setGeometry(QtCore.QRect(80, 560, 65, 16))
        self.checkBox_27.setObjectName("checkBox_27")
        self.checkBox_28 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_28.setGeometry(QtCore.QRect(80, 580, 65, 16))
        self.checkBox_28.setObjectName("checkBox_28")
        self.checkBox_29 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_29.setGeometry(QtCore.QRect(160, 300, 65, 16))
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_30 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_30.setGeometry(QtCore.QRect(160, 320, 65, 16))
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_31.setGeometry(QtCore.QRect(160, 340, 65, 16))
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_32 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_32.setGeometry(QtCore.QRect(160, 360, 65, 16))
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_33 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_33.setGeometry(QtCore.QRect(160, 380, 65, 16))
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_34.setGeometry(QtCore.QRect(160, 400, 65, 16))
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_35 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_35.setGeometry(QtCore.QRect(160, 420, 65, 16))
        self.checkBox_35.setObjectName("checkBox_35")
        self.checkBox_36 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_36.setGeometry(QtCore.QRect(160, 440, 65, 16))
        self.checkBox_36.setObjectName("checkBox_36")
        self.checkBox_37 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_37.setGeometry(QtCore.QRect(160, 460, 65, 16))
        self.checkBox_37.setObjectName("checkBox_37")
        self.checkBox_38 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_38.setGeometry(QtCore.QRect(160, 480, 65, 16))
        self.checkBox_38.setObjectName("checkBox_38")
        self.checkBox_39 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_39.setGeometry(QtCore.QRect(160, 500, 65, 16))
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_40 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_40.setGeometry(QtCore.QRect(160, 520, 65, 16))
        self.checkBox_40.setObjectName("checkBox_40")
        self.checkBox_41 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_41.setGeometry(QtCore.QRect(160, 540, 65, 16))
        self.checkBox_41.setObjectName("checkBox_41")
        self.checkBox_42 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_42.setGeometry(QtCore.QRect(160, 560, 65, 16))
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_43 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_43.setGeometry(QtCore.QRect(160, 580, 65, 16))
        self.checkBox_43.setObjectName("checkBox_43")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 570, 131, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, 110, 20, 551))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 151, 16))
        self.label_6.setObjectName("label_6")
        self.checkBox_23 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_23.setGeometry(QtCore.QRect(80, 480, 65, 16))
        self.checkBox_23.setObjectName("checkBox_23")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 22))
        self.menubar.setObjectName("menubar")
        self.menusdf = QtWidgets.QMenu(self.menubar)
        self.menusdf.setObjectName("menusdf")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menusdf.addSeparator()
        self.menusdf.addAction(self.action1)
        self.menusdf.addAction(self.action2)
        self.menusdf.addAction(self.action3)
        self.menusdf.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menusdf.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "大气数据清洗与可视化"))
        self.lineEdit.setText(_translate("MainWindow", "57495"))
        self.label_3.setText(_translate("MainWindow", "检索起始时间"))
        self.comboBox.setItemText(0, _translate("MainWindow", "YIIP"))
        self.comboBox.setItemText(1, _translate("MainWindow", "风向"))
        self.comboBox.setItemText(2, _translate("MainWindow", "温度"))
        self.label_2.setText(_translate("MainWindow", "ID号"))
        self.pushButton_2.setText(_translate("MainWindow", "存入数据库（2）"))
        self.label_5.setText(_translate("MainWindow", "区站号"))
        self.lineEdit_2.setText(_translate("MainWindow", "000"))
        self.label_4.setText(_translate("MainWindow", "传感器类型"))
        self.lineEdit_3.setText(_translate("MainWindow", "ReceivedTofile-TCPSERVER-2019_11_5_10-04-51.DAT"))
        self.label_7.setText(_translate("MainWindow", "请输入文件名称"))
        self.label_8.setText(_translate("MainWindow", "帧标识"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "001"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "005"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "010"))
        self.label_9.setText(_translate("MainWindow", "检索结束时间"))
        self.label_10.setText(_translate("MainWindow", "检索间隔"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1分钟"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "5分钟"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "10分钟"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "一小时"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">未读取配置文件 请点击读取按钮</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "检索（3）"))
        self.pushButton_4.setText(_translate("MainWindow", "输出图像（4）"))
        self.pushButton_5.setText(_translate("MainWindow", "保存配置文件（5）"))
        self.pushButton_6.setText(_translate("MainWindow", "读取配置文件（6）"))
        self.checkBox_1.setText(_translate("MainWindow", "AAA"))
        self.checkBox_2.setText(_translate("MainWindow", "AAA5i"))
        self.checkBox_3.setText(_translate("MainWindow", "AB10"))
        self.checkBox_4.setText(_translate("MainWindow", "AB20"))
        self.checkBox_5.setText(_translate("MainWindow", "AB30"))
        self.checkBox_6.setText(_translate("MainWindow", "AB40"))
        self.checkBox_7.setText(_translate("MainWindow", "AB50"))
        self.checkBox_8.setText(_translate("MainWindow", "ADA"))
        self.checkBox_9.setText(_translate("MainWindow", "ADB"))
        self.checkBox_10.setText(_translate("MainWindow", "AEA"))
        self.checkBox_11.setText(_translate("MainWindow", "AEA150"))
        self.checkBox_12.setText(_translate("MainWindow", "AEB"))
        self.checkBox_13.setText(_translate("MainWindow", "AEB150"))
        self.checkBox_14.setText(_translate("MainWindow", "AEC"))
        self.checkBox_15.setText(_translate("MainWindow", "AEC150"))
        self.checkBox_16.setText(_translate("MainWindow", "AED"))
        self.checkBox_17.setText(_translate("MainWindow", "AED150"))
        self.checkBox_18.setText(_translate("MainWindow", "AEF"))
        self.checkBox_19.setText(_translate("MainWindow", "AEF150"))
        self.checkBox_20.setText(_translate("MainWindow", "AFA"))
        self.checkBox_21.setText(_translate("MainWindow", "AFA150"))
        self.checkBox_22.setText(_translate("MainWindow", "AFA150a"))
        self.checkBox_24.setText(_translate("MainWindow", "AFB"))
        self.checkBox_25.setText(_translate("MainWindow", "AFB150"))
        self.checkBox_26.setText(_translate("MainWindow", "AFC"))
        self.checkBox_27.setText(_translate("MainWindow", "AFC150"))
        self.checkBox_28.setText(_translate("MainWindow", "AFD"))
        self.checkBox_29.setText(_translate("MainWindow", "AFD150"))
        self.checkBox_30.setText(_translate("MainWindow", "AGA"))
        self.checkBox_31.setText(_translate("MainWindow", "AHA"))
        self.checkBox_32.setText(_translate("MainWindow", "AHA5"))
        self.checkBox_33.setText(_translate("MainWindow", "AHC"))
        self.checkBox_34.setText(_translate("MainWindow", "AHC5"))
        self.checkBox_35.setText(_translate("MainWindow", "AJA"))
        self.checkBox_36.setText(_translate("MainWindow", "AJAa"))
        self.checkBox_37.setText(_translate("MainWindow", "AJAc"))
        self.checkBox_38.setText(_translate("MainWindow", "AJT"))
        self.checkBox_39.setText(_translate("MainWindow", "ARG10"))
        self.checkBox_40.setText(_translate("MainWindow", "ARG20"))
        self.checkBox_41.setText(_translate("MainWindow", "ARG30"))
        self.checkBox_42.setText(_translate("MainWindow", "ARG40"))
        self.checkBox_43.setText(_translate("MainWindow", "ARG50"))
        self.pushButton_7.setText(_translate("MainWindow", "清空窗口"))
        self.label_6.setText(_translate("MainWindow", "数据元素选择："))
        self.checkBox_23.setText(_translate("MainWindow", "AFAa"))
        self.menusdf.setTitle(_translate("MainWindow", "file"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuForm.setTitle(_translate("MainWindow", "Form"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.action1.setText(_translate("MainWindow", "New"))
        self.action2.setText(_translate("MainWindow", "Open"))
        self.action3.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
