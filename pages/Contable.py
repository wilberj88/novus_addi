import streamlit as st
import time
from streamlit_extras.colored_header import colored_header
from streamlit_echarts import st_echarts

st.header('Central Contable')
st.subheader('Configuración, Monitor, Alarmas y Recomendaciones')
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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Producción hoy", "200 Toneladas", "50%")
col2.metric("Abastecimiento hoy", "80%", "-8%")
col3.metric("Costos Calderas hoy", "125%", "25%")
col4.metric("Rentabilidad hoy", "15%", "3%")

meta_zona_1 = 10290
meta_zona_2 = 11986
meta_zona_3 = 11368
meta_zona_4 = 14018
meta_zona_5 = 14036
meta_zona_6 = 5241
meta_zona_7 = 3112
meta_zona_8 = 110
meta_zona_9 = 7338

col5, col6, col7 = st.columns(3)
with col5:
    
    meta = 35000
    st.subheader("Ritmo Turno Actual Vs Último")
    option = {
    "xAxis": {
        "type": "category",
        "data": ["Hora_1", "Hora_2", "Hora_3", "Hora_4", "Hora_5", "Hora_6", "Hora_7"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [meta*0.1, meta*0.2, meta*0.35, meta*0.5, meta*0.75, meta*0.9, meta], "type": "line"},
        {"data": [meta*0.15, meta*0.25, meta*0.4, meta*0.55, meta*0.75, meta*0.9, meta], "type": "line"},
    ],
    }
    st_echarts(
        options=option, height="625px",
    )
with col6:
    
    st.subheader("Calderas")
    acelerometro2 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 50, "name": "Temperatura"}],
            }
        ],
    }
    st_echarts(options=acelerometro2)
    acelerometro1 = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": 30, "name": "Humedad"}],
            }
        ],
    }

    st_echarts(options=acelerometro1)
     
with col7:
    st.subheader("Por Tipo de Cerámica")
    options = {
            "title": {"text": "🧱"},
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
            },
            "legend": {"data": ["Producto_5", "Producto_4", "Producto_3", "Producto_2", "Producto_1"]},
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00", "23:59"],
                }
            ],
            "yAxis": [{"type": "value"}],
            "series": [
                {
                    "name": "Producto_5",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_5*0.1, meta_zona_5*0.2, meta_zona_5*0.35, meta_zona_5*0.45, meta_zona_5*0.5, meta_zona_5*0.75, meta_zona_5],
                },
                  {
                    "name": "Producto_4",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_4*0.1, meta_zona_4*0.2, meta_zona_4*0.35, meta_zona_4*0.45, meta_zona_4*0.5, meta_zona_4*0.75, meta_zona_4],
                },
                  {
                    "name": "Producto_3",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_3*0.1, meta_zona_3*0.2, meta_zona_3*0.35, meta_zona_3*0.45, meta_zona_3*0.5, meta_zona_3*0.75, meta_zona_3],
                },
                  {
                    "name": "Producto_2",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_2*0.1, meta_zona_2*0.2, meta_zona_2*0.35, meta_zona_2*0.45, meta_zona_2*0.5, meta_zona_2*0.75, meta_zona_2],
                },
                  {
                    "name": "Producto_1",
                    "type": "line",
                    "stack": "总量",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": [meta_zona_1*0.1, meta_zona_1*0.2, meta_zona_1*0.35, meta_zona_1*0.45, meta_zona_1*0.5, meta_zona_1*0.75, meta_zona_1],
                },
            ],
        }
    st_echarts(options=options, height="600px")

    

    
colored_header(
    label="Cronograma Paradas de Planta Próxima Semana",
    description="Horarios y Resultados Requeridos",
    color_name="violet-70",
)


