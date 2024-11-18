import streamlit as st
from fpdf import FPDF
import datetime

# Função para calcular o valor do serviço
def calcular_valor_servico(tipo_servico):
    servicos = {0: 500 + 250,  # Reparo de Carburetor + Retoque
        1: 1000,       # Pintura Simples
        2: 2000,       # Pintura Complexa
        3: 500 + 1000, # Reparo de Carburetor + Pintura Simples
        4: 500 + 2000  # Reparo de Carburetor + Pintura Complexa}
    return servicos.get(tipo_servico, 0)  # Caso o tipo não esteja no dicionário, retorna 0

# Função para gerar o PDF da Ordem de Serviço
def gerar_pdf(nome_cliente, numero_cliente, marca_bike, numero_bike, tipo_servico, como_era, como_ficara, valor_total):
    tipo_servico_str = ["Reparo de Carburetor + Retoque","Pintura Simples","Pintura Complexa","Reparo de Carburetor + Pintura Simples","Reparo de Carburetor + Pintura Complexa" ][tipo_servico]
    
    # Criar o objeto PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Definir a fonte
    pdf.set_font("Arial", size=12)
    
    # Título
    pdf.cell(200, 10, txt="Ordem de Serviço", ln=True, align="C")
    pdf.ln(10)
    
    # Informações do cliente e serviço
    pdf.cell(200, 10, txt=f"Cliente: {nome_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Número do Cliente: {numero_cliente}", ln=True)
    pdf.cell(200, 10, txt=f"Marca da Bicicleta: {marca_bike}", ln=True)
    pdf.cell(200, 10, txt=f"Número de Série: {numero_bike}", ln=True)
    pdf.cell(200, 10, txt=f"Serviço Selecionado: {tipo_servico_str}", ln=True)
    pdf.cell(200, 10, txt=f"Descrição Original: {como_era}", ln=True)
    pdf.cell(200, 10, txt=f"Personalização: {como_ficara}", ln=True)
    pdf.cell(200, 10, txt=f"Total do Serviço: R${valor_total}", ln=True)
    
    # Salvar o PDF em um arquivo
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_output_path = f"OS_{numero_cliente}_{numero_bike}_{data_atual}.pdf"
    pdf.output(pdf_output_path)
    
    return
