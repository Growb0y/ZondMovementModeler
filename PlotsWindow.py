import matplotlib
from PyQt5.QtGui import QIcon

matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=100, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axs = fig.subplots(2, sharey='col')
        fig.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.8,
                            hspace=0.4)
        fig.suptitle('Графики')
        super(MplCanvas, self).__init__(fig)


class PlotsWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(PlotsWindow, self).__init__()
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("Modeler: Отчёт. Графики")

    def setupUi(self, Window, points_list):

        Window.setObjectName("ModelWindow")
        Window.resize(900, 900)

        sc = MplCanvas(self, width=100, height=100, dpi=100)

        x, y, t = [], [], []
        for point in points_list:
            x.append(point[0])
            y.append(point[1])
            t.append(point[2])
        sc.axs[0].set_title("Отклонение от вертикали - время")
        sc.axs[0].set_xlabel("Время")
        sc.axs[0].set_ylabel("Отклонение от вертикали")
        sc.axs[0].plot(t, x)
        sc.axs[1].set_title("Высота - время")
        sc.axs[1].set_xlabel("Время")
        sc.axs[1].set_ylabel("Высота")
        sc.axs[1].plot(t, y)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
