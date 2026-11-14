from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# fastapy convierte archivo python en un servidor web, Basemodel valida que los datos tengan estructura correcta, joblib abre el archivo pkl

# Encender motores cargar IA 

app = FastAPI()
modelo_ia = joblib.load('modelo_seniorsafe.pkl')

# MOLDE del mensaje 

class DatosSensor(BaseModel):
    nombre_paciente: str
    edad: int
    fase_etapa: str
    nivel_riesgo: int
    sensor_movimiento: str

    # ENDPOINT

@app.post("/evaluar_sensor")
def evaluar_riesgo(datos: DatosSensor):
    fase_lower = str(datos.fase_etapa).lower()
    
    # Mapeo de la fase para la IA

    if fase_lower in ["grave", "moderada"]:
        fase_num = 10
    else:
        fase_num = 0

    # DataFrame para la IA

    df_ia = pd.DataFrame({
        'edad': [datos.edad], 
        'fase_num': [fase_num]
    })
    
   # Lógica de negocio basada en el nivel de riesgo (síntomas) y edad
   
    if datos.nivel_riesgo == 1 or (datos.edad >= 70 and fase_lower in ["grave", "moderada"]):
        return {"estado": "🚨 CRÍTICO O ALTO", "accion": "Notificar a familiar"}
    else:
        return {"estado": "✅ BAJO NORMAL", "accion": "Solo registrar"}
    