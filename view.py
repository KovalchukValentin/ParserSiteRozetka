import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLabel, QTextEdit, QVBoxLayout, QWidget, \
    QLineEdit, QDockWidget, QMenu


class CustomToolbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create buttons and labels for the left toolbar
        button1 = QAction("Button 1", self)
        button2 = QAction("Button 2", self)

        # Create an entry widget for the left toolbar
        entry = QLineEdit(self)

        # Add buttons and entry to the left toolbar
        self.addAction(button1)
        self.addAction(button2)
        self.addWidget(entry)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a central widget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a top toolbar
        top_toolbar = QToolBar()
        self.addToolBar(top_toolbar)

        # Create a menu for the top button
        top_button_menu = QMenu(self)
        open_action_toolbar = top_button_menu.addAction("Toolbar")

        # Create a top button with the menu
        top_button = QAction("Windows", self)
        top_button.setMenu(top_button_menu)
        top_toolbar.addAction(top_button)

        # Create a text edit field (QTextEdit)
        text_edit = QTextEdit()
        layout.addWidget(text_edit)

        # Create a custom toolbar for the left side
        self.custom_toolbar = CustomToolbar()

        # Create a dock widget and set the custom toolbar as its widget for the left side
        self.dock_widget = QDockWidget("Toolbar", self)
        self.dock_widget.setWidget(self.custom_toolbar)

        # Initially, the left toolbar is open
        self.addDockWidget(1, self.dock_widget)  # 1 represents the left dock widget area

        self.setWindowTitle("Parcer")
        self.setGeometry(100, 100, 800, 600)

        # Connect menu actions to the corresponding methods
        open_action_toolbar.triggered.connect(self.show_or_hide_toolbar)

    def show_or_hide_toolbar(self):
        # Show or hide toolbar
        if self.dock_widget.isHidden():
            self.dock_widget.show()
        else:
            self.dock_widget.hide()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()