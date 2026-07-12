import streamlit as st
from openai import OpenAI

# Inicializa o cliente da OpenAI com a sua chave de API
modelo_ia = OpenAI(api_key="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")

# Título da página
st.write("## Chatbot com IA")
st.write("#### feito pelo Samuel Rodrigues")

# Cria a lista de mensagens no histórico caso ela não exista
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Campo de entrada de texto do usuário
texto_usuario = st.chat_input("Digite sua mensagem")

# Mostra as mensagens anteriores na tela para o chat não sumir ao recarregar
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# Se o usuário digitou alguma coisa e apertou Enter
if texto_usuario:
    # 1. Mostra a mensagem do usuário na tela e salva no histórico
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    # 2. Envia todo o histórico para a OpenAI gerar a resposta
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    # 3. Pega o texto puro da resposta da IA
    texto_resposta_ia = resposta_ia.choices[0].message.content
    
    # 4. Mostra a resposta da IA na tela e salva no histórico
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)