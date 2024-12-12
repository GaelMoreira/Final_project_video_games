import streamlit as st
import pandas as pd
import numpy as np

# Configurar la página
st.set_page_config(page_title="Explorador de Videojuegos", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('C:/Users/gaelm/Desktop/videogames_final_projects.csv')

data = load_data()

st.title("🎮 Explorador de Videojuegos 🎮")
st.markdown(
    """
    ¡Descubre los videojuegos que te interesan! Usa los filtros a la izquierda para buscar por plataforma, género, publicante y año.
    También puedes ver los juegos con mejores ventas.
    """
)

# Barra lateral para filtros
st.sidebar.image("C:/Users/gaelm/Desktop/lab/streamlit_projects/DALL·E 2024-12-12 23.03.31 - A futuristic logo design for a video game theme, featuring turquoise and purple as the main colors. The logo incorporates sleek, angular shapes and gl.webp",width=150)
st.sidebar.header("Filtros 🎯")

platforms = st.sidebar.multiselect(
    "Plataformas", options=data["Platform"].unique(), default=[]
)
genres = st.sidebar.multiselect(
    "Géneros", options=data["Genre"].unique(), default=[]
)
publishers = st.sidebar.multiselect(
    "Publicantes", options=data["Publisher"].unique(), default=[]
)
years = st.sidebar.slider(
    "Año de publicación", int(data["Year"].min()), int(data["Year"].max()), (1980, 2020)
)

# Botones para filtrar y mostrar mejores ventas
if st.sidebar.button("🎮 Aplicar Filtros"):
    filtered_data = data.copy()

    # Aplicar filtros seleccionados
    if platforms:
        filtered_data = filtered_data[filtered_data["Platform"].isin(platforms)]

    if genres:
        filtered_data = filtered_data[filtered_data["Genre"].isin(genres)]

    if publishers:
        filtered_data = filtered_data[filtered_data["Publisher"].isin(publishers)]

    filtered_data = filtered_data[
        (filtered_data["Year"] >= years[0]) & (filtered_data["Year"] <= years[1])
    ]

    st.write(f"### 🎮 Resultados filtrados ({len(filtered_data)} juegos encontrados)")
    if len(filtered_data) > 0:
        for index, row in filtered_data.iterrows():
            st.write(f"**Nombre:** {row['Name']}")
            st.write(f"**Publicante:** {row['Publisher']}")
            st.write(f"**Año:** {int(row['Year'])}")
            st.write(f"**Género:** {row['Genre']}")
            st.write(f"**Plataforma:** {row['Platform']}")
            st.write("---")
    else:
        st.write("No se encontraron juegos con los filtros seleccionados.")

if st.sidebar.button("🔥 Mostrar Mejores Ventas"):
    best_sellers = data.sort_values(by="Global_Sales", ascending=False).head(5)

    st.write("### 🔝 Juegos con mejores ventas")

    # Información personalizada para cada juego
    urls = [
        "https://www.amazon.es/Nintendo-Wii-Sports/dp/B000P5FZ0A/ref=sr_1_2?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O4KHY0AFJ7SP&dib=eyJ2IjoiMSJ9.-FWAxE8E2E_jpYAYjyrl87iPQ2sQ3oG5U-nnuFu6oPltzck9F0cOmPTpaEVyi3bU3NI1f-1EAW5T6340lTPXSOavAbJgXELygp6lw8V1dBdqraNdoMcWRXX2uKQsrtj2hP6F2n0C5hNmxvbrrMHRlc5h9k6jp0NkcC4XVfYEUE5mQ020V15skgtNmv2Ie27DS4HkfZOo92VDuYzKYStMMvvW9FWH9py67U3e6qRqUca1XlhKVghXI_GDDzWHNxHad_nTg_XZq7PhUtdVt14ZegQBgUlePxrkcnVGSYjAMl8.2UsVMJxT0EllOajiTQDO0-YuZZii1UfYBYIImk3y3SU&dib_tag=se&keywords=wii+sport&nsdOptOutParam=true&qid=1734041966&sprefix=wii+sport%2Caps%2C86&sr=8-2",
        "https://www.todoconsolas.com/juegos-nes/1465-super_mario_bros_nes_sp_po7399-045496630140.html",
        "https://www.amazon.es/Nintendo-Wii-Mario-Kart/dp/B00784GOBA/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2NWVPOVYKIKFJ&dib=eyJ2IjoiMSJ9.-wtWPvoKi4x19CoP_hxYp7-YsOV8pk3_2TXKdVn49tPGMzcIbCuEF42ftV7jdOHB6lSPsWwKxQD-Mn_gPUu3DAIuuU4m6FppijHtflbOxBh_fhyZx0QBJswoe4wg0TO-K1xY6arF92eVRANu9yhNPkHU7wCAfEnVpFgv0mCbo6_DCNKg1ShXt5xaYGz1fj4xsJvvqjRy1uoEP5XjKIv6xP-cZCiId5Pxeqcg4W_DHF7cXepb6zT1hoDIaDRBPyYWdf3uJCnSMMyXBjxHLSQAHBZ-q5xi1BgeeTD2b3p_5lU.fBDrJjmMFVzaTbk6X7J-TRZsgRI9Sp81iYKjTPBzOUo&dib_tag=se&keywords=mario+kart+wii&nsdOptOutParam=true&qid=1734044256&sprefix=mario+kart+wii%2Caps%2C78&sr=8-3",
        "https://www.amazon.es/Nintendo-Wii-Sports-Resort/dp/B00784HBHG/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3R6F3YW1K73QH&dib=eyJ2IjoiMSJ9.pTVMeBMSXpg4lFjUnkdRcIvyJfwmj_ARTZj2wF3E2nxLXn2z4UrwxAtZ3QEWg1Ol5Hh5u3-cnkJLrJDbUTce9D3ypEgHUiu1sTT9T_umjDq-xUxMU0m0iUQ3hSVDYfsSRQFBw2t2pAHJRq0fRy09-9_2csB5iIGOCpHbqXbXa3NDRAGoT8vMjK0CguLE3AXe-EgAp82aX6UZ9ihC4RMDCB6wTYev2oGMaIixWtADdTgJjli2CtvpXDpth79g5fXcRgsK5tRtbwDttHRA4ojOoxlvom_iYnUu5QogASB5Yn4.FxcrUnk2TpUIY9O6esT1GL1aieT8yebdatcFLqyj2OE&dib_tag=se&keywords=wii+sport+resort&nsdOptOutParam=true&qid=1734044391&sprefix=wii+sport+resort%2Caps%2C94&sr=8-1",
        "https://www.todoconsolas.com/juegos-gb/11865-pokemon_edicion_roja_gb_sp_po0610-045496460730.html",
    ]

    images = [
        "C:/Users/gaelm/Desktop/lab/streamlit_projects/co3vge.webp",
        "C:/Users/gaelm/Desktop/lab/streamlit_projects/Super_Mario_Bros_Logo.webp",
        "C:/Users/gaelm/Desktop/lab/streamlit_projects/9c1976ae0d1370ad3b1513351aa12d92.jpg",
        "C:/Users/gaelm/Desktop/lab/streamlit_projects/co2may.webp",
        "C:/Users/gaelm/Desktop/lab/streamlit_projects/a8f54c32ac03e94fc0d8b584aae1237e.jpg",
    ]

    for index, row in best_sellers.iterrows():
        st.write(f"**Nombre:** {row['Name']}")
        st.write(f"**Publicante:** {row['Publisher']}")
        st.write(f"**Año:** {int(row['Year'])}")
        st.write(f"**Género:** {row['Genre']}")
        st.write(f"**Plataforma:** {row['Platform']}")
        st.write(f"**Ventas Globales:** {row['Global_Sales']} millones")
        st.write(f"[Comprar aquí]({urls[index]})")
        st.image(images[index], width=150)
        st.write("---")




