import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

def gerar_imagem_gemini(caminho):
    sample_file = genai.upload_file(path=caminho,
                            display_name="Imagem enviada")
    
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

    return sample_file