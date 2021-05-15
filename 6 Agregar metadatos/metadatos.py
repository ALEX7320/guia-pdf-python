from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()


# TEXTO
pdf.set_font('Arial', '', 15)

pdf.cell(w = 0, h = 15, txt = 'Hola mundo', border = 1, ln = 1,
         align = 'C', fill = 0)

pdf.cell(w = 0, h = 15, txt = 'Hola mundo', border = 1, ln = 2,
         align = 'C', fill = 0)



# METADATOS

# titulo
pdf.set_title(title = 'Hoja metadatos')

# autor
pdf.set_author(author = 'ALEX7320')

# creador
pdf.set_creator('Kodexam')

# palabras clave
pdf.set_keywords(keywords = 'Hoja, PDF, Prueba')

# asunto
pdf.set_subject(subject = 'Prueba de metadatos en PDF')


pdf.output('hoja.pdf')
