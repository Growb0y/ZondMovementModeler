import sys
from multiprocessing import Process
from threading import Thread
from time import sleep

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon

from MainWindowUi import Ui_MainWindow
from ModelWindow import ModelWindow
from PlotsWindow import PlotsWindow

from PointsCalculator import make_points_list
from GifMaker import make_gif

# Set app taskbar icon
# https://stackoverflow.com/a/1552105/984421 for more info
import ctypes
my_app_id = u'modeler'  # Custom application id
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

points_list = []


class Modeler(QMainWindow):

    def __init__(self):
        super(Modeler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Adding Functions to Buttons
        self.ui.pushButton.clicked.connect(self.start_modeling)
        self.ui.pushButton_2.clicked.connect(self.show_plots)
        self.plots_window = PlotsWindow()
        self.ui.pushButton_3.clicked.connect(self.show_model)
        self.model_window = ModelWindow()

        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)

        self.make_gif_process = None
        self.check_if_gif_done_thread = None

        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Modeler")

    def check_if_process_is_alive(self):

        while self.make_gif_process.is_alive():
            sleep(1)
            print("make_gif_process isn't finished yet...")
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton.setEnabled(True)

        # Manipulate with ui components from worker thread
        act = QAction("Action", self)
        act.triggered.connect(self.onGifIsDone)
        act.trigger()

    def start_modeling(self):

        global points_list

        print("Modeling has started")
        self.ui.plainTextEdit_4.setPlainText("Подождите, идёт моделирование...")

        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton.setEnabled(False)

        v0 = int(self.ui.plainTextEdit.toPlainText())
        v_plane = int(self.ui.plainTextEdit_2.toPlainText())
        g = float(self.ui.plainTextEdit_3.toPlainText())

        points_list, time, H, L = make_points_list(v0, v_plane, g)

        self.ui.pushButton_2.setEnabled(True)

        # make_gif(points_list, time, H, L)

        # self.make_gif_thread = Thread(target=make_gif, args=(points_list, time, H, L))
        # self.make_gif_thread.start()

        self.make_gif_process = Process(target=make_gif, name='make_gif_process', args=(points_list, time, H, L))
        self.make_gif_process.start()

        self.check_if_gif_done_thread = Thread(target=self.check_if_process_is_alive)
        self.check_if_gif_done_thread.start()

    def show_plots(self):

        print("Showing plots")
        print(points_list)
        self.plots_window.setupUi(self.plots_window, points_list)
        self.plots_window.show()

    def show_model(self):

        print("Showing model")
        self.model_window.setupUi(self.model_window)
        self.model_window.show()

    def onGifIsDone(self):
        self.ui.plainTextEdit_4.setPlainText("Моделирование завершено.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Modeler()
    mainWin.show()
    sys.exit(app.exec_())
