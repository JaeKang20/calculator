from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        main_layout = QVBoxLayout()

        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        # 수식 결과
        self.equation_ = QLineEdit()
        self.solution_ = QLineEdit()
        layout_equation_solution.addRow("Equation:", self.equation_)
        layout_equation_solution.addRow("Solution:", self.solution_)

        # 사칙연산 버튼
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_multiply = QPushButton("*")
        button_divide = QPushButton("/")

        button_plus.clicked.connect(self.ButtonPlusClicked)
        button_minus.clicked.connect(self.ButtonMinusClicked)
        button_multiply.clicked.connect(self.ButtonMultiplyClicked)
        button_divide.clicked.connect(self.ButtonDivideClicked)

        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_multiply)
        layout_operation.addWidget(button_divide)

        # clear와 equal 버튼
        button_clear = QPushButton("AC")
        button_backspace = QPushButton("C")
        button_equal = QPushButton("=")

        button_clear.clicked.connect(self.ButtonClearClicked)
        button_backspace.clicked.connect(self.ButtonBackspaceClicked)
        button_equal.clicked.connect(self.ButtonEqualClicked)

        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        # 숫자 버튼
        number_button_dict = {}
        for number in range(10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(
                lambda state, num=number: self.NumberButtonClicked(num)
            )
            if number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)
            else:
                x, y = divmod(number - 1, 3)
                layout_number.addWidget(number_button_dict[number], 2 - x, y)

        # GUI 레이아웃 설정
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)
        self.setLayout(main_layout)
        self.show()

    def ButtonPlusClicked(self):
        equation = self.equation_.text()
        if not equation.endswith(("+", "-", "*", "/")):
            equation += "+"
            self.equation_.setText(equation)

    def ButtonMinusClicked(self):
        equation = self.equation_.text()
        if not equation.endswith(("+", "-", "*", "/")):
            equation += "-"
            self.equation_.setText(equation)

    def ButtonMultiplyClicked(self):
        equation = self.equation_.text()
        if not equation.endswith(("+", "-", "*", "/")):
            equation += "*"
            self.equation_.setText(equation)

    def ButtonDivideClicked(self):
        equation = self.equation_.text()
        if not equation.endswith(("+", "-", "*", "/")):
            equation += "/"
            self.equation_.setText(equation)

    def NumberButtonClicked(self, num):
        equation = self.equation_.text()
        equation += str(num)
        self.equation_.setText(equation)

    def ButtonEqualClicked(self):
        equation = self.equation_.text()
        solution = eval(equation)
        solution = round(solution)
        self.solution_.setText(str(solution))

    def ButtonClearClicked(self):
        self.equation_.clear()
        self.solution_.clear()

    def ButtonBackspaceClicked(self):
        equation = self.equation_.text()
        self.equation_.setText(equation[:-1])


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    sys.exit(app.exec_())
