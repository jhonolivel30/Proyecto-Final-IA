"""
    Módulo de personalización para HealthWise
    -----------------------------------------
    Nombre: Jhon Olivel Castillo Caraballo
    Matricula: 22-SISN-2-063
    
    Este módulo contiene la clase Custom que define los estilos CSS personalizados
    y el contenido HTML para los diversos modales informativos utilizados en la
    interfaz de usuario de la aplicación HealthWise.
"""


class Custom:
    """
    Clase que contiene los elementos visuales personalizados para la interfaz de usuario.

    Esta clase proporciona:
    - Estilos CSS personalizados para mejorar la apariencia de los componentes de Gradio
    - Contenido HTML para los modales informativos (ejemplos, información, recursos, etc.)
    - Esquemas de colores y estilos consistentes para diferentes secciones de la aplicación

    Atributos:
        custom_css (str): Cadena de texto con reglas CSS personalizadas para aplicar a la interfaz.
        ejemplos_modal (str): Contenido HTML para el modal de ejemplos de consultas médicas.
        info_modal (str): Contenido HTML para el modal de información sobre HealthWise.
        recursos_modal (str): Contenido HTML para el modal de recursos médicos confiables.
        emergencias_modal (str): Contenido HTML para el modal de información sobre emergencias.
        consejos_modal (str): Contenido HTML para el modal de consejos saludables.
    """

    def __init__(self):
        """
        Inicializa la clase Custom con los estilos CSS y contenidos HTML para los modales.

        Configura todos los elementos visuales necesarios para la interfaz de usuario,
        incluyendo estilos para componentes de chat, botones, tablas y modales con 
        información médica relevante.
        """
        self.custom_css = """
            #chatbot {
                border-radius: 12px;
                border: 1px solid rgba(0, 0, 0, 0.1);
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            #user_input {
                border-radius: 8px;
                border: 1px solid rgba(0, 0, 0, 0.2);
                padding: 10px;
            }
            .feedback {
                float: right;
                color: rgba(0, 0, 0, 0.5);
                font-size: 0.9rem;
            }
            .title {
                text-align: center;
                color: #3498db;
                font-weight: bold;
            }
            button {
                border-radius: 8px !important;
                font-weight: 600 !important;
            }
            .examples-table {
                border-radius: 10px;
                overflow: hidden;
            }
            .contain {
                border-radius: 15px;
                overflow: hidden;
            }
            /* Estilos personalizados adicionales */
                .resource-btn {
                    border-radius: 15px !important;
                    padding: 12px 16px !important;
                    margin: 5px 0 !important;
                    font-weight: 600 !important;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
                    transition: all 0.3s ease !important;
                    border: none !important;
                    display: flex !important;
                    align-items: center !important;
                    justify-content: center !important;
                    width: 100% !important;
                }
                .resource-btn:hover {
                    transform: translateY(-2px) !important;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
                }
                .examples-btn {
                    background-color: #4CAF50 !important;
                    color: white !important;
                }
                .info-btn {
                    background-color: #2196F3 !important;
                    color: white !important;
                }
                .resources-btn {
                    background-color: #FF9800 !important;
                    color: white !important;
                }
                .emergency-btn {
                    background-color: #F44336 !important;
                    color: white !important;
                }
                .health-btn {
                    background-color: #009688 !important;
                    color: white !important;
                }

                /* Estilos para el contenido modal */
                .modal-content h3, .modal-content h4 {
                    color: #333333 !important;
                    text-shadow: 0 0 1px rgba(0,0,0,0.1) !important;
                }
                .modal-content p, .modal-content li, .modal-content td, .modal-content th {
                    color: #333333 !important;
                }
                .modal-content {
                    background-color: #ffffff !important;
                }
                .modal-content a {
                    color: #0066cc !important;
                }
                .modal-section {
                    border-radius: 8px !important;
                    margin-bottom: 15px !important;
                    padding: 15px !important;
                }
                /* Mejoras de legibilidad para modales */
                .modal-content b, .modal-content strong {
                    color: #333333 !important;
                }

                /* Restaurar colores de las secciones específicas con texto legible */
                /* Sección de ejemplos (verde) */
                .modal-content[style*="border: 2px solid #4CAF50"] table {
                    background-color: #f1f8e9 !important;
                }
                .modal-content[style*="border: 2px solid #4CAF50"] table tr:nth-child(even) td {
                    background-color: #e8f5e9 !important;
                }
                .modal-content[style*="border: 2px solid #4CAF50"] table tr:nth-child(odd) td {
                    background-color: #f1f8e9 !important;
                }
                .modal-content[style*="border: 2px solid #4CAF50"] table th {
                    background-color: #4CAF50 !important;
                    color: white !important;
                }

                /* Sección de información (azul) */
                .modal-section[style*="border-left: 4px solid #2196F3"] {
                    background-color: #e3f2fd !important;
                }

                /* Sección de recursos (naranja) */
                .modal-section[style*="border-left: 4px solid #FF9800"] {
                    background-color: #fff3e0 !important;
                }
                .modal-content[style*="border: 2px solid #FF9800"] table tr:nth-child(even) td {
                    background-color: #fff8e1 !important;
                }
                .modal-content[style*="border: 2px solid #FF9800"] table th {
                    background-color: #ffe0b2 !important;
                }

                /* Sección de emergencias (rojo) */
                .modal-section[style*="border-left: 4px solid #F44336"] {
                    background-color: #ffebee !important;
                }
                .modal-content[style*="border: 2px solid #F44336"] table tr:nth-child(even) td {
                    background-color: #ffebee !important;
                }
                .modal-content[style*="border: 2px solid #F44336"] table th {
                    background-color: #ffcdd2 !important;
                }

                /* Sección de consejos de salud (verde-azulado) */
                .modal-section[style*="border-left: 4px solid #009688"],
                .modal-section[style*="border: 1px solid #009688"] {
                    background-color: #e0f2f1 !important;
                }
                .modal-content[style*="border: 2px solid #009688"] table tr:nth-child(even) td {
                    background-color: #e0f2f1 !important;
                }
                .modal-content[style*="border: 2px solid #009688"] table th {
                    background-color: #b2dfdb !important;
                }

                /* Asegurar contraste en todas las tablas */
                .modal-content table tr td,
                .modal-content table tr th {
                    color: #333333 !important;
                }
            """

        # # Ejemplos de consultas médicas modal
        self.ejemplos_modal = """
                <div class = "modal-content" style = "padding: 20px; border-radius: 12px; margin-bottom: 15px; background-color: #ffffff; border: 2px solid #4CAF50;" >
                <h3 style = "color: #1b5e20; margin-top: 0;" > 📋 Ejemplos de consultas médicas < /h3 >
                <p style = "color: #333333; font-weight: 500;" > Selecciona cualquier ejemplo para comenzar una consulta rápida < /p >
                <table style = "width: 100%; border-collapse: collapse; margin-top: 15px; background-color: #ffffff;" >
                   <tr >
                        <th style = "padding: 12px; text-align: left; border: 1px solid #4CAF50; color: #333333; font-weight: 600;" > Consulta < /th >
                        <th style = "padding: 12px; text-align: left; border: 1px solid #4CAF50; color: #333333; font-weight: 600;" > Tema < /th >
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">Tengo dolor de cabeza intenso y sensibilidad a la luz desde ayer 🤕</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">Síntomas neurológicos</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">¿Qué medicamento es mejor para la fiebre? 🤒</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Medicamentos</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">¿Cuáles son los síntomas comunes de diabetes? 🩸</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">Condiciones crónicas</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Tengo tos seca y dolor de garganta, ¿qué podría ser? 😷</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Infecciones respiratorias</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">¿Cuándo debo preocuparme por un dolor en el pecho? ❤️</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">Salud cardiovascular</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">¿Cómo puedo aliviar el dolor de espalda? 🦴</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Dolor músculo-esquelético</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">¿Qué alimentos son buenos para la presión arterial alta? 🥗</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #ffffff;">Nutrición</td>
                    </tr >
                    <tr >
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Mi hijo tiene erupción cutánea y fiebre, ¿qué podría ser? 👶</td>
                        <td style = "padding: 12px; border: 1px solid #4CAF50; color: #333333; background-color: #f8f8f8;">Pediatría</td>
                    </tr >
                </table >
                </div >
                """

        # # Información modal
        self.info_modal = """
                <div class="modal-content" style="padding: 20px; border-radius: 12px; margin-bottom: 15px; background-color: #ffffff; border: 2px solid #2196F3;">
                <h3 style="color: #0d47a1; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🏥 Sobre HealthWise</h3>
                
                <p style="color: #333333; font-weight: 500;">HealthWise es tu asistente médico virtual que te proporciona información confiable sobre salud y bienestar. Nuestro objetivo es brindarte orientación preliminar sobre condiciones médicas comunes.</p>
                
                <div class="modal-section" style="background-color: #ffffff; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #2196F3; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <h4 style="color: #0d47a1; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">📢 Limitaciones importantes:</h4>
                <ul style="color: #333333; margin-bottom: 0;">
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🔍 Esta herramienta proporciona información preliminar</b>, no diagnósticos definitivos.</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">👨‍⚕️ Siempre consulta a un profesional médico</b> para síntomas preocupantes.</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">📝 La información no reemplaza</b> la consulta médica presencial.</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">⚠️ En caso de emergencia</b>, contacta inmediatamente a servicios médicos.</li>
                </ul>
                </div>
                
                <div class="modal-section" style="background-color: #ffffff; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #2196F3; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <h4 style="color: #0d47a1; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">✅ Puedes preguntar sobre:</h4>
                <ul style="color: #333333; margin-bottom: 0;">
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🩺 Síntomas y posibles causas</b> de diferentes condiciones</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">💊 Información sobre medicamentos</b> comunes y sus usos</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🚑 Cuándo buscar atención médica</b> según los síntomas</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🧪 Interpretación general</b> de análisis clínicos</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🥗 Recomendaciones</b> de alimentación saludable</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">💤 Consejos</b> para mejorar hábitos de sueño</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🏃‍♀️ Sugerencias</b> de ejercicio y actividad física</li>
                </ul>
                </div>
                
                <div class="modal-section" style="background-color: #ffffff; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #2196F3; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <h4 style="color: #0d47a1; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">❓ Cómo hacer mejores consultas:</h4>
                <ul style="color: #333333; margin-bottom: 0;">
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🔹 Describe tus síntomas con detalle</b> (intensidad, duración, etc.)</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🔹 Menciona si tienes condiciones médicas</b> preexistentes</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🔹 Indica tu edad y sexo</b> para respuestas más precisas</li>
                  <li style="margin-bottom: 8px; color: #333333;"><b style="color: #333333;">🔹 Puedes subir imágenes relevantes</b> para mejores resultados</li>
                </ul>
                </div>
                </div>
                """

        # # Recursos modal
        self.recursos_modal = """
                <div class="modal-content" style="padding: 20px; border-radius: 12px; margin-bottom: 15px; background-color: #ffffff; border: 2px solid #FF9800;">
                <h3 style="color: #e65100; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">📚 Enlaces y recursos confiables</h3>
                
                <div class="modal-section" style="background-color: #fff3e0; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #FF9800;">
                <h4 style="color: #e65100; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">🌐 Portales médicos oficiales:</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                  <a href="https://www.who.int/es" target="_blank" style="display: block; color: #0066cc; text-decoration: none; padding: 15px; border-radius: 8px; background-color: #ffffff; margin-bottom: 10px; border: 1px solid #FFB74D;">
                    <div style="font-weight: bold; color: #e65100; font-size: 1.1em;">🌍 Organización Mundial de la Salud (OMS)</div>
                    <div style="font-size: 0.9em; color: #333333; margin-top: 5px;">Organismo internacional de salud pública</div>
                  </a>
                  <a href="https://www.cdc.gov/spanish/" target="_blank" style="display: block; color: #0066cc; text-decoration: none; padding: 15px; border-radius: 8px; background-color: #ffffff; margin-bottom: 10px; border: 1px solid #FFB74D;">
                    <div style="font-weight: bold; color: #e65100; font-size: 1.1em;">🔬 CDC</div>
                    <div style="font-size: 0.9em; color: #333333; margin-top: 5px;">Control y Prevención de Enfermedades</div>
                  </a>
                  <a href="https://medlineplus.gov/spanish/" target="_blank" style="display: block; color: #0066cc; text-decoration: none; padding: 15px; border-radius: 8px; background-color: #ffffff; margin-bottom: 10px; border: 1px solid #FFB74D;">
                    <div style="font-weight: bold; color: #e65100; font-size: 1.1em;">📚 MedlinePlus</div>
                    <div style="font-size: 0.9em; color: #333333; margin-top: 5px;">Biblioteca Nacional de Medicina</div>
                  </a>
                  <a href="https://www.mayoclinic.org/es-es" target="_blank" style="display: block; color: #0066cc; text-decoration: none; padding: 15px; border-radius: 8px; background-color: #ffffff; margin-bottom: 10px; border: 1px solid #FFB74D;">
                    <div style="font-weight: bold; color: #e65100; font-size: 1.1em;">🏥 Mayo Clinic</div>
                    <div style="font-size: 0.9em; color: #333333; margin-top: 5px;">Información médica de prestigio</div>
                  </a>
                </div>
                </div>
                
                <div class="modal-section" style="background-color: #fff3e0; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #FF9800;">
                <h4 style="color: #e65100; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">📱 Aplicaciones recomendadas:</h4>
                <table style="width: 100%; border-collapse: collapse; background-color: #ffffff;">
                  <tr style="background-color: #ffe0b2;">
                    <th style="padding: 12px; text-align: left; border: 1px solid #ffcc80; color: #333333; font-weight: 600;">Aplicación</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #ffcc80; color: #333333; font-weight: 600;">Función</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #ffcc80; color: #333333; font-weight: 600;">Plataforma</th>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">📊 MyFitnessPal</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">Seguimiento de nutrición y ejercicio</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">iOS/Android</td>
                  </tr>
                  <tr style="background-color: #fff8e1;">
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">💤 Sleep Cycle</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">Análisis de patrones de sueño</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">iOS/Android</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">💊 Medisafe</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">Recordatorio de medicamentos</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333; background-color: #ffffff;">iOS/Android</td>
                  </tr>
                  <tr style="background-color: #fff8e1;">
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">❤️ HeartRate</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">Monitoreo de ritmo cardíaco</td>
                    <td style="padding: 12px; border: 1px solid #ffcc80; color: #333333;">iOS/Android</td>
                  </tr>
                </table>
                </div>
                
                <div class="modal-section" style="background-color: #fff3e0; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #FF9800;">
                <h4 style="color: #e65100; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">📅 Calendario de salud:</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;">
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">💗</div>
                    <div style="font-weight: bold; color: #333333;">Febrero</div>
                    <div style="font-size: 0.9em; color: #333333;">Mes del corazón</div>
                  </div>
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">🧠</div>
                    <div style="font-weight: bold; color: #333333;">Junio</div>
                    <div style="font-size: 0.9em; color: #333333;">Mes de la salud mental</div>
                  </div>
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">🩸</div>
                    <div style="font-weight: bold; color: #333333;">Octubre</div>
                    <div style="font-size: 0.9em; color: #333333;">Cáncer de mama</div>
                  </div>
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">👨</div>
                    <div style="font-weight: bold; color: #333333;">Noviembre</div>
                    <div style="font-size: 0.9em; color: #333333;">Salud masculina</div>
                  </div>
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">🦠</div>
                    <div style="font-weight: bold; color: #333333;">Diciembre</div>
                    <div style="font-size: 0.9em; color: #333333;">Vacunación</div>
                  </div>
                  <div style="padding: 15px; border-radius: 8px; background-color: #ffffff; text-align: center; border: 1px solid #FFB74D;">
                    <div style="font-size: 1.5em;">🫁</div>
                    <div style="font-weight: bold; color: #333333;">Mayo</div>
                    <div style="font-size: 0.9em; color: #333333;">Asma y alergia</div>
                  </div>
                </div>
                </div>
                """

        # # Emergencias modal
        self.emergencias_modal = """
          <div class="modal-content" style="padding: 20px; border-radius: 12px; margin-bottom: 15px; background-color: #ffffff; border: 2px solid #F44336;">
          <h3 style="color: #b71c1c; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🚨 Información para emergencias</h3>
          
          <div class="modal-section" style="background-color: #ffebee; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #F44336;">
          <h4 style="color: #b71c1c; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">⚠️ Números de emergencia por país:</h4>
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 15px; background-color: #ffffff;">
            <tr style="background-color: #ffcdd2;">
              <th style="padding: 12px; text-align: left; border: 1px solid #ef9a9a; color: #333333; font-weight: 600;">País</th>
              <th style="padding: 12px; text-align: left; border: 1px solid #ef9a9a; color: #333333; font-weight: 600;">Número general</th>
              <th style="padding: 12px; text-align: left; border: 1px solid #ef9a9a; color: #333333; font-weight: 600;">Ambulancia</th>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">🇲🇽 México</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;"><b>911</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">065</td>
            </tr>
            <tr style="background-color: #ffebee;">
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">🇺🇸 Estados Unidos</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;"><b>911</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">911</td>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">🇪🇸 España</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;"><b>112</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">061</td>
            </tr>
            <tr style="background-color: #ffebee;">
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">🇨🇴 Colombia</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;"><b>123</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">123</td>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">🇦🇷 Argentina</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;"><b>911</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">107</td>
            </tr>
            <tr style="background-color: #ffebee;">
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">🇨🇱 Chile</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;"><b>131</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333;">131</td>
            </tr>
            <tr>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">🇩🇴 República Dominicana</td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;"><b>911</b></td>
              <td style="padding: 12px; border: 1px solid #ef9a9a; color: #333333; background-color: #ffffff;">911</td>
            </tr>
          </table>
          </div>
          
          <div class="modal-section" style="background-color: #ffebee; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #F44336;">
          <h4 style="color: #b71c1c; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">🚑 Busca atención médica INMEDIATA si experimentas:</h4>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">💔 Dolor en el pecho</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Especialmente si es intenso, opresivo, se extiende al brazo, mandíbula o espalda</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">🫁 Dificultad para respirar</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Sensación de ahogo, respiración rápida o imposibilidad de hablar</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">🧠 Signos de derrame cerebral</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Debilidad súbita, entumecimiento facial, confusión, problemas de habla</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">🩸 Sangrado severo</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Hemorragia que no se detiene con presión directa</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">⚡ Convulsiones</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Especialmente si duran más de 5 minutos o se repiten</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">🤒 Fiebre muy alta</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Superior a 39.5°C, especialmente con rigidez de cuello o erupción</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">💫 Pérdida de conciencia</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Desmayo prolongado o incapacidad para despertar</p>
            </div>
            <div style="background-color: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #ef9a9a;">
              <p style="margin: 0; color: #b71c1c; font-weight: 600;">🧪 Reacción alérgica grave</p>
              <p style="margin-top: 5px; font-size: 0.9em; color: #333333;">Hinchazón facial, dificultad para respirar, urticaria generalizada</p>
            </div>
          </div>
          </div>
          
          <div class="modal-section" style="background-color: #ffebee; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #F44336;">
          <h4 style="color: #b71c1c; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🏃‍♀️ Protocolo rápido para emergencias:</h4>
          <ol style="color: #333333; margin-bottom: 0;">
            <li style="margin-bottom: 8px; color: #333333;"><b>Mantén la calma</b> y evalúa la situación</li>
            <li style="margin-bottom: 8px; color: #333333;"><b>Llama al número de emergencia local</b> - Sé claro y preciso</li>
            <li style="margin-bottom: 8px; color: #333333;"><b>Sigue las instrucciones del operador</b> - No cuelgues hasta que te lo indiquen</li>
            <li style="margin-bottom: 8px; color: #333333;">Si estás capacitado, <b>proporciona primeros auxilios básicos</b></li>
            <li style="margin-bottom: 8px; color: #333333;">No muevas a la persona lesionada a menos que sea <b>absolutamente necesario</b></li>
          </ol>
          </div>
          </div>
          """

        # # Consejos modal
        self.consejos_modal = """
                <div class="modal-content" style="padding: 20px; border-radius: 12px; margin-bottom: 15px; background-color: #ffffff; border: 2px solid #009688;">
                <h3 style="color: #004d40; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">💪 Hábitos saludables recomendados</h3>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px;">
                  <div class="modal-section" style="background-color: #e0f2f1; padding: 15px; border-radius: 8px; border: 1px solid #009688;">
                    <h4 style="color: #004d40; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🥗 Alimentación</h4>
                    <ul style="margin-bottom: 0;">
                      <li style="margin-bottom: 8px; color: #333333;"><b>5 porciones</b> de frutas y verduras al día</li>
                      <li style="margin-bottom: 8px; color: #333333;">Limita el consumo de <b>azúcares y grasas saturadas</b></li>
                      <li style="margin-bottom: 8px; color: #333333;">Mantente hidratado (<b>8 vasos</b> de agua diarios)</li>
                      <li style="margin-bottom: 8px; color: #333333;">Reduce el consumo de <b>alimentos ultraprocesados</b></li>
                      <li style="margin-bottom: 8px; color: #333333;">Prioriza proteínas <b>magras</b> (pollo, pescado, legumbres)</li>
                      <li style="margin-bottom: 8px; color: #333333;">Incluye <b>grasas saludables</b> (aguacate, frutos secos, aceite de oliva)</li>
                    </ul>
                  </div>
                  <div class="modal-section" style="background-color: #e0f2f1; padding: 15px; border-radius: 8px; border: 1px solid #009688;">
                    <h4 style="color: #004d40; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🏃‍♂️ Actividad física</h4>
                    <ul style="margin-bottom: 0;">
                      <li style="margin-bottom: 8px; color: #333333;"><b>150 minutos</b> de ejercicio moderado a la semana</li>
                      <li style="margin-bottom: 8px; color: #333333;">Incluye <b>2 días</b> de entrenamiento de fuerza</li>
                      <li style="margin-bottom: 8px; color: #333333;">Evita permanecer <b>sentado por períodos prolongados</b></li>
                      <li style="margin-bottom: 8px; color: #333333;">Busca actividades que <b>disfrutes</b> para mantener constancia</li>
                      <li style="margin-bottom: 8px; color: #333333;">Incorpora <b>estiramientos</b> para mejorar la flexibilidad</li>
                      <li style="margin-bottom: 8px; color: #333333;">Incrementa la actividad <b>gradualmente</b> si eres principiante</li>
                    </ul>
                  </div>
                  <div class="modal-section" style="background-color: #e0f2f1; padding: 15px; border-radius: 8px; border: 1px solid #009688;">
                    <h4 style="color: #004d40; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">😴 Descanso</h4>
                    <ul style="margin-bottom: 0;">
                      <li style="margin-bottom: 8px; color: #333333;">Duerme entre <b>7-9 horas</b> diarias</li>
                      <li style="margin-bottom: 8px; color: #333333;">Mantén un <b>horario regular</b> de sueño</li>
                      <li style="margin-bottom: 8px; color: #333333;">Evita <b>pantallas 1 hora</b> antes de dormir</li>
                      <li style="margin-bottom: 8px; color: #333333;">Crea un ambiente <b>oscuro y fresco</b> para dormir</li>
                      <li style="margin-bottom: 8px; color: #333333;">Reduce la <b>cafeína</b> después del mediodía</li>
                      <li style="margin-bottom: 8px; color: #333333;">Practica una <b>rutina relajante</b> antes de acostarte</li>
                    </ul>
                  </div>
                  <div class="modal-section" style="background-color: #e0f2f1; padding: 15px; border-radius: 8px; border: 1px solid #009688;">
                    <h4 style="color: #004d40; margin-top: 0; text-shadow: 0 0 1px rgba(0,0,0,0.1);">🧘‍♀️ Salud mental</h4>
                    <ul style="margin-bottom: 0;">
                      <li style="margin-bottom: 8px; color: #333333;">Practica <b>técnicas de relajación</b> o meditación</li>
                      <li style="margin-bottom: 8px; color: #333333;">Mantén <b>conexiones sociales</b> significativas</li>
                      <li style="margin-bottom: 8px; color: #333333;">Establece <b>límites saludables</b> en trabajo y tecnología</li>
                      <li style="margin-bottom: 8px; color: #333333;">Busca <b>ayuda profesional</b> si experimentas ansiedad o depresión</li>
                      <li style="margin-bottom: 8px; color: #333333;">Dedica tiempo a <b>actividades placenteras</b> cada día</li>
                      <li style="margin-bottom: 8px; color: #333333;">Cultiva la <b>gratitud</b> y el pensamiento positivo</li>
                    </ul>
                  </div>
                </div>
                
                <div class="modal-section" style="background-color: #e0f2f1; margin: 15px 0; border-radius: 8px; padding: 15px; border-left: 4px solid #009688;">
                <h4 style="color: #004d40; text-shadow: 0 0 1px rgba(0,0,0,0.1); margin-top: 0;">📅 Chequeos médicos recomendados:</h4>
                <table style="width: 100%; border-collapse: collapse; background-color: #ffffff;">
                  <tr style="background-color: #b2dfdb;">
                    <th style="padding: 12px; text-align: left; border: 1px solid #80cbc4; color: #333333; font-weight: 600;">Examen</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #80cbc4; color: #333333; font-weight: 600;">Frecuencia</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #80cbc4; color: #333333; font-weight: 600;">Recomendado para</th>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Examen físico general</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Anual</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Todos los adultos</td>
                  </tr>
                  <tr style="background-color: #e0f2f1;">
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Presión arterial</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Anual</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Adultos 18+</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Perfil lipídico</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Cada 4-6 años</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Adultos 20+</td>
                  </tr>
                  <tr style="background-color: #e0f2f1;">
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Mamografía</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Cada 1-2 años</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Mujeres 40+</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Papanicolaou</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Cada 3 años</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Mujeres 21-65</td>
                  </tr>
                  <tr style="background-color: #e0f2f1;">
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Examen de próstata</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Consultar médico</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Hombres 50+</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Colonoscopía</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Cada 10 años</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Adultos 45+</td>
                  </tr>
                  <tr style="background-color: #e0f2f1;">
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Examen dental</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Cada 6 meses</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333;">Todas las edades</td>
                  </tr>
                  <tr>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Examen ocular</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Cada 1-2 años</td>
                    <td style="padding: 12px; border: 1px solid #80cbc4; color: #333333; background-color: #ffffff;">Adultos 40+</td>
                  </tr>
                </table>
                </div>
                </div>
                """
