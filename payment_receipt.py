# Import necessary modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf():
    # Base document template size A4
    doc = SimpleDocTemplate("receipt.pdf", pagesize=A4)
    elements = []  # Define elements inside the function

    # Standard stylesheet
    styles = getSampleStyleSheet()

    # Style for the top-level heading (Heading1)
    title_style = styles["Heading1"]
    title_style.alignment = 1  # 0: left, 1: center, 2: right

    # Add the title
    title = Paragraph("Acme Limited", title_style)
    elements.append(title)

    # Define table data (Correctly placed here)
    data = [
        ["Date", "Name", "Price(ksh.)"],
        ["16/11/2020", "Kasuku Notebook 96 Pages", "200/-"],
        ["16/11/2020", "Ballpoint Pen Black", "500/-"],
        ["Discount", "", "-"],
        ["Total", "", "700/-"],
    ]

    # Create the table
    table = Table(data)

    # Define table style
    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )
    table.setStyle(style)

    # Add the table to elements
    elements.append(table)

    # Build the document
    doc.build(elements)

# Ensure the script runs correctly
if __name__ == "__main__":
    create_pdf()
