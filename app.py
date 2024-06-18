import pandas as pd
from PIL import Image
from datetime import datetime
from automatizacion import GPS, ultima_ubicacion, uso_vehiculo, exceso_velocidad, enviar_email
import streamlit as st
logo = Image.open(r'imagenes/logo.png')
gps = Image.open(r'imagenes/GPS.png')
st.set_page_config(page_title="UNIDADES | GPS   ", page_icon="🚛",layout="wide")
def main():
    st.sidebar.title('GENERADOR DE REPORTE')
    st.sidebar.image(logo, width=270)
    st.sidebar.write("---")
    st.sidebar.image(gps, width= 270)
    st.markdown(
    """<div style= padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 3.5em;'><center><b>Procesamiento de Archivos de Excel</center></span>
    </div>""",unsafe_allow_html=True)
    col1, col2 ,col3 = st.columns((1,2,1))
    uploaded_files = col2.file_uploader("Cargar los archivos 3 archivos de Excel descargados en el paso anterior", type=["xlsx"], accept_multiple_files=True)
    archivo1_cargado,archivo2_cargado,archivo3_cargado = False,False, False
    df1, df2, df3 = None, None, None
    if uploaded_files:
        for file in uploaded_files:
            st.subheader("Archivo " + file.name+ " cargado correctamente")
            # Leer el archivo Excel PROCESADO en un DataFrame
            if "Exceso de Velocidad" in file.name:
                df1 = exceso_velocidad(file)
                st.write(df1)
                archivo1_cargado = True
            elif "Última posición conocida" in file.name:
                df2 = ultima_ubicacion(file)
                st.write(df2)
                archivo2_cargado = True
            else:
                df3 = uso_vehiculo(file)
                st.write(df3)
                archivo3_cargado = True       
    if archivo1_cargado and archivo2_cargado and archivo3_cargado:
        with pd.ExcelWriter('Reporte GPS.xlsx') as writer:
            df1.to_excel(writer, sheet_name="Exceso de velocidad", index=False)
            df2.to_excel(writer, sheet_name="Ultima Ubicacion", index=False)
            df3.to_excel(writer, sheet_name="Info del recorrido", index=False)
        col1, col2, col3 = st.columns((3,4,4))
        col2.warning("Puedes descargar el reporte clasificado aquí")
        with open('Reporte GPS.xlsx', 'rb') as f:  
            bytes_data = f.read()
        sub1, sub2, sub3 = st.columns((4,2,4))
        with sub2:
            descarga = st.download_button(label="Descargar Excel Procesado", data=bytes_data, file_name=f'Reporte GPS {datetime.today().strftime("%d/%m/%Y")}.xlsx', mime='application/vnd.ms-excel')                 
            if descarga:
                st.success("Archivo descargado")
        st.write("---") 
        col1, col2 ,col3 = st.columns((1,2,1))
        uploaded_file = col2.file_uploader("Carga el archivo PDF una vez lo proceses", type=["pdf"])
        b1, sub2, sub3 = st.columns((4,2,4))
        if uploaded_file is not None:
            if sub2.button("Enviar correo"):
                col1, col2, col3 = st.columns((3,4,4))
                enviar_email(uploaded_file)
                col2.success("El correo se envio correctamente")
if __name__ == "__main__":
    main()