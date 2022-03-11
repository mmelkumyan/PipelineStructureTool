import sys
import os
import json

from PyQt5 import QtWidgets, QtCore

from PipelineScript.ui.ui_mainWindow import Ui_MainWindow
from folderStructureGenerator import generate_dirs, generate_root
import projects

# Regenerate source ui class: ` pyuic5 -x .\PipelineScript\ui\pipelineToolQT.ui -o .\PipelineScript\ui\ui_mainWindow.py`


class MainWindow(QtWidgets.QMainWindow):
    row_cnt = 0
    row_to_model_name_map = {}

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # PROJECT SAVE/LOAD
    def sLoadProject(self):
        print("Load project")
        self.clearModelRows()
        project_path = self.browseFile("./Projects", "Browse Projects", "Project", "json")
        if project_path:
            with open(project_path) as project_file:
                project = json.load(project_file)
                name = project["name"]
                self.ui.projectNameText.setText(name)
                models = project["models"]
                for r, (model_name, fields) in enumerate(models.items()):
                    row_name = self.createNewModelRow(r)
                    getattr(self.ui, row_name + "ModelLabel").setText(model_name)
                    self.row_to_model_name_map[row_name] = model_name
                    getattr(self.ui, row_name + "NumberText").setText(fields["numTemplate"])
                    getattr(self.ui, row_name + "LocationText").setText(fields["modelFile"])
                    getattr(self.ui, row_name + "RootText").setText(fields["rootDir"])
                    self.row_cnt += 1

    def sSaveProject(self):
        if self.row_cnt == 0:
            self.showErrorPopup("Failed to save: No directory models")
            return

        print("Save project")
        project_name = self.ui.projectNameText.text()
        self.saveProject(project_name)
        self.showInfoPopup("Project saved!")

    def saveProject(self, name):
        project = {
            "name": name,
            "models": {},
            "structure": {}
        }

        for row_name, model_name in self.row_to_model_name_map.items():
            project["models"][model_name] = {}
            project["models"][model_name]["numTemplate"] = getattr(self.ui, row_name + "NumberText").text()
            project["models"][model_name]["modelFile"] = getattr(self.ui, row_name + "LocationText").text()
            project["models"][model_name]["rootDir"] = getattr(self.ui, row_name + "RootText").text()

        json_object = json.dumps(project, indent=4)
        root = os.path.join(os.getcwd(), "Projects")
        suffix = "_PipelineProject"
        file_name = name.replace(" ", "") + suffix + ".json"
        file_path = os.path.join(root, file_name)

        with open(file_path, "w") as out:
            out.write(json_object)

    def sNewRow(self):
        print("new row!")
        self.createNewModelRow(self.row_cnt)
        self.row_cnt += 1

    def createNewModelRow(self, row):
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
        number_text_name = row_name + "NumberText"
        number_text = QtWidgets.QLineEdit(self.ui.verticalLayoutWidget)
        number_text.setObjectName(number_text_name)
        new_horizontal_layout.addWidget(number_text)
        setattr(self.ui, number_text_name, number_text)

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

        new_horizontal_layout.setStretch(0, 7)  # Model name
        new_horizontal_layout.setStretch(1, 1)  # Number text
        new_horizontal_layout.setStretch(2, 10)  # Model location
        new_horizontal_layout.setStretch(4, 10)  # Root location

        self.ui.modelsVerticleLayout.insertLayout(self.ui.modelsVerticleLayout.count(), new_horizontal_layout)
        setattr(self.ui, horizontal_layout_name, new_horizontal_layout)

        # RE-TRANSLATE UI
        _translate = QtCore.QCoreApplication.translate
        model_text.setText(_translate("MainWindow", "<Model Name>"))
        model_text.setPlaceholderText(_translate("MainWindow", "Name of structure"))
        number_text.setText(_translate("MainWindow", "M###"))
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

        return row_name

    # SIGNALS
    def sModelBrowse(self, row_name):
        print(f"Browse model {row_name}")
        model_name = self.row_to_model_name_map[row_name]
        file_name = self.browseFile("./Models", f"Browse {model_name} Models", "Model", "txt")
        if file_name:
            getattr(self.ui, row_name + "LocationText").setText(file_name)

    def sRootBrowse(self, row_name):
        print(f"Browse root {row_name}")
        model_name = self.row_to_model_name_map[row_name]
        dir_name = self.browseDirectory("./", model_name + " Root")
        if dir_name:
            getattr(self.ui, row_name + "RootText").setText(dir_name)

    def sGenerate(self, row_name):
        print(f"Generate {row_name}")
        model_file = getattr(self.ui, row_name + "LocationText").text()
        number_text = getattr(self.ui, row_name + "NumberText").text()
        episode_root = getattr(self.ui, row_name + "RootText").text()
        if number_text != "":
            episode_root = generate_root(episode_root, number_text)
        status, details = generate_dirs(episode_root, model_file)
        if status == 0:
            model_name = self.row_to_model_name_map[row_name]
            self.showInfoPopup(f"Generated {model_name}!", details)
        else:
            self.showErrorPopup("An error has occurred", details)

    def sModelTextChange(self, row_name, text):
        print(f"{row_name}, new text: {text}")
        self.row_to_model_name_map[row_name] = text

    def sClearAllModels(self):
        print("Clearing all model rows")
        self.clearModelRows()

    # POP-UP WINDOWS
    @staticmethod
    def showInfoPopup(main_text, details_text=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Pipeline Structure Tool")
        msg.setText(main_text + "                ")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        if details_text != "":
            msg.setDetailedText(details_text)
        msg.exec_()

    @staticmethod
    def showErrorPopup(main_text, details_text=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Pipeline Structure Tool")
        msg.setText(main_text + "                ")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        if details_text != "":
            msg.setDetailedText(details_text)
        msg.exec_()

    # HELPER FUNCTIONS
    def clearModelRows(self):
        self.deleteItemsOfLayout(self.ui.modelsVerticleLayout)
        self.row_cnt = 0
        self.row_to_model_name_map = {}

    def browseFile(self, root, window_title, file_name, file_ext):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, window_title, root, f"{file_name} files (*.{file_ext})",
                                                             options=options)
        return file_name

    def browseDirectory(self, root, dir_type):
        options = QtWidgets.QFileDialog.Options()
        file_name = QtWidgets.QFileDialog.getExistingDirectory(self, f"Browse {dir_type}", root, options=options)
        return file_name

    # Initially sourced from: https://stackoverflow.com/questions/37564728/pyqt-how-to-remove-a-layout-from-a-layout
    def deleteItemsOfLayout(self, layout):
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                delattr(self.ui, widget.objectName())
                del widget
            else:  # If it's not a widget, it is a layout
                self.deleteItemsOfLayout(item.layout())
                delattr(self.ui, item.layout().objectName())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
