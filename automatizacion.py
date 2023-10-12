from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import credenciales
import streamlit as st
import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd
from datetime import datetime


def GPS():
    #browser = webdriver.Chrome('./chromedriver.exe')
    browser = webdriver.Chrome()
    browser.set_window_size(1530, 1200)  # Ejemplo para una resolución de pantalla de 1920x1080

    # Abre GPS TRACKER
    browser.get('https://www.trackergps.com/ven/clientes')

    wait = WebDriverWait(browser, 30)
    # Ingresa usuario y contraseña
    username_elem = wait.until(EC.presence_of_element_located((By.ID, 'txtUserLogin')))
    username_elem.send_keys(credenciales.usuario)
    password_elem = wait.until(EC.presence_of_element_located((By.ID, 'txtPassword')))
    password_elem.send_keys(credenciales.clave)
    password_elem.send_keys(Keys.RETURN)
    # hacemos click en la ventana ok
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
    ok_button.click()
    #hacemos click en el boton menu
    button = browser.find_element(By.CSS_SELECTOR, "button.navbar-toggler")
    button.click()
    # seleccionamos la opcion menu
    reportes_element = browser.find_element(By.XPATH, "//span[@class='menu-title' and text()=' Reportes']")
    reportes_element.click()
    # luego el submenu reportes
    reportes_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and text()='Reportes ']")))
    # Hacemos click en el enlace
    reportes_link.click()
    # buscamos la opcion lhistorico de localizacion
    localizacion = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Históricos de localización')]")))
    # Hacemos clic en el historial de localizacion
    localizacion.click()
    # Buscamos el reporte de exceso de velocidad
    exceso_velocidad = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Reporte de Exceso de Velocidad')]")))
    # Hacer clic en Reporte de exceso de velocidad
    exceso_velocidad.click()
    # buscamos el switch
    switch_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dx-switch-handle')))
    # Hacer clic en el switch
    switch_button.click()
    # Espera explícita para asegurarse de que la flecha esté visible
    arrow_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='dx-button-content']/i[@class='dx-icon dx-icon-arrowright']")))
    # Hacer clic en la flecha
    arrow_button.click()
    # Localizar el botón para generar reporte
    boton_generar_reporte = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Generar reporte"]')))
    time.sleep(1)
    # Hacer clic en el botón generar reporte
    boton_generar_reporte.click()
    # localizar y exportar a excel el archivo de exceso dde velocidad
    elemento_exportar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.dx-button-content>i.dx-icon-exportxlsx')))
    # Hacer clic para exportar a excel
    elemento_exportar.click()
    time.sleep(2)
    browser.get('https://cloud.ve.trackergps.com/home')
    #time.sleep(2)
    #hacemos click en la ventana emergente
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
    time.sleep(1)
    ok_button.click()
    # nuevamente en el menu
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.navbar-toggler")))
    button.click()
    time.sleep(1)
    # en la opcion logistica
    logistica_span = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='p-2 m-2 pl-3 mb-0 pb-0 rounded-top sub-menu-report']//span[@class='menu-title' and text()='Logística']")))
    logistica_span.click()
    # buscamos la opcion ultima posicion conocida
    ultima_posicion = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='menu-title ml-2' and text()=' Última posición conocida']")))
    ultima_posicion.click()
    # buscamos el switch
    switch_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'dx-switch-off')))
    # Hacer clic en el switch
    switch_button.click()
    # cerramos el anuncio 
    close_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa.fa-times.cursor-pointer")))
    close_icon.click()
    # seleccionamos la flecha para avanzar
    arrowright_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dx-button-content > i.dx-icon-arrowright")))
    arrowright_button.click()
    # Localizar el botón para generar reporte
    report_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Generar reporte']")))
    time.sleep(1)
    report_button.click()
    # localizar y exportar a excel el archivo de ultima posicion conocida
    elemento_exportar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.dx-button-content>i.dx-icon-exportxlsx')))
    # Hacer clic para exportar a excel
    elemento_exportar.click()
    time.sleep(2)
    # regresamos al home
    browser.get('https://cloud.ve.trackergps.com/home')
    time.sleep(1)
    # cerramos la ventana emergente
    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
    time.sleep(1)
    ok_button.click()
    time.sleep(1)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.navbar-toggler")))
    button.click()
    time.sleep(1)
    logistica_span = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='p-2 m-2 pl-3 mb-0 pb-0 rounded-top sub-menu-report']//span[@class='menu-title' and text()='Logística']")))
    logistica_span.click()
    close_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.fa.fa-times.cursor-pointer")))
    close_icon.click()
    # Localizar el elemento por el texto "Uso del Vehículo"
    us0_vehiculo = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='menu-title ml-2' and text()=' Uso del Vehículo']")))
    us0_vehiculo.click()
    switch_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'dx-switch-off')))
    # Hacer clic en el switch
    switch_button.click()
    arrowright_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dx-button-content > i.dx-icon-arrowright")))
    arrowright_button.click()
    time.sleep(1)
    report_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Generar reporte']")))
    report_button.click()
    # exportamos a excel el archivo de Uso del vehiculo
    elemento_exportar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.dx-button-content>i.dx-icon-exportxlsx')))
    elemento_exportar.click()
    time.sleep(2)
    browser.get('https://cloud.ve.trackergps.com/home')
    return "Proceso culiminado"

