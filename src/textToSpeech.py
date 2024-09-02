from utils.functions import *

def textToSpeech():
    # Mostrar opciones al usuario
    print('Seleccione cómo desea convertir el texto:')
    print('1. Escribir texto')
    print('2. Seleccionar texto del sistema')
    
    # Leer la opción seleccionada por el usuario
    option = input('\n→')

    # Procesar la opción seleccionada
    match option:
        case '1':
            # Obtener texto ingresado directamente por el usuario
            text = getTextUser()
            print(f'Texto ingresado por el usuario: {text}')
        case '2':
            # Obtener texto desde un archivo del sistema
            text = getTextFile()
            if text:
                print(f'Texto seleccionado del archivo: {text}')
            else:
                print('No se seleccionó ningún archivo o el archivo está vacío.')
                return
        case _:
            # Manejar una opción no válida
            print('Opción no válida. Por favor, seleccione una opción válida.')
            return

    # Convertir el texto a voz utilizando gTTS
    output = gTTS(text, lang='es')
    file = 'output.mp3'  # Nombre del archivo de salida
    output.save(file)  # Guardar el archivo de audio

    # Confirmar que el archivo de audio se ha guardado correctamente
    print(f'El archivo de audio se ha guardado como {file}.')

if __name__ == '__main__':
    textToSpeech()