def render_heatmap_cartesian():
    hours = [
        "12a",
        "1a",
        "2a",
        "3a",
        "4a",
        "5a",
        "6a",
        "7a",
        "8a",
        "9a",
        "10a",
        "11a",
        "12p",
        "1p",
        "2p",
        "3p",
        "4p",
        "5p",
        "6p",
        "7p",
        "8p",
        "9p",
        "10p",
        "11p",
    ]
    days = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]

    data = [
        [0, 0, 5],
        [0, 1, 1],
        [0, 2, 0],
        [0, 3, 0],
        [0, 4, 0],
        [0, 5, 0],
        [0, 6, 0],
        [0, 7, 0],
        [0, 8, 0],
        [0, 9, 0],
        [0, 10, 0],
        [0, 11, 2],
        [0, 12, 4],
        [0, 13, 1],
        [0, 14, 1],
        [0, 15, 3],
        [0, 16, 4],
        [0, 17, 6],
        [0, 18, 4],
        [0, 19, 4],
        [0, 20, 3],
        [0, 21, 3],
        [0, 22, 2],
        [0, 23, 5],
        [1, 0, 7],
        [1, 1, 0],
        [1, 2, 0],
        [1, 3, 0],
        [1, 4, 0],
        [1, 5, 0],
        [1, 6, 0],
        [1, 7, 0],
        [1, 8, 0],
        [1, 9, 0],
        [1, 10, 5],
        [1, 11, 2],
        [1, 12, 2],
        [1, 13, 6],
        [1, 14, 9],
        [1, 15, 11],
        [1, 16, 6],
        [1, 17, 7],
        [1, 18, 8],
        [1, 19, 12],
        [1, 20, 5],
        [1, 21, 5],
        [1, 22, 7],
        [1, 23, 2],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 0],
        [2, 3, 0],
        [2, 4, 0],
        [2, 5, 0],
        [2, 6, 0],
        [2, 7, 0],
        [2, 8, 0],
        [2, 9, 0],
        [2, 10, 3],
        [2, 11, 2],
        [2, 12, 1],
        [2, 13, 9],
        [2, 14, 8],
        [2, 15, 10],
        [2, 16, 6],
        [2, 17, 5],
        [2, 18, 5],
        [2, 19, 5],
        [2, 20, 7],
        [2, 21, 4],
        [2, 22, 2],
        [2, 23, 4],
        [3, 0, 7],
        [3, 1, 3],
        [3, 2, 0],
        [3, 3, 0],
        [3, 4, 0],
        [3, 5, 0],
        [3, 6, 0],
        [3, 7, 0],
        [3, 8, 1],
        [3, 9, 0],
        [3, 10, 5],
        [3, 11, 4],
        [3, 12, 7],
        [3, 13, 14],
        [3, 14, 13],
        [3, 15, 12],
        [3, 16, 9],
        [3, 17, 5],
        [3, 18, 5],
        [3, 19, 10],
        [3, 20, 6],
        [3, 21, 4],
        [3, 22, 4],
        [3, 23, 1],
        [4, 0, 1],
        [4, 1, 3],
        [4, 2, 0],
        [4, 3, 0],
        [4, 4, 0],
        [4, 5, 1],
        [4, 6, 0],
        [4, 7, 0],
        [4, 8, 0],
        [4, 9, 2],
        [4, 10, 4],
        [4, 11, 4],
        [4, 12, 2],
        [4, 13, 4],
        [4, 14, 4],
        [4, 15, 14],
        [4, 16, 12],
        [4, 17, 1],
        [4, 18, 8],
        [4, 19, 5],
        [4, 20, 3],
        [4, 21, 7],
        [4, 22, 3],
        [4, 23, 0],
        [5, 0, 2],
        [5, 1, 1],
        [5, 2, 0],
        [5, 3, 3],
        [5, 4, 0],
        [5, 5, 0],
        [5, 6, 0],
        [5, 7, 0],
        [5, 8, 2],
        [5, 9, 0],
        [5, 10, 4],
        [5, 11, 1],
        [5, 12, 5],
        [5, 13, 10],
        [5, 14, 5],
        [5, 15, 7],
        [5, 16, 11],
        [5, 17, 6],
        [5, 18, 0],
        [5, 19, 5],
        [5, 20, 3],
        [5, 21, 4],
        [5, 22, 2],
        [5, 23, 0],
        [6, 0, 1],
        [6, 1, 0],
        [6, 2, 0],
        [6, 3, 0],
        [6, 4, 0],
        [6, 5, 0],
        [6, 6, 0],
        [6, 7, 0],
        [6, 8, 0],
        [6, 9, 0],
        [6, 10, 1],
        [6, 11, 0],
        [6, 12, 2],
        [6, 13, 1],
        [6, 14, 3],
        [6, 15, 4],
        [6, 16, 0],
        [6, 17, 0],
        [6, 18, 0],
        [6, 19, 0],
        [6, 20, 1],
        [6, 21, 2],
        [6, 22, 2],
        [6, 23, 6],
    ]
    data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": 10,
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "Punch Card",
                "type": "heatmap",
                "data": data,
                "label": {"show": True},
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
            }
        ],
    }
    st_echarts(option, height="600px")


