from fpdf import FPDF

from referencias import *


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()

'''
# texto *-*-*-*-*-*-*-*-*
set_text_color

# relleno *-*-*-*-*-*-*-*-*
set_fill_color

# trazos y bordes *-*-*-*-*-*-*-*-*
set_draw_color

# ESTILO TEXTO *-*-*-*-*-*-*-*-*
U : linea inferior
B : bold
I : recostado
'''

# TEXTO (grid)
pdf.set_font('Arial', '', 15)


bcol_set(pdf , 'red')
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=1,
         align = 'C', fill = 1)

bcol_set(pdf , 'blue')
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=2,
         align = 'C', fill = 1)


tfont_size(pdf, 30)
tcol_set(pdf , 'white')
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=2,
         align = 'C', fill = 1)
tfont_size(pdf, 15)


tfont(pdf,'B')
bcol_set(pdf , 'blue')
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=2,
         align = 'C', fill = 1)

tfont(pdf,'')
bcol_set(pdf , 'rose')
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=2,
         align = 'C', fill = 1)


# TRAZOS
dcol_set(pdf , 'green')
tcol_set(pdf , 'blue')


'''
F : fill (relleno)
D : draw (trazos, bordes y dibujado)
'''

pdf.rect(x=60, y=200, w=100, h=80, style='DF')
pdf.dashed_line(50, 150, 190, 200, dash_length = 10, space_length = 6)

pdf.text(x=150, y=150, txt='Hola mundo')


pdf.output('hoja.pdf')
