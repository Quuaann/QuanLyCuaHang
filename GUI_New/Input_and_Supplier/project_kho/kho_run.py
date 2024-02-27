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
        uic.loadUi("project_kho/UI/warehouse.ui", self)
        self.show()
        self.pdf_btn.clicked.connect(self.pdf_btn_handler)
        
    def pdf_btn_handler(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if filename:
            self.create_pdf(filename, self.table_pdf)  # Pass the table widget reference here

    def create_pdf(self, filename, table_widget):
        table_content = self.get_table_content(table_widget)
        if table_content:
            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []

            # Title
            title_style = getSampleStyleSheet()["Title"]
            title_text = Paragraph("Table Content", title_style)
            elements.append(title_text)

            # Date and time
            datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            datetime_text = Paragraph(f"Exported on: {datetime_str}", title_style)
            elements.append(datetime_text)

            # Who exported the table (You can replace "Your Name" with the actual name)
            exporter_text = Paragraph("Exported by: Your Name", title_style)
            elements.append(exporter_text)

            # Line separating table rows
            table_style = TableStyle([('LINEABOVE', (0, 0), (-1, -1), 1, colors.black)])
            table = Table(table_content)
            table.setStyle(table_style)
            elements.append(table)

            doc.build(elements)
            print("PDF created successfully.")
        else:
            print("Table is empty.")

    def get_table_content(self, table_widget):
        table_content = []
        # Get headers
        header_row = []
        for column in range(table_widget.columnCount()):
            item = table_widget.horizontalHeaderItem(column)
            if item is not None:
                header_row.append(item.text())
            else:
                header_row.append("")
        table_content.append(header_row)

        # Get table content
        for row in range(table_widget.rowCount()):
            row_data = []
            for column in range(table_widget.columnCount()):
                item = table_widget.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            table_content.append(row_data)
        return table_content
        
        
 
        
if __name__ == "__main__":
    app = QApplication([])
    ui = Project()
    sys.exit(app.exec_())