from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()

# TEXTO  -----

pdf.set_font('Arial','',18)

pdf.text(x= 60, y= 50, txt='Hola mundo 2')
pdf.text(x= 60, y= 60, txt='Hola mundo 2')


# IMAGEN (jpg/png) -----

url = 'https://github.com/ALEX7320'

pdf.image('logo.png',
        x= 50, y= 120,
        w = 60, h = 60,
        link = url)


pdf.output('hoja.pdf')
