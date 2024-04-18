import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(100, 100, 300, 200)
        
        self.weight_label = QLabel("Enter your weight in kilograms:")
        self.weight_input = QLineEdit()
        
        self.height_label = QLabel("Enter your height in meters:")
        self.height_input = QLineEdit()
        
        self.result_label = QLabel("Your BMI:")
        self.category_label = QLabel("Category:")
        
        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)
        
        layout = QVBoxLayout()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.category_label)
        
        self.setLayout(layout)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
        except ValueError:
            self.result_label.setText("Invalid input")
            self.category_label.setText("")
            return
        
        bmi = weight / (height ** 2)
        self.result_label.setText(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = " Underweight"
        elif bmi < 25:
            category = " Normal weight"
        elif bmi < 30:
            category = " Overweight"
        else:
            category = " Obesity"
        
        self.category_label.setText(f"Category: {category}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = BMICalculator()
    calculator.show()
    sys.exit(app.exec_())
