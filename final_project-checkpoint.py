import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Análisis de Videojuegos")

df = pd.read_csv("C:/Users/gaelm/Desktop/videogames_final_projects.csv")

st.subheader("Vista previa de los datos")
st.dataframe(df.head())

    # Mostrar información básica del dataset
st.subheader("Información del dataset")
st.write(f"**Total de filas:** {df.shape[0]}")
st.write(f"**Total de columnas:** {df.shape[1]}")


st.sidebar.title("Filtros")
publishers = st.sidebar.multiselect("Selecciona compañías publicadoras", options=df['Publisher'].unique())
genres = st.sidebar.multiselect("Selecciona géneros", options=df['Genre'].unique())
platforms = st.sidebar.multiselect("Selecciona plataformas", options=df['Platform'].unique())
years = st.sidebar.slider("Selecciona el rango de años", int(df['Year'].min()), int(df['Year'].max()), (int(df['Year'].min()), int(df['Year'].max())))

filtered_df = df[
        (df['Publisher'].isin(publishers) if publishers else True) &
        (df['Genre'].isin(genres) if genres else True) &
        (df['Platform'].isin(platforms) if platforms else True) &
        (df['Year'].between(years[0], years[1]))
    ]
st.subheader("Datos Filtrados")
st.write(f"**Total de filas filtradas:** {filtered_df.shape[0]}")
st.dataframe(filtered_df)

NA_group =df.groupby(['Genre','%_sales_NA'],as_index=False).count()
EU_group =df.groupby(['Genre','%_sales_EU'],as_index=False).count()
JP_group =df.groupby(['Genre','%_sales_JP'],as_index=False).count()
Other_group =df.groupby(['Genre','%_sales_Other'],as_index=False).count()
Global_group =df.groupby(['Genre','%_sales_Global'],as_index=False).count()

st.write("¿Que visualizacion quieres?")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("cuantos videojuegos hay de cada genero"):
        plt.figure(figsize=(15,10))
        sns.countplot(df['Genre'], palette='cool',order = df['Genre'].value_counts().index)
        plt.ylabel('Genre',fontsize=15)
        st.pyplot(plt)
with col2:
    if st.button("cuantos juegos se hciceron por año"):
        plt.figure(figsize=(15,10))
        sns.countplot(x="Year", data=df, palette='cool', order = df.groupby(by=['Year'])['Name'].count().sort_values(ascending=False).index)
        plt.ylabel("count",fontsize=15)
        plt.xticks(rotation=90)
        st.pyplot(plt)
with col3:
    if st.button("categorias de juegos mas vendidas en los años con mas ventas"):
        plt.figure(figsize=(30, 10))
        sns.countplot(x="Year", data=df, palette ="cool", hue='Genre', order=df.Year.value_counts().iloc[:5].index)
        plt.xticks(size=16, rotation=90)
        st.pyplot(plt)
with col4:
    if st.button("porcentaje que representa cada genero en norte america por ventas"):
        plt.figure(figsize=(8,6))
        NA_group["Genre"].value_counts().plot(kind='pie',textprops={'color':'black'},autopct='%.2f',cmap='cool')
        plt.title('Norte América',fontsize=15)
        plt.ylabel("")
        st.pyplot(plt)

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("porcentaje que representa cada genero en europa por ventas"):
        plt.figure(figsize=(8,6))
        EU_group["Genre"].value_counts().plot(kind='pie',textprops={'color':'black'},autopct='%.2f',cmap='cool')
        plt.title('Europa',fontsize=15)
        plt.ylabel("")
        st.pyplot(plt)
with col2:
    if st.button("porcentaje que representa cada genero en japon por ventas"):
        plt.figure(figsize=(8,6))
        JP_group["Genre"].value_counts().plot(kind='pie',textprops={'color':'black'},autopct='%.2f',cmap='cool')
        plt.title('Japon',fontsize=15)
        plt.ylabel("")
        st.pyplot(plt)
