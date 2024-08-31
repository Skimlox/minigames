import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('TicTacToe')
        self.setGeometry(200, 200, 300, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.buttons = [[QPushButton() for x in range(3)] for x in range(3)]
        self.current_player = 'X'

        for row in range(3):
            for column in range(3):
                button = self.buttons[row][column]
                button.setFixedSize(100, 100)
                button.setFont(QFont('Arial', 24))
                button.setStyleSheet("background-color: white; border: 1px solid black;")
                button.clicked.connect(lambda _, r=row, c=column: self.click(r, c))
                self.layout.addWidget(button, row, column)  # Use QGridLayout

        self.show()
    def click(self, row, col):
        button = self.buttons[row][col]
        if button.text() == "":
            button.setText(self.current_player)
            if self.winner():
                QMessageBox.information(self, 'Game Over', f'Player {self.current_player} wins!')
                self.reset_game()
            elif self.draw():
                QMessageBox.information(self, 'Game Over', 'It\'s a draw!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    def winner(self):
        for row in self.buttons:
            if row[0].text() == row[1].text() == row[2].text() != "":
                return True
        for column in range(3):
            if self.buttons[0][column].text() == self.buttons[1][column].text() == self.buttons[2][column].text() != "":
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True

        return False
    def draw(self):
        return all(button.text() != "" for row in self.buttons for button in row)

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.setText("")
        self.current_player = 'X'
if __name__ == '__main__':
    app = QApplication(sys.argv)
    play_game = TicTacToe()
    sys.exit(app.exec())