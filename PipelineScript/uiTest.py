import sys

from PyQt5 import QtWidgets, QtCore

from PipelineScript.ui.ui_mainWindow import Ui_MainWindow
from folderStructureGenerator import generate_dirs

# Regenerate source ui class: ` pyuic5 -x .\PipelineScript\ui\pipelineToolQT.ui -o .\PipelineScript\ui\ui_mainWindow.py`


class MainWindow(QtWidgets.QMainWindow):
    row_cnt = 0
    row_to_model_name_map = {}

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # PROJECT SAVE/LOAD
    def signalLoadProject(self):
        print("Load project")
        return

    def signalSaveProject(self):
        print("Save project")
        return

    def signalNewRow(self):
        print("new row!")
        self.createNewRow(self.row_cnt)
        self.row_cnt += 1

        # print(self.src_ui.row0_HorizontalLayout.text() + " wow!")
        # x=self.src_ui.row0HorizontalLayout.itemAt(0).widget()
        # print(x.text() + " wow!")

    def createNewRow(self, row):
        # CREATE WIDGETS
        row_name = f"row{row}"

        # Create horizontal layout group
        horizontal_layout_name = row_name + "HorizontalLayout"
        new_horizontal_layout = QtWidgets.QHBoxLayout()
        new_horizontal_layout.setObjectName(horizontal_layout_name)

        # Create row Label
        model_text_name = row_name + "ModelLabel"
        model_text = QtWidgets.QLineEdit(self.ui.verticalLayoutWidget)
        model_text.setObjectName(model_text_name)
        model_text.setText(model_text_name)
        new_horizontal_layout.addWidget(model_text)
        setattr(self.ui, model_text_name, model_text)

        # Create number label
        number_label_name = row_name + "NumberLabel"
        number_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
        number_label.setObjectName(number_label_name)
        new_horizontal_layout.addWidget(number_label)
        setattr(self.ui, number_label_name, number_label)

        # Create location text field
        location_text_name = row_name + "LocationText"
        location_text = QtWidgets.QLineEdit(self.ui.verticalLayoutWidget)
        location_text.setObjectName(location_text_name)
        new_horizontal_layout.addWidget(location_text)
        setattr(self.ui, location_text_name, location_text)

        # Create location browse button
        location_browse_button_name = row_name + "LocationBrowseButton"
        location_browse_button = QtWidgets.QPushButton(self.ui.verticalLayoutWidget)
        location_browse_button.setObjectName(location_browse_button_name)
        new_horizontal_layout.addWidget(location_browse_button)
        setattr(self.ui, location_browse_button_name, location_browse_button)

        # Create root text field
        root_text_name = row_name + "RootText"
        root_text = QtWidgets.QLineEdit(self.ui.verticalLayoutWidget)
        root_text.setObjectName(root_text_name)
        new_horizontal_layout.addWidget(root_text)
        setattr(self.ui, root_text_name, root_text)

        # Create root browse button
        root_browse_button_name = row_name + "RootBrowseButton"
        root_browse_button = QtWidgets.QPushButton(self.ui.verticalLayoutWidget)
        root_browse_button.setObjectName(root_browse_button_name)
        new_horizontal_layout.addWidget(root_browse_button)
        setattr(self.ui, root_browse_button_name, root_browse_button)

        # Create generate button
        generate_button_name = row_name + "GenerateButton"
        generate_button = QtWidgets.QPushButton(self.ui.verticalLayoutWidget)
        generate_button.setObjectName(generate_button_name)
        new_horizontal_layout.addWidget(generate_button)
        setattr(self.ui, generate_button_name, generate_button)

        # self.horizontalLayout.setStretch(2, 5)
        # self.horizontalLayout.setStretch(4, 5)

        self.ui.modelsVerticleLayout.insertLayout(self.ui.modelsVerticleLayout.count()-2, new_horizontal_layout)
        setattr(self.ui, horizontal_layout_name, new_horizontal_layout)

        # RE-TRANSLATE UI
        _translate = QtCore.QCoreApplication.translate
        model_text.setText(_translate("MainWindow", "<Model Name>"))
        model_text.setPlaceholderText(_translate("MainWindow", "Name of structure"))
        number_label.setText(_translate("MainWindow", "001"))
        location_text.setPlaceholderText(_translate("MainWindow", "/modelFile.txt"))
        location_browse_button.setText(_translate("MainWindow", "Browse Model"))
        root_text.setPlaceholderText(_translate("MainWindow", "/rootDirectory"))
        root_browse_button.setText(_translate("MainWindow", "Browse Root"))
        generate_button.setText(_translate("MainWindow", "Generate"))

        # CONNECT SLOTS
        location_browse_button.clicked.connect(lambda: self.sModelBrowse(row_name))
        root_browse_button.clicked.connect(lambda: self.sRootBrowse(row_name))
        generate_button.clicked.connect(lambda: self.sGenerate(row_name))
        model_text.editingFinished.connect(lambda: self.sModelTextChange(row_name, model_text.text()))
        QtCore.QMetaObject.connectSlotsByName(self)

        # SAVE INFO TO MAP
        self.row_to_model_name_map[row_name] = ""

    # SIGNALS
    def sModelBrowse(self, row_name):
        print(f"Browse model {row_name}")
        model_name = self.row_to_model_name_map[row_name]
        file_name = self.browseFile("./Models", model_name + " Model")
        if file_name:
            getattr(self.ui, row_name+"LocationText").setText(file_name)
        return

    def sRootBrowse(self, row_name):
        print(f"Browse root {row_name}")
        model_name = self.row_to_model_name_map[row_name]
        dir_name = self.browseDirectory("./", model_name + " Root")
        if dir_name:
            getattr(self.ui, row_name + "RootText").setText(dir_name)
        return

    def sGenerate(self, row_name):
        print(f"Generate {row_name}")
        model_file = getattr(self.ui, row_name + "LocationText").text()
        episode_root = getattr(self.ui, row_name + "RootText").text()
        generate_dirs(episode_root, model_file)
        # TODO: increment cnt
        return

    def sModelTextChange(self, row_name, text):
        print(f"{row_name}, new text: {text}")
        self.row_to_model_name_map[row_name] = text
        return

    def browseFile(self, root, file_type):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, f"Browse {file_type}", root, "Model files (*.txt)",
                                                   options=options)
        return file_name

    def browseDirectory(self, root, dir_type):
        options = QtWidgets.QFileDialog.Options()
        file_name = QtWidgets.QFileDialog.getExistingDirectory(self, f"Browse {dir_type}", root, options=options)
        return file_name

    # TODO:
    # Add signal/slot for setting project
    # Write project info to project json


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
