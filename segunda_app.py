import streamlit as st

# Conversión de temperatura
def temperatura_conversion():
    st.header("Conversiones de Temperatura")
    opciones_temperatura = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    seleccion_temperatura = st.selectbox("Selecciona una conversión de temperatura:", opciones_temperatura)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_temperatura == "Celsius a Fahrenheit":
        resultado = (valor * 9/5) + 32
    elif seleccion_temperatura == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
    elif seleccion_temperatura == "Celsius a Kelvin":
        resultado = valor + 273.15
    elif seleccion_temperatura == "Kelvin a Celsius":
        resultado = valor - 273.15
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de longitud
def longitud_conversion():
    st.header("Conversiones de Longitud")
    opciones_longitud = ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"]
    seleccion_longitud = st.selectbox("Selecciona una conversión de longitud:", opciones_longitud)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_longitud == "Pies a Metros":
        resultado = valor * 0.3048
    elif seleccion_longitud == "Metros a Pies":
        resultado = valor / 0.3048
    elif seleccion_longitud == "Pulgadas a Centímetros":
        resultado = valor * 2.54
    elif seleccion_longitud == "Centímetros a Pulgadas":
        resultado = valor / 2.54
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de peso/masa
def peso_conversion():
    st.header("Conversiones de Peso/Masa")
    opciones_peso = ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"]
    seleccion_peso = st.selectbox("Selecciona una conversión de peso/masa:", opciones_peso)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_peso == "Libras a Kilogramos":
        resultado = valor * 0.453592
    elif seleccion_peso == "Kilogramos a Libras":
        resultado = valor / 0.453592
    elif seleccion_peso == "Onzas a Gramos":
        resultado = valor * 28.3495
    elif seleccion_peso == "Gramos a Onzas":
        resultado = valor / 28.3495
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de volumen
def volumen_conversion():
    st.header("Conversiones de Volumen")
    opciones_volumen = ["Galones a Litros", "Litros a Galones", "Pulgadas Cúbicas a Centímetros Cúbicos", "Centímetros Cúbicos a Pulgadas Cúbicas"]
    seleccion_volumen = st.selectbox("Selecciona una conversión de volumen:", opciones_volumen)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_volumen == "Galones a Litros":
        resultado = valor * 3.78541
    elif seleccion_volumen == "Litros a Galones":
        resultado = valor / 3.78541
    elif seleccion_volumen == "Pulgadas Cúbicas a Centímetros Cúbicos":
        resultado = valor * 16.3871
    elif seleccion_volumen == "Centímetros Cúbicos a Pulgadas Cúbicas":
        resultado = valor / 16.3871
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de tiempo
def tiempo_conversion():
    st.header("Conversiones de Tiempo")
    opciones_tiempo = ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"]
    seleccion_tiempo = st.selectbox("Selecciona una conversión de tiempo:", opciones_tiempo)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_tiempo == "Horas a Minutos":
        resultado = valor * 60
    elif seleccion_tiempo == "Minutos a Segundos":
        resultado = valor * 60
    elif seleccion_tiempo == "Días a Horas":
        resultado = valor * 24
    elif seleccion_tiempo == "Semanas a Días":
        resultado = valor * 7
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de velocidad
def velocidad_conversion():
    st.header("Conversiones de Velocidad")
    opciones_velocidad = ["Millas por Hora a Kilómetros por Hora", "Kilómetros por Hora a Metros por Segundo", "Nudos a Millas por Hora", "Metros por Segundo a Pies por Segundo"]
    seleccion_velocidad = st.selectbox("Selecciona una conversión de velocidad:", opciones_velocidad)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_velocidad == "Millas por Hora a Kilómetros por Hora":
        resultado = valor * 1.60934
    elif seleccion_velocidad == "Kilómetros por Hora a Metros por Segundo":
        resultado = valor * 0.277778
    elif seleccion_velocidad == "Nudos a Millas por Hora":
        resultado = valor * 1.15078
    elif seleccion_velocidad == "Metros por Segundo a Pies por Segundo":
        resultado = valor * 3.28084
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de área
def area_conversion():
    st.header("Conversiones de Área")
    opciones_area = ["Metros Cuadrados a Pies Cuadrados", "Pies Cuadrados a Metros Cuadrados", "Kilómetros Cuadrados a Millas Cuadradas", "Millas Cuadradas a Kilómetros Cuadrados"]
    seleccion_area = st.selectbox("Selecciona una conversión de área:", opciones_area)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_area == "Metros Cuadrados a Pies Cuadrados":
        resultado = valor * 10.7639
    elif seleccion_area == "Pies Cuadrados a Metros Cuadrados":
        resultado = valor / 10.7639
    elif seleccion_area == "Kilómetros Cuadrados a Millas Cuadradas":
        resultado = valor * 0.386102
    elif seleccion_area == "Millas Cuadradas a Kilómetros Cuadrados":
        resultado = valor / 0.386102
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de energía
def energia_conversion():
    st.header("Conversiones de Energía")
    opciones_energia = ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-Hora a Megajulios", "Megajulios a Kilovatios-Hora"]
    seleccion_energia = st.selectbox("Selecciona una conversión de energía:", opciones_energia)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_energia == "Julios a Calorías":
        resultado = valor * 0.239006
    elif seleccion_energia == "Calorías a Kilojulios":
        resultado = valor / 0.239006
    elif seleccion_energia == "Kilovatios-Hora a Megajulios":
        resultado = valor * 3.6
    elif seleccion_energia == "Megajulios a Kilovatios-Hora":
        resultado = valor / 3.6
    
    st.write(f"Resultado: {resultado:.2f}")

