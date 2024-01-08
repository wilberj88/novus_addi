import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import pandas as pd
import time
from datetime import time
import plotly.graph_objects as go
import pydeck as pdk


if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = 'Novus_Addi'
)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)


title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1.3,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Novus Mando<br>Addi Consulting</p>', unsafe_allow_html = True)

with btc_col:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Hostelería<br></p><p class="price_details">29.4%</p>', unsafe_allow_html = True)
       
with eth_col:
    with st.container(border=True):
        #eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">Servicios<br></p><p class="price_details">22.1%</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container(border=True):
        #xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">Comercio<br></p><p class="price_details">19.1%</p>', unsafe_allow_html = True)

with sol_col:
    with st.container(border=True):
        #sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">Producción Audiovisual<br></p><p class="price_details">14.7%</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container(border=True):
        #xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">Otros<br></p><p class="price_details">14.7%</p>', unsafe_allow_html = True)


params_col, chart_col, data_col = st.columns([0.7,1.6,1.1])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">PARÁMETROS', unsafe_allow_html = True)
                
        tipo_empresa = st.selectbox("Selecciona tipo de empresa:", ("S.L.", "S.A.", "S.L.L.", "Holding", "Comunidades de bienes", "Cooperativas", "Asociaciones", "Autónomos", "Emprendedores", "Particulares"), index=None, placeholder="Choose an option")
        
        servicios_contables_internacionales = st.selectbox("Selecciona tipo de servicio contable internacional:", ("Reporting", "Estados Financieros", "Informes Casa Matriz", "Auditorías de Control Interno"), index=None, placeholder="Choose an option")
        
        servicios_contables_outsourcing_gerencial = st.selectbox("Selecciona tipo de servicio contable outsourging gerencial necesitas:", ("Asistencia a Justa de Socios", "Análisis de Estados Financieros", "Atención Entidades Bancarias", "Estrategia Corporativa"), index=None, placeholder="Choose an option")

        a = st.slider("Indica nivel mínimo de facturación anual", 0, 100000, 5000)
        st.divider()
        update_chart = st.form_submit_button('Update chart')
        
        if update_chart:
           

            with chart_col:

                with st.container(border=True):
                    st.header("Diagnóstico de Riesgos Climáticos + Transición Energética")
                    st.write("Probabilidades de ocurrencia en el periodo ", categoria)
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Derrumbes", "70%", "40%")
                    col2.metric("Sequías", "30%", "-82%")
                    col3.metric("Incedios", "16%", "43%")
                    col4.metric("Inundaciones", "87%", "78%")
                    st.write("Georreferenciación de riesgos climáticos")
                    #datos
                    df = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [4.2620, -75.13],
                    columns=['lat', 'lon'])
                    st.pydeck_chart(pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=4.26,
                        longitude=-75.13,
                        zoom=11,
                        pitch=50,
                    ),
                    layers=[
                        pdk.Layer(
                           'HexagonLayer',
                           data=df,
                           get_position='[lon, lat]',
                           radius=200,
                           elevation_scale=4,
                           elevation_range=[0, 1000],
                           pickable=True,
                           extruded=True,
                        ),
                        pdk.Layer(
                            'ScatterplotLayer',
                            data=df,
                            get_position='[lon, lat]',
                            get_color='[200, 30, 0, 160]',
                            get_radius=200,
                        ),
                        ],
                        ))
                    fig1 = go.Figure(data=[go.Sankey(
                        node = dict(
                            pad = 15,
                            thickness = 20,
                            line = dict(color = "black", width = 0.5),
                            label = ["Gastos Mensuales", "Necesidades", "Entretenimiento", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
                            color = "red"
                            ),
                        link = dict(
                        source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
                        target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                        value = [50, 20, 30, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
                        ))])
                    
                    fig1.update_layout(title_text="Usos promedio de tu presupuesto💰", font_size=10)
                    st.plotly_chart(fig1, theme="streamlit")
                    df = pd.DataFrame(
                        {
                            "name": ["Roadmap", "Extras", "Issues"],
                            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                            "stars": [random.randint(0, 1000) for _ in range(3)],
                            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                        }
                    )
                    st.dataframe(
                        df,
                        column_config={
                            "name": "App name",
                            "stars": st.column_config.NumberColumn(
                                "Github Stars",
                                help="Number of stars on GitHub",
                                format="%d ⭐",
                            ),
                            "url": st.column_config.LinkColumn("App URL"),
                            "views_history": st.column_config.LineChartColumn(
                                "Views (past 30 days)", y_min=0, y_max=5000
                            ),
                        },
                        hide_index=True,
                    )
                       
                    
            with data_col:
                data_df = pd.DataFrame(
                    {
                        "name": ["Mando", "Atento", "Campus"],
                        "apps": [
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                        ],
                        "sales": [
                            [0, 4, 26, 80, 100, 40],
                            [80, 20, 80, 35, 40, 100],
                            [10, 20, 80, 80, 70, 0],
                        ],
                        "Performance": [200, 550, 1000],
                    }
                )                
                st.dataframe(
                    data_df,
                    column_config={
                        "name": "Tech Required",
                        "apps": st.column_config.ImageColumn(
                            "Preview Image", help="Streamlit app preview screenshots"
                        ),
                        "sales": st.column_config.BarChartColumn(
                            "Sales (last 6 months)",
                            help="The sales volume in the last 6 months",
                            y_min=0,
                            y_max=100,
                        ),
                        "Performance": st.column_config.ProgressColumn(
                            "Performance",
                            help="The sales volume in USD",
                            format="$%f",
                            min_value=0,
                            max_value=1000,
                        ),
                    },
                    hide_index=True,
                )
                st.caption("By Wilber Jimenez Hernandez")
                
               

                                  

