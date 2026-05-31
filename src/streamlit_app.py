import streamlit as st

from rtl_parser import analyze_rtl
from tb_generator import generate_tb

st.title("AI Assisted RTL Generator")

rtl_code = st.text_area(
    "Paste SystemVerilog RTL Here",
    height=300
)

if st.button("Analyze RTL"):

    info = analyze_rtl(rtl_code)

    st.subheader("RTL Information")

    st.json(info)

    tb = generate_tb(info)

    st.subheader("Generated Testbench")

    st.code(
        tb,
        language="verilog"
    )
