import os
from google import genai
from dotenv import load_dotenv

# Carga de variables de entorno
load_dotenv()

clave_api = os.getenv("GEMINI_API_KEY")

# Inicialización del cliente
cliente = genai.Client(api_key=clave_api)

def ejecutar_consulta():
    print("👌 Ejecutando consulta a Gemini...")

    try:
        respuesta = cliente.models.generate_content(
            model="gemini-3.5-flash",
            contents="Preséntate como experto en machine learning y responde: ¿Qué es el aprendizaje automático? en un parrafo"
        )

        print("✅ Respuesta de Gemini:")
        print(respuesta.text)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    ejecutar_consulta()