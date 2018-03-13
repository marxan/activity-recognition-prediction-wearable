# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'andy_reco.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 830)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.standing_strongly_bent = QtWidgets.QProgressBar(self.groupBox)
        self.standing_strongly_bent.setProperty("value", 24)
        self.standing_strongly_bent.setObjectName("standing_strongly_bent")
        self.gridLayout.addWidget(self.standing_strongly_bent, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../app/figs/standing5.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../app/figs/walking0.png"))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../app/figs/standing2.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../app/figs/standing3.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.standing_bent_forward = QtWidgets.QProgressBar(self.groupBox)
        self.standing_bent_forward.setProperty("value", 24)
        self.standing_bent_forward.setObjectName("standing_bent_forward")
        self.gridLayout.addWidget(self.standing_bent_forward, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.walking_upright = QtWidgets.QProgressBar(self.groupBox)
        self.walking_upright.setProperty("value", 24)
        self.walking_upright.setInvertedAppearance(False)
        self.walking_upright.setObjectName("walking_upright")
        self.gridLayout.addWidget(self.walking_upright, 0, 2, 1, 1)
        self.standing_upright = QtWidgets.QProgressBar(self.groupBox)
        self.standing_upright.setProperty("value", 24)
        self.standing_upright.setObjectName("standing_upright")
        self.gridLayout.addWidget(self.standing_upright, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 1, 1, 1)
        self.standing_overhead_elbow = QtWidgets.QProgressBar(self.groupBox)
        self.standing_overhead_elbow.setProperty("value", 24)
        self.standing_overhead_elbow.setObjectName("standing_overhead_elbow")
        self.gridLayout.addWidget(self.standing_overhead_elbow, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../app/figs/standing4.png"))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../app/figs/standing6.png"))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)
        self.standing_overhead_hands = QtWidgets.QProgressBar(self.groupBox)
        self.standing_overhead_hands.setProperty("value", 24)
        self.standing_overhead_hands.setObjectName("standing_overhead_hands")
        self.gridLayout.addWidget(self.standing_overhead_hands, 5, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.kneeling_upright = QtWidgets.QProgressBar(self.groupBox_2)
        self.kneeling_upright.setProperty("value", 24)
        self.kneeling_upright.setObjectName("kneeling_upright")
        self.gridLayout_3.addWidget(self.kneeling_upright, 1, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../../app/figs/kneeling12.png"))
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("../../app/figs/kneeling13.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("../../app/figs/kneeling14.png"))
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 1, 1, 1)
        self.kneeling_bent = QtWidgets.QProgressBar(self.groupBox_2)
        self.kneeling_bent.setProperty("value", 24)
        self.kneeling_bent.setObjectName("kneeling_bent")
        self.gridLayout_3.addWidget(self.kneeling_bent, 2, 3, 1, 1)
        self.kneeling_elbow = QtWidgets.QProgressBar(self.groupBox_2)
        self.kneeling_elbow.setProperty("value", 24)
        self.kneeling_elbow.setObjectName("kneeling_elbow")
        self.gridLayout_3.addWidget(self.kneeling_elbow, 3, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.object_yes = QtWidgets.QProgressBar(self.groupBox_3)
        self.object_yes.setProperty("value", 24)
        self.object_yes.setObjectName("object_yes")
        self.gridLayout_4.addWidget(self.object_yes, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("../../app/figs/objYes.png"))
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setMinimumSize(QtCore.QSize(150, 0))
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("../../app/figs/objNo.png"))
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 1, 1, 1, 1)
        self.object_no = QtWidgets.QProgressBar(self.groupBox_3)
        self.object_no.setProperty("value", 24)
        self.object_no.setObjectName("object_no")
        self.gridLayout_4.addWidget(self.object_no, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 3, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAndy_Recognition = QtWidgets.QAction(MainWindow)
        self.actionAndy_Recognition.setObjectName("actionAndy_Recognition")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnDy Activity Recognition"))
        self.groupBox.setTitle(_translate("MainWindow", "Standing / walking"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Standing strongly </p><p>bent forward</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Standing upright"))
        self.label_4.setText(_translate("MainWindow", "Walking upright"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Standing bent</p><p>forward</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Standing overhead work</p><p>Elbow at/above shoulder</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>Standing overhead work</p><p>Hands above head</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kneeling / crouching"))
        self.label_13.setText(_translate("MainWindow", "Kneeling upright"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>Kneeling elbow</p><p>at/above shoulder</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Kneeling bent"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Load"))
        self.label_20.setText(_translate("MainWindow", "Object in hand"))
        self.label_22.setText(_translate("MainWindow", "No object"))
        self.actionAndy_Recognition.setText(_translate("MainWindow", "Andy Recognition"))