def exceso_velocidad(excel):
    # Cargar el archivo Excel en un DataFrame
    df = pd.read_excel(excel, header=8)
    # Seleccionar las columnas necesarias
    df = df[['Fecha de Reporte ','Unidad ','Estado ', 'Velocidad (km/h)']]
    # Filtrar las filas donde 'Unidad ' es "ForesightGPS" o NaN
    filas_remover = df[df['Unidad '].isna() | (df['Unidad '] == 'ForesightGPS')].index
    # Eliminar esas filas del DataFrame
    df_cleaned = df.drop(filas_remover)
    # Agrupar por Unidad y estado para calcular el promedio de la velocidad
    
    # Filtrar las filas donde la velocidad es mayor a 100 km/h
    df_filtrado = df_cleaned[df_cleaned["Velocidad (km/h)"] > 100]
    # hacemos una copia del df
    df_filtrado = df_filtrado.copy()
    # Agrupar por "Unidad " (con espacio) y agregar las velocidades en una lista
    df_filtrado['Alta velocidad'] = df_filtrado.groupby(['Unidad ', 'Estado '])["Velocidad (km/h)"].transform(lambda x: ', '.join(map(str, x)))
    # Eliminar duplicados
    df_final = df_filtrado.drop_duplicates(subset='Unidad ').reset_index(drop=True)
    # Agrupar por "Unidad " y "Estado " y agregar las velocidades en una lista
    df_filtrado['Veces Excedido'] = df_filtrado.groupby(['Unidad ', 'Estado '])["Velocidad (km/h)"].transform(lambda x: len(x))
    # Eliminar duplicados basados en "Unidad " y "Estado "
    df_final = df_filtrado.drop_duplicates(subset=['Unidad ', 'Estado ']).reset_index(drop=True)
    #filtramos
    df_final = df_final[['Unidad ', 'Estado ', 'Veces Excedido' ,'Alta velocidad']]
    #renombramos columnas
    df_final = df_final.rename(columns={'Velocidad (km/h)': "Velocidad promedio", 'Veces Excedido':'Veces Excedido por minuto','Alta velocidad':"Por encima de 100"})
    df_final['Veces Excedido por minuto'] = df_final['Veces Excedido por minuto'].astype("int64")
    df_final = df_final.sort_values(by='Veces Excedido por minuto', ascending=True)
    df_definitivo =  df_final.copy()
    df_definitivo = df_definitivo[df_definitivo['Veces Excedido por minuto'] >= 10]
    return df_definitivo

