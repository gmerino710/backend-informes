from fastapi import APIRouter, Depends, status, HTTPException 
from google import genai
from dotenv import load_dotenv
import os    
import re
import json
from fastapi.responses import JSONResponse       
load_dotenv()  # Carga las variables de entorno desde el archivo .env

# Obtiene las credenciales de la API desde las variables de entorno
API_KEY = os.getenv("GEMINI_API_KEY")

router = APIRouter()
from fastapi import Query

@router.get("/puntos-escenario", response_model=dict, status_code=status.HTTP_200_OK)
async def get_gemini_response(escenario: str = Query(..., description="Escenario de prueba")):
    try:
        # Initialize the Gemini client
        client = genai.Client()
        client.api_key = API_KEY  # Set your API key here
        # Suponiendo que tienes el objetivo del escenario en una variable
        objetivo_escenario = escenario

        # Plantilla del prompt
        prompt = f"""
        Eres un asistente de desarrollo y aseguramiento de calidad (QA). Tu tarea es generar puntos de prueba detallados y específicos.

        Instrucciones:
        1. Analiza el siguiente objetivo de escenario de prueba.
        2. Basándote en el objetivo, genera una lista de 5 puntos de prueba.
        3. Cada punto debe ser una acción concreta que un probador pueda ejecutar.
        4. Incluye tanto pruebas de éxito (validación de inicio de sesión) como de fracaso (manejo de credenciales incorrectas).
        5. Asegúrate de que los puntos de prueba sean claros y fáciles de entender.
        6. Utiliza un lenguaje técnico apropiado para desarrolladores y testers.
        7. No incluyas explicaciones adicionales, solo los puntos de prueba.
        
        Objetivo del Escenario:
        "{objetivo_escenario}"

        Puntos de Prueba:
        """
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                thinking_config=genai.types.ThinkingConfig(thinking_budget=0)  # Disables thinking
            )
        )
     
        
        if not response:
            raise HTTPException(status_code=404, detail="No response from Gemini API")
        
        partes = response.text.split("Puntos de Prueba:", 1)

        if len(partes) > 1:
            texto_limpio = partes[1].strip()
        else:
            texto_limpio = response.text.strip()

        # Opcional: si quieres una lista de Python
        # Dividir el texto por los saltos de línea para obtener una lista
        puntos_de_prueba = texto_limpio.split("\n")

        # Limpiar cada elemento de la lista para quitar la numeración
        puntos_limpios = [re.sub(r'^\d+\.\s*', '', punto).strip() for punto in puntos_de_prueba if punto.strip()]

        return {"response": puntos_limpios}
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener respuesta de Gemini: {str(e)}"
        )   