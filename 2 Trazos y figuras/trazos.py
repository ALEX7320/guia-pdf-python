from fpdf import FPDF


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()

# RECTA 
pdf.rect(x= 90, y= 80, w= 50, h= 50)

# LINEA
#_________x1__y1___x2__y2_
pdf.line(50, 150, 190, 200)

# LINEA ENTRECORTADA
#________________x1__y1_x2_y2_
pdf.dashed_line(15, 78, 80, 90, dash_length = 10, space_length = 6)

# ELIPSE
pdf.ellipse(x=10, y=15, w=100, h=80)


pdf.output('hoja.pdf')
