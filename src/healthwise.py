"""
    HealthWise - Asistente Médico Preliminar
    ---------------------------------
    Nombre: Jhon Olivel Castillo Caraballo
    Matricula: 22-SISN-2-063
    
    Una aplicación que permite a los usuarios describir síntomas y recibir información 
    preliminar sobre posibles condiciones médicas, recomendaciones generales
    y cuándo buscar atención médica profesional.
    
    Este módulo principal es el punto de entrada de la aplicación HealthWise.
    Se encarga de verificar la configuración del entorno, inicializar los componentes
    necesarios y lanzar la interfaz de usuario.
"""

import os
import sys
from dotenv import load_dotenv
from ui.interface import HealthWiseUI


def main():
    """
    Función principal que inicia la aplicación HealthWise.
    
    Este método:
    1. Carga las variables de entorno desde un archivo .env
    2. Verifica que la clave API de OpenAI esté configurada
    3. Inicializa la interfaz de usuario
    4. Lanza la aplicación web
    
    Raises:
        SystemExit: Si no se encuentra configurada la clave API de OpenAI,
                   el programa termina con código de error 1.
    
    Returns:
        None: Esta función no devuelve ningún valor, pero lanza la aplicación
             que se ejecutará hasta que el usuario la cierre.
    """
    # Cargar variables de entorno
    load_dotenv()

    # Verificar la clave API de OpenAI
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️ Error: No se ha configurado la clave API de OpenAI.")
        print("Por favor, crea un archivo .env en la raíz del proyecto con tu clave API.")
        print("Ejemplo: OPENAI_API_KEY=tu-clave-api")
        sys.exit(1)

    # Inicializar y lanzar la interfaz de usuario
    app = HealthWiseUI()
    app.launch()


if __name__ == "__main__":
    main()
