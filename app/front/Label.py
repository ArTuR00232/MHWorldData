from PyQt5.QtWidgets import QLabel

def label(self):
    self.label = QLabel(self)
    self.label.move(350,100)
    self.label.setStyleSheet('QLabel{font:bold;font-size:25px}')
    self.label.resize(350,25)
    return label
    

def settext(self,label):
        label.setText('count')