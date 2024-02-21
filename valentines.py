import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

def display_valentines_message():
    hearts = '<3' * 5
    header = hearts
    footer = hearts
    valentines_message = f"{header}\nHappy Valentine's Day!!\n{footer}"
    output_label.setText(valentines_message)

# Create the main application
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Message for Daphnet")

# Create a label to display the message
output_label = QLabel("", window)
font = output_label.font()
font.setPointSize(font.pointSize() + 4)
output_label.setFont(font)
output_label.setAlignment(Qt.AlignCenter)

# Create a button to trigger the message display
display_button = QPushButton("For Daphnet", window)
display_button.clicked.connect(display_valentines_message)

# Layout setup
layout = QVBoxLayout()
layout.addWidget(output_label)
layout.addWidget(display_button)
window.setLayout(layout)

# Show the window
window.show()

# Execute the application
sys.exit(app.exec_())
