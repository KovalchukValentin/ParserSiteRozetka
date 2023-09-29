import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLabel, QTextEdit, QVBoxLayout, QWidget, \
    QLineEdit, QDockWidget, QMenu, QPushButton, QGridLayout

from core import Parcer

class CustomToolbar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        # Create a widget for the custom toolbar content
        content_widget = QWidget()
        self.addWidget(content_widget)
        # Create a QGridLayout for the content widget
        layout = QGridLayout(content_widget)
        layout.setSpacing(15)
        # Add widgets to the layout
        label_link = QLabel("Link:")
        layout.addWidget(label_link, 0, 0)

        label_tag = QLabel("Tag:")
        layout.addWidget(label_tag, 1, 0)

        label_class = QLabel("Class:")
        layout.addWidget(label_class, 2, 0)

        self.entry_link = QLineEdit()
        layout.addWidget(self.entry_link, 0, 1, 1, 2)

        self.entry_tag = QLineEdit()
        layout.addWidget(self.entry_tag, 1, 1, 1, 2)

        self.entry_class = QLineEdit()
        layout.addWidget(self.entry_class, 2, 1, 1, 2)

        self.label_error = QLabel("")
        self.label_error.setStyleSheet("color: red;")
        self.label_error.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_error, 3, 0, 1, 3)

        btn_clean = QPushButton("Clean")
        btn_clean.clicked.connect(self.press_clean)
        layout.addWidget(btn_clean, 5, 1)

        btn_parce = QPushButton("Parce")
        btn_parce.clicked.connect(self.press_parce)
        layout.addWidget(btn_parce, 5, 2)

    def press_clean(self):
        self.parent.text_edit.setText("")

    def press_parce(self):
        try:
            parser = Parcer(url=self.entry_link.text())
        except Exception as e:
            self.label_error.setText(str(e))
            return

        for results in parser.get_all_tag_with_class(tag=self.entry_tag.text(), class_=self.entry_class.text()):
            for link in results:
                self.parent.text_edit.append(f'{link.text}\n')


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
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # Create a custom toolbar for the left side
        self.custom_toolbar = CustomToolbar(self)

        # Create a dock widget and set the custom toolbar as its widget for the left side
        self.dock_widget = QDockWidget("Toolbar", self)
        self.dock_widget.setWidget(self.custom_toolbar)

        # Initially, the left toolbar is open
        self.addDockWidget(1, self.dock_widget)  # 1 represents the left dock widget area

        self.setWindowTitle("Parser")
        self.setGeometry(0, 0, 1280, 720)

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