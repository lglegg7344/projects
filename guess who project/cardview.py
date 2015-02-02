import sys
from PyQt4 import QtGui #imports




class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        WINDOW_WIDTH=1876
        WINDOW_HEIGHT=1000
        SPACING = 0
        COLS = 10
        ROWS = 10
        grid = QtGui.QGridLayout()
        grid.setSpacing(SPACING)
        cards = []
        picWidth = ((WINDOW_WIDTH-((COLS+1)*SPACING))/COLS)
        print(WINDOW_WIDTH)
        print(picWidth)
        for x in range(1,(2*ROWS),2):
            for y in range(1,(2*COLS),2):
                pic = QtGui.QPixmap("IMG_4138.jpg")
                card = QtGui.QLabel(self)
                
                card.setPixmap(pic.scaledToWidth(picWidth))
                grid.addWidget(card,x,y,1,2)
            
        self.setLayout(grid)
        self.setGeometry(30,30,WINDOW_WIDTH,WINDOW_HEIGHT)
        self.setWindowTitle('Pi Guess  Who')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

def main():
    
    app = QtGui.QApplication(sys.argv) # define app using system arguments

    ex = Example()
    sys.exit(app.exec())    #enter main loop for the app

if __name__ == '__main__':
    main()