# Conversión de presión
def presion_conversion():
    st.header("Conversiones de Presión")
    opciones_presion = ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por Pulgada Cuadrada", "Libras por Pulgada Cuadrada a Bares"]
    seleccion_presion = st.selectbox("Selecciona una conversión de presión:", opciones_presion)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_presion == "Pascales a Atmósferas":
        resultado = valor * 9.86923e-6
    elif seleccion_presion == "Atmósferas a Pascales":
        resultado = valor / 9.86923e-6
    elif seleccion_presion == "Barras a Libras por Pulgada Cuadrada":
        resultado = valor * 14.5038
    elif seleccion_presion == "Libras por Pulgada Cuadrada a Bares":
        resultado = valor / 14.5038
    
    st.write(f"Resultado: {resultado:.4f}")

# Conversión de tamaño de datos
def datos_conversion():
    st.header("Conversiones de Tamaño de Datos")
    opciones_datos = ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
    seleccion_datos = st.selectbox("Selecciona una conversión de tamaño de datos:", opciones_datos)
    
    valor = st.number_input("Ingresa el valor a convertir:")
    resultado = 0.0
    
    if seleccion_datos == "Megabytes a Gigabytes":
        resultado = valor * 0.001
    elif seleccion_datos == "Gigabytes a Terabytes":
        resultado = valor * 0.001
    elif seleccion_datos == "Kilobytes a Megabytes":
        resultado = valor * 0.001
    elif seleccion_datos == "Terabytes a Petabytes":
        resultado = valor * 0.001
    
    st.write(f"Resultado: {resultado:.4f}")

# Menú principal
def main():
    st.title("App de Conversiones")
    opciones_conversiones = [
        "Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo",
        "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"
    ]
    seleccion_conversion = st.sidebar.selectbox("Selecciona el tipo de conversión:", opciones_conversiones)
    
    if seleccion_conversion == "Temperatura":
        temperatura_conversion()
    elif seleccion_conversion == "Longitud":
        longitud_conversion()
    elif seleccion_conversion == "Peso/Masa":
        peso_conversion()
    elif seleccion_conversion == "Volumen":
        volumen_conversion()
    elif seleccion_conversion == "Tiempo":
        tiempo_conversion()
    elif seleccion_conversion == "Velocidad":
        velocidad_conversion()
    elif seleccion_conversion == "Área":
        area_conversion()
    elif seleccion_conversion == "Energía":
        energia_conversion()
    elif seleccion_conversion == "Presión":
        presion_conversion()
    elif seleccion_conversion == "Tamaño de Datos":
        datos_conversion()

if __name__ == "__main__":
    main()
