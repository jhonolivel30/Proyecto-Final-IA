"""
    Módulo de interfaz para HealthWise
    ---------------------------------
    Nombre: Jhon Olivel Castillo Caraballo
    Matricula: 22-SISN-2-063
    
    Este módulo implementa la interfaz de usuario de la aplicación HealthWise,
    proporcionando una experiencia interactiva mediante componentes de Gradio
    para la consulta médica, procesamiento de archivos y respuestas en formato
    de texto y voz.
"""


import gradio as gr
import os
import asyncio
from config.settings import APP_TITLE, APP_DESCRIPTION, THEME, PRIMARY_COLOR, USER_AVATAR, ASSISTANT_AVATAR
from ai.assistant import AIHealthAssistant
from gradio_modal import Modal  # type: ignore
from ui.custom import Custom  # type: ignore


class HealthWiseUI:
    """
    Clase para manejar la interfaz de usuario de la aplicación HealthWise.

    Esta clase proporciona todos los componentes de interfaz necesarios para:
    - Mostrar y gestionar conversaciones de chat médico
    - Procesar entradas multimodales (texto, voz, imágenes y documentos)
    - Generar respuestas en formato de texto y audio
    - Presentar recursos útiles y ejemplos para el usuario

    Atributos:
        assistant (AIHealthAssistant): Instancia del asistente de IA para procesar consultas.
        is_processing (bool): Indicador de si hay una consulta en procesamiento.
        custom_css (str): Estilos CSS personalizados para la interfaz.
        ejemplos_medicos_modal (str): Contenido HTML del modal de ejemplos médicos.
        info_modal (str): Contenido HTML del modal de información sobre HealthWise.
        recursos_modal (str): Contenido HTML del modal de recursos médicos confiables.
        emergencias_modal (str): Contenido HTML del modal de información sobre emergencias.
        consejos_modal (str): Contenido HTML del modal de consejos saludables.
        chat_history (list): Historial de la conversación actual.
        interface (gradio.Blocks): Interfaz principal de Gradio con todos los componentes.
    """

    def __init__(self):
        """
        Inicializa la interfaz de usuario y el asistente IA.

        Crea una instancia del asistente de IA, inicializa las variables de estado,
        carga los contenidos de los modales desde el módulo Custom, inicializa el
        historial de chat y construye la interfaz de usuario completa.
        """
        self.assistant = AIHealthAssistant()
        self.is_processing = False
        self.custom_css = Custom().custom_css
        self.ejemplos_medicos_modal = Custom().ejemplos_modal
        self.info_modal = Custom().info_modal
        self.recursos_modal = Custom().recursos_modal
        self.emergencias_modal = Custom().emergencias_modal
        self.consejos_modal = Custom().consejos_modal
        self.chat_history = []
        self.interface = self.build_interface()

    def build_interface(self):
        """
        Construye la interfaz de usuario completa usando componentes de Gradio.

        Este método crea y configura todos los elementos de la interfaz:
        - Encabezado y descripción de la aplicación
        - Ventanas modales para información y recursos
        - Componente de chat con avatares
        - Área de entrada multimodal para texto y archivos
        - Grabación y reproducción de audio
        - Botones de control y opciones de configuración
        - Enlaces de eventos para todas las interacciones

        Returns:
            gradio.Blocks: Objeto de interfaz completo listo para ser lanzado.
        """
        with gr.Blocks(theme=THEME, title=APP_TITLE, css=self.custom_css) as interface:
            # Encabezado con estilo mejorado
            gr.Markdown(f"# {APP_TITLE} 🏥 💊 🩺")
            gr.Markdown(f"### {APP_DESCRIPTION}")

            # Definición de modales para información con estilos de alto contraste
            with Modal(visible=False, allow_user_close=True) as modal_ejemplos:
                # Ejemplos de consultas médicas
                gr.Markdown(self.ejemplos_medicos_modal)

            with Modal(visible=False, allow_user_close=True) as modal_info:
                # HealthWise info modal
                gr.Markdown(self.info_modal)

            with Modal(visible=False, allow_user_close=True) as modal_recursos:
                # Recursos confiables
                gr.Markdown(self.recursos_modal)

            with Modal(visible=False, allow_user_close=True) as modal_emergencias:
              # Emergencias Modal
                gr.Markdown(self.emergencias_modal)

            with Modal(visible=False, allow_user_close=True) as modal_consejos:
                gr.Markdown(self.consejos_modal)

            with gr.Row():
                # Columna principal (chat y entrada)
                with gr.Column(scale=4):
                    # Componente principal: Chatbot
                    chatbot = gr.Chatbot(
                        [],
                        type="messages",
                        elem_id="chatbot",
                        show_copy_button=True,
                        bubble_full_width=False,
                        height=620,  # Aumentado ligeramente para más espacio
                        avatar_images=(
                            ASSISTANT_AVATAR,  # Avatar del asistente
                            USER_AVATAR       # Avatar del usuario
                        ),
                    )

                    # Sección de entrada con mejor organización
                    with gr.Row():
                        # Entrada multimodal para el usuario (texto y archivos) con más espacio
                        user_input = gr.MultimodalTextbox(
                            show_label=False,
                            placeholder="✍️ Describe tus síntomas o haz una pregunta médica.",
                            elem_id="user_input",
                            scale=6,
                            file_types=["image", "text",
                                        "application/pdf", "application"],
                            render=True,
                        )

                    # Indicador de procesamiento mejorado (ahora ubicado encima de los botones)
                    with gr.Row(visible=False) as processing_indicator:
                        with gr.Column():
                            status_box = gr.Markdown(
                                """<div style="display: flex; align-items: center; justify-content: center; background-color: #f0f8ff; padding: 10px; border-radius: 8px; border-left: 6px solid #007bff; margin-bottom: 10px;">
                                <div style="margin-right: 10px;"><span style="font-size: 20px;">⏳</span></div>
                                <div style="font-weight: bold; color: #007bff;">Procesando tu consulta... Por favor espera...</div>
                                </div>""",
                                elem_id="processing_status"
                            )

                    # Botones de control en una fila separada para mayor consistencia visual
                    with gr.Row():
                        # Botones con tamaño consistente y mejor espaciado
                        submit_btn = gr.Button(
                            "📤 Enviar mensaje",
                            variant="primary",
                            scale=1,
                            min_width=150  # Ancho mínimo para consistencia
                        )

                        voice_input_btn = gr.Button(
                            "🎤 Hablar",
                            scale=1,
                            min_width=150  # Mismo ancho que el botón de enviar
                        )

                        clear_btn = gr.Button(
                            "🗑️ Borrar chat",
                            variant="secondary",
                            scale=1,
                            min_width=150  # Mismo ancho que los otros botones
                        )

                # Columna lateral (opciones y ayuda)
                with gr.Column(scale=2):
                    # Panel de configuración mejorado
                    with gr.Group():
                        gr.Markdown("### ⚙️ Configuración")

                        # Checkbox para habilitar respuestas por voz
                        tts_enabled = gr.Checkbox(
                            label="🔊 Activar respuestas por voz",
                            value=False,
                            info="Escuchar respuestas en formato audio"
                        )

                    # Sección de botones para abrir modales mejorados
                    with gr.Group():
                        gr.Markdown("### 📚 Recursos de ayuda")

                        with gr.Row():
                            btn_ejemplos = gr.Button("📋 Ejemplos de consultas", elem_classes=[
                                                     "resource-btn", "examples-btn"])
                            btn_info = gr.Button("ℹ️ Sobre HealthWise", elem_classes=[
                                                 "resource-btn", "info-btn"])

                        with gr.Row():
                            btn_recursos = gr.Button("📚 Recursos médicos", elem_classes=[
                                                     "resource-btn", "resources-btn"])
                            btn_emergencias = gr.Button("🚨 Emergencias", elem_classes=[
                                                        "resource-btn", "emergency-btn"])

                        with gr.Row():
                            btn_consejos = gr.Button("💪 Consejos saludables", elem_classes=[
                                                     "resource-btn", "health-btn"])

                    # Ejemplos rápidos en formato acordeón (oculto por defecto)
                    with gr.Accordion("📝 Ejemplos rápidos", open=False):
                        gr.Examples(
                            examples=[
                                ["Tengo dolor de cabeza intenso y sensibilidad a la luz desde ayer 🤕"],
                                ["¿Qué medicamento es mejor para la fiebre? 🤒"],
                                ["¿Cuáles son los síntomas comunes de diabetes? 🩸"],
                                ["Tengo tos seca y dolor de garganta, ¿qué podría ser? 😷"],
                                ["¿Cuándo debo preocuparme por un dolor en el pecho? ❤️"],
                                ["¿Cómo puedo aliviar el dolor de espalda? 🦴"],
                                ["¿Qué alimentos son buenos para la presión arterial alta? 🥗"],
                                ["Mi hijo tiene erupción cutánea y fiebre, ¿qué podría ser? 👶"],
                            ],
                            inputs=user_input,
                            label=""
                        )

            # Componente Audio para entrada de voz (oculto visualmente)
            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                visible=False,
                label="🎤 Grabación de voz"
            )

            # Componente Audio para salida de voz (oculto hasta que se genere)
            audio_output = gr.Audio(
                visible=False,
                elem_id="tts_output",
                autoplay=True
            )

            # === Conexiones de eventos para modales ===
            btn_ejemplos.click(fn=lambda: Modal(
                visible=True), outputs=modal_ejemplos)
            btn_info.click(fn=lambda: Modal(visible=True), outputs=modal_info)
            btn_recursos.click(fn=lambda: Modal(
                visible=True), outputs=modal_recursos)
            btn_emergencias.click(fn=lambda: Modal(
                visible=True), outputs=modal_emergencias)
            btn_consejos.click(fn=lambda: Modal(
                visible=True), outputs=modal_consejos)

            # === Conexiones de eventos ===

            # Botón de entrada de voz activa el micrófono
            voice_input_btn.click(
                fn=self.toggle_audio_input,
                outputs=[audio_input, processing_indicator],
                show_progress="minimal"
            )

            # Procesar audio cuando se envía - usando función sincrónica como wrapper
            audio_input.stop_recording(
                fn=self.process_audio_input_wrapper,
                inputs=[audio_input],
                outputs=[user_input, audio_input, processing_indicator],
                show_progress="minimal"
            )

            # Enviar mensaje (tanto por botón como por Enter en el textbox)
            submit_event = submit_btn.click(
                fn=self.add_user_message,
                inputs=[chatbot, user_input],
                outputs=[chatbot, user_input, processing_indicator],
                show_progress="minimal"
            ).then(
                fn=self.generate_assistant_response_wrapper,
                inputs=[chatbot, tts_enabled],
                outputs=[chatbot, audio_output, processing_indicator],
                show_progress="minimal"
            )
            # Usar el mismo evento para el textbox
            user_input.submit(
                fn=self.add_user_message,
                inputs=[chatbot, user_input],
                outputs=[chatbot, user_input, processing_indicator],
                show_progress="minimal"
            ).then(
                fn=self.generate_assistant_response_wrapper,
                inputs=[chatbot, tts_enabled],
                outputs=[chatbot, audio_output, processing_indicator],
                show_progress="minimal"
            )

            # Borrar conversación
            clear_btn.click(
                fn=self.clear_conversation,
                outputs=[chatbot, audio_output],
                show_progress="minimal"
            )

            # Evento de retroalimentación (like/dislike)
            chatbot.like(
                fn=self.handle_feedback,
                inputs=[chatbot]
            )

        return interface

    def toggle_audio_input(self):
        """
        Activa/desactiva la entrada de audio para grabación de voz.

        Este método muestra u oculta el componente de grabación de audio y
        actualiza el indicador de procesamiento según corresponda.

        Returns:
            tuple: Contiene el componente de audio actualizado y el indicador de procesamiento.
        """
        return gr.Audio(
            sources=["microphone"],
            type="filepath",
            visible=True,
            label="🎤 Habla claramente al micrófono"
        ), gr.Row(visible=True)

    def process_audio_input_wrapper(self, audio_file):
        """
        Wrapper sincrónico para el método asincrónico de procesamiento de audio.

        Este método crea un nuevo bucle de eventos para ejecutar la función asincrónica
        que procesa el archivo de audio grabado por el usuario.

        Args:
            audio_file (str): Ruta al archivo de audio grabado.

        Returns:
            tuple: Contiene el texto transcrito, el componente de audio actualizado
                  y el indicador de procesamiento actualizado.
        """
        if not audio_file:
            return "", gr.Audio(visible=False), gr.Row(visible=False)

        # Crear un nuevo event loop en lugar de intentar obtener uno existente
        new_loop = asyncio.new_event_loop()
        try:
            result = new_loop.run_until_complete(
                self._process_audio_input_async(audio_file))
            return result[0], result[1], gr.Row(visible=False)
        finally:
            new_loop.close()

    async def _process_audio_input_async(self, audio_file):
        """
        Implementación asincrónica del procesamiento de audio.

        Utiliza el asistente IA para transcribir el audio a texto usando
        la API de OpenAI.

        Args:
            audio_file (str): Ruta al archivo de audio grabado.

        Returns:
            tuple: Contiene el texto transcrito y el componente de audio actualizado.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        try:
            # Transcribir el audio usando la API de OpenAI
            transcribed_text = await self.assistant.transcribe_audio(audio_file)

            # Ocultar el control de audio una vez procesado
            return transcribed_text, gr.Audio(visible=False)
        except Exception as e:
            print(f"Error en la transcripción: {e}")
            return "Error al procesar el audio, intenta de nuevo o escribe tu mensaje.", gr.Audio(visible=False)

    def add_user_message(self, history, user_message):
        """
        Agrega el mensaje del usuario al historial de chat.

        Procesa tanto mensajes de texto como archivos adjuntos y los añade
        al historial de conversación. Si hay archivos, los analiza mediante
        el asistente IA.

        Args:
            history (list): Historial actual del chat.
            user_message (str o dict): Mensaje del usuario, puede ser texto plano
                                      o un diccionario multimodal con texto y archivos.

        Returns:
            tuple: Contiene el historial actualizado, el campo de entrada limpio
                  y el indicador de procesamiento.
        """
        # Si no hay mensaje y no hay archivos, no hacer nada
        if isinstance(user_message, dict):
            # Es un mensaje multimodal (puede contener texto y archivos)
            has_text = user_message.get(
                "text") and user_message["text"].strip()
            has_files = user_message.get("files") and len(
                user_message["files"]) > 0

            if not has_text and not has_files:
                return history, "", gr.Row(visible=False)

            # Procesar archivos si existen
            if has_files:
                for file_path in user_message["files"]:
                    # Agregar archivo al historial
                    file_name = os.path.basename(file_path)
                    history.append({
                        "role": "user",
                        "content": {"path": file_path},
                        "metadata": {"title": f"📁 Archivo: {file_name}"}
                    })

                # Procesar cada archivo inmediatamente después de agregarlo
                asyncio.run(self.process_files(history, user_message["files"]))

            # Agregar texto si existe
            if has_text:
                history.append(
                    {"role": "user", "content": user_message["text"]})
        else:
            # Formato antiguo (solo texto)
            if not user_message or not user_message.strip():
                return history, "", gr.Row(visible=False)

            history.append({"role": "user", "content": user_message})

        return history, "", gr.Row(visible=True)

    async def process_files(self, history, file_paths):
        """
        Procesa archivos subidos por el usuario de forma asincrónica.

        Analiza cada archivo médico subido (imágenes, PDFs, documentos) utilizando
        el asistente IA y añade los análisis al historial de chat.

        Args:
            history (list): Historial actual del chat.
            file_paths (list): Lista de rutas a los archivos subidos.

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        try:
            for file_path in file_paths:
                # Analizar el archivo
                analysis = await self.assistant.process_file(file_path)

                if analysis:
                    # Agregar el análisis como respuesta del asistente
                    history.append({
                        "role": "assistant",
                        "content": analysis,
                        "metadata": {"title": "🔍 Análisis del archivo"}
                    })
        except Exception as e:
            print(f"Error al procesar archivos: {e}")
            history.append({
                "role": "assistant",
                "content": "Lo siento, no pude procesar correctamente el archivo. Por favor, intenta con otro formato o describe su contenido en texto."
            })

    def generate_assistant_response_wrapper(self, history, tts_enabled):
        """
        Wrapper sincrónico para el método asincrónico de generación de respuesta.

        Crea un nuevo bucle de eventos para ejecutar la función asincrónica 
        que genera la respuesta del asistente IA.

        Args:
            history (list): Historial actual del chat.
            tts_enabled (bool): Indica si la respuesta debe generarse también en formato de audio.

        Returns:
            tuple: Contiene el historial actualizado con la respuesta del asistente,
                  el componente de audio (si se generó) y el indicador de procesamiento.
        """
        if not history or len(history) == 0:
            return history, None, gr.Row(visible=False)

        # Crear un nuevo event loop en lugar de intentar obtener uno existente
        new_loop = asyncio.new_event_loop()
        try:
            result = new_loop.run_until_complete(
                self._generate_assistant_response_async(history, tts_enabled))
            return result[0], result[1], gr.Row(visible=False)
        finally:
            new_loop.close()

    async def _generate_assistant_response_async(self, history, tts_enabled):
        """
        Implementación asincrónica de la generación de respuesta del asistente.

        Utiliza el asistente IA para generar una respuesta textual y, opcionalmente,
        una respuesta en formato de audio si está habilitada la función de TTS.

        Args:
            history (list): Historial actual del chat.
            tts_enabled (bool): Indica si la respuesta debe generarse también en formato de audio.

        Returns:
            tuple: Contiene el historial actualizado y el archivo de audio generado (si existe).

        Raises:
            No lanza excepciones directamente; captura internamente los errores y los registra.
        """
        try:
            # Generar respuesta del modelo
            assistant_response = await self.assistant.generate_response(history)

            # Agregar respuesta con texto al historial
            # (Añadimos primero el texto para que esté disponible en la interfaz inmediatamente)
            history.append(
                {"role": "assistant", "content": assistant_response})

            # Generar audio si está habilitado
            audio_output = None
            if tts_enabled:
                try:
                    # Generamos audio basado en el texto exacto que ya devolvió el modelo
                    audio_file_path = await self.assistant.generate_speech(assistant_response)
                    if audio_file_path:
                        audio_output = audio_file_path

                        # Agregar respuesta de audio como mensaje adicional del asistente
                        history.append({
                            "role": "assistant",
                            "content": gr.Audio(value=audio_file_path, visible=True, label="🔊 Reproducir respuesta"),
                            "metadata": {"title": "🔊 Respuesta de voz"}
                        })
                except Exception as e:
                    print(f"Error al generar audio: {e}")
                    # No es necesario agregar el texto nuevamente, ya que lo hicimos antes

            return history, audio_output
        except Exception as e:
            print(f"Error general en la respuesta: {e}")
            history.append(
                {"role": "assistant", "content": "Lo siento, ha ocurrido un error. Por favor, intenta de nuevo."})
            return history, None

    def clear_conversation(self):
        """
        Limpia el historial de la conversación y los componentes de audio.

        Returns:
            tuple: Contiene un historial vacío y un componente de audio vacío.
        """
        return [], None

    def handle_feedback(self, like_data):
        """
        Maneja la retroalimentación del usuario (likes/dislikes) para futuras mejoras.

        Registra en la consola la información sobre la retroalimentación recibida,
        incluyendo el índice del mensaje, su valor y si fue marcado positiva o negativamente.

        Args:
            like_data: Datos de retroalimentación desde el componente de chat de Gradio.
                      Puede ser un objeto con atributos index, value y liked, o una lista.

        Returns:
            None: Esta función no devuelve ningún valor para la interfaz.
        """
        # Registrar la retroalimentación para futuras mejoras
        try:
            # Verificar si like_data es un objeto con atributos esperados
            if hasattr(like_data, 'index') and hasattr(like_data, 'value') and hasattr(like_data, 'liked'):
                print(
                    f"Feedback: índice {like_data.index}, valor {like_data.value}, liked {like_data.liked}")
            # Si es una lista u otro tipo, manejarlo apropiadamente
            elif isinstance(like_data, list):
                print(f"Feedback recibido como lista: {like_data}")
            else:
                print(
                    f"Feedback recibido con tipo desconocido: {type(like_data)}, contenido: {like_data}")
        except Exception as e:
            print(f"Error al procesar feedback: {e}")

        return None

    def launch(self):
        """
        Lanza la interfaz de Gradio para hacer accesible la aplicación.

        Configura una cola para manejar múltiples solicitudes y lanza la interfaz
        web sin compartirla públicamente.
        """
        self.interface.queue()
        self.interface.launch(share=False)