ST_HEATMAP_DEMOS = {
    "Heatmap: Heatmap Cartesian": (
        render_heatmap_cartesian,
        "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
    ),
}

render_heatmap_cartesian()


colored_header(
    label="Alarmas",
    description="Operativas, Temporales y Climáticas",
    color_name="violet-70",
)

my_grid = grid(3, 3, vertical_align="bottom")
# Row 1:
a = my_grid.selectbox("Indica una Producto", ["Producto_1", "Producto_2", "Producto_3", "Producto_4"])
b = my_grid.selectbox("Indica tipo de Proveedor", ["Arcillas", "Energía", "Agua", "Herramientas"])
c = my_grid.selectbox("Indica un Fecha", ["Hoy", "Mañana", "Próxima Semana"])

# Row 2:
my_grid.button("Activar Protocolo Alarma a Equipos en Turno", use_container_width=True)
my_grid.button("Activar Protocolo Alarma a Proveedores", use_container_width=True)
my_grid.button("Activar Protocolo Alarma a Clientes", use_container_width=True)

   
if a and b and c:
    colx, coly, colz = st.columns(3)
    with colx:
        st.subheader("Costo Financiación a 12 meses")
        colx.metric("Renovables todo", "10%", "1%")
        colx.metric("Renovables medio", "13%", "5%")
        colx.metric("Renovables bajo", "15%", "3%")
        colx.metric("No Renovable", "17%", "3%")
    with coly:
        st.subheader("Inflación Energética")
        def render_basic_radar():
            option = {
                "title": {"text": "A 12 meses 💲"},
                "legend": {"data": ["Renovables", "Mixto", "No Renovables"]},
                "radar": {
                    "indicator": [
                        {"name": "Agua", "max": 100},
                        {"name": "Coke", "max": 100},
                        {"name": "Biomasa", "max": 100},
                        {"name": "Aire", "max": 100},
                        {"name": "Solar", "max": 100},
                    ]
                },
                "series": [
                    {
                        "name": "Votos por Zonas",
                        "type": "radar",
                        "data": [
                            {
                                "value": [90, 0, 0, 90, 90],
                                "name": "Renovables",
                            },
                            {
                                "value": [24, 50, 50, 5, 5],
                                "name": "Mixto",
                            },
                            {
                                "value": [10, 90, 90, 5, 5],
                                "name": "No Renovables",
                            },
                        ],
                    }
                ],
            }
            st_echarts(option, height="500px")
        ST_RADAR_DEMOS = {
            "Radar: Basic Radar": (
                render_basic_radar,
                "https://echarts.apache.org/examples/en/editor.html?c=radar",
            ),
        }
        render_basic_radar()
    
    
    with colz:
       fig1 = go.Figure(data=[go.Sankey(
            node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = ["Carbon", "Biomasa", "Coke", "No Renovable", "Renovable", "Calor"],
            color = "blue"
            ),
            link = dict(
            source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
            target = [3, 4, 3, 5, 5],
            value = [8, 4, 5, 13, 4]
            ))])
       fig1.update_layout(title_text="Participación Energética en Calderas", font_size=10)
       st.plotly_chart(fig1, theme="streamlit")
        
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

