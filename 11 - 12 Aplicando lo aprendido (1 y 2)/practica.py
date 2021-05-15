from fpdf import FPDF

from referencias import *

class PDF(FPDF):

    def header(self):
        self.image('logo.png',
                x = 10, y = 10, w = 30, h = 30)

        self.set_font('Arial', '', 15)

        tcol_set(self, 'blue')
        tfont_size(self,45)
        tfont(self,'B')
        self.cell(w = 0, h = 20, txt = 'Reporte', border = 0, ln=1,
                align = 'C', fill = 0)

        tfont_size(self,10)
        tcol_set(self, 'black')
        tfont(self,'I')
        self.cell(w = 0, h = 10, txt = 'Generado el 2020/11/25', border = 0, ln=2,
                align = 'C', fill = 0)

        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
                 border = 0,
                align = 'C', fill = 0)   



lista_datos = (
    (1, 'Carlos', 'carlos@gmail.com', '2020-02-25'),
    (2, 'Jose', 'jose@gmail.com', '2019-03-12'),
    (3, 'Marcos', 'marcos@gmail.com', '2018-01-31'),
    (4, 'Luz', 'luz@gmail.com', '2017-02-15'),
    (5, 'Elmer', 'elmer@gmail.com', '2016-11-23'),
)#*8


pdf = PDF(orientation = 'P', unit = 'mm', format='A4') 
pdf.alias_nb_pages()

pdf.add_page()

# TEXTO
pdf.set_font('Arial', '', 15) 


# 1er encabezado ----

bcol_set(pdf, 'green')
tfont_size(pdf,15)
tfont(pdf,'B')
pdf.multi_cell(w = 0, h = 15, txt = 'Gerente', border = 0,
         align = 'C', fill = 1)
tfont(pdf,'')


h_sep = 15
pdf.ln(3)
tfont_size(pdf,12)

# fila 1 --

tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Nombre:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')         
pdf.cell(w = 45, h = h_sep, txt = 'Alex', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Correo:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black') 
pdf.multi_cell(w = 0, h = h_sep, txt = 'alex7320k@gmail.com', border = 0,
         align = 'L', fill = 0)


# fila 2 --
tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Apellido:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.cell(w = 45, h = h_sep, txt = 'Chuquillanqui', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Fecha de contrato:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.multi_cell(w = 0, h = h_sep, txt = '2019/09/11', border = 0,
         align = 'L', fill = 0)

# fila 3 --
tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Residencia:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.cell(w = 45, h = h_sep, txt = 'av. Python - calle 3', border = 0,
         align = 'L', fill = 0)

tcol_set(pdf, 'gray')
pdf.cell(w = 45, h = h_sep, txt = 'Estado actividad:', border = 0, 
         align = 'R', fill = 0)

tcol_set(pdf, 'black')
pdf.multi_cell(w = 0, h = h_sep, txt = 'Retirado', border = 0,
         align = 'L', fill = 0)




pdf.ln(15)
# tabla ----

bcol_set(pdf, 'green')
tfont_size(pdf,15)
tfont(pdf,'B')
pdf.cell(w = 0, h = 15, txt = 'Delegados', border = 0,ln = 2, align = 'C', fill = 1)
tfont(pdf,'')

tfont_size(pdf,13)
bcol_set(pdf, 'blue')

pdf.cell(w = 20, h = 10, txt = 'ID', border = 0, align = 'C', fill = 1)
pdf.cell(w = 40, h = 10, txt = 'Nombre', border = 0, align = 'C', fill = 1)
pdf.cell(w = 70, h = 10, txt = 'Correo', border = 0, align = 'C', fill = 1)
pdf.multi_cell(w = 0, h = 10, txt = 'Fecha contrato', border = 0, align = 'C',
             fill = 1)


tfont_size(pdf,12)
dcol_set(pdf, 'blue')
tcol_set(pdf, 'gray')
pdf.rect(x= 10, y= 60, w= 190, h= 53)
c = 0
for datos in lista_datos:

    c+=1
    if(c%2==0):bcol_set(pdf, 'gray2')
    else:bcol_set(pdf, 'white')

    pdf.cell(w = 20, h = 10, txt = str(datos[0]), border = 'TBL', align = 'C', fill = 1)
    pdf.cell(w = 40, h = 10, txt = datos[1], border = 'TB', align = 'C', fill = 1)
    pdf.cell(w = 70, h = 10, txt = datos[2], border = 'TB', align = 'C', fill = 1)
    pdf.multi_cell(w = 0, h = 10, txt = datos[3], border = 'TBR', align = 'C', fill = 1)



pdf.output('hoja.pdf')
