#Importación de librerias.
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
import speech_recognition as sr
from gtts import gTTS 

def getTextUser():
    # Solicitar al usuario que ingrese un texto.
    text = input('Escribe el texto que deseas convertir:\n') 
    return text

def getAudioUser():
    # Captura audio del micrófono del usuario

    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Por favor, habla ahora...')
        # Escuchar el audio del micrófono
        audio = recognizer.listen(source)
        
        try:
            # Convertir el audio a texto usando el servicio de Google
            text = recognizer.recognize_google(audio, language='es-ES')
            return text
        except sr.UnknownValueError:
            print('No se pudo entender el audio.')
        except sr.RequestError:
            print('Error al solicitar resultados del servicio de reconocimiento de voz.')
    
    return None

def getTextFile():
    # Permitir al usuario seleccionar un archivo de texto
    
    # Crear la aplicación Qt para el diálogo de archivo
    app = QApplication(sys.argv)

    # Configurar opciones del diálogo para seleccionar archivo
    options = QFileDialog.Options()
    selected_file, _ = QFileDialog.getOpenFileName(
        None,
        'Selecciona un archivo de texto',
        '',
        'Archivos de texto (*.txt);;Todos los archivos (*)',
        options=options
    )

    if selected_file:
        try:
            # Leer el contenido del archivo de texto
            with open(selected_file, 'r', encoding='utf-8') as file:
                text = file.read()
            return text  
        except Exception as e:
            # Manejar cualquier error al abrir el archivo
            return f'Ocurrió un error: {e}'
    else:
        return 'No se seleccionó ningún archivo.'

def getWavFile():
    # Permitir al usuario seleccionar un archivo WAV.

    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()

    # Crear la aplicación Qt para el diálogo de archivo
    app = QApplication(sys.argv)

    # Configurar opciones del diálogo para seleccionar archivo
    options = QFileDialog.Options()
    selected_file, _ = QFileDialog.getOpenFileName(
        None,
        'Selecciona un archivo WAV',
        '',
        'Archivos WAV (*.wav);;Todos los archivos (*)',
        options=options
    )

    if selected_file:
        try:
            # Procesar el archivo WAV seleccionado
            with sr.AudioFile(selected_file) as source:
                audio = recognizer.record(source)
                
                try:
                    # Convertir el audio a texto usando el servicio de Google
                    texto = recognizer.recognize_google(audio, language='es-ES')
                    return f'Texto del audio seleccionado del archivo: {texto}'
                except sr.UnknownValueError:
                    return 'No se pudo entender el audio.'
                except sr.RequestError as e:
                    return f'Error al conectar con el servicio de reconocimiento de voz; {e}'
        except Exception as e:
            # Manejar cualquier error al abrir el archivo
            return f'Ocurrió un error: {e}'
    else:
        return 'No se seleccionó ningún archivo.'
