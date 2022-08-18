import os
import webbrowser as w

from fpdf import FPDF
from filestack import Client


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
        pdf.image("/Users/praveen/Documents/PycharmProjects/PythonProCourses/App-2-Flatmates-Bill/files/bills.jpeg",
                  w=50, h=60)

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
        pdf.cell(w=80, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0)

        os.chdir("/Users/praveen/Documents/PycharmProjects/PythonProCourses/App-2-Flatmates-Bill/files/")

        pdf.output(self.filename)
        # You will have to provide the full path of the file in Mac and Linux.
        # Whereas in Windows - webbrowser.open(self.filename) would work fine.
        w.open('file://' + os.path.realpath(self.filename))


class FileSharer:

    def __init__(self, filepath, apikey="ABbXmMQ2DRLGwfCWVAvuZz"):
        self.filepath = filepath
        self.apikey = apikey

    def share(self):
        client = Client(self.apikey)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
