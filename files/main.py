import webbrowser

from fpdf import FPDF
import os
import webbrowser


class Bill:
    """
    Object that contains data about a Bill, such as
    total amount and period of Bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        return bill.amount * self.days_in_house / (self.days_in_house + flatmate2.days_in_house)


class PdfReport:
    """
    Creates a report in pdf format detailing how much each
    flatmate has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', format='A4', unit='pt')
        pdf.add_page()

        # Add icon
        pdf.image('bills.jpeg', w=50, h=60)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=80, h=40, txt="Period", border=0)
        pdf.cell(w=80, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=80, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=80, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=80, h=30, txt=flatmate2.name, border=0)
        pdf.cell(w=80, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0)

        pdf.output(self.filename)
        # You will have to provide the full path of the file in Mac and Linux.
        # Whereas in Windows - webbrowser.open(self.filename) would work fine.
        webbrowser.open('file://' + os.path.realpath(self.filename))


the_bill = Bill(120, "July 2022")
kushi = Flatmates("kushi", 25)
praveen = Flatmates("praveen", 27)
print(kushi.pays(the_bill, praveen), praveen.pays(the_bill, kushi),
      kushi.pays(the_bill, praveen) + praveen.pays(the_bill, kushi))
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(kushi, praveen, the_bill)
