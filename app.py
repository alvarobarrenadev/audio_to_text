# Descripción de cada modelo de Whisper:

# tiny: Es el modelo más pequeño y rápido, pero con menor precisión. Ideal para dispositivos con recursos limitados.
# base: Un poco más grande que el modelo tiny, ofrece un equilibrio entre velocidad y precisión.
# small: Modelo de tamaño intermedio, con mejor precisión que los modelos tiny y base, pero aún relativamente rápido.
# medium: Modelo más grande que small, con una precisión significativamente mejorada, adecuado para tareas que requieren mayor exactitud.
# large: El modelo más grande y preciso, pero también el más lento y que consume más recursos.
# large-v2: Una versión mejorada del modelo large, con ajustes adicionales para mejorar la precisión.

# pip install openai-whisper yt_dlp

import os
import yt_dlp
import whisper
import warnings

# Ignorar advertencias de tipo FutureWarning
# warnings.filterwarnings("ignore", category=FutureWarning)

def descargar_audio_youtube(url):
    # Descargar audio del video de YouTube usando yt_dlp
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
    
    # Retornar la ruta del archivo de audio descargado
    audio_path = 'audio.mp3'
    return audio_path

def transcribir_audio(archivo_audio):
    # Utilizar el modelo Whisper para transcribir
    modelo = whisper.load_model("large-v2")
    resultado = modelo.transcribe(archivo_audio)
    
    # Retornar el texto transcrito
    return resultado['text']

def guardar_transcripcion(texto, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

def main():
    url = input("Introduce la URL del video de YouTube: ")
    archivo_audio = descargar_audio_youtube(url)
    # archivo_audio = "audio.mp3"
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

if __name__ == "__main__":
    main()
