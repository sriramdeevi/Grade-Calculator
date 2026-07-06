import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    # Initialize the application
    app = QApplication(sys.argv)
    
    # Create a basic window widget
    window = QWidget()
    window.resize(1600, 800)
    window.setWindowTitle('Flight Sim Test Window')
    
    # Show the window on screen
    window.show()
    
    # Safely close out the application process when exiting
    sys.exit(app.exec())

if __name__ == '__main__':
    main()