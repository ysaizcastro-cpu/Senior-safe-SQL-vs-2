import pandas as pd
import psycopg
import sklearn
import joblib

# Piezas del "cerebro artificial" de Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Definir la conexión (¡Esto es lo que faltaba arriba!)
conexion = psycopg.connect(
    host="localhost",
    dbname="seniorsafe",
    user="postgres",
    password="12345",
    port="5432"
)


# 2. Consulta con un JOIN seguro entre Alerta y Hogar## se complementa desde la fila 29 para hacer el modelo predictivo

query = """
SELECT 
    
    a.tipo_alerta,
    a.nivel_riesgo,
    a.estado,
    am.edad,
    dc.fase_etapa
FROM alerta a
JOIN hogar h ON a.hogar_id = h.hogar_id
JOIN adultomayor am ON h.adultomayor_id = am.adultomayor_id
JOIN padecer p ON am.adultomayor_id = p.adultomayor_id
JOIN diagnostico_cognitivo dc ON p.diagnostico_id = dc.diagnostico_id
"""
# Ejecutar y cargar en Pandas

df = pd.read_sql(query, conexion)

# 3. traducir palabras a numeros--- nivel de riesgo critico o alto colocar 1 --de lo contrario 0

df['nivel_num'] = df['nivel_riesgo'].apply(lambda x: 1 if str(x).lower() in ['critico', 'alto'] else 0)

# La fase grave moderada ---10 --- de lo contrario 0

df['fase_num'] = df['fase_etapa'].apply(lambda x: 10 if str (x).lower() in ['grave','moderada'] else 0)

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


# PASO 6: Entrenar la Inteligencia Artificial


# 1. Definir X (las pistas o características: edad y fase de la patología)---definir x pistas edad, y fase num (etapa Y --lo que queremos predecir nivel de riesgo)

X = df[['edad', 'fase_num']]  

# 2. Definir Y (lo que queremos adivinar: si el riesgo es alto/crítico o no)

Y = df['nivel_num']  

# 3. Dividir los datos (80% para estudiar/entrenar, 20% para el examen/prueba)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# 4. Crear el modelo del Árbol de Decisiones y entrenarlo

modelo = DecisionTreeClassifier()
modelo.fit(X_train, Y_train)  # ¡Aquí la IA aprende con los datos de entrenamiento!

print("¡El modelo de Inteligencia Artificial de Senior Safe ha sido entrenado con éxito!")

#5 evaluar modelo datos nuevos 

predicciones = modelo.predict(X_test)
precision = accuracy_score(Y_test, predicciones)

print(f"precision del modelo: {precision * 100}%")

#6 simulando caso nuevo***

adulto_nuevo = pd.DataFrame({
    'edad': [78],
    'fase_num': [10]
})


#pedimos al modelo que adivine el nivel de riesgo de este adulto_nuevo

prediccion_nuevo = modelo.predict(adulto_nuevo)

#mostramos el resultado

if prediccion_nuevo[0] == 1:
    print("\n🚨 Alerta: El modelo predice que este adulto tiene un nivel de riesgo CRITICO O ALTO.")
else:
    print("\n✅ El modelo predice que este adulto tiene un nivel de riesgo BAJO O NORMAL.")           


joblib.dump(modelo, 'modelo_seniorsafe.pkl')
print("📦 ¡Modelo exportado con éxito a 'modelo_seniorsafe.pkl'!")


# Cerrar conexión

conexion.close()
