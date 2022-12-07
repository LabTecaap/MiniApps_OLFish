import streamlit as st
import auxiliar as aux

st.title('OL FISH 🎣')
st.subheader('Despescou, vendeu! 😉')
st.text('Seja bem vindo (a) a nossa plataforma de compra e venda de peixes!')

tab = aux.carregar_dados('docc.csv')

cliente = st.text_input('Digite seu nome:')
especie = st.text_input('Digite a espécie:')
kg = st.number_input('Digite a quantidade de kg:')
valor = st.number_input('Digite o preço do kg:')
contato = st.number_input('Digite seu contato:', step=1)
localizacao = st.text_input('Digite sua localização:')
descricao = st.text_input('Descrição')


  
dados = {'Cliente': [cliente], 
         'Especie': [especie],
         'Kg': [kg],
         'Preco': [valor],
         'Contato': [f'<a href="https://api.whatsapp.com/send?phone=55{contato}">WhatsApp</a>'],
         'Localizacao': [localizacao],
         'Descricao': [descricao],
        }

if st.button('Cadastrar'):
    st.write(aux.inserir_dados('docc.csv',dados)),
    st.write(f' {cliente}, você foi cadastrado em nossa plataforma.')

esp = st.text_input('Qual a espécie você procura?')

if st.button('Pesquisar'):
    tab_show = tab.loc[tab['ESPECIE']== esp]
    st.write(tab_show.to_html(escape=False, index=False), unsafe_allow_html=True) 