with col3:
    if st.button("porcentaje que representa cada genero en otros continentes/paises por ventas"):
        plt.figure(figsize=(8,6))
        Other_group["Genre"].value_counts().plot(kind='pie',textprops={'color':'black'},autopct='%.2f',cmap='cool')
        plt.title('otros continentes/paises',fontsize=15)
        plt.ylabel("")
        st.pyplot(plt)
with col4:
    if st.button("porcentaje que representa cada genero en global por ventas"):
        plt.figure(figsize=(8,6))
        Global_group["Genre"].value_counts().plot(kind='pie',textprops={'color':'black'},autopct='%.2f',cmap='cool')
        plt.title('Global',fontsize=15)
        plt.ylabel("")
        st.pyplot(plt)


comp_publisher = df[['Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
comp_publisher = comp_publisher.groupby(by=['Publisher']).sum().reset_index().sort_values(by=['Global_Sales'], ascending=False)
comp_publisher = comp_publisher.head(20)
comp_publisher = pd.melt(comp_publisher, id_vars=['Publisher'], value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], var_name='Sale_Area', value_name='Sale_Price')

sale_pbl = df[['Publisher', 'Global_Sales']]
sale_pbl = sale_pbl.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(20)
sale_pbl = pd.DataFrame(sale_pbl).reset_index()

NA_sale_pbl = df[['Publisher', 'NA_Sales']]
NA_sale_pbl = NA_sale_pbl.groupby('Publisher')['NA_Sales'].sum().sort_values(ascending=False).head(20)
NA_sale_pbl = pd.DataFrame(NA_sale_pbl).reset_index()

EU_sale_pbl = df[['Publisher', 'EU_Sales']]
EU_sale_pbl = EU_sale_pbl.groupby('Publisher')['EU_Sales'].sum().sort_values(ascending=False).head(20)
EU_sale_pbl = pd.DataFrame(EU_sale_pbl).reset_index()

JP_sale_pbl = df[['Publisher', 'JP_Sales']]
JP_sale_pbl = JP_sale_pbl.groupby('Publisher')['JP_Sales'].sum().sort_values(ascending=False).head(20)
JP_sale_pbl = pd.DataFrame(JP_sale_pbl).reset_index()

Other_sale_pbl = df[['Publisher', 'Other_Sales']]
Other_sale_pbl = Other_sale_pbl.groupby('Publisher')['Other_Sales'].sum().sort_values(ascending=False).head(20)
Other_sale_pbl = pd.DataFrame(Other_sale_pbl).reset_index()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("publicantes con mas juegos"):
        plt.figure(figsize=(15, 10))
        sns.countplot(x="Publisher", data=df, palette='cool', order = df.groupby(by=['Publisher'])['Year'].count().sort_values(ascending=False).iloc[:20].index)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)
with col2:
    if st.button("top 20 publicantes y las ventas en cada lugar"):
        plt.figure(figsize=(8,6))
        plt.figure(figsize=(30, 15))
        sns.barplot(x='Publisher', y='Sale_Price', palette='cool', hue='Sale_Area', data=comp_publisher)
        plt.xticks(fontsize=14, rotation=-50, ha="left")
        plt.yticks(fontsize=14)
        st.pyplot(plt)
with col3:
    if st.button("ventas globales de los difernetes publicantes"):
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Publisher', y='Global_Sales',palette = "cool", data=sale_pbl)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)
with col4:
    if st.button("ventas en América del norte de los difernetes publicantes"):
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Publisher', y='NA_Sales',palette = "cool", data=NA_sale_pbl)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("ventas en Europa de los difernetes publicantes"):
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Publisher', y='EU_Sales',palette = "cool", data=EU_sale_pbl)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)
with col2:
    if st.button("ventas en Japon de los difernetes publicantes"):
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Publisher', y='JP_Sales',palette = "cool", data=JP_sale_pbl)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)
with col3:
    if st.button("ventas en otros continentes/paises de los difernetes publicantes"):
        plt.figure(figsize=(15, 10))
        sns.barplot(x='Publisher', y='Other_Sales',palette = "cool", data=Other_sale_pbl)
        plt.xticks(rotation=-50, ha = "left")
        st.pyplot(plt)




