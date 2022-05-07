from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QMovie, QIcon

from PyQt5.QtWidgets import QMainWindow


class ModelWindow(QMainWindow):

    def __init__(self):
        super(ModelWindow, self).__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Modeler: Отчёт. Модель")

    def setupUi(self, Window):
        Window.setObjectName("ModelWindow")
        Window.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setMaximumSize(QtCore.QSize(600, 600))
        self.label.setObjectName("label")

        # add label to main window
        Window.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("simulation.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
