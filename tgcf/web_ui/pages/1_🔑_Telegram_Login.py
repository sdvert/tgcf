import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Telegram Login",
    page_icon="🔑",
)
hide_st(st)
switch_theme(st,CONFIG)
if check_password(st):
    CONFIG.login.API_ID = int(
        st.text_input("API ID", value=str(CONFIG.login.API_ID), type="password")
    )
    CONFIG.login.API_HASH = st.text_input(
        "API HASH", value=CONFIG.login.API_HASH, type="password"
    )
    st.write("You can get api id and api hash from https://my.telegram.org.")

    user_type = st.radio(
        "Choose account type", ["Bot", "User"], index=CONFIG.login.user_type
    )
    if user_type == "Bot":
        CONFIG.login.user_type = 0
        CONFIG.login.BOT_TOKEN = st.text_input(
            "Enter bot token", value=CONFIG.login.BOT_TOKEN, type="password"
        )
    else:
        CONFIG.login.user_type = 1
        CONFIG.login.SESSION_STRING = st.text_input(
            "Enter session string", value=CONFIG.login.SESSION_STRING, type="password"
        )
        with st.expander("How to get session string ?"):
            st.markdown(
                """

            Entre com sua conta em: https://t.me/SessionStringsBot

            Clique em /start ou digite /start

            Depois: Clique no botão Telethon

            Depois: Digite as credenciais conforme o bot for solicitando (api ID primeiro, depois HASH, depois seu número de telefone)

            Irá chegar um código no telegram, e você deverá digitar ele conforme o bot solicita.

            Quando ele gerar com sucesso, irá aparecer um botão com o nome SAVED MESSAGES. Digite isso na barra de busca do telegram.

            Você encontrará uma mensagem salva com a sessão string. Copie ela e traga até o site.
            Dúvidas? meu contato: https://api.whatsapp.com/send?phone=5584998493595
            """
            )

    if st.button("Save"):
        write_config(CONFIG)
