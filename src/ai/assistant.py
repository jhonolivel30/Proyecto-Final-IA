"""
    Módulo asistente para HealthWise
    ---------------------------------
    Nombre: Jhon Olivel Castillo Caraballo
    Matricula: 22-SISN-2-063
    
    Este módulo implementa un asistente de salud basado en inteligencia artificial
    que utiliza la API de OpenAI para responder consultas médicas, procesar archivos
    de documentación médica, transcribir audio y generar respuestas en formato de voz.
"""

import os
import tempfile
import base64
from openai import AsyncOpenAI, OpenAI
from config.settings import MAX_TOKENS, OPENAI_API_KEY, OPENAI_MODEL, OPENAI_MODEL_RESPONSE_AUDIO, OPENAI_MODEL_TRANSCRIPTION, RESPONDE_VOICE_NORMAL, SYSTEM_PROMPT


class AIHealthAssistant:
    """
    Clase para manejar la interacción con la API de OpenAI para responder consultas de salud.

    Esta clase proporciona funcionalidades para:
    - Generar respuestas a consultas médicas usando modelos de lenguaje avanzados
    - Procesar archivos médicos como imágenes, PDFs y documentos de texto
    - Transcribir mensajes de audio a texto
    - Convertir respuestas de texto a audio

    Atributos:
        client (OpenAI): Cliente síncrono de OpenAI.
        async_client (AsyncOpenAI): Cliente asíncrono de OpenAI.
        model (str): Modelo de OpenAI a utilizar.
        chat_history (list): Historial de la conversación en formato OpenAI.
        system_prompt (str): Prompt inicial del sistema que define el comportamiento del asistente.
        temp_dir (str): Directorio temporal para almacenar archivos de audio.
    """

    def __init__(self):
        """
        Inicializa el asistente de salud con IA.

        Configura los clientes de OpenAI (síncrono y asíncrono), establece el modelo a usar, 
        inicializa el historial de chat vacío, carga el prompt del sistema y crea un directorio
        temporal para almacenar archivos de audio generados.
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.async_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
        self.chat_history = []  # Almacena la conversación en formato OpenAI
        self.system_prompt = SYSTEM_PROMPT
        self.temp_dir = tempfile.mkdtemp()  # Directorio temporal para archivos de audio

    async def generate_response(self, messages):
        """
        Genera una respuesta basada en IA a partir de los mensajes del usuario.

        Este método toma una lista de mensajes en formato Gradio, los convierte al formato
        de OpenAI, añade el prompt del sistema si es necesario, y envía la consulta al
        modelo de OpenAI para obtener una respuesta.

        Args:
            messages (list): Lista de mensajes en formato de Gradio (diccionarios con 'role' y 'content').

        Returns:
            str: Texto de respuesta generado por el modelo de IA.
                En caso de error, devuelve un mensaje amigable solicitando al usuario intentar de nuevo.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        # Convertir mensajes de formato Gradio a formato OpenAI
        openai_messages = self._convert_to_openai_format(messages)

        # Agregar el mensaje del sistema al inicio si no está ya
        if openai_messages and openai_messages[0].get('role') != 'system':
            openai_messages.insert(
                0, {'role': 'system', 'content': self.system_prompt})

        try:
            # Usar el cliente asíncrono para la respuesta
            response = await self.async_client.chat.completions.create(
                model=self.model,
                messages=openai_messages,
                temperature=0.7,
                max_tokens=MAX_TOKENS,
            )

            # Extraer y devolver el texto de la respuesta
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error al generar respuesta: {e}")
            return "Lo siento, ha ocurrido un error al procesar tu consulta. Por favor, intenta de nuevo más tarde."

    async def process_file(self, file_path):
        """
        Procesa un archivo médico para su análisis utilizando IA.

        Este método analiza diferentes tipos de archivos médicos:
        - Imágenes (.png, .jpg, .jpeg): Analizadas con el modelo de visión de OpenAI
        - PDFs (.pdf): Extrae texto y lo analiza, o analiza visualmente si no hay texto
        - Documentos de texto (.txt, .doc, .docx): Extrae y analiza el contenido textual

        Args:
            file_path (str): Ruta absoluta al archivo que se va a procesar.

        Returns:
            str: Análisis detallado del archivo médico.
                En caso de error, devuelve un mensaje descriptivo del problema.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        if not file_path or not os.path.exists(file_path):
            return "No se pudo procesar el archivo."

        try:
            # Determinar tipo de archivo basado en extensión
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_name)[1].lower()

            # Lista de extensiones permitidas
            allowed_extensions = ['.pdf', '.png',
                                  '.jpg', '.jpeg', '.txt', '.doc', '.docx']

            if file_ext not in allowed_extensions:
                return f"El tipo de archivo {file_ext} no está soportado. Por favor, sube un PDF, imagen o documento de texto."

            print(f"Procesando archivo: {file_name} con extensión {file_ext}")

            # Leer el archivo como bytes
            with open(file_path, "rb") as file:
                file_data = file.read()

            # Determinar el tipo MIME basado en la extensión
            mime_type = None
            if file_ext in ['.png']:
                mime_type = 'image/png'
            elif file_ext in ['.jpg', '.jpeg']:
                mime_type = 'image/jpeg'
            elif file_ext == '.pdf':
                mime_type = 'application/pdf'
            elif file_ext == '.txt':
                mime_type = 'text/plain'
            elif file_ext == '.doc':
                mime_type = 'application/msword'
            elif file_ext == '.docx':
                mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

            # Codificar en base64
            base64_data = base64.b64encode(file_data).decode("utf-8")

            # Procesar según el tipo de archivo
            if file_ext in ['.png', '.jpg', '.jpeg']:
                # Procesar imagen usando el formato correcto de la API de Vision
                print("Procesando imagen médica...")
                file_url = f"data:{mime_type};base64,{base64_data}"

                # Usar el modelo para analizar la imagen con el formato correcto de la API
                response = await self.async_client.responses.create(
                    model=self.model,
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": "Por favor, analiza esta imagen médica y proporciona información detallada sobre lo que muestra. Si es una radiografía, un resultado de examen, o cualquier otra imagen relacionada con la salud, explica lo que puedes ver. Si no hay contenido médico significativo, por favor menciona esto también."},
                                {"type": "input_image",
                                    "image_url": file_url, "detail": "high"}
                            ]
                        }
                    ]
                )
                # Extraer el texto de la respuesta
                analysis = response.output_text

            elif file_ext == '.pdf':
                # Procesar PDF
                print("Procesando documento PDF...")
                # Para PDFs simplemente leemos el texto y enviamos una consulta genérica
                # ya que la API directa de archivos puede ser complicada

                try:
                    # Intento de usar pypdf para extraer texto
                    import pypdf
                    reader = pypdf.PdfReader(file_path)
                    text_content = ""
                    for page in reader.pages:
                        text_content += page.extract_text() + "\n"

                    # Si el PDF tiene texto, lo analizamos
                    if text_content.strip():
                        prompt = f"Analiza este documento médico PDF. Contenido:\n\n{text_content[:4000]}..."
                    else:
                        prompt = "Este PDF parece no contener texto extraíble. Puede ser un documento escaneado o una imagen."
                except Exception as pdf_error:
                    print(f"Error al extraer texto del PDF: {pdf_error}")
                    prompt = "Analiza este documento médico PDF. No pude extraer texto, así que analiza basado en la información visual disponible."

                response = await self.async_client.responses.create(
                    model=self.model,
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": prompt}
                            ]
                        }
                    ]
                )
                # Extraer el texto de la respuesta
                analysis = response.output_text

            else:
                # Documentos de texto
                print(f"Procesando documento de texto ({file_ext})...")

                # Leer contenido como texto si es posible
                try:
                    with open(file_path, 'r', encoding='utf-8') as text_file:
                        text_content = text_file.read()
                    prompt = f"Analiza este documento médico. Contenido:\n\n{text_content[:4000]}..."
                except Exception as text_error:
                    print(f"Error al leer el documento de texto: {text_error}")
                    prompt = f"Analiza este documento médico ({file_name}). No pude extraer el texto debido al formato del archivo."

                response = await self.async_client.responses.create(
                    model=self.model,
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": prompt}
                            ]
                        }
                    ]
                )
                # Extraer el texto de la respuesta
                analysis = response.output_text

            print("Análisis completado correctamente")
            return analysis

        except Exception as e:
            error_msg = f"Error al procesar el archivo: {str(e)}"
            print(error_msg)
            return f"No se pudo analizar el archivo correctamente. Error: {str(e)}"

    async def transcribe_audio(self, audio_file_path):
        """
        Transcribe un archivo de audio a texto utilizando la API de OpenAI.

        Este método toma un archivo de audio grabado por el usuario, verifica
        que sea válido, y lo envía a la API de OpenAI para obtener una transcripción
        textual del contenido hablado.

        Args:
            audio_file_path (str): Ruta absoluta al archivo de audio a transcribir.

        Returns:
            str: Texto transcrito del audio.
                Si ocurre un error o el audio no se puede entender, devuelve un
                mensaje de error descriptivo.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        if not audio_file_path or not os.path.exists(audio_file_path):
            return "No se pudo procesar el audio."

        try:
            # Asegurar que el archivo existe y tiene contenido
            file_size = os.path.getsize(audio_file_path)
            if file_size == 0:
                return "El archivo de audio está vacío."

            with open(audio_file_path, "rb") as audio_file:
                # Usar Whisper a través de la API de OpenAI para transcribir
                transcription = await self.async_client.audio.transcriptions.create(
                    file=audio_file,
                    model=OPENAI_MODEL_TRANSCRIPTION,
                    language="es",
                    response_format="text"
                )

                if not transcription or transcription.strip() == "":
                    return "No pude entender el audio. Por favor, intenta hablar más claro."

                return transcription
        except Exception as e:
            print(f"Error en la transcripción de audio: {e}")
            return "No se pudo transcribir el audio. Por favor, intenta hablar más claro o usa la entrada de texto."

    async def generate_speech(self, text):
        """
        Convierte texto a voz utilizando la API de OpenAI.

        Este método toma un texto y lo convierte en un archivo de audio
        que contiene la versión hablada del mismo, usando la API de generación
        de voz de OpenAI.

        Args:
            text (str): Texto a convertir en voz.

        Returns:
            str o None: Ruta al archivo de audio generado si la operación es exitosa,
                      None si ocurre algún error.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        if not text or text.strip() == "":
            return None

        try:
            response = await self.async_client.audio.speech.create(
                model=OPENAI_MODEL_RESPONSE_AUDIO,  # Modelo de TTS
                voice=RESPONDE_VOICE_NORMAL,  # Voz a utilizar
                input=text,
            )

            # Crear un nombre de archivo único
            audio_file_path = os.path.join(
                self.temp_dir, f"response_{id(text)}.mp3")

            # Guardar el archivo de audio
            with open(audio_file_path, "wb") as f:
                f.write(response.content)

            # Verificar que el archivo se guardó correctamente
            if not os.path.exists(audio_file_path) or os.path.getsize(audio_file_path) == 0:
                print("Error al guardar el archivo de audio")
                return None

            return audio_file_path
        except Exception as e:
            print(f"Error al generar voz: {e}")
            return None

    def _convert_to_openai_format(self, gradio_messages):
        """
        Convierte mensajes del formato de Gradio Chatbot al formato compatible con la API de OpenAI.

        Este método privado toma los mensajes estructurados por Gradio y los transforma
        al formato esperado por la API de OpenAI, filtrando los mensajes inválidos y
        manejando casos especiales como archivos subidos.

        Args:
            gradio_messages (list): Lista de mensajes en formato Gradio (diccionarios con 'role' y 'content').

        Returns:
            list: Lista de mensajes formateados para la API de OpenAI.

        Notas:
            - Los roles válidos son 'user', 'assistant' y 'system'.
            - Si el contenido es un diccionario con una clave 'path', se considera un archivo subido.
            - Los mensajes con formatos no válidos son omitidos.
        """
        if not gradio_messages:
            return []

        openai_messages = []

        for message in gradio_messages:
            # Verificar que el mensaje tiene el formato esperado
            if not isinstance(message, dict) or "role" not in message or "content" not in message:
                continue

            role = message.get('role')
            content = message.get('content')

            # Asegurar que el rol sea válido para OpenAI
            if role not in ['user', 'assistant', 'system']:
                continue

            # Si el contenido es un diccionario con 'path', es un archivo
            if isinstance(content, dict) and 'path' in content:
                # Procesar archivos
                file_path = content.get('path')
                openai_messages.append({
                    'role': role,
                    'content': f"[Archivo subido: {os.path.basename(file_path)}]"
                })
                # No agregamos el archivo directamente a los mensajes de OpenAI
                # En su lugar, lo procesaremos por separado con la API de visión/archivos
                continue

            # Asegurar que el contenido es una cadena de texto
            if not isinstance(content, str):
                continue

            openai_messages.append({
                'role': role,
                'content': content
            })

        return openai_messages
