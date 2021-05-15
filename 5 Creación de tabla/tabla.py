from fpdf import FPDF

# datos para usar
lista_datos = (
    (1, 'Carlos', 'carlos@gmail.com', '2020-02-25'),
    (2, 'Jose', 'jose@gmail.com', '2019-03-12'),
    (3, 'Marcos', 'marcos@gmail.com', '2018-01-31'),
    (4, 'Luz', 'luz@gmail.com', '2017-02-15'),
    (5, 'Elmer', 'elmer@gmail.com', '2016-11-23'),
    )*8

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 15)

# titulo
pdf.cell(w = 0, h = 15, txt = 'Reporte', border = 1, ln=1,
         align = 'C', fill = 0)

# encabezado
pdf.cell(w = 20, h = 15, txt = 'ID', border = 1,
         align = 'C', fill = 0)

pdf.cell(w = 40, h = 15, txt = 'Nombre', border = 1,
         align = 'C', fill = 0)

pdf.cell(w = 70, h = 15, txt = 'Correo', border = 1,
         align = 'C', fill = 0)

pdf.multi_cell(w = 0, h = 15, txt = 'Fecha de contrato', border = 1,
         align = 'C', fill = 0)


# valores
for valor in lista_datos:

    pdf.cell(w = 20, h = 9, txt = str(valor[0]), border = 1,
            align = 'C', fill = 0)

    pdf.cell(w = 40, h = 9, txt = valor[1], border = 1,
            align = 'C', fill = 0)

    pdf.cell(w = 70, h = 9, txt = valor[2], border = 1,
            align = 'C', fill = 0)

    pdf.multi_cell(w = 0, h = 9, txt = valor[3], border = 1,
            align = 'C', fill = 0)


pdf.output('hoja.pdf')
