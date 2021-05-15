from fpdf import FPDF

'''
P : portrait (vertical)
L : landscape (horizontal)

A4 : 210x297mm
'''

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()


pdf.output('hoja.pdf')
