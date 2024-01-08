import streamlit as st
import time
from streamlit_extras.colored_header import colored_header

colored_header(
    label="Central Contable",
    description="Configuración, Monitor, Alarmas y Recomendaciones",
    color_name="violet-70",
)
current_time = time.ctime()
st.write("Siendo HOY y AHORA las: ", current_time)

st.header('Configuración')

tipo_empresa = st.selectbox("Selecciona qué tipo de empresa eres:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")


servicios_contables_internacionales = st.selectbox("Selecciona qué tipo de servicio contable internacional necesitas:", ("Reporting", "Estados Financieros", "Informes Casa Matriz", "Auditorías de Control Interno"), index=None, placeholder="Choose an option")

servicios_contables_outsourcing_gerencial = st.selectbox("Selecciona qué tipo de servicio contable outsourging gerencial necesitas:", ("Asistencia a Justa de Socios", "Análisis de Estados Financieros", "Atención Entidades Bancarias", "Estrategia Corporativa"), index=None, placeholder="Choose an option")

