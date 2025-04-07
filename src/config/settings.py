"""
    Módulo de configuración para HealthWise
    ---------------------------------------
    Nombre: Jhon Olivel Castillo Caraballo
    Matricula: 22-SISN-2-063
    
    Este módulo contiene todas las configuraciones y constantes utilizadas en la aplicación
    HealthWise, incluyendo claves de API, modelos utilizados, parámetros de configuración,
    rutas de archivos, y textos predefinidos.
"""

import os
from pathlib import Path


# Ruta del directorio del proyecto
PROJECT_DIR: Path = Path(__file__).resolve().parent.parent.parent
"""Path: Ruta absoluta al directorio raíz del proyecto HealthWise."""

# Configuración OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
"""str o None: Clave de API de OpenAI obtenida de las variables de entorno."""

OPENAI_MODEL = "gpt-4o-mini"
"""str: Modelo principal de OpenAI utilizado para procesar las consultas de los usuarios."""

OPENAI_MODEL_TRANSCRIPTION = "gpt-4o-mini-transcribe"
"""str: Modelo de OpenAI utilizado para la transcripción de audio a texto."""

OPENAI_MODEL_RESPONSE_AUDIO = "gpt-4o-mini-tts"
"""str: Modelo de OpenAI utilizado para la generación de respuestas en formato de audio."""

# Parámetros adicionales
MAX_TOKENS = 800
"""int: Número máximo de tokens permitidos en las respuestas generadas."""

RESPONDE_VOICE_NORMAL = "alloy"
"""str: Tipo de voz utilizada para la generación de respuestas en audio."""


# Configuración de la aplicación
APP_TITLE = "HealthWise - Asistente Médico Preliminar"
"""str: Título de la aplicación que se muestra en la interfaz y en la pestaña del navegador."""

APP_DESCRIPTION = """
HealthWise es una herramienta que permite a los usuarios describir síntomas y recibir información preliminar sobre posibles condiciones médicas y recomendaciones generales.
"""
"""str: Descripción breve de la aplicación que se muestra en la interfaz principal."""

# Configuración de la interfaz de usuario
THEME = "soft"
"""str: Tema visual de Gradio utilizado en la interfaz de usuario."""

PRIMARY_COLOR = "#3498db"
"""str: Color primario en formato hexadecimal utilizado para elementos destacados de la interfaz."""

# Rutas de avatares
USER_AVATAR: Path = PROJECT_DIR / "assets" / "avatar_bot.png"
"""Path: Ruta al archivo de imagen utilizado como avatar del usuario en el chat."""

ASSISTANT_AVATAR: Path = PROJECT_DIR / "assets" / "avatar_user.png"
"""Path: Ruta al archivo de imagen utilizado como avatar del asistente en el chat."""

# Prompt del sistema
SYSTEM_PROMPT = """
Eres una asistente médica virtual llamada Jesse diseñada para proporcionar información médica preliminar.
Tu objetivo es ayudar a los usuarios a entender mejor sus síntomas, analizar documentos médicos, explicar medicamentos y determinar si deben buscar atención médica.

CAPACIDADES:
1. Analizar documentos médicos, recetas e informes para explicarlos en términos sencillos.
2. Explicar medicamentos, incluyendo usos comunes, posibles efectos secundarios y precauciones generales.
3. Interpretar terminología médica compleja de forma accesible.
4. Proporcionar información sobre procedimientos médicos comunes.
5. Ofrecer pautas generales sobre nutrición y estilo de vida saludable.

IMPORTANTE:
1. NUNCA diagnostiques condiciones específicas. Sólo proporciona información general sobre posibles causas.
2. SIEMPRE recomienda consultar a un profesional médico para síntomas preocupantes o dudas sobre medicación.
3. Proporciona información basada en evidencia científica y médica actualizada.
4. Si los síntomas sugieren una emergencia, indica claramente que deben buscar atención médica inmediata.
5. Organiza tu respuesta en secciones relevantes según la consulta (ej: 'Análisis del documento', 'Información del medicamento', 'Posibles causas', 'Recomendaciones generales').
6. Cuando analices documentos o expliques medicamentos, destaca que tu interpretación es informativa y no reemplaza la orientación profesional.

Mantén un tono profesional pero comprensivo y adaptado al nivel de conocimiento médico del usuario.
"""
"""str: Instrucciones detalladas que definen el comportamiento, capacidades y limitaciones
del asistente de IA. Estas instrucciones se envían al inicio de cada conversación."""


if __name__ == "__main__":
    # Para verificar la ruta del proyecto (Debug)
    print("Ruta del proyecto:")
    # Imprime la ruta del directorio del proyecto
    print(PROJECT_DIR)
