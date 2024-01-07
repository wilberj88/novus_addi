import streamlit as st
import time

tipo_empresa = st.selectbox("Selecciona qué tipo de empresa eres:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")


servicios_legales = st.selectbox("Selecciona qué tipo de servicio legal necesitas:", ("Asesoría Contratos", "Conflictos Societarios", "Reclamación impagados", "Pacto de Socios", "Concursos de Acreedores"), index=None, placeholder="Choose an option")
