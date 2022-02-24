# from PyQt5 import QtWidgets
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_mainWindow import Ui_MainWindow
from folderStructureGenerator import generate_dirs


# Regenerate ui class: `pyuic5 -x .\PipelineScript\pipelineToolQT.ui -o .\PipelineScript\ui_mainWindow.py`

class MainWindow(QMainWindow):
    episode_cnt = 0
    season_cnt = 0

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

    # MAIN MODEL
    def signalMainBrowse(self):
        file_name = self.browseModelFile("Main Model", "./Models", False)
        if file_name:
            self.ui.mainLocation.setText(file_name)
        return

    def signalMainRootBrowse(self):
        file_name = self.browseModelFile("root location", "./", True)
        if file_name:
            self.ui.mainRoot.setText(file_name)
        return


    def signalMainGenerate(self):
        episode_root = self.ui.mainRoot.text()
        model_file = self.ui.mainLocation.text()
        generate_dirs(episode_root, model_file)
        return

    # EPISODE MODEL
    def signalEpisodeBrowse(self):
        file_name = self.browseModelFile("Episode Model", "./Models", False)
        if file_name:
            self.ui.episodeLocation.setText(file_name)

    def signalEpisodeGenerate(self):
        # episode_root = "root/StoryMedicine/SMS_S###/EDITORIAL/E###"
        self.episode_cnt += 1
        episode_root = f"root/StoryMedicine/SMS_S##/EDITORIAL/E{self.episode_cnt}"
        os.mkdir(episode_root)
        model_file = self.ui.episodeLocation.text()
        generate_dirs(episode_root, model_file)
        self.ui.episodeNumberLabel.setText(str(self.episode_cnt))
        return

    # SEASON MODEL
    def signalSeasonBrowse(self):
        return

    def signalSeasonGenerate(self):
        return

    def browseModelFile(self, file_type, root, is_dir):
        options = QFileDialog.Options()
        if is_dir:
            file_name = QFileDialog.getExistingDirectory(self, "test caption", root, options=options)
        else:
            file_name, _ = QFileDialog.getOpenFileName(self, f"Browse {file_type}", root, "Model files (*.txt)",
                                                       options=options)
        if file_name:
            return file_name
        else:
            return None

    # TODO:
    # Add signal/slot for setting project
    # Write project info to project json




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
