import streamlit as st
import time


tipo_empresa = st.selectbox("Selecciona qué tipo de empresa eres:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")


servicios_fiscales = st.selectbox("Selecciona qué tipo de servicio fiscal necesitas:", ("Asesoría Tributaria", "Declaraciones Fiscales", "Fiscalidad internacional", "Plan Contable"), index=None, placeholder="Choose an option")
