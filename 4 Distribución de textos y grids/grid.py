texto = '''Lorem ipsum dolor sit amet consectetur, adipiscing elit ornare mollis feugiat natoque, tortor facilisis torquent mauris. Eleifend quis condimentum conubia auctor urna metus neque eget suspendisse, dictumst sagittis quisque gravida natoque nunc phasellus molestie tellus, donec platea dis pretium ad laoreet erat ornare. Tortor etiam varius class neque posuere eleifend mus risus donec, dis suspendisse aenean quam accumsan lectus ligula fermentum, a leo vel sociosqu pulvinar bibendum nunc sociis.

Dignissim vel massa faucibus senectus integer habitasse facilisi, consequat sem condimentum curae ut egestas lacus semper, sapien gravida platea tortor sagittis mattis. Aliquam lacus fusce ante laoreet mattis lobortis vestibulum a magnis, lectus feugiat est mi gravida dapibus tristique etiam orci nisi, rutrum pharetra elementum donec quam congue habitasse egestas. Habitasse congue torquent nascetur suscipit hendrerit sapien vivamus ante habitant senectus blandit, odio eget non etiam nibh ultricies dis nam elementum.''' 



from fpdf import FPDF


pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()


# TEXTO
pdf.set_font('Arial', '', 16)


'''
Border

0 = no | 1 = Si | T = ↑ | B = ↓ |L = ← |R = →

Align

C = centro |L = ← |R = →
'''


# Margen 1
pdf.cell(w = 50, h = 15, txt = 'Git', border = 1, 
         align = 'C', fill = 0)

pdf.cell(w = 30, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.cell(w = 20, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.multi_cell(w = 0, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

# Margen 2
pdf.cell(w = 50, h = 15, txt = 'Git', border = 1, 
         align = 'C', fill = 0)

pdf.cell(w = 30, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.cell(w = 50, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.multi_cell(w = 0, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

# Margen 3
pdf.cell(w = 50, h = 15, txt = 'Git', border = 1, 
         align = 'C', fill = 0)

pdf.cell(w = 30, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.cell(w = 50, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)

pdf.multi_cell(w = 0, h = 15, txt = 'Perfil', border = 1,
         align = 'C', fill = 0)


# texto
pdf.multi_cell(w = 0, h = 10, txt = texto, border = 1,
         align = 'L', fill = 0)

pdf.output('hoja.pdf')

