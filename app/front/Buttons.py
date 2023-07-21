from PyQt5.QtWidgets import QPushButton



def button(self, move1, move2, size1,size2, name):
    button = QPushButton(name, self)
    button.move(move1,move2)
    button.resize(size1,size2)
    return button

def testa():
    print('deu')

