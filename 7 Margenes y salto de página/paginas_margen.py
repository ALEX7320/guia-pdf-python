from fpdf import FPDF


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 


pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 16)

pdf.cell(w = 0, h = 15, txt = 'Hola mundo', border = 1,
         align = 'C', fill = 0)


pdf.add_page() #---------------------------------------

pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1,
         align = 'C', fill = 0)

pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1,
         align = 'C', fill = 0)
pdf.multi_cell(w = 0, h = 15, txt = 'Hola mundo', border = 1,
         align = 'C', fill = 0)

pdf.output('hoja.pdf')