def ultima_ubicacion(excel):
    df = pd.read_excel(excel, header=8)
    df = df[['Último reporte ','Unidad ','Conductor ','Localización ']]
    texto_a_eliminar = "GH2103 4D"
    df = df[df['Unidad '] != texto_a_eliminar]
    df['Localización '] = df['Localización '].str.split(',').str[:3].str.join(',')
    filas_remover = df[df['Unidad '].isna() | (df['Unidad '] == 'ForesightGPS')].index
    
    # Eliminar esas filas del DataFrame
    df_cleaned = df.drop(filas_remover)
    df_cleaned['Conductor '].fillna('SIN CHOFER ASIGNADO', inplace=True)
    df_cleaned = df_cleaned.sort_values(by='Conductor ',ascending=False ,key=lambda x: x != 'SIN CHOFER ASIGNADO')
    return df_cleaned

def uso_vehiculo(excel):
    # Cargar el archivo Excel en un DataFrame
    df2 = pd.read_excel(excel, header=8)
    # Seleccionar las columnas necesarias
    df2 = df2[['Unidad ', 'Conductor ','Kilometraje (km)','Horas de Uso (h) ']]
    # Encontrar las filas que cumplen las condiciones
    filas_remover = df2[df2['Unidad '].isna() | (df2['Unidad '] == 'ForesightGPS')].index
    # Eliminar esas filas del DataFrame
    df2_limpio = df2.drop(filas_remover)
    # Renombrar las columnas
    df2_limpio = df2_limpio.rename(columns={"Kilometraje (km)":"Kilometros recorridos", "Horas de Uso (h) ":"Horas de recorrido"})
    df2_limpio['Conductor '].fillna('SIN CHOFER ASIGNADO', inplace=True)
    df2_limpio = df2_limpio.sort_values(by='Kilometros recorridos', ascending=True)
    df2_limpio = df2_limpio[df2_limpio['Kilometros recorridos'] > 15]
    return df2_limpio

def enviar_email(archivo_adjunto):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
    hora_actual = datetime.now().time()
    if hora_actual.hour < 12:
        saludo = "Buenos Dias"
    else:
        saludo = "Buenas Tardes"
    emisor = credenciales.correo  # Cambia esto por tu dirección de correo Gmail
    clave = credenciales.contraseña  # Cambia esto por tu contraseña de correo Gmail
    receptores = ["gustavoboadalugo@gmail.com","gustavoserviplus@gmail.com"]  # Cambia esto por la dirección de correo destino

    asunto = f"Reporte GPS TRACKER"
    cuerpo = f"""{saludo} reciban un cordial saludo, en este archivo podrán visualizar informacion obtenida de GPS TRACKER del dia {fecha_formateada} que muestra:

            - Reporte donde la Unidad Estuvo encendida, que muestra la fecha de la ultima ubicacion. y la direccion donde se encuentra.
            - Reporte de Exceso de Velocidad agrupado por Unidad y estado, que muestra la cantidad de veces que se excedio de 100 km/h, y la velcidad exactas excediad separadas por comas. 
            - Reporte del recorrido que muestra los kilometros y horas del recorrido.

                
Este es un correo automatizado por Gustavo Boada 
Data Analyst Senior.
Tlf: 04141240654 / 04126050917"""

    em = EmailMessage()
    em["From"] = emisor
    em["To"] = ", ".join(receptores)
    em["Subject"] = asunto
    em.set_content(cuerpo)

    # Leer el contenido del archivo PDF cargado desde el uploader
    archivo = archivo_adjunto.read()
    em.add_attachment(archivo, maintype="application", subtype="pdf", filename=f"Reporte-{fecha_formateada}.pdf")

    contexto = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
            smtp.login(emisor, clave)
            smtp.sendmail(emisor, receptores, em.as_string())
    except Exception as e:
        st.error(f"Error al enviar el correo electrónico: {str(e)}")