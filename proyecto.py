import pandas as pd
import psycopg
import sklearn

# 1. Definir la conexión (¡Esto es lo que faltaba arriba!)
conexion = psycopg.connect(
    host="localhost",
    dbname="seniorsafe",
    user="postgres",
    password="12345",
    port="5432"
)


# 2. Consulta SQL para traer las alertas
query = """
    SELECT 
        alerta_id,
        tipo_alerta,
        nivel_riesgo
    FROM alerta
"""

df = pd.read_sql(query, conexion)

# ¡La conexión se cierra al final!


# 3. Asignar un número diferente a cada nivel de riesgo usando .apply()

def convertir_riesgo(riesgo):
    riesgo_str = str(riesgo).lower()
    if riesgo_str == 'critico':
        return 4
    elif riesgo_str == 'alto':
        return 3
    elif riesgo_str == 'medio':
        return 2
    elif riesgo_str == 'bajo':
        return 1
    else:
        return 0

df['nivel_num'] = df['nivel_riesgo'].apply(convertir_riesgo)

# 4. Calcular la cantidad y el porcentaje de cada nivel de riesgo sobre el total

total_alertas = len(df)
conteo_riesgos = df['nivel_riesgo'].value_counts()
porcentaje_riesgos = (conteo_riesgos / total_alertas) * 100

# Creamos la tabla resumen con la cantidad y el porcentaje por categoría

df_porcentajes = pd.DataFrame({
    'Cantidad': conteo_riesgos,
    'Porcentaje (%)': porcentaje_riesgos.round(2)
})

print("=== TABLA GENERAL DE ALERTAS CON NÚMEROS ===")
print(df.head(15))

print("\n" + "="*50 + "\n")
print("=== RESUMEN DE PORCENTAJES POR NIVEL DE RIESGO ===")
print(df_porcentajes)

conexion.close()