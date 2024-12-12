import streamlit as st

st.title('dalmiro webon')

st.write("Dalmiro es un ebon que que le encanta el mate y lo culos y es tremendo capo y le aprecio")
col1,col2 = st.columns(2)
with col1:
    st.header("parte izquierda")

with col2:
    st.header("parte derecha")

captured_image = st.camera_input("hazte uan foto para nuestra trabajadora sepa como eres:")
if captured_image is not None:
    st.image(captured_image, caption="Imagen capturada")

slider_valor = st.slider("cuanta intensidad quieres de sexo", min_value = 0, max_value=100, value=50)

st.write(slider_valor)
st.write("elije que quieres hacerme")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("APRIETAME"):
        st.write("Me ha gustado mucho")
with col2:
    if st.button("ESTRUJAME"):
        st.write("Me ha gustado mucho")
with col3:
    if st.button("AGARRAME"):
        st.write("Me ha gustado mucho")
with col4:
    if st.button("AMARRAME"):
        st.write("Me ha gustado mucho")

opcion_elegida = st.selectbox("que mas quieres que hagamos",("seguir duro","hablar un rato (te cobramos igual)","te devolvemos el dinero"))
st.write(f"La opcion que has elegido es {opcion_elegida}")

st.image("C:/Users/gaelm/Pictures/Camera Roll/WIN_20241202_09_37_56_Pro.jpg")

