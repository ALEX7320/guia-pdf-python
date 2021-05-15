from fpdf import FPDF
from referencias import *


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()

'''
Fuentes disponibles de FPDF:

Courier
Helvetica
Arial
Times
Symbol
ZapfDingbats
'''

# FONTS
pdf.set_font('Arial', '', 25)

pdf.add_font(family = 'Karmatic Arcade', style='', 
               fname= 'fuentes/ka1.ttf', uni=True)

tfont(pdf,'','Karmatic Arcade')

pdf.cell(w = 0, h = 15, txt = 'Texto de pueba', border = 1, ln=2,
         align = 'C', fill = 0)


pdf.cell(w = 0, h = 15, txt = 'Times', border = 1, ln=2,
         align = 'C', fill = 0)


pdf.output('hoja.pdf')
