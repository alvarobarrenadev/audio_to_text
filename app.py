# pip install openai-whisper yt_dlp

import os
import yt_dlp
import whisper
import warnings

# Ignorar advertencias de tipo FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

def descargar_audio(url):
    """
    Descargar el audio de un video dado su URL.
    Soporta YouTube y TikTok.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    audio_path = 'audio.mp3'
    return audio_path

def transcribir_audio(archivo_audio):
    """Transcribe el audio usando el modelo Whisper."""
    modelo = whisper.load_model("large-v2")
    resultado = modelo.transcribe(archivo_audio)
    return resultado['text']

def guardar_transcripcion(texto, nombre_archivo):
    """Guarda la transcripción en un archivo de texto."""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

def main():
    url = input("Introduce la URL del video: ")

    try:
        archivo_audio = descargar_audio(url)
        print("Audio descargado correctamente.")

        # Transcribir el audio
        print("Transcribiendo audio...")
        transcripcion = transcribir_audio(archivo_audio)
        print("Transcripción completa.")

        # Guardar la transcripción
        nombre_archivo = "transcripcion.txt"
        guardar_transcripcion(transcripcion, nombre_archivo)
        print(f"Transcripción guardada en el archivo {nombre_archivo}.")

        # Eliminar el archivo de audio para ahorrar espacio
        os.remove(archivo_audio)

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()