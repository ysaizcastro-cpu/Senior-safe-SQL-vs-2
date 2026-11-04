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


# 2. Consulta con un JOIN seguro entre Alerta y Hogar

query = """
    SELECT 
        a.alerta_id,
        h.municipio,
        a.tipo_alerta,
        a.nivel_riesgo,
        a.estado
    FROM alerta a
    JOIN hogar h ON a.hogar_id = h.hogar_id
"""

# Ejecutar y cargar en Pandas

df = pd.read_sql(query, conexion)

# 3. Mantener la columna original con letras y crear una numérica por si la necesitas para el modelo

df['nivel_num'] = df['nivel_riesgo'].apply(lambda x: 1 if str(x).lower() in ['critico', 'alto'] else 0)

# 4. Calcular porcentajes usando los textos originales de los niveles de riesgo

total_alertas = len(df)
conteo_riesgos = df['nivel_riesgo'].value_counts()
porcentaje_riesgos = (conteo_riesgos / total_alertas) * 100

# Crear la tabla resumen de porcentajes

df_porcentajes = pd.DataFrame({
    'Cantidad': conteo_riesgos,
    'Porcentaje (%)': porcentaje_riesgos.round(2)
})

# 5. Mostrar resultados en consola

print("=== TABLA GENERAL COMPLETÍSIMA DE SENIOR SAFE ===")
print(df)


print("=== RESUMEN DE PORCENTAJES POR NIVEL DE RIESGO ===")
print(df_porcentajes)

# Cerrar conexión

conexion.close()
