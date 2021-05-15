from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        # Logo
        self.image('logo.png', x = 10, y = 10, w = 15, h = 15)

        # Arial bold 25
        self.set_font('Arial', 'B', 25)

        # Title
        self.cell(w = 0, h = 15, txt = 'Encabezado', border = 1, ln=1,
                align = 'C', fill = 0)   

        # Line break
        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}', border = 1,
                align = 'C', fill = 0)   

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()

pdf.add_page()

pdf.set_font('Arial', '', 12)

for i in range(80):

    pdf.cell(w = 0, h = 10, txt = 'Texto', border = 1, ln=1,
            align = 'C', fill = 0)


pdf.output('hoja.pdf', 'F')