# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *

#url da imagem no GitHub 
img_url = https://github.com/RenanCarvalho21/webapp00/blob/main/Materiais%20Eletricos%20Foto.jpg?raw=true

#Exibe a imagem 
st.image(img_url, caption="Minha Imagem", use_column_width=True)

from fpdf import FPDF
import datetime

# Função para calcular o valor do serviço
def calcular_valor_servico(tipo_servico):
    servicos = {
        0: 500 + 250,  # Fusível para Transformadores + Base
        1: 1000,       # Fusível Ação Lenta
        2: 2000,       # Fusível ação Rápida
        3: 500 + 1000, # Fusível Ação Ultra-rápida
        4: 500 + 2000  # Fusível Média Tensão + Chave Seccionadora
    }
    return servicos.get(tipo_servico, 0)  # Caso o tipo não esteja no dicionário, retorna 0

# Função para gerar o PDF da Ordem de Serviço
def gerar_pdf(nome_cliente, numero_cliente, marca_fusivel, descricao_fusivel, tipo_servico, como_era, como_ficara, valor_total):
    tipo_servico_str = ["Fusível para Transformadores + Base", 
                        "Fusível Ação Lenta", 
                        "Fusível Ação Rápida", 
                        "Fusível Ação Ultra-rápida + Base", 
                        "Fusível Média Tensão + Chave Seccionadora"][tipo_servico]
    
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
    pdf.cell(200, 10, txt=f"Marca do Fusível: {marca_fusivel}", ln=True)
    pdf.cell(200, 10, txt=f"Corrente e Tensão Descrita pelo fabricante: {descricao_fusivel}", ln=True)
    pdf.cell(200, 10, txt=f"Serviço Selecionado: {tipo_servico_str}", ln=True)
    pdf.cell(200, 10, txt=f"Qual fusível está instalado?: {como_era}", ln=True)
    pdf.cell(200, 10, txt=f"Qual será a nova instalação?: {como_ficara}", ln=True)
    pdf.cell(200, 10, txt=f"Total do Serviço: R${valor_total}", ln=True)
    
    # Salvar o PDF em um arquivo
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_output_path = f"OS_{numero_cliente}_{descricao_fusivel}_{data_atual}.pdf"
    pdf.output(pdf_output_path)
    
    return pdf_output_path

# Função principal da interface Streamlit
def main():
    # Título da aplicação
    st.title("Ordem de Serviço - Materiais Elétricos")
    
    # Formulário para preencher os dados da OS
    st.header("Preencha os dados da Ordem de Serviço")
    
    # Campos de entrada para os dados do cliente e do fusível
    nome_cliente = st.text_input("Nome do Cliente")
    numero_cliente = st.number_input("Número do Cliente", min_value=1)
    marca_fusivel = st.text_input("Marca do fusível")
    descricao_fusivel = st.number_input("Corrente e Tensão Descrita pelo fabricante", min_value=1)
    
    # Seleção do serviço
    tipo_servico = st.radio("Escolha o Serviço", 
                            options=["Fusível para Transformadores + Base", 
                                     "Fusível Ação Lenta", 
                                     "Fusível Ação Rápida", 
                                     "Fusível Ação Ultra-rápida + Base", 
                                     "Fusível Média Tensão + Chave Seccionadora"])
    
    # Definindo qual fusível o cliente tem e qual ele precisa trocar
    como_era = st.text_area("Qual fusível está instalado?")
    como_ficara = st.text_area("Qual será a nova instalação?")
    
    # Calcular o valor do serviço
    tipo_servico_num = ["Fusível para Transformadores + Base", 
                        "Fusível Ação Lenta", 
                        "Fusível Ação Rápida", 
                        "Fusível Ação Ultra-rápida + Base", 
                        "Fusível Média Tensão + Chave Seccionadora"].index(tipo_servico)
    
    valor_total = calcular_valor_servico(tipo_servico_num)
    
    if st.button("Gerar Ordem de Serviço"):
        if nome_cliente and numero_cliente and marca_fusivel and descricao_fusivel:
            # Exibir o resumo da ordem de serviço
            st.subheader("Resumo da Ordem de Serviço")
            st.write(f"Cliente: {nome_cliente}")
            st.write(f"Número do Cliente: {numero_cliente}")
            st.write(f"Marca do Fusível: {marca_fusivel}")
            st.write(f"Corrente e Tensão Descrita pelo fabricante: {descricao_fusivel}")
            st.write(f"Serviço Selecionado: {tipo_servico}")
            st.write(f"Qual fusível está instalado?: {como_era}")
            st.write(f"Qual será a nova instalação?: {como_ficara}")
            st.write(f"Total do Serviço: R${valor_total}")
            
            # Gerar o PDF da Ordem de Serviço
            pdf_path = gerar_pdf(nome_cliente, numero_cliente, marca_fusivel, descricao_fusivel, tipo_servico_num, como_era, como_ficara, valor_total)
            
            # Adicionar botão para download do PDF
            with open(pdf_path, "rb") as file:
                st.download_button(label="Baixar Ordem de Serviço (PDF)", data=file, file_name=pdf_path)
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")

# Executando a aplicação
if __name__ == "__main__":
    main()
