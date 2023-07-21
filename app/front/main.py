import sys
sys.path.append('./app/back/')
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
import Buttons
import Armor as a 
 
class window (QMainWindow):
    def __init__(self):
        super().__init__()
        count = 3
        self.top =  100 
        self.left = 100
        self.weigth = 800
        self.high = 600
        self.title = "test"

        self.search_box = QLineEdit(self)
        self.search_box.move(50,20)
        self.search_box.setStyleSheet('QLabel{font:bold;font-size:25px}')
        self.search_box.resize(300,20)

        
        self.label = QLabel(self)
        self.label.move(250,300)
        self.label.setStyleSheet('QLabel{font:bold;font-size:25px}')
        self.label.resize(350,25)



        self.text = QLabel(self)
        self.text.move(50,100)
        self.text.setStyleSheet('QLabel{font:bold;font-size:10px}')
        self.text.resize(570,450)



        button2 = Buttons.button(self,451,20,50,20,'search')
        button = Buttons.button(self,250,400,100,100,'button1')
        
        button.clicked.connect(self.butt_clicks)
        button2.clicked.connect(self.search_click)

        self.loadwindow()

    def loadwindow (self):
        self.setGeometry(self.left, self.top,self.weigth,self.high)
        self.setWindowTitle(self.title)
        self.show()

    def butt_clicks(self):
        self.label.setText('count')      


    def search_click(self):
        content = self.search_box.text()
        result = a.armor('pt',content)
        print(result)
        result = str(result)
        self.text.setText(result)
        

app= QApplication(sys.argv)
w = window()
sys.exit(app.exec_())        