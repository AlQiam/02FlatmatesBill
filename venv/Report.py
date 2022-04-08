import webbrowser

from fpdf import FPDF


class PdfReport:
    """    Create a PDF file that containing data about the flatmates such as
    their names, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, flatmates_usd, the_bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')  # 'P' = Portrait mode
        pdf.add_page(orientation='')

        # Add Icon
        pdf.image(name='Other Files\\house.png', w=55, h=55)
        # The orientation is the same as that when the object was instantiated

        # Add Company Name
        pdf.set_font(family='Times', size=30, style='B')
        pdf.cell(w=0, h=60, txt='Irbid District Electricity Company', ln=1,
                 align='C', border=0)
        # Add Title
        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=0, h=60, txt='Flatmates Bill', border=0, align='C', ln=1)
        # if w = 0, then the cell will take the entire horizontal length of that line

        # Add Period
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=70, h=40, txt='Period:', border=0)
        pdf.cell(w=110, h=40, txt=the_bill.period, border=0, ln=1)
        pdf.cell(w=160, h=40, txt='The Individual Bill', border=0, ln=1)

        # Add the USD each flatmate should pay
        pdf.set_font(family='Times', size=14, style='BI')
        for line in range(0, len(flatmates)):
            pdf.cell(w=100, h=25, ln=1, border=0,
                     txt=f'{flatmates[line].name}: {flatmates_usd[line]}$')
        pdf.output(self.filename)
        webbrowser.open(self.filename)

from filestack import Client

class FileSharer:

    def __init__(self, filename, api_key='A5UGt0qSwQN2Z6fsFfZ5Tz'):
        # create a free account on filestack.com and copy your API
        # and replace my API with yours
        self.filename = filename
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filename)
        return new_filelink.url