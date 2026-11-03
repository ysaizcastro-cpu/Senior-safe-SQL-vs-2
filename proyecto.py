import pandas as pd
import psycopg
import sklearn

# Configurar Pandas para que muestre todas las columnas y no las oculte
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("¡Todo listo con el INNER JOIN de Senior Safe!")

conexion = psycopg.connect(
    host="localhost", 
    dbname="seniorsafe", 
    user="postgres", 
    password="12345", 
    port="5432"
)

query = """
    SELECT *
	FROM alerta
	WHERE fecha_hora BETWEEN '2026-01-01 12:00' AND '2026-12-31 11:55';
"""
df = pd.read_sql(query, conexion)

print("¡Consulta exitosa con datos cruzados!")
print(df)


query_1 ="""
	 SELECT 
      alerta.*,
      hogar.*
     FROM 
      alerta
       
	INNER JOIN hogar ON alerta.hogar_id = hogar.hogar_id
"""
df_1 = pd.read_sql(query_1, conexion)

print("¡Consulta exitosa con Municipios cruzados!")
print(df_1)


conexion.close()