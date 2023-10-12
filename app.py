import pandas as pd
import streamlit as st
from datetime import datetime
from automatizacion import GPS, ultima_ubicacion, uso_vehiculo, exceso_velocidad, enviar_email
from PIL import Image

logo = Image.open(r'imagenes/logo.png')

st.set_page_config(
    page_title="UNIDADES | GPS   ",
    page_icon="🚛",
    layout="wide")
def main():
    st.sidebar.image(logo, width=310)
    st.sidebar.title('Generador de reportes')
    st.sidebar.write('Clickea para generar los 3 reportes desde la pagina Tracker-GPS.')

    if st.sidebar.button('Generar reportes'):
        # Configurar el webdriver (esto podría ser Chrome, Firefox, etc.)
        # Asegúrate de tener el driver correspondiente instalado
        # Define tus credenciales aquí o consíguelas de alguna manera segura
        GPS()
        st.sidebar.success('Archivos descargados desde TRACKERGPS correctamente!')
    st.markdown(
    """<div style= padding: 5px; border-radius:5px;'>
    <span style='color: ##1D20FA; font-size: 3.5em;'><center><b>Procesamiento de Archivos de Excel</center></span>
    </div>""",unsafe_allow_html=True)

    # Agregar la posibilidad de cargar archivos
    col1, col2 ,col3 = st.columns((1,2,1))
    uploaded_files = col2.file_uploader("Cargar los archivos 3 archivos de Excel descargados en el paso anterior", type=["xlsx"], accept_multiple_files=True)

    # Variables para verificar si se han cargado los tres archivos
    archivo1_cargado = False
    archivo2_cargado = False
    archivo3_cargado = False

    # Inicializar DataFrames
    df1 = None
    df2 = None
    df3 = None

    if uploaded_files:
        # Procesar cada archivo cargado
        for file in uploaded_files:
            st.subheader("Archivo " + file.name+ " cargado correctamente")
            # Leer el archivo Excel en un DataFrame
            if "Exceso de Velocidad" in file.name:
                df1 = exceso_velocidad(file)
                st.write(df1)
                archivo1_cargado = True
            elif "Última posición conocida" in file.name:
                df2 = ultima_ubicacion(file)
                st.write(df2)
                archivo2_cargado = True
            else:
                # Si tienes un tercer archivo con un nombre específico, procesa con la tercera función.
                df3 = uso_vehiculo(file)
                st.write(df3)
                archivo3_cargado = True

            # Nombre del archivo cargado
            

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