import sys

from PyQt5 import QtWidgets


from PyQt5 import QtPrintSupport


from PyQt5 import QtGui, QtCore


class Main(QtWidgets.QtMainWindow):


    def __init__(self, parent = None):
        QtGui.QtMainWindow.__init__(self,parent)

        self.initUI()
    
    def initUI(self):
        self.setGeometry()

        self.setWindowTitle("Writer")


def main():

    app = QtGui.QtApplication(sys.argv)

    main = Main()
    main.show()


    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


