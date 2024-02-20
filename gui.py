# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_Dialog(object):



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1109, 853)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 770, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 489, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setMouseTracking(True)
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_3.addWidget(self.checkBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setMouseTracking(True)
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setTristate(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_5.addWidget(self.checkBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 229, 491, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.verticalLayout_2.addWidget(self.horizontalSlider_4)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_2.addWidget(self.horizontalSlider_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(620, 10, 361, 471))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 500, 291, 28))
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        from serialcom import Serialcom
        self.serial = Serialcom()
        self.pushButton_2.clicked.connect(self.on_button_clicked)
        self.pushButton.clicked.connect(self.on_button_clicked_2)
        self.pushButton_3.clicked.connect(self.on_button_clicked_3)
        self.pushButton_4.clicked.connect(self.on_button_clicked_4)
        self.pushButton_5.clicked.connect(self.on_button_clicked_5)

        self.pushButton_7.clicked.connect(self.click_slider)
        self.pushButton_8.clicked.connect(self.click_slider2)
        self.pushButton_6.clicked.connect(self.click_slider4)
        self.pushButton_9.clicked.connect(self.click_slider3)

        self.pushButton_10.clicked.connect(self.read_form1)

    def click_slider(self):
        new_value = self.horizontalSlider.value()
        print("slider value", new_value)
        new_value = new_value * 2.58
        self.serial.write_to_analog_register(int(new_value), 200)
        time.sleep(0.5)
        print(self.serial.read_from_analog_register(200))

    def click_slider2(self):
        new_value = self.horizontalSlider_2.value()
        print("slider value", new_value)
        new_value = new_value * 2.58
        self.serial.write_to_analog_register(int(new_value), 201)
        time.sleep(0.5)
        print(self.serial.read_from_analog_register(201))

    def click_slider3(self):
        new_value = self.horizontalSlider_3.value()
        print("slider value", new_value)
        new_value = new_value * 2.58
        self.serial.write_to_analog_register(int(new_value), 210)
        time.sleep(0.5)
        print(self.serial.read_from_analog_register(202))

    def click_slider4(self):
        new_value = self.horizontalSlider_4.value()
        print("slider value", new_value)
        new_value = new_value * 2.58
        self.serial.write_to_analog_register(int(new_value), 202)
        time.sleep(0.5)
        print(self.serial.read_from_analog_register(210))


    def checbox_state_change(self, checkBox, register, bit):

        if self.serial.read_from_digital_register(register, bit) == 1:
            checkBox.setChecked(True)
        else:
            checkBox.setChecked(False)

        time.sleep(0.5)

        if checkBox.checkState() == 0:
            self.serial.write_to_digital_register(register, bit, 1)
        else:
            checkBox.setChecked(False)
            self.serial.write_to_digital_register(register, bit, 0)

        time.sleep(0.5)

        if self.serial.read_from_digital_register(register, bit) == 1:
            checkBox.setChecked(True)
        else:
            checkBox.setChecked(False)

    def on_button_clicked(self):
        self.checbox_state_change(self.checkBox, 300, 0)

    def on_button_clicked_2(self):
        self.checbox_state_change(self.checkBox_2, 301, 0)

    def on_button_clicked_3(self):
        self.checbox_state_change(self.checkBox_3, 301, 1)

    def on_button_clicked_4(self):
        self.checbox_state_change(self.checkBox_4, 301, 5)

    def on_button_clicked_5(self):
        self.checbox_state_change(self.checkBox_5, 302, 0)



    def read_analog(self,registers):
        for register in registers:
            yield str(self.serial.read_from_analog_register(register) * 0.03)

    def read_digital(self,registers):
        for register in registers:
            yield str(self.serial.read_from_digial_register(register,0)  * 0.03)

    def parse(self,names,values):
        for name,value in zip(names, values):
            yield str(name) + ": " + str(value)

    def read_form1(self): #czytanie kaczmara i print wszystkiego
        analog_names = ["Czujnik temp. zewnętrznej","Czujnik temp. powietrza nawiewanego","Czujnik temp. powietrza w pomieszczeniu"]
        analog_registers = [10,12,16]

        digital_names = ["Termostat p-zamr. nagrzewnicy","Presostat filtra podstawowego nawiewu","Presostat wentylatora nawiewu"]
        digital_registers = [100,101,102]


        analog_values = list(self.read_analog(analog_registers))
        digital_values = list(self.read_analog(digital_registers))
        message = list(self.parse(analog_names,analog_values))
        message2 = list(self.parse(digital_names, digital_values))
        message.extend(message2)

        message = "\n".join(message)


        self.textEdit.setText(message)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Siłownik przepustnicy na wlocie nawiewu"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.pushButton_3.setText(_translate("Dialog", "Załączenie pompy nagrzewnicy wtórnej"))
        self.checkBox_3.setText(_translate("Dialog", "CheckBox"))
        self.pushButton_4.setText(_translate("Dialog", "Załączenie pompy nagrzewnicy wstępnej"))
        self.checkBox_4.setText(_translate("Dialog", "CheckBox"))
        self.pushButton.setText(_translate("Dialog", "Załączenie agregatu chłodnicy freonowej"))
        self.checkBox_2.setText(_translate("Dialog", "CheckBox"))
        self.pushButton_5.setText(_translate("Dialog", "Załączenie wentylatora nawiewu"))
        self.checkBox_5.setText(_translate("Dialog", "CheckBox"))
        self.pushButton_7.setText(_translate("Dialog", "Siłownik zaworu nagrzewnicy wstępnej"))
        self.pushButton_8.setText(_translate("Dialog", "Siłownik zaworu nagrzewnicy wtórnej"))
        self.pushButton_6.setText(_translate("Dialog", "Siłownik zaworu chłodnicy"))
        self.pushButton_9.setText(_translate("Dialog", "Prędkość obrotowa wentylatora nawiewu"))
        self.pushButton_10.setText(_translate("Dialog", "Sprawdzenie stanów wejścia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
