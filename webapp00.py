# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *

#url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFwxxM13bxUC0dpyd0w0PxfZIrJ-hp4Px-R6rsTiG3c3n-89JApzA0jYJpU9vNfxeNCvtJ0Cg35KtO/pub?gid=556192647&single=true&output=csv"
#db = Ler_GooglePlanilha(url)
#db.fillna('', inplace=True)
#Escrever(db)

import streamlit as st
from fpdf import FPDF
import datetime

# Função para gerar PDF
def gerar_pdf(nome_cliente, descricao_servico, data_inicio, data_fim, valor, numero_os):
    # Criação do objeto PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Definindo título e fonte
    pdf.set_font("Arial", size=12)
    
    # Cabeçalho
    pdf.cell(200, 10, txt=f'Ordem de Serviço - {numero_os}', ln=True, align="C")
    pdf.ln(10)  # Linha em branco
    
    # Detalhes da OS
    pdf.cell(200, 10, txt=f'Número da OS: {numero_os}', ln=True)
    pdf.cell(200, 10, txt=f'Cliente: {nome_cliente}', ln=True)
    pdf.cell(200, 10, txt=f'Descrição do Serviço: {descricao_servico}', ln=True)
    pdf.cell(200, 10, txt=f'Data de Início: {data_inicio}', ln=True)
    pdf.cell(200, 10, txt=f'Data de Término: {data_fim}', ln=True)
    pdf.cell(200, 10, txt=f'Valor: R${valor}', ln=True)
    
    # Salvar PDF
    pdf_output_path = f"OS_{numero_os}.pdf"
    pdf.output(pdf_output_path)
    
    return pdf_output_path

# Função principal da interface Streamlit
def main():
    # Título da aplicação
    st.title("Sistema de Ordem de Serviço")
    
    # Formulário para preencher os dados da OS
    st.header("Preencha os dados da Ordem de Serviço")
    
    # Campos do formulário
    nome_cliente = st.text_input("Nome do Cliente")
    descricao_servico = st.text_area("Descrição do Serviço")
    data_inicio = st.date_input("Data de Início")
    data_fim = st.date_input("Data de Término")
    valor = st.number_input("Valor do Serviço (R$)", min_value=0.0, format="%.2f")
    
    # Gerar número da OS (simulação simples de geração automática)
    numero_os = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    if st.button("Gerar Ordem de Serviço"):
        if nome_cliente and descricao_servico and valor > 0.0:
            # Gerar PDF da OS
            pdf_path = gerar_pdf(nome_cliente, descricao_servico, data_inicio, data_fim, valor, numero_os)
            
            # Exibir link para download do PDF
            st.success(f"Ordem de Serviço gerada com sucesso! Você pode fazer o download abaixo.")
            st.download_button(label="Baixar PDF da Ordem de Serviço", data=open(pdf_path, "rb").read(), file_name=pdf_path)
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

if __name__ == "__main__":
    main()
