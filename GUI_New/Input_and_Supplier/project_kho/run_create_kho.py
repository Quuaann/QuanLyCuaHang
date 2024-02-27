import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction,QFileDialog
from PyQt5 import uic
from PyQt5.QtCore import QFileInfo
from reportlab.pdfgen import canvas
from PyQt5.QtWidgets import QFileDialog
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
class Project(QMainWindow):
    
    def __init__(self):
        super( ).__init__()
        uic.loadUi("project_kho/UI/create_kho.ui", self)
        self.show()
        
    
        
 
        
if __name__ == "__main__":
    app = QApplication([])
    ui = Project()
    sys.exit(app.exec_())