import streamlit as st
import time
from streamlit_extras.colored_header import colored_header

st.header('Central Contable')
st.subheadr('Configuración, Monitor, Alarmas y Recomendaciones')
current_time = time.ctime()
st.write("Siendo HOY y AHORA las: ", current_time)

colored_header(
    label="Configuración",
    description="Por servicio, tipo de compañía y presupuesto",
    color_name="violet-70",
)


tipo_empresa = st.selectbox("Selecciona qué tipo de empresa eres:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")


servicios_contables_internacionales = st.selectbox("Selecciona qué tipo de servicio contable internacional necesitas:", ("Reporting", "Estados Financieros", "Informes Casa Matriz", "Auditorías de Control Interno"), index=None, placeholder="Choose an option")

servicios_contables_outsourcing_gerencial = st.selectbox("Selecciona qué tipo de servicio contable outsourging gerencial necesitas:", ("Asistencia a Justa de Socios", "Análisis de Estados Financieros", "Atención Entidades Bancarias", "Estrategia Corporativa"), index=None, placeholder="Choose an option")



colored_header(
    label="Mando",
    description="Por servicio, tipo de compañía y presupuesto",
    color_name="violet-70",
)

colored_header(
    label="Alarma",
    description="Por servicio, tipo de compañía y presupuesto",
    color_name="violet-70",
)

colored_header(
    label="Recomendaciones",
    description="Por servicio, tipo de compañía y presupuesto",
    color_name="violet-70",
)

