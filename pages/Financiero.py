import streamlit as st
import time

tipo_empresa = st.selectbox("Selecciona qué tipo de empresa eres:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")

servicios_finacieros_outsourcing_administrativo = st.selectbox("Selecciona qué tipo de servicio financiero de outsourging administrativo necesitas:", ("Emisión, envío y cobro de facturas a clientes", "Control y reclamación de impagados", "Programación de facturación"), index=None, placeholder="Choose an option")
