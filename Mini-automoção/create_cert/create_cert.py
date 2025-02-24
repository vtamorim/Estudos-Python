from fpdf import FPDF
import pandas as pd

dados = pd.read_csv("create_cert/dados.csv")
#print(dados['nomecompleto'])

# Dados do certificado
titulo =    "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que"
nome = "Alexandre Sauer"
texto2 = "concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
texto3 = " PROF. SAUER entre 23/08/2024 e 28/08/2024,"
texto4 = "com carga horária de aproximadamente 08 horas."


for nome in dados['nomecompleto']:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=15)
    pdf.image("create_cert/template.png", x=0, y=0)
    pdf.set_text_color(33, 24, 136)
    # Adicionar o texto
    # Note que as coordenadas para o texto podem precisar ser ajustadas
    pdf.text(65, 95, titulo)
    pdf.text(67, 120, subtitulo)

    pdf.text(70, 145, nome)
    pdf.text(20, 165, texto2)
    pdf.text(50, 175, texto3)
    pdf.text(50, 185, texto4)

    # Salvar o PDF com um nome de arquivo único
    pdf.output(f"Certificado_{nome}.pdf")