# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try_txt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.file_path_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.file_path_txt.setObjectName("file_path_txt")
        self.verticalLayout_3.addWidget(self.file_path_txt)
        self.label_path_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.label_path_txt.setObjectName("label_path_txt")
        self.verticalLayout_3.addWidget(self.label_path_txt)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cluster_kind_lb = QtWidgets.QLabel(self.centralwidget)
        self.cluster_kind_lb.setObjectName("cluster_kind_lb")
        self.horizontalLayout_4.addWidget(self.cluster_kind_lb)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.km_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.km_radio.setObjectName("km_radio")
        self.verticalLayout.addWidget(self.km_radio)
        self.av_ensembel_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.av_ensembel_radio.setObjectName("av_ensembel_radio")
        self.verticalLayout.addWidget(self.av_ensembel_radio)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.aimK_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.aimK_txt.setText("")
        self.aimK_txt.setObjectName("aimK_txt")
        self.horizontalLayout.addWidget(self.aimK_txt)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_iter = QtWidgets.QLabel(self.centralwidget)
        self.label_iter.setObjectName("label_iter")
        self.horizontalLayout_2.addWidget(self.label_iter)
        self.iters_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.iters_txt.setText("")
        self.iters_txt.setObjectName("iters_txt")
        self.horizontalLayout_2.addWidget(self.iters_txt)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.save_path_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.save_path_txt.setObjectName("save_path_txt")
        self.verticalLayout_4.addWidget(self.save_path_txt)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chose_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.chose_file_btn.setObjectName("chose_file_btn")
        self.verticalLayout_2.addWidget(self.chose_file_btn)
        self.label_btn = QtWidgets.QPushButton(self.centralwidget)
        self.label_btn.setObjectName("label_btn")
        self.verticalLayout_2.addWidget(self.label_btn)
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setObjectName("run_btn")
        self.verticalLayout_2.addWidget(self.run_btn)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_2.addWidget(self.save_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree.setObjectName("tree")
        self.horizontalLayout_6.addWidget(self.tree)
        self.text_content = QtWidgets.QTextEdit(self.centralwidget)
        self.text_content.setObjectName("text_content")
        self.horizontalLayout_6.addWidget(self.text_content)
        self.horizontalLayout_6.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.ARI_show = QtWidgets.QLabel(self.centralwidget)
        self.ARI_show.setObjectName("ARI_show")
        self.horizontalLayout_7.addWidget(self.ARI_show)
        self.horizontalLayout_7.setStretch(1, 2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#3776ff;\">文本聚类系统</span></p></body></html>"))
        self.cluster_kind_lb.setText(_translate("MainWindow", "聚类算法："))
        self.km_radio.setText(_translate("MainWindow", "simpleKmeans"))
        self.av_ensembel_radio.setText(_translate("MainWindow", "Average-Ensemble"))
        self.label_3.setText(_translate("MainWindow", "目标簇数："))
        self.label_iter.setText(_translate("MainWindow", "迭代次数："))
        self.chose_file_btn.setText(_translate("MainWindow", "选择文件"))
        self.label_btn.setText(_translate("MainWindow", "真实标签"))
        self.run_btn.setText(_translate("MainWindow", "开始聚类"))
        self.save_btn.setText(_translate("MainWindow", "保存"))
        self.tree.headerItem().setText(0, _translate("MainWindow", "文件名"))
        self.tree.headerItem().setText(1, _translate("MainWindow", "类别"))
        self.label_5.setText(_translate("MainWindow", "ARI："))
        self.ARI_show.setText(_translate("MainWindow", "0.0"))
