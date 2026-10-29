import streamlit as st

st.title("Conversión de temperatura en tiempo real")


if "celsius" not in st.session_state:
    st.session_state.celsius = 0.0
    st.session_state.fahrenheit = 32.0
    st.session_state.kelvin = 273.15
    st.session_state.rankine = 491.67

def actualizar_valores(origen):
    if origen == "celsius":
        c = st.session_state.celsius
    elif origen == "fahrenheit":
        c = (st.session_state.fahrenheit - 32) / 1.8
    elif origen == "kelvin":
        c = st.session_state.kelvin - 273.15
    elif origen == "rankine":
        c = (st.session_state.rankine - 491.67) / 1.8

    st.session_state.celsius = c
    st.session_state.fahrenheit = (c * 1.8) + 32
    st.session_state.kelvin = c + 273.15
    st.session_state.rankine = (c + 273.15) * 1.8


st.number_input(
    "Celsius (°C):",
    key="celsius",
    on_change=actualizar_valores,
    args=("celsius",),
    format="%.2f"
)

st.number_input(
    "Kelvin (K):",
    key="kelvin",
    on_change=actualizar_valores,
    args=("kelvin",),
    format="%.2f"
)

st.number_input(
    "Fahrenheit (°F):",
    key="fahrenheit",
    on_change=actualizar_valores,
    args=("fahrenheit",),
    format="%.2f"
)

st.number_input(
    "Rankine (°R):",
    key="rankine",
    on_change=actualizar_valores,
    args=("rankine",),
    format="%.2f"
)