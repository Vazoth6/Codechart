import sys

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QTextEdit,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
    QMenuBar,
    QMenu,
    QStatusBar,
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

class MainWindow:

    def __init__(self):
        super().__init__()

        # Configurar a interface da janela principal
        self._setup_tool_bar()


    def _setup_tool_bar(self):
        """Configura a barra do menu."""

        menubar = self.menuBar()

        # Menu Ficheiro
        file_menu = menubar.addMenu("&Ficheiro")

        open_action = QAction("Open File", self)
        open_action.setShortcut("Ctrl + O")
        open_action.triggered.connect(self._on_open_file)
        file_menu.addAction(open_action)

        open_action = QAction("Open Recent File", self)
        open_action.setShortcut("")
        open_action.triggered.connect(self._on_open_recent)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        open_action = QAction("Save File", self)
        open_action.setShortcut("Ctrl + S")
        open_action.triggered.connect(self._on_save_file)
        file_menu.addAction(open_action)

        open_action = QAction("Save File As", self)
        open_action.setShortcut("Ctrl + S")
        open_action.triggered.connect(self._on_save_file_as)
        file_menu.addAction(open_action)

        # Menu Editar
        edit_menu = self.menuBar()
        
        # Menu Ferramentas
        tools_menu = self.menuBar()
        
        # Menu Sobre
        about_menu = self.menubar()

    def _setup_toolbar(self, layout):
        return self, layout   
    
    def _apply_style(self):
        return self

    def _on_open_file():
        """Ação ao selecionar abrir um ficheiro"""
        return None
    
    def _on_open_recent():
        return None
    
    def _on_save_file():
        return None
    
    def _on_save_file_as():
        return None
    
    def _on_validate(self):
        return self

    def _on_convert(self):
        return self
    
    def _on_clear(self):
        return self
    
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Quit",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())