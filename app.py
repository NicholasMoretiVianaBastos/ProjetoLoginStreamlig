import streamlit as st
import time
from controllers.load_usuarios import load_usuarios  
from components.cadastro import cadastrar_aluno

st.set_page_config("Sistema de Casdastro", layout="wide")

st.title("Projeto streamlit")

if "email" not in st.session_state:
    st.session_state.email = None

if "nome" not in st.session_state:
    st.session_state.nome = None

if "contador" not in st.session_state:
    st.session_state.contador = 0

def login():
    usuarios = load_usuarios()
    email = st.text_input("Email", placeholder="Email")
    senha = st.text_input("Senha", placeholder="senha", type="password")
    login = st.button("login")

    if login:
        for user in usuarios:
            if user["email"] == email and user["senha"] == senha:
                st.session_state.email = user["email"]
                st.session_state.nome = user["nome"]
                st.success("login efetuado com sucesso!")
                time.sleep(3)
                st.rerun()
        else:
            st.error("Email ou senha incorretos")

def logout():
    if st.button("Logout"):
        st.session_state.clear()
        st.success("Finalizando o Sistema")
        time.sleep(3)

def main_page():
    tabs = st.tabs(["Dashboard", "Cadastro", "Logout"])
    nome = st.session_state.nome

    with tabs[0]:
        st.subheader("Dashboard")
        st.write(f"**Usuario Logado:** {nome}")

    with tabs[1]:
        st.subheader("Cadastro")
        if st.button("Abrir formulario de cadastro"):
            cadastrar_aluno()

    with tabs[2]:
        st.subheader("Logout")
        logout()
   
  
if st.session_state.email:
    main_page()
else:
    login()

# if st.button("Adicionar"):
#     st.session_state.contador += 1

# if st.button("Diminuir"):
#     if st.session_state.contador > 0:
#         st.session_state.contador -= 1

# st.write(st.session_state)