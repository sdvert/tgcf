import streamlit as st

from tgcf.web_ui.utils import hide_st, switch_theme
from tgcf.config import read_config

CONFIG = read_config()

st.set_page_config(
    page_title="Inicío",
    page_icon="👋",
)
hide_st(st)
switch_theme(st,CONFIG)
st.write("# Bem vindo ao Robô de repasse do Telegram (JV.BOTS) 👋")

html = """
<p align="center">
<img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120>
</p>
"""

st.components.v1.html(html, width=None, height=None, scrolling=False)
with st.expander("Features"):
    st.markdown(
        """
    Essa é a ferramenta definitiva para automatizar o encaminhamento personalizado de mensagens do telegram.

    Os principais recursos são:

    - Encaminhe mensagens ou envie uma cópia das mensagens dos bate-papos de origem para destino. Uma mensagem pode ser enviada com qualquer coisa: para um grupo, canal, pessoa ou até outro bot.

    - Suporta dois modos de operação passado ou ativo. O modo anterior trata de todas as mensagens existentes, enquanto o modo ao vivo é para as próximas.
    
    - Você pode fazer login com um bot ou uma conta de usuário. O Telegram impõe certas limitações às contas de bot. Você pode usar uma conta de usuário para realizar os encaminhamentos, se desejar.

    - Execute manipulação personalizada em mensagens. Você pode filtrar, formatar, substituir, colocar marca d'água, ocr e fazer o que mais precisar!

    - Wiki detalhado + tutorial em vídeo. 

    - Se você é um desenvolvedor python, escrever plugins para tgcf é como roubar doce de um bebê. Os plug-ins modificam a mensagem antes de serem enviadas ao chat de destino.

    Confira nosso canal no youtube: https://www.youtube.com/channel/UCuK62MxQZFulRALHMq6hS9w

        """
    )

st.warning("Please press Save after changing any config.")
