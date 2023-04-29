from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QSpinBox, QApplication
from moviepy.editor import ImageSequenceClip, AudioFileClip
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

          # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 215, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(9)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.spinbox = QSpinBox(self.centralwidget)
        self.spinbox.setRange(0, 60)
        self.spinbox.setGeometry(QtCore.QRect(10, 245, 281, 28))
        self.spinbox.setObjectName("Set_fps")
        self.spinbox.valueChanged.connect(self.setFPS_func)
        self.value = None

          # Buttons
        self.selectfolder_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectfolder_button.setGeometry(QtCore.QRect(10, 110, 281, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectfolder_button.setFont(font)
        self.selectfolder_button.setObjectName("selectfolder_button")
        self.selectfolder_button.clicked.connect(self.selectfolder_func)

        self.selectaudio_button = QtWidgets.QPushButton(self.centralwidget)
        self.selectaudio_button.setGeometry(QtCore.QRect(10, 180, 281, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectaudio_button.setFont(font)
        self.selectaudio_button.setObjectName("selectaudio_button")
        self.selectaudio_button.clicked.connect(self.selectaudio_func)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(10, 290, 281, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_button.setFont(font)
        self.generate_button.setObjectName("generate_button")
        self.generate_button.clicked.connect(self.generate_func)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

          # Functions
    def selectfolder_func(self):
        self.photo_dir = QFileDialog.getExistingDirectory(None, "Select a folder", ".../")
        print(self.photo_dir)

    def selectaudio_func(self):
        self.audio = QFileDialog.getOpenFileName(None, "Select an MP3/MP4", ".../")
        print(self.audio[0])

    def setFPS_func(self, value):
        self.fps_value = value

    def generate_func(self):
        # Creating a list of files using os library in order to iterate over it
        photo_files = sorted(os.listdir(self.photo_dir))

        # Creating ImageSequenceClip from the jpg files
        clip = ImageSequenceClip([os.path.join(self.photo_dir, i) for i in photo_files], fps=self.fps_value)

        # Changing / Adding audio to the generated file
        audio = AudioFileClip(self.audio[0])
        print(audio)
        clip = clip.set_audio(audio)

        clip.write_videofile("output.mp4", audio_codec="aac")
        print(self.fps_value)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NDNJ"))
        self.label.setText(_translate("MainWindow", "Welcome to"))
        self.label_2.setText(_translate("MainWindow", "NewDayNewJpg"))
        self.selectfolder_button.setText(_translate("MainWindow", "Select folder."))
        self.selectaudio_button.setText(_translate("MainWindow", "Select audio."))
        self.label_3.setText(_translate("MainWindow", "The folder must contain photos only."))
        self.label_4.setText(_translate("MainWindow", "If wanted, select the audio to add."))
        self.label_5.setText(_translate("MainWindow", "Set the desired FPS value."))
        self.generate_button.setText(_translate("MainWindow", "GENERATE THE MP4"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
