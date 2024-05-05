import streamlit as st
from src.services.IronyDetector import IronyDetector


@st.cache_data
def get_model():
    detector = IronyDetector()
    detector.init()
    return detector


def show():
    st.title("Здесь вы можете определить иронично ли вам ответили или нет ;)")
    text_to_detect = st.text_area(
        label="Итак, что же вам такого написали? (Желательно на англ)",
        placeholder="Введите текст",
        key="text_to_detect",
    )
    btn = st.button("Определить", type="primary")

    if btn and text_to_detect:
        model = get_model()
        rslt = model.analyze(text_to_detect)
        label_map = {
            "irony": "(: Вам ответили иронично:  ",
            "non-irony": "Вполне серьезный комментарий:  ",
        }

        for key in rslt:
            st.write(f"{label_map[key]} {rslt[key] * 100}%")
