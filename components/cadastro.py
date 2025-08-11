import streamlit as st
import re
from utils.validar_email import validar_email
from detetime import date
from controllers.alunos_controllers import select_aluno_por_email,select_aluno_por_cpf

@st.dialog("Formulario de cadastro de aluno", width=True)
def cadastrar_aluno():
    data_minima = date(1900, 1, 1)
    data_maxima = date.today()
    nome_aluno = st.text_input("Nome do Aluno", placeholder= "Nome do Aluno")
    email_aluno = st.text_input("Email do Aluno", placeholder= "Email do Aluno")
    cpf_aluno = st.text_input(
        "CPF do Aluno",
        placeholder= "CPF do Aluno",
        max_chars=11
        )
    datadenasci_aluno = st.date_input(
        "Data do Aluno",
        value=data_maxima,
        min_value=data_minima,
        max_value=data_maxima

        )
    telefone_aluno = st.text_input(
        "Telefone do Aluno",
        placeholder= "Telefone do Aluno",
        max_chars=11
        )

    cpf_aluno_numeros = re.sub(r"\D", "", cpf_aluno)
    telefone_aluno_numeros = re.sub(r"\D", "", telefone_aluno)
    email_isvalid = validar_email(email_aluno)

    colunas = st.columns(2)

    with colunas[0]:
      btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)
    
    with colunas[1]:
      btn_cancelar = st.form_submit_button("Cancelar", use_container_width=True)

    if btn_cadastrar:
        if not nome_aluno:
           return st.warning("Campo não pode ser vazio!")
        
        if not email_aluno:
           return st.warning("Campo email não pode ser vazio!")
        
        if not email_isvalid:
           return st.warning("Email invalido!")
        
        if not cpf_aluno:
           return st.warning("Campo CPF não pode ser vazio!")
        
        if len(cpf_aluno_numeros) !=11 or len(cpf_aluno_numeros) < 11:
            return st.warning("CPF invalido")
       
        if not telefone_aluno:
           return st.warning("Campo telefone não pode ser vazio!")
        
        if len(telefone_aluno_numeros) !=11 or len(telefone_aluno_numeros) < 11:
            return st.warning("Telefone invalido")

    if btn_cadastrar:
        st_rerun()