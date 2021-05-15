from fpdf import FPDF
from referencias import *


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()


# FONTS
pdf.set_font('Arial', '', 25)


# normal
pdf.add_font(family = 'Caviar Dreams', style='', 
               fname= 'fuentes2/CaviarDreams.ttf', uni=True)

# bold
pdf.add_font(family = 'Caviar Dreams', style='B', 
               fname= 'fuentes2/CaviarDreams_Bold.ttf', uni=True)

# italic
pdf.add_font(family = 'Caviar Dreams', style='I', 
               fname= 'fuentes2/CaviarDreams_Italic.ttf', uni=True)

# bold italic
pdf.add_font(family = 'Caviar Dreams', style='BI', 
               fname= 'fuentes2/CaviarDreams_BoldItalic.ttf', uni=True)



tfont(pdf,'','Caviar Dreams')


# textos ----------

pdf.cell(w = 0, h = 15, txt = 'Texto de pueba', border = 1, ln=2,
         align = 'C', fill = 0)

pdf.cell(w = 0, h = 15, txt = 'Times', border = 1, ln=2,
         align = 'C', fill = 0)


pdf.output('hoja.pdf')
