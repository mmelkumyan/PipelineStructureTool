# from PyQt5 import QtWidgets
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_mainWindow import Ui_MainWindow
from folderStructureGenerator import generate_dirs


# Regenerate ui class: `pyuic5 -x .\pipelineToolQT.ui -o ui_mainWindow_BACKUP.py`

class MainWindow(QMainWindow):
    episode_cnt = 0
    season_cnt = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # MAIN MODEL
    def signalMainBrowse(self):
        file_name = self.browseModelFile("Main", "./Models")
        if file_name:
            self.ui.mainLocation.setText(file_name)
        return

    def signalMainGenerate(self):
        episode_root = "root/"
        model_file = self.ui.mainLocation.text()
        generate_dirs(episode_root, model_file)
        return

    # EPISODE MODEL
    def signalEpisodeBrowse(self):
        file_name = self.browseModelFile("Episode", "./Models")
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

    def browseModelFile(self, model_name, root):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, f"Browse {model_name} Model", root, "Model files (*.txt)",
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
