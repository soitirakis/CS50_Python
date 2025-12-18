from fpdf import FPDF

class Generate:
    def __init__(self, name):
        self.name = name

        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_margin(0)
        pdf.set_font("helvetica", "B", size=45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x = 0, y=70)
        pdf.set_font_size(30)
        pdf.set_text_color(255,255,255)
        #pdf.cell(0, 60, text=f"{self.name} took CS50", align="C")
        pdf.text(x=50, y=140, text=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")


name = input("Name: ")
name = name.title()
pdf = Generate(name)
