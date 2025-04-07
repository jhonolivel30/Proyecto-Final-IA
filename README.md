# HealthWise - Asistente Médico Preliminar

## Nombre

Jhon Olivel Castillo Caraballo

## Matrícula

22-SISN-2-063

## Descripción

HealthWise es una aplicación que permite a los usuarios describir síntomas y recibir información preliminar sobre posibles condiciones médicas, recomendaciones generales y cuándo buscar atención médica profesional.

La aplicación utiliza la API de OpenAI y Gradio para proporcionar una interfaz de chat intuitiva donde los usuarios pueden consultar sobre síntomas y recibir respuestas informativas.

**IMPORTANTE**: HealthWise NO sustituye el consejo médico profesional. Si tienes síntomas graves o preocupantes, busca atención médica inmediata.

## Características

- Interfaz de chat amigable basada en Gradio
- Procesamiento de lenguaje natural con OpenAI
- Historial de conversación
- Organización modular del código (UI, IA, configuración)
- Respuestas estructuradas con posibles causas, recomendaciones y cuándo buscar atención médica

## Instalación

1. Clone el repositorio:

   ```bash
   git clone https://github.com/tuusuario/healthwise.git
   cd healthwise
   ```

2. Instale las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure su clave API de OpenAI:

   - Copia el archivo `.env.example` a `.env`
   - Edita el archivo `.env` y añade tu clave API de OpenAI

   ```bash
    cp .env.example .env
    OPENAI_API_KEY=tu_clave_api_aqui
   ```

## Uso

Ejecute la aplicación desde la carpeta principal:

```bash
python src/healthwise.py
```

Esto iniciará una interfaz web local donde podrá interactuar con el asistente HealthWise.

## Estructura del Proyecto

```plaintext
HealthWise/
├── .env                  # Variables de entorno (clave API)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación
└── src/                  # Código fuente
    ├── healthwise.py     # Punto de entrada principal
    ├── ai/               # Componentes de IA
    │   ├── __init__.py
    │   └── assistant.py  # Integración con OpenAI
    ├── config/           # Configuración
    │   ├── __init__.py
    │   └── settings.py   # Constantes y configuraciones
    └── ui/               # Interfaz de usuario
        ├── __init__.py
        ├── interface.py  # Interfaz Gradio
        └── custom.py     # Estilos de la interfaz
```
