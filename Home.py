import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import numpy as np
import pandas as pd
import time
from datetime import time
import plotly.graph_objects as go
import pydeck as pdk
import folium
from streamlit_folium import st_folium
from streamlit_extras.grid import grid


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
                        
                    fig1.update_layout(title_text="Usos promedio de tu presupuesto💰", font_size=5)
                    st.plotly_chart(fig1, theme="streamlit")

                                        
                    my_grid2 = grid(3, vertical_align="bottom")
                    my_grid2.button("Actualizar Ubicación Clientes", use_container_width=True)
                    my_grid2.button("Actualizar Ubicación Proveedores", use_container_width=True)
                    my_grid2.button("Actualizar Ubicación Deudores", use_container_width=True)
                    
                    
                    # center on Liberty Bell, add marker
                    m = folium.Map(location=[10.4735, -73.2486], zoom_start=13)
                    n = folium.Map(location=[10.45358, -73.26678], zoom_start=13)
                    l = folium.Map(location=[10.44664, -73.30750], zoom_start=13)
                    
                    #zona1
                    folium.Marker(
                        [10.47358, -73.248639], popup="Z1 PV1 PV1 COL Nacional Loperena 3de10K", tooltip="Z1 PV1 PV1 COL Nacional Loperena. 3K de 8K", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    folium.Marker(
                        [10.474139, -73.25125], popup="Z1 PV2 PV2 ESC Bellas Artes. 2K de 5K", tooltip="Z2 PV2 PV2 ESC Bellas Artes. 2K de 5K", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    folium.Marker(
                        [10.478472, -73.245361], popup="Z1 PV3 PV3 UDES. 1,5K de 4K", tooltip="Z1 PV3 PV3 UDES. 1,5K de 4K", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    folium.Marker(
                        [10.468500, -73.247278], popup="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", tooltip="Z1 PV4 PV4 COL Prudencia Daza. 1K de 3K", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    folium.Marker(
                        [10.469667, -73.238056], popup="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", tooltip="Z1 PV5 PV5 COL SantoDomingo. 2,5K de 6K", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    folium.Marker(
                        [10.474130, -73.251115], popup="PV6 COL Parroquial El Carmelo (Nuevo 2023)", tooltip="PV6 COL Parroquial El Carmelo", icon=folium.Icon(icon='cloud')
                    ).add_to(m)
                    #zona2
                    folium.Marker(
                        [10.46006, -73.22889], popup="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", tooltip="Z2 PV1 PV7 COL Francisco Molina Sanchez. 4K de 9K", icon=folium.Icon(icon='flag')
                    ).add_to(m)
                    folium.Marker(
                        [10.46322, -73.23575], popup="Z2 PV2 PV8 I.E. Manuel Germán Cuello. 2K de 4K", tooltip="Z2 PV1 PV8 I.E. Manuel Germán Cuello. 2K de 4K", icon=folium.Icon(icon='flag')
                    ).add_to(m)
                    folium.Marker(
                        [10.45389, -73.24211], popup="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", tooltip="Z2 PV3 PV9 Inst. Educ. Leonidas Acuña. 4K de 8K", icon=folium.Icon(icon='flag')
                    ).add_to(m)
                    folium.Marker(
                        [10.45100, -73.23672], popup="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", tooltip="Z2 PV4 PV10 UNV. Abierta y a Distancia. 2K de 4,5K", icon=folium.Icon(icon='flag')
                    ).add_to(m)
                    #zona3
                    folium.Marker(
                        [10.44578, -73.25128], popup="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", tooltip="Z3 PV1 PV13 CON. Milciades Cantillo. 3K de 7K", icon=folium.Icon(icon='star')
                    ).add_to(m)
                    folium.Marker(
                        [10.44950, -73.25075], popup="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", tooltip="Z3 PV2 PV14 CON. Alfonso Araujo Cotes. 2K de 5K", icon=folium.Icon(icon='star')
                    ).add_to(n)
                    folium.Marker(
                        [10.45131, -73.25711], popup="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", tooltip="Z3 PV3 PV15 INS. TEC. Enrique Pupo. 2K de 5K", icon=folium.Icon(icon='star')
                    ).add_to(n)
                    folium.Marker(
                        [10.45714, -73.25153], popup="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", tooltip="Z3 PV4 PV16 I.E. Rafael Valle Meza. 2,5K de 6K", icon=folium.Icon(icon='star')
                    ).add_to(n)
                    folium.Marker(
                        [10.43650, -73.25356], popup="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", tooltip="Z3 PV5 PV17 I.E. Joaquin Ochoa Mestre. 1,6K de 4K", icon=folium.Icon(icon='star')
                    ).add_to(n)
                    #zona4
                    folium.Marker(
                        [10.45358, -73.26678], popup="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", tooltip="Z4 PV1 PV20 COL Jose Eugenio Martinez. 5K de 11K", icon=folium.Icon(icon='info-sign')
                    ).add_to(n)
                    folium.Marker(
                        [10.45892, -73.25958], popup="Z4 PV2 PV21 COL Nacionalizado UPAR. 3,5K de 8K", tooltip="Z4 PV2 PV21 COL Nacionalizado UPAR 8K. 3,5K de 8K", icon=folium.Icon(icon='info-sign')
                    ).add_to(n)
                    folium.Marker(
                        [10.46157, -73.26789], popup="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", tooltip="Z4 PV3 PV22 INS TEC Villa Corelca. 1,5K de 4K", icon=folium.Icon(icon='info-sign')
                    ).add_to(n)
                    folium.Marker(
                        [10.46661, -73.25814], popup="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", tooltip="Z4 PV4 PV23 Escuela Mixta No 4. 2K de 5K", icon=folium.Icon(icon='info-sign')
                    ).add_to(m)
                    folium.Marker(
                        [10.44381, -73.27533], popup="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", tooltip="Z4 PV5 PV24 I.E Consuelo Araujo Noguera. 2K de 6K", icon=folium.Icon(icon='info-sign')
                    ).add_to(m)
                    #zona5
                    folium.Marker(
                        [10.47242, -73.26011], popup="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", tooltip="Z5 PV1 PV26 COL. Nacionalizado Alfonso López. 2,6K de 7K", icon=folium.Icon(icon='bicycle')
                    ).add_to(m)
                    folium.Marker(
                        [10.47242, -73.26011], popup="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", tooltip="Z5 PV2 PV27 IE Loperena Garupal. 3,2K de 8K", icon=folium.Icon(icon='bicycle')
                    ).add_to(m)
                    folium.Marker(
                        [10.47928, -73.27719], popup="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", tooltip="Z5 PV3 PV28 IE Técnico La Esperanza. 3,7K de 9,3K", icon=folium.Icon(icon='bicycle')
                    ).add_to(m)
                    folium.Marker(
                        [10.47842, -73.29089], popup="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", tooltip="Z5 PV4 PV29 IE Bello Horizonte. 1,5K de 4K", icon=folium.Icon(icon='bicycle')
                    ).add_to(m)
                    folium.Marker(
                        [10.48606, -73.28081], popup="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", tooltip="Z5 PV5 PV30 COL COMFACESAR. 2,7K de 7K", icon=folium.Icon(icon='bicycle')
                    ).add_to(m)
                    #zona6
                    folium.Marker(
                        [10.48044, -73.24781], popup="Z6 PV1 PV33 COL. Pablo Sexto 5K", tooltip="Z6 PV1 PV33 COL. Pablo Sexto 5K", color='red'
                    ).add_to(m)
                    folium.Marker(
                        [10.48181, -73.25644], popup="Z6 PV2 PV34 CONC.San Joaquin 4K", tooltip="Z6 PV2 PV34 CONC.San Joaquin 4K", color='red'
                    ).add_to(l)
                    folium.Marker(
                        [10.49319, -73.26533], popup="Z6 PV3 PV35 COL. Sagrada Familia 3K", tooltip="Z6 PV3 PV35 COL. Sagrada Familia 3K", color='red'
                    ).add_to(l)
                    #zona7
                    folium.Marker(
                        [10.47475, -73.25969], popup="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", tooltip="Z7 PV1 PV36 INST. TEC. PEDRO CASTRO MONSALVO 8K", color='red'
                    ).add_to(l)
                    #zona8
                    folium.Marker(
                        [10.46442, -73.25625], popup="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", tooltip="Z8 PV1 PV37 CARCEL JUDICIAL 0.1K", color='red'
                    ).add_to(l)
                    folium.Marker(
                        [10.44664, -73.30750], popup="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", tooltip="Z8 PV2 PV38 CARCEL TRAMACUA 0.1K", color='red'
                    ).add_to(l)



                    
                    st.markdown('<p class="dashboard_title">🌎 Diagnóstico Georreferenciado 🔎</p>', unsafe_allow_html = True)
                    
                    #datos
                    df = pd.DataFrame(
                    np.random.randn(500, 2) / [50, 50] + [-1.9868735, 43.3205582],
                    columns=['lat', 'lon'])
                    st.pydeck_chart(pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=-1.9868735,
                        longitude=43.3205582,
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
                           elevation_range=[0, 2000],
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
                    
                       
                    
            with data_col:
                
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
                col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Ingresos", "70%", "40%")
                    col2.metric("Gastos", "30%", "-82%")
                    col3.metric("Rentabilidad", "16%", "43%")
                    col4.metric("Rotación Personal", "87%", "78%")
                   
                st.caption("By Wilber Jimenez Hernandez")
                
               

                                  

