from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QScrollArea, QAction, QMenu
from PyQt5.QtGui import QPalette, QImage, QPixmap, QPainter


from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.printer = QPrinter()

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        #self.scrollArea =QScrollArea()
        #self.scrollArea.setBackgroundRole(QPalette.Dark)
        #self.scrollArea.setWidget(self.imageLabel)
        

        #self.setCentralWidget(self.scrollArea)
        self.setCentralWidget(self.imageLabel)

        self.image = QImage('lifecycle.png')
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))


        self.createActions()
        self.createMenus()

        self.setWindowTitle('fuckprint')
        self.resize(self.image.width(), self.image.height())

        self.printimg()

    def printimg(self):
        self.printer.setPageSize(QPrinter.A4)
        self.printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)

        print type(QPrinter.A4)

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            width = painter.window().width()
            height = painter.window().height()
            #width2 = self.printer.width()
            #height2 = self.printer.height()

            #painter.drawLine(0, 0, , )

            painter.drawText(200, 200, 'heheheheheh')


    def createActions(self):
        self.printAction = QAction('&Print...', self, shortcut='Ctrl+P', triggered=self.printimg)
        self.exitAction = QAction('&Exit...', self, shortcut='Ctrl+Q', triggered=self.close)

    def createMenus(self):
        self.fileMenu = QMenu('&File', self)
        self.fileMenu.addAction(self.printAction)
        self.fileMenu.addAction(self.exitAction)

        self.menuBar().addMenu(self.fileMenu)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())