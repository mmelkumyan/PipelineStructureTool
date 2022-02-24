# -*- coding: utf-8 -*-

# Form implementation generated from reading src_ui file '.\PipelineScript\pipelineToolQT.src_ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 481, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.projectsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.projectsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.projectsGridLayout.setObjectName("projectsGridLayout")
        self.projectLoadButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.projectLoadButton.setObjectName("projectLoadButton")
        self.projectsGridLayout.addWidget(self.projectLoadButton, 1, 2, 1, 1)
        self.projectSaveButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.projectSaveButton.setObjectName("projectSaveButton")
        self.projectsGridLayout.addWidget(self.projectSaveButton, 1, 4, 1, 1)
        self.projectNameText = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.projectNameText.setObjectName("projectNameText")
        self.projectsGridLayout.addWidget(self.projectNameText, 1, 1, 1, 1)
        self.projectNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectsGridLayout.addWidget(self.projectNameLabel, 1, 0, 1, 1)
        self.newRowButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.newRowButton.setObjectName("newRowButton")
        self.projectsGridLayout.addWidget(self.newRowButton, 1, 5, 1, 1)
        self.rootLocationLabel = QtWidgets.QLabel(self.centralwidget)
        self.rootLocationLabel.setGeometry(QtCore.QRect(340, 100, 91, 24))
        self.rootLocationLabel.setObjectName("rootLocationLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 120, 811, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.modelsVerticleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.modelsVerticleLayout.setContentsMargins(0, 0, 0, 0)
        self.modelsVerticleLayout.setObjectName("modelsVerticleLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baseModelLable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.baseModelLable.setObjectName("baseModelLable")
        self.horizontalLayout.addWidget(self.baseModelLable)
        self.baseNumberLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.baseNumberLabel.setObjectName("baseNumberLabel")
        self.horizontalLayout.addWidget(self.baseNumberLabel)
        self.baseLocationText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.baseLocationText.setStatusTip("")
        self.baseLocationText.setText("")
        self.baseLocationText.setObjectName("baseLocationText")
        self.horizontalLayout.addWidget(self.baseLocationText)
        self.baseLocationBrowseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.baseLocationBrowseButton.setObjectName("baseLocationBrowseButton")
        self.horizontalLayout.addWidget(self.baseLocationBrowseButton)
        self.baseRootText = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.baseRootText.setStatusTip("")
        self.baseRootText.setText("")
        self.baseRootText.setObjectName("baseRootText")
        self.horizontalLayout.addWidget(self.baseRootText)
        self.baseRootBrowseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.baseRootBrowseButton.setObjectName("baseRootBrowseButton")
        self.horizontalLayout.addWidget(self.baseRootBrowseButton)
        self.baseGenerateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.baseGenerateButton.setObjectName("baseGenerateButton")
        self.horizontalLayout.addWidget(self.baseGenerateButton)
        self.horizontalLayout.setStretch(2, 5)
        self.horizontalLayout.setStretch(4, 5)
        self.modelsVerticleLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.modelsVerticleLayout.addItem(spacerItem)
        self.dirModelLocationLabel = QtWidgets.QLabel(self.centralwidget)
        self.dirModelLocationLabel.setGeometry(QtCore.QRect(100, 100, 121, 21))
        self.dirModelLocationLabel.setObjectName("dirModelLocationLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCreate_Model = QtWidgets.QMenu(self.menubar)
        self.menuCreate_Model.setObjectName("menuCreate_Model")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCreate_Model.menuAction())

        self.retranslateUi(MainWindow)
        # self.baseGenerateButton.clicked.connect(MainWindow.signalMainGenerate) # type: ignore
        # self.baseLocationBrowseButton.clicked.connect(MainWindow.signalMainBrowse) # type: ignore
        self.projectLoadButton.clicked.connect(MainWindow.signalLoadProject) # type: ignore
        self.projectSaveButton.clicked.connect(MainWindow.signalSaveProject) # type: ignore
        # self.baseRootBrowseButton.clicked.connect(MainWindow.signalMainRootBrowse) # type: ignore
        self.newRowButton.clicked.connect(MainWindow.signalNewRow) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectLoadButton.setText(_translate("MainWindow", "Load"))
        self.projectSaveButton.setText(_translate("MainWindow", "Save"))
        self.projectNameText.setText(_translate("MainWindow", "Story Medicine"))
        self.projectNameLabel.setText(_translate("MainWindow", "Project Name"))
        self.newRowButton.setText(_translate("MainWindow", "New Row"))
        self.rootLocationLabel.setText(_translate("MainWindow", "Root location"))
        self.baseModelLable.setText(_translate("MainWindow", "Base Model"))
        self.baseNumberLabel.setText(_translate("MainWindow", "001"))
        self.baseLocationText.setPlaceholderText(_translate("MainWindow", "/model/location.txt"))
        self.baseLocationBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.baseRootText.setPlaceholderText(_translate("MainWindow", "/root"))
        self.baseRootBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.baseGenerateButton.setText(_translate("MainWindow", "Generate"))
        self.dirModelLocationLabel.setText(_translate("MainWindow", "Directory model location"))
        self.menuFile.setTitle(_translate("MainWindow", "Generate"))
        self.menuCreate_Model.setTitle(_translate("MainWindow", "Create Model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
