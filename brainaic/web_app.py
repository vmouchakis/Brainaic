import streamlit as st
from brainaic.bot import Bot
from brainaic.config import DATA_PATH
import os


def main():
    st.set_page_config(page_title="LeGo", page_icon="🤖", layout="wide", )

    model = st.selectbox("What is the model of your choice?",
                         ("gpt", "llama"),
                         index=None)

    filenames = os.listdir(DATA_PATH)
    selected_filename = st.selectbox('Select a directory',
                                     filenames,
                                     index=None)

    path = None
    if model is not None and selected_filename is not None:
        path = os.path.join(DATA_PATH, selected_filename)
        st.write('Selected path:', path)

    question = st.text_input("What do you want to know?")

    if question:
        bot = Bot(data_path=path, model_name=model)
        ans = bot.get_response(question)
        print(ans)
        st.write(ans)


if __name__ == "__main__":
    main()
