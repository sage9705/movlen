import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QProgressBar
)
from moviepy.editor import VideoFileClip
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class VideoLengthCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Length Calculator')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Select a folder to calculate total video length', self)
        layout.addWidget(self.label)

        self.button = QPushButton('Select Folder', self)
        self.button.clicked.connect(self.showDialog)
        layout.addWidget(self.button)

        self.resultLabel = QLabel('', self)
        layout.addWidget(self.resultLabel)

        self.progressBar = QProgressBar(self)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)

        self.setLayout(layout)

    def showDialog(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.calculateTotalLength(folder)

    def calculateTotalLength(self, folder):
        self.progressBar.setValue(0)
        self.resultLabel.setText('')

        self.thread = VideoLengthThread(folder)
        self.thread.progress_update.connect(self.updateProgressBar)
        self.thread.result_ready.connect(self.displayResult)
        self.thread.error_occurred.connect(self.displayError)
        self.thread.start()

    def updateProgressBar(self, value):
        self.progressBar.setValue(value)

    def displayResult(self, total_length):
        hours, remainder = divmod(total_length, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.resultLabel.setText(f'Total video length: {int(hours):02}:{int(minutes):02}:{int(seconds):02}')

    def displayError(self, message):
        QMessageBox.warning(self, 'Error', message)


class VideoLengthThread(QThread):
    progress_update = pyqtSignal(int)
    result_ready = pyqtSignal(float)
    error_occurred = pyqtSignal(str)

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def run(self):
        total_length = 0
        video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.mpeg', '.mpg')
        video_files = [f for f in os.listdir(self.folder) if f.lower().endswith(video_extensions)]
        total_files = len(video_files)

        if total_files == 0:
            self.error_occurred.emit('No video files found in the selected folder.')
            return

        for i, filename in enumerate(video_files):
            filepath = os.path.join(self.folder, filename)
            try:
                clip = VideoFileClip(filepath)
                total_length += clip.duration
                clip.close()
            except Exception as e:
                self.error_occurred.emit(f'Error reading file {filename}: {str(e)}')
                continue
            progress = int((i + 1) / total_files * 100)
            self.progress_update.emit(progress)

        self.result_ready.emit(total_length)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoLengthCalculator()
    ex.show()
    sys.exit(app.exec_())
