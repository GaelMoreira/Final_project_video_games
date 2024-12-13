# Proyecto: Análisis y Exploración de Videojuegos

Este proyecto se centra en la exploración, análisis y visualización de un dataset de videojuegos, proporcionando herramientas interactivas para filtrar y explorar datos relevantes.

## Descripción
El proyecto incluye las siguientes funcionalidades:

1. **Análisis Exploratorio de Datos (EDA)**: Un script de Python analiza el dataset y genera gráficos para comprender mejor los datos.
2. **Consultas en SQL**: Se incluyen queries para analizar los datos directamente desde una base de datos.
3. **Aplicaciones Streamlit**:
   - Una aplicación para visualizar el EDA de forma más intuitiva.
   - Una aplicación que permite explorar videojuegos mediante filtros (género, publicante, plataforma) y visualizar un top de videojuegos más vendidos con enlaces para comprarlos.

## Dataset
El dataset contiene información sobre videojuegos, incluyendo:
- **Rank**: Clasificación del videojuego.
- **Name**: Nombre del videojuego.
- **Platform**: Plataforma de lanzamiento.
- **Year**: Año de lanzamiento.
- **Genre**: Género del videojuego.
- **Publisher**: Publicante.
- **Ventas**: Distribuidas por región (NA, EU, JP, Other) y a nivel global.
- **Porcentajes de Ventas**: Proporción de ventas por región y globalmente.

### Ejemplo de los datos:
| Rank | Name                 | Platform | Year | Genre        | Publisher | Global_Sales |
|------|----------------------|----------|------|--------------|-----------|--------------|
| 1    | Wii Sports           | Wii      | 2006 | Sports       | Nintendo  | 82.74        |
| 2    | Super Mario Bros.    | NES      | 1985 | Platform     | Nintendo  | 40.24        |


## Contribución
Si deseas contribuir, por favor:
1. Haz un fork del proyecto.
2. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza un pull request.
